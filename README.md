# Akash-Deployment-Gen CLI Tool

The Akash-Deployment-Gen CLI tool is designed to simplify the process of converting Docker Compose and Kubernetes deployments into [Akash deployments](https://akash.network). This tool automates the conversion, making it easier for developers to deploy their applications on the Akash decentralized cloud.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- An active Akash wallet 
- you need to create and fund an openai api account and generate an OPENAI_API_KEY ( we are still woring on the open source llm version of this )

Additionally, you must set the `OPENAI_API_KEY` and `OPENAI_MODEL_NAME` environment variables to use this CLI tool. You can obtain an API key from [OpenAI](https://platform.openai.com/api-keys).

## Installation
To install the Auto-Akash-Deployments CLI tool, follow these steps:

1. **Create and activate a new Conda environment:**

Ensure Conda is installed on your system. If not, follow the instructions on the [official Conda installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

After installing Conda, create a new environment by executing the following command in your terminal: `conda create -n akash-deployment-gen && conda activate akash-deployment-gen`

2. **Install the required Python packages:**

After activating your Conda environment, install the necessary Python packages by running the following command in your terminal: `pip install -r requirements.txt`

This command will install all the dependencies listed in the `requirements.txt` file, ensuring that you have all the necessary libraries and tools to use the Auto-Akash-Deployments CLI tool.


3. **Use cli tool to generate akash deployments **

Run an docker-compose example  `python akash_deployment_generation.py --input-file ./examples/dewy/dewy-docker-compose.yml --input-type docker-compose --github-repo-url https://github.com/DewyKB/dewy --output-file ./examples/dewy/akash_dewy.yml`
Run an kubernetes example  `python deployment_generation.py --input-file ./examples/dewy/k8s.yml --input-type k8s --github-repo-url https://github.com/DewyKB/dewy --output-file ./examples/dewy/akash_dewy.yml`


## Limitations 

This tool doesn't currently support rebuilding docker images and their start scripts to use make some k8s or docker compose services work on akash. 

If the k8s/docker compose container uses environment variables and ports in the entrypoint command this tool will not work without adding a new entrypoint script that can adjust the environment variables and port appropriately.

## Credits

This code uses langgraph and the language agent tree search [example](https://github.com/langchain-ai/langgraph/blob/main/examples/lats/lats.ipynb) to do the heavy lifting and duckduckgo for the search tool. 

[lats](https://arxiv.org/abs/2310.04406) is the current best coding chain of thought approach that doesn't use a code interpreter. 



