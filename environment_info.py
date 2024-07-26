# environment_info.py

import platform
import subprocess

def get_os_info():
    os_info = platform.uname()
    return {
        "system": os_info.system,
        "node_name": os_info.node,
        "release": os_info.release,
        "version": os_info.version,
        "machine": os_info.machine,
        "processor": os_info.processor,
    }

def get_python_version():
    return platform.python_version()

def get_git_branch():
    try:
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def main():
    os_info = get_os_info()
    python_version = get_python_version()
    git_branch = get_git_branch()

    with open("environment_info.txt", "w") as f:
        f.write(f"OS Info: {os_info}\n")
        f.write(f"Python Version: {python_version}\n")
        f.write(f"Git Branch: {git_branch}\n")

if __name__ == "__main__":
    main()