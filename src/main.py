# !/usr/bin/env python

import click
from commands import git_clone, git_init, git_add, git_commit
from utils import console

@click.group(name="nut",invoke_without_command=True)
@click.version_option("1.0.0")
@click.pass_context
def nut(ctx):
    if ctx.invoked_subcommand is None:
        console.print("\nThanks for using Nut 🥜\n", style="title",justify="left")
        console.print("Use nut --help to see available commands", style="subtitle")


@click.command(name="clone")
@click.argument("url", required=True, type=str)
def clone(url):
    git_clone(url)
    

@click.command(name="add")
@click.argument("files", required=True, type=click.Path(exists=True), nargs=-1) 
def add(files):
    git_add(files)

@click.command(name="init")
@click.option("--gitignore", "-g", is_flag=True, help="Create a .gitignore file")
def init(gitignore):
    git_init(gitignore)


@click.command(name="commit")
@click.option("--message", "-m", required=True, help="Commit message")
def commit(message):
    git_commit(message)




nut.add_command(init)
nut.add_command(clone)
nut.add_command(add)
nut.add_command(commit)



if __name__ == '__main__':
    nut()