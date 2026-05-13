from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

def get_system_info() -> str:
    """
    Retrieves comprehensive OS, hardware, and runtime environment details.
    """
    # Gather architecture details safely
    arch_bits, _ = platform.architecture()
    
    # Structure data into a clean, human-and-LLM-readable format
    lines = [
        "=== Operating System ===",
        f"OS System:    {platform.system()}",
        f"OS Release:   {platform.release()}",
        f"OS Version:   {platform.version()}",
        f"Platform ID:  {platform.platform()}",
        f"Node Name:    {platform.node()}",
        "",
        "=== Hardware & Architecture ===",
        f"Machine Arch: {platform.machine()} ({arch_bits})",
        f"Processor:    {platform.processor()}",
        f"CPU Cores:    {os.cpu_count() or 'Unknown'} (Logical)",
        "",
        "=== Python Runtime ===",
        f"Python Ver:   {platform.python_version()}",
        f"Compiler:     {platform.python_compiler()}",
        f"Exec Path:    {sys.executable}",
        f"Process ID:   {os.getpid()}"
    ]
    
    return "\n".join(lines)

if __name__ == "__main__":
    mcp.run()