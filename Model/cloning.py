# Install gitpython if not already installed
# !pip install gitpython
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Example: install gitpython
install("gitpython")

import shutil
from git import Repo

local_path = "./"  # current folder
repo_url = "https://huggingface.co/openai/gpt-oss-120b"

# Delete folder contents (be careful!)
shutil.rmtree(local_path, ignore_errors=True)

Repo.clone_from(repo_url, local_path)
print("Repo cloned successfully!")




