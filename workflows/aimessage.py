from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
 
llm = ChatOpenAI(model="gpt-4o-mini")
 
def run_model(state: MessagesState) -> dict:
    system = SystemMessage("You are a support agent for a SaaS product. "
                           "Be concise and helpful.")
    response = llm.invoke([system] + state["messages"])
    return {"messages": [response]}

from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage
 
builder = StateGraph(MessagesState)
builder.add_node("run_model", run_model)
builder.add_edge(START, "run_model")
builder.add_edge("run_model", END)
 
graph = builder.compile()
 
result = graph.invoke({"messages": [HumanMessage("My dashboard isn't loading. What should I try?")]})
print(result["messages"][-1].content)


from langchain_core.tools import tool
 
@tool
def get_customer_tier(customer_id: str) -> str:
    """Look up the subscription tier for a customer by their ID.
    Returns 'free', 'pro', or 'enterprise'."""
    tiers = {
        "cust_1001": "enterprise",
        "cust_2002": "pro",
        "cust_3003": "free",
    }
    return tiers.get(customer_id, "not found")
tools = [get_customer_tier]
llm_with_tools = llm.bind_tools(tools)
 
def run_model(state: MessagesState) -> dict:
    system = SystemMessage("You are a support agent for a SaaS product. "
                           "Use available tools when you need account-specific information.")
    response = llm_with_tools.invoke([system] + state["messages"])
    return {"messages": [response]}
from langgraph.prebuilt import ToolNode, tools_condition
 
tool_node = ToolNode(tools)
 
builder = StateGraph(MessagesState)
builder.add_node("run_model", run_model)
builder.add_node("tools", tool_node)
 
builder.add_edge(START, "run_model")
builder.add_conditional_edges("run_model", tools_condition)
builder.add_edge("tools", "run_model")
 
graph = builder.compile()
result = graph.invoke({"messages": [
    HumanMessage("Can you check what plan customer cust_1001 is on?")
]})
 
for msg in result["messages"]:
    print(type(msg).__name__, ":", msg.content or msg.tool_calls)
    