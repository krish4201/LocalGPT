# Install gitpython if not already installed
# !pip install gitpython

from git import Repo

# URL of the Hugging Face repository
repo_url = "https://huggingface.co/openai/gpt-oss-120b"
# Local path where you want to clone the repo
local_path = "./"

# Clone the repository
Repo.clone_from(repo_url, local_path)

print(f"Repository cloned to {local_path}")
