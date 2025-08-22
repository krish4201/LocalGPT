# Install gitpython if not already installed
# !pip install gitpython
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Example: install gitpython
install("gitpython")

from git import Repo

repo_url = "https://huggingface.co/openai/gpt-oss-120b"
local_path = "./gpt-oss-120b"  # NEW empty folder

Repo.clone_from(repo_url, local_path)
print(f"Cloned to {local_path}")


