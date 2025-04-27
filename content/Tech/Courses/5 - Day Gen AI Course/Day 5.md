# MLOps for Generative AI
Operationalizing Generative AI

## Lifecycle of Generative AI system
1. Discover
	Finding the right tool for the job:
	1. **Quality :** How good is the model at actually doing what we need it to do (Benchmark scores, latency, costs, legal and compliance considerations etc.)
	2. **Vertex Model Garden :** Collection of a lot of models at one place to choose from
2. Develop and Experiment
	* Refinement of data, playing around with the model, evaluating the results
3. Evaluate
4. Deploy
5. Govern

## Prompted Model Component
* In traditional AI, we have a model and input and we are good to go
* But in Generative AI, we have an extra layer **The Prompt**. Often, we use a prompt template (Structured way of providing instructions and information to the model)
* It's the combination of the model and the prompt

## Chain & Augment
* Connecting multiple prompted model components together along with calls to some external APIs, custom logic etc. all working together to solve complex problems
* **Commonly known chaining pattern :**
	* **RAG :** Deals with the recency issue and hallucination, at the time of query we feed the relevant information to the model. Helps ground the model's response
	* **Agents :** They use the LLM as brain and interact with different tools. They can take actions based on the information they're processing 
	*   **VertexAI** helps build and manage these chains (Has integration with LangChain)

## Tuning Foundational Models
* Tuning is basically adapting the models to perform better on a specific task or in a specific domain
* **Supervised Fine Tuning :** Training a model on a labelled dataset
* **Reinforcement Learning from Human Feedback (RLHF) :** Use human feedback to train a reward model and then use that to guide LLM in the tuning process

## Data Practices 
* In traditional ML, data was everything
* With Generative AI, we can often build prototypes with very little data. We might need few examples, prompt template and start getting interesting results
* **Challenge :** 
	1. We're dealing with much wider range of data types now. We now have things like conditioning prompts, few shot prompts, etc. feeding into the system
	2. Need systems to manage, evolve, adapt and integrate all these different data types in a way they are reproducible, version-able and trackable. 

## Deploy
* **Version Control** - Need to track the evolution of prompt templates, chain definitions, external data sets that we use
* **Data Management** - Leveraging BigQuery and LADB, Vertex feature store for managing external data stores 
* **CI/CD** - Every code change should automatically be tested before it's merge. Need a reliable pipeline for moving tested code into production
* **Logging and Monitoring** - Since Generative AI involves chained components, we need to track the flow of data through the entire system, lineage tracking is very importang
* **Skewed Detection** - Comparing the distribution of the input data that we use to evaluate our system with the distribution of system in the production. If those distribution start to diverge, it means our system is not well suited for the data in the real world

# AgentOps
* In AgentOps, we are dealing with systems that are much more autonomous since they take decisions and take actions without human intervention
* Agents often interact with wide ranges of external systems and data sources, that's another challenge for security
* Limiting the set of tools specific to a task instead of letting the agent choose a random tool of it's choice
* Deploying agent to production - Involves robust CI/CD pipeline, automated tool registration, continuous monitoring, and an iterative improvement loop