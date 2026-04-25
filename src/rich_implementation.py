from rich.console import Console

def print_exe_info(info=""):
    console = Console()
    width = console.size.width

    text = info
    line_char = "─"

    remaining = width - len(text)
    left = remaining // 2
    right = remaining - left

    line = f"{line_char * left}{text}{line_char * right}"

    console.print(line, style="bold green")
