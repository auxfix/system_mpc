from fastmcp import FastMCP
import platform
import psutil
import os
import sys

mcp = FastMCP("System Info MPC")

@mcp.tool
def get_list_of_dirs(path :str) -> str:
    """
    Retrieves list of dirs in specific path
    """
    with os.scandir(path) as entries:
        dirs = [f"{path}{entry.name}" for entry in entries if entry.is_dir()]
    
    return "\n".join(dirs)


@mcp.tool
def get_discs() -> str:
    """
    Retrieves list of all discs in computer.
    """
    partitions = psutil.disk_partitions()
    discs = []
    for p in partitions:
        discs.append(f"Device: {p.device}, Mountpoint: {p.mountpoint}, FileSystem: {p.fstype}")
    
    return "\n".join(discs)

@mcp.tool
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