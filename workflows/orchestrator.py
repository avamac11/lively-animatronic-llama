from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool
import operator
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
import os
from typing import Annotated, TypedDict
import subprocess
import json
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import re

# Load agent instructions
with open('/home/avam11/lively-animatronic-llama/.opencode/agents/admet-mie.md', 'r') as f:
    admet_mie_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/aop-constructor.md', 'r') as f:
    aop_constructor_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/aop-expert.md', 'r') as f:
    aop_expert_instructions = f.read()

with open('/home/avam11/lively-animatronic-llama/.opencode/agents/visuals-agent.md', 'r') as f:
    visuals_agent_instructions = f.read()

# Initialize LLM with better configuration
llm = ChatOpenAI(
    model="gemma-4-31b", 
    temperature=0.7, 
    max_tokens=2048,  # Increased token limit for better responses
    api_key=os.environ.get("OPENAI_API_KEY"),
    timeout=60,  # Increased timeout
    max_retries=2
)

def generate_topological_map(molecule_name, aop_analysis):
    """Generate a topological map from AOP analysis and save as PNG"""
    # Extract key information from AOP analysis
    try:
        # Parse the AOP analysis to extract nodes and edges
        lines = aop_analysis.split('\n')
        
        # Initialize graph
        G = nx.DiGraph()
        
        # Extract nodes and edges using improved pattern matching
        nodes = []
        edges = []
        
        # Look for MIE, KE, AO patterns with more robust parsing
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # More robust pattern matching for different formats
            if 'MIE' in line and ':' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    node_id = f"MIE_{len(nodes)+1}"
                    label = parts[1].strip()
                    # Handle multi-line labels
                    if i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith(('MIE', 'KE', 'AO')):
                        label += ' ' + lines[i+1].strip()
                    nodes.append((node_id, {'label': label, 'type': 'MIE'}))
            elif 'KE' in line and ':' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    node_id = f"KE_{len(nodes)+1}"
                    label = parts[1].strip()
                    # Handle multi-line labels
                    if i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith(('MIE', 'KE', 'AO')):
                        label += ' ' + lines[i+1].strip()
                    nodes.append((node_id, {'label': label, 'type': 'KE'}))
            elif 'AO' in line and ':' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    node_id = f"AO_{len(nodes)+1}"
                    label = parts[1].strip()
                    # Handle multi-line labels
                    if i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith(('MIE', 'KE', 'AO')):
                        label += ' ' + lines[i+1].strip()
                    nodes.append((node_id, {'label': label, 'type': 'AO'}))
        
        # Add stressor node
        stressor_id = 'S'
        nodes.insert(0, (stressor_id, {'label': f'Stressor: {molecule_name}', 'type': 'Stressor'}))
        
        # Add edges with improved connectivity logic
        if len(nodes) > 1:
            # Connect stressor to first MIE
            if nodes[1][1]['type'] == 'MIE':
                edges.append((stressor_id, nodes[1][0]))
            
            # Connect MIE to KE and KE to AO
            mie_nodes = [n for n in nodes[1:] if n[1]['type'] == 'MIE']
            ke_nodes = [n for n in nodes[1:] if n[1]['type'] == 'KE']
            ao_nodes = [n for n in nodes[1:] if n[1]['type'] == 'AO']
            
            # Connect MIEs to KEs
            for mie in mie_nodes:
                for ke in ke_nodes:
                    edges.append((mie[0], ke[0]))
            
            # Connect KEs to AOs
            for ke in ke_nodes:
                for ao in ao_nodes:
                    edges.append((ke[0], ao[0]))
        
        # Add nodes to graph
        for node_id, attr in nodes:
            G.add_node(node_id, **attr)
        
        # Add edges to graph
        G.add_edges_from(edges)
        
        # Use force-directed layout for better organization
        if len(nodes) > 1:
            pos = nx.spring_layout(G, seed=42, k=0.5, iterations=1000)
        else:
            # Fallback layout if only one node
            pos = {stressor_id: (0, 0)}
        
        # Color mapping with improved colorblind-friendly scheme
        color_map = {
            'Stressor': '#999999',   # Grey
            'MIE': '#FF9999',        # Light Red
            'KE': '#66B2FF',         # Light Blue
            'AO': '#FF3333'          # Red
        }
        
        node_colors = [color_map[G.nodes[n]['type']] for n in G.nodes()]
        
        # Create figure with improved sizing
        plt.figure(figsize=(15, 12))
        
        # Draw nodes with improved styling
        nx.draw_networkx_nodes(G, pos, node_size=3000, node_color=node_colors,
                               edgecolors='black', linewidths=2.0, alpha=0.9)
        
        # Draw labels with improved formatting
        labels = {n: G.nodes[n]['label'] for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels,
                                font_size=10, font_weight='bold', 
                                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1))
        
        # Draw edges with improved styling
        nx.draw_networkx_edges(G, pos, width=2.5, edge_color='gray',
                               arrowstyle='->', arrowsize=25, connectionstyle='arc3,rad=0.1')
        
        # Enhanced legend
        legend_elements = [
            Patch(facecolor='#999999', edgecolor='black', label='Stressor'),
            Patch(facecolor='#FF9999', edgecolor='black', label='Molecular Initiating Event (MIE)'),
            Patch(facecolor='#66B2FF', edgecolor='black', label='Key Event (KE)'),
            Patch(facecolor='#FF3333', edgecolor='black', label='Adverse Outcome (AO)')
        ]
        plt.legend(handles=legend_elements, loc='upper right', title="Node Types", fontsize=11)
        
        plt.title(f"Topological Map of {molecule_name} AOP Network", fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        
        # Save map with higher quality
        output_path = f'{molecule_name.lower()}_aop_map.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return output_path
        
    except Exception as e:
        print(f"Error generating topological map: {e}")
        return None

def admet_mie_agent(state: Annotated[dict, "State"]) -> Annotated[dict, "State"]:
    """ADMET and MIE analysis agent"""
    molecule = state["molecule"]
    
    # Create system message with loaded instructions
    system_message = SystemMessage(content=admet_mie_instructions)
    
    # Create chat chain - pass the system message and user message together
    response = llm.invoke([
        system_message, 
        f"Analyze the molecule {molecule} for ADMET properties and potential molecular initiating events. "
        f"Provide a comprehensive analysis including absorption, distribution, metabolism, excretion, and toxicity. "
        f"Identify specific molecular initiating events (MIEs) that this molecule may trigger."
    ])
    
    return {"admet_analysis": response.content, **state}

def aop_expert_agent(state: Annotated[dict, "State"]) -> Annotated[dict, "State"]:
    """AOP expert agent"""
    molecule = state["molecule"]
    admet_analysis = state["admet_analysis"]
    
    # Create system message with loaded instructions
    system_message = SystemMessage(content=aop_expert_instructions)
    
    # Create chat chain - pass the system message and user message together
    response = llm.invoke([
        system_message, 
        f"Based on this ADMET analysis for {molecule}: {admet_analysis}, "
        f"identify potential adverse outcome pathways. Include detailed information about "
        f"Molecular Initiating Events (MIE), Key Events (KE), and Adverse Outcomes (AO). "
        f"Format the response clearly with proper section headers."
    ])
    
    return {"aop_analysis": response.content, **state}

def visuals_agent(state: Annotated[dict, "State"]):
    """Visualization agent"""
    molecule = state["molecule"]
    aop_analysis = state["aop_analysis"]
    
    # Create system message with loaded instructions
    system_message = SystemMessage(content=visuals_agent_instructions)
    
    # Create chat chain - pass the system message and user message together
    response = llm.invoke([
        system_message, 
        f"Create visualizations for this AOP analysis of {molecule}: {aop_analysis}. "
        f"Focus on topological mapping and network analysis. "
        f"Identify critical pathways and intervention points."
    ])
    
    # Generate topological map
    map_path = generate_topological_map(molecule, aop_analysis)
    
    visualizations = response.content
    if map_path:
        visualizations += f"\n\nTopological map generated: {map_path}"
    
    return {"visualizations": visualizations, "map_path": map_path, **state}

def aop_constructor_agent(state: Annotated[dict, "State"]):
    """AOP constructor agent"""
    molecule = state["molecule"]
    admet_analysis = state["admet_analysis"]
    aop_analysis = state["aop_analysis"]
    visualizations = state["visualizations"]
    map_path = state.get("map_path", "")
    
    # Create system message with loaded instructions
    system_message = SystemMessage(content=aop_constructor_instructions)
    
    # Include map reference in the report
    map_reference = f"\n\n![Topological Map]({map_path})" if map_path else ""
    
    # Create chat chain - pass the system message and user message together
    response = llm.invoke([
        system_message, 
        f"Construct a comprehensive AOP report for {molecule} using:\n\n" +
        f"**ADMET Analysis:**\n{admet_analysis}\n\n" +
        f"**AOP Analysis:**\n{aop_analysis}\n\n" +
        f"**Visualizations:**\n{visualizations}\n\n" +
        f"**Map Reference:**{map_reference}\n\n" +
        f"Format this as a professional markdown report with clear sections, tables, and proper formatting."
    ])
    
    return {"final_report": response.content, "map_path": map_path, **state}


# Define state
class AgentState(TypedDict):
    molecule: str
    admet_analysis: str
    aop_analysis: str
    visualizations: str
    map_path: str
    final_report: str

# Build the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("admet_mie", admet_mie_agent)
workflow.add_node("aop_expert", aop_expert_agent)
workflow.add_node("visuals", visuals_agent)
workflow.add_node("constructor", aop_constructor_agent)

# Define edges
workflow.set_entry_point("admet_mie")
workflow.add_edge("admet_mie", "aop_expert")
workflow.add_edge("aop_expert", "visuals")
workflow.add_edge("visuals", "constructor")
workflow.add_edge("constructor", END)

# Compile the workflow
app = workflow.compile()

if __name__ == "__main__":
    # Prompt user for chemical input
    molecule_name = input("Enter the name of the chemical/molecule to analyze: ")
    
    # Run the workflow with user-provided molecule
    inputs = {"molecule": molecule_name}
    final_state = app.invoke(inputs)
    
    map_info = f"\nTopological map saved: {final_state['map_path']}" if final_state.get('map_path') else ""
    print(f"Workflow complete. Report generated: {final_state['final_report']}{map_info}")
        