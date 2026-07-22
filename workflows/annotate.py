from dotenv import load_dotenv
load_dotenv()

print("Running annotate.py workflow...")

from typing import Annotated
import operator
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
 
class TicketState(TypedDict):
    customer_message: str
    log: Annotated[list, operator.add]
 
def log_received(state: TicketState) -> dict:
    return {"log": [f"Received: {state['customer_message']}"]}
 
def log_assigned(state: TicketState) -> dict:
    return {"log": ["Assigned to support queue"]}
 
builder = StateGraph(TicketState)
builder.add_node("log_received", log_received)
builder.add_node("log_assigned", log_assigned)
builder.add_edge(START, "log_received")
builder.add_edge("log_received", "log_assigned")
builder.add_edge("log_assigned", END)
graph = builder.compile()
 
result = graph.invoke({"customer_message": "My invoice looks wrong", "log": []})
print(result)

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
    from langgraph.checkpoint.memory import InMemorySaver
 
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "ticket-7741"}}
 
graph.invoke(
    {"messages": [HumanMessage("Hi, I can't access my account.")]},
    config,
)
 
result = graph.invoke(
    {"messages": [HumanMessage("My ID is cust_2002, can you check my plan?")]},
    config,
)
 
print(result["messages"][-1].content)