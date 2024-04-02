import argparse
import pyaml
import yaml
import os

# Setting up the argument parser
parser = argparse.ArgumentParser(description="Generate Akash SDL from Docker Compose or Kubernetes YAML")
parser.add_argument("--input-file", type=str, required=True, help="Path to the Docker Compose or Kubernetes YAML file")
parser.add_argument("--input-type", type=str, required=True, choices=['docker-compose', 'k8s'], help="Type of the input file ('docker-compose' or 'k8s')")
parser.add_argument("--github-repo-url", type=str, required=True, help="URL of the GitHub repository")
parser.add_argument("--output-file", type=str, required=True, help="Path to the output file for the generated SDL")

# Parsing arguments
args = parser.parse_args()
print("starting to create an akash yaml ... please wait for up to 2 minutes ")
assert os.environ["OPENAI_API_KEY"] != "", "Error you need to set env OPENAI_API_KEY to use this cli.  An open llm version is coming soon. you can get an api key from openai @ https://platform.openai.com/api-keys "
assert os.environ["OPENAI_MODEL_NAME"] != "", "Error you need to set env OPENAI_MODEL_NAME to use this cli we recommend using gpt-4-turbo-preview for this  "
from lats import apply_lats_and_save, write_file

if os.environ["OPENAI_MODEL_NAME"] != "gpt-4-turbo-preview":
    print(f"Warning! you are using {os.environ['OPENAI_MODEL_NAME']} as your llm model. We recommend using gpt-4-turbo for this tool for best results. ")

# Reading input YAML based on the input type
if args.input_type == 'docker-compose':
    with open(args.input_file, 'r') as file:
        input_yaml = file.read()
    conversion_type = "docker compose"
elif (args.input_type == 'k8s') or (args.input_type == 'kubernetes'):
    with open(args.input_file, 'r') as file:
        input_yaml = file.read()
    conversion_type = "Kubernetes"

final_prompt = f"""Write an akash sdl based on akash docs at https://akash.network/docs/ by converting a {conversion_type} file in the dewy github repo {args.github_repo_url} to its sdl equivalent. {input_yaml}"""
final_results = apply_lats_and_save(final_prompt, filepath="")

if "```yaml" in final_results:
    only_yaml = final_results.split("```yaml")[1]
    only_yaml = only_yaml.split("```")[0]
    with open(args.output_file, "w") as file:
        pyaml.dump(yaml.safe_load(only_yaml), file, sort_keys=False)
else:
    write_file(final_results, args.output_file)

# Example uses:
# For Docker Compose input:
# python akash_deployment_generation.py --input-file ./path/to/docker-compose.yml --input-type docker-compose --github-repo-url https://github.com/DewyKB/dewy --output-file ./path/to/output.yml
# For Kubernetes input:
# python akash_deployment_generation.py --input-file ./path/to/kubernetes.yml --input-type k8s --github-repo-url https://github.com/DewyKB/dewy --output-file ./path/to/output.yml
