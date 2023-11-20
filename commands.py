import subprocess
import sys
from utils import console

def git_clone(url):
    console.print(f"Cloning {url}...", style="processing")
    


def git_init(gitignore):
    response = subprocess.run(["git", "init"], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        if gitignore:
            with open(".gitignore", "a+") as f:
                f.write("\nvenv")
            console.print(".gitignore file created\n", style="info")
        current_git_status = subprocess.run(["git", "status"], capture_output=True).stdout.decode("utf-8").splitlines()
        current_git_status_text = '\n'.join(current_git_status[4:8]).replace('"git','"nut')
        console.print(current_git_status_text, style="normal")
        console.print("\nYour Nut 🥜 journey started, now start rocking 🤘 ", style="success")
    else:
        console.print("Unable to initialize", style="error")
        sys.exit(1)

def git_add(files):
    for file in files:
        response = subprocess.run(["git", "add", file], capture_output=True)
        console.print(f'Added {file}', style='green italic')
        
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files added", style="success")
    else:
        console.print("Unable to add files", style="error")
        sys.exit(1)

   

def git_commit(message):
    response = subprocess.run(["git", "commit", "-m", message], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files committed", style="success")
    else:
        console.print("Unable to commit files", style="error")
        sys.exit(1)
    

def git_status():
    response = subprocess.run(["git", "status"], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files committed", style="success")
    else:
        console.print("Unable to commit files", style="error")
        sys.exit(1)


def git_push():
    response = subprocess.run(["git", "push"], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files committed", style="success")
    else:
        console.print("Unable to commit files", style="error")
        sys.exit(1)

def git_pull():
    response = subprocess.run(["git", "pull"], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files committed", style="success")
    else:
        console.print("Unable to commit files", style="error")
        sys.exit(1)

def git_branch():
    response = subprocess.run(["git", "branch"], capture_output=True)
    response_str = response.stdout.decode("utf-8")
    exit_code = response.returncode
    console.print(response_str, style="info")
    if exit_code == 0:
        console.print("Files committed", style="success")
    else:
        console.print("Unable to commit files", style="error")
        sys.exit(1)