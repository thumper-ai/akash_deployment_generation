# Akash-Deployment-Gen CLI Tool: Generate Akash SDL from K8s / Docker Compose files
**By Logan Cerkovnik, Founder of Thumper AI, April 1st, 2024** 

Converting between DevOps yamls formats for different cloud platforms is a relatively simple, but tedious task that is easily automated by LLM Agents.  The Akash Cloud deployment yaml format is unique to the platform and thus we created a tool to make it easier to migrate k8s deployment yamls and Docker Compose files to Akash's deployment format.

## What is the Akash-Deployment-Gen CLI Tool?
The Akash-Deployment-Gen CLI tool is a  python script designed to automate the conversion of Kubernetes (k8s) and Docker Compose configurations into Akash deployment manifests.  By doing so, it significantly lowers the barrier to entry for developers looking to leverage the Akash cloud without learning another single platform yaml DevOps deployment file format.  We automate this using a gpt-4-turbo powered LLM Agent.

### Key Features:
* Automatic Conversion: Seamlessly converts K8s deployments and Docker Compose files into Akash deployment manifests.
* Language Agent Tree Search (LATS): Utilizes SOTA code generation algorithms to generate yamls
* Search: Uses the DuckDuckGo search tool in LangGraph / LangChain to access Akash and target software documentation 

## Inspiration for this Tool
One of the primary hurdles in migrating workloads to the Akash Cloud involves converting existing k8s or Docker Compose files into Akash deployment YAML files, alongside guiding companies through the process of acquiring AKT or utilizing a crypto wallet. Thankfully, with the advent of LLM Agents, the conversion across numerous DevOps file formats has become easy to automate. Thumper can also be of assistance for enterprise customers interested in using Akash with the convenience of payments through conventional methods such as ECH or credit card rather than crypto.  Feel free to reach out to us at info@thumper.ai if you are interested.  Migrating cloud workloads to Akash is now easier than it has ever been before.

## How Does It Work?
At the heart of the Auto-Akash-Deployment tool are two cutting-edge technologies: Language Agent Tree Search implemented with LangGraph and Internet Search Tool Calling through the DuckDuckGo LangChain search tool.
### Language Agent Tree Search
Thie ingenious approach applies the famous Monte Carlo Tree Search Algorthim from reinforcement learning to chain of thought style prompting for LLM agents.  It is one of the most effective code generation methods to use without a code interpreter.  
### LangGraph
LangGraph is a library built on top of LangChain for letting llm agent systems do cycles or loops through processes. We also use the DuckDuckGo search tool from LangChain with our LATS agent. 

## Getting Started with the Auto-Akash-Deployment Tool
To demonstrate the power and simplicity of the Auto-Akash-Deployment CLI tool, let's walk through an example of converting a Docker Compose file into an Akash deployment manifest.
### Prerequisites
* Docker Compose file of your application
* Installed Auto-Akash-Deployment CLI tool
* Akash account and AKT tokens
### Step 1: Convert Your Docker Compose File
Run the following command in your terminal, replacing your-docker-compose.yml with the path to your Docker Compose file:

```python akash_deployment_generation.py --input-file ./examples/dewy/dewy-docker-compose.yml --input-type docker-compose --github-repo-url https://github.com/DewyKB/dewy --output-file ./examples/dewy/akash_dewy.yml```

This command generates an Akash deployment manifest based on your Docker Compose configuration.
### Step 2: Deploy on Akash Network
With your Akash deployment manifest ready, you can now deploy your application on the Akash Network using the Akash CLI:

Run the following command in your terminal or head to the the [akash console](https://console.akash.network), replacing `your-docker-compose.yml` with the path to your Docker Compose file:
`akash tx deployment create your-deployment.yml --from <your-wallet> --chain-id akashnet-2 --node https://rpc.akash.forbole.com:443 -y`

### Step 3: Test Your Deployment
After your deployment is live, you can interact with your application and test its functionality through the Akash console. This allows you to verify that the conversion process has successfully maintained your application's behavior and performance.

## Conclusion
The Akash-Deployment-Gen CLI tool should be able to make migrating to the Akash Network easier for everyone.  We encourage devs to explore the capabilities of the Auto-Akash-Deployment tool and experience firsthand the benefits of deploying on the Akash Network.  Feel free to open an issue if you have any bugs or feedback on the tool. 

If you create new Akash Deployments, you can share them with the community by submitting a deployment to the [awesome akash community repo](https://github.com/akash-network/awesome-akash)

#### About Thumper:
Thumper is a Generative AI company offering products and consulting services to make Generative AI cheaper and more accesssble for our customers. For companies interested in saving 75% or more on GPU servers relative AWS, Thumper can offer the convenience of payments through conventional methods such as ECH or Credit Cards rather than AKT on Akash.  For more details, feel free to reach out to us at info@thumper.ai .