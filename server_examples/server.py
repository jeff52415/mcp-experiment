# server.py
from typing import List, Dict, Any
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent

# Create an MCP server
mcp = FastMCP("Comprehensive Demo")

# Add mathematical tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers"""
    return sum(numbers) / len(numbers) if numbers else 0

# Add string manipulation tools
@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string"""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    """Count the number of words in a string"""
    return len(text.split())

# Add time-related tools
@mcp.tool()
def get_current_time() -> str:
    """Get the current time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Add dynamic resources
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("math://constants")
def get_math_constants() -> Dict[str, float]:
    """Get common mathematical constants"""
    return {
        "pi": 3.14159,
        "e": 2.71828,
        "golden_ratio": 1.61803
    }

@mcp.resource("time://current")
def get_current_time_resource() -> Dict[str, str]:
    """Get current time information"""
    now = datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "timezone": "UTC"
    }

# Add prompts
@mcp.prompt()
def math_assistant_prompt(operation: str, numbers: List[float]) -> List[PromptMessage]:
    """Create a prompt for math operations"""
    return [
        PromptMessage(
            role="system",
            content=TextContent(
                type="text",
                text="You are a helpful math assistant. Perform the requested operation on the given numbers."
            )
        ),
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"Please {operation} the following numbers: {', '.join(map(str, numbers))}"
            )
        )
    ]

@mcp.prompt()
def text_analysis_prompt(text: str) -> List[PromptMessage]:
    """Create a prompt for text analysis"""
    return [
        PromptMessage(
            role="system",
            content=TextContent(
                type="text",
                text="You are a text analysis expert. Analyze the given text and provide insights."
            )
        ),
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"Please analyze the following text: {text}"
            )
        )
    ]

if __name__ == "__main__":
    # Run the server
    mcp.run(transport='sse')


