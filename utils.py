from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown

# *Custom theme dictionary
custom_theme_dict = {
    'info': 'bold blue',
    'normal': ' white',
    'warning': 'bold yellow',
    'danger': 'bold red',
    'success': 'bold green',
    'error': 'bold red',
    'processing': 'bold cyan',
    'title': 'bold magenta',
    'subtitle': 'bold blue',
    'bold': 'bold',
    'italic': 'italic',
    'underline': 'underline',
    'blink': 'blink',
}

# *Custom rich theme 
custom_theme = Theme(custom_theme_dict)

# *Custom rich console 
console = Console(theme=custom_theme)

# *Intro Markdown
intro_raw_markdown = """
# Nut 🥜
A simple CLI tool to automate your git workflow
Made with ❤️  by @iamBijoyKar
"""

intro_markdown = Markdown(intro_raw_markdown)