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

# URL of the Hugging Face repository
repo_url = "https://huggingface.co/openai/gpt-oss-120b"
# Local path where you want to clone the repo
local_path = "./"

# Clone the repository
Repo.clone_from(repo_url, local_path)


print(f"Repository cloned to {local_path}")
