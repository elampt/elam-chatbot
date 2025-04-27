# Intro Unit – “Foundational Large Language Models & Text Generation”

# Podcast

# Large Language Models


## Transformer(Neural Model) Architecture - Foundation for most model LLM's
- Has Encoder(Input) and Decoder(Outputs Token)
- Transformers transform all the tokens at the same time, need to do positional encoding to ensure the order of appearance of the tokens 
- "The tiger jumped out of a tree to get a drink because it was thirsty". We make the model to figure out that "it" refers to the tiger
	- The model compares all the tokens with each other to get the similarity between each, with this value, we infer that "it" has the most similarity with "tiger"
* Input text -> Tokens -> Vector Embeddings -> Output
* Many new LLM's have Decoder only model
	* Encoders main part is only to create a representation for the whole input sequence upfront. Whereas, Decoder directly provides output token by token
	* Can be used for Generating Text
* **MoE (Mixture of Experts)** - Set of expert models, for any given input, the required expert models alone gets called. Offers better efficiency 

## The Timeline
* GPT1 - Open AI - 2018 - Decoder Only
	* They did Unsupervised pre-training on the data, then fine-tune for specific tasks
	* Limitation: It would get stuck repeating same text, wasn't good for long conversations
* Bert - Google - 2018 - Encoder Only
	* Focused on understanding language, not generating it
* GPT2 - Open AI - 2019 
	* Web Text Corpus dataset training
	* Better coherence, could learn new tasks before even training it particularly for it (**Zero short learning**)
* GPT3
	* 175 billion parameters
	* Got better at **few shot learning**
* GPT3.5
	* Can understand and write code
* GPT4
	* Game changer. True Multimodal model
* Lambda - 2021
	* Google conversational AI. More about dialouges
* Gopher - DeepMind
	* Decoder only model
	* Used for knowledge intensive tasks
* GLAM - Google
	* Better performance with less computing power
* Chinchilla - DeepMind - 2022
	* 70 billion parameter model, was trained on a much scaled data which in turn gave better results
* Paulm, Paulm 2 - Google - 2022, 2023
	* Was better at reasoning, coding, math. Foundation of most of Google's current GenAI
* Gemini - Google
	* Multimodal from start, pushing boundaries
	* Designed to handle images, videos, audios. Run's on google TPU (Tensor Processing Units)
* **Open Source Models**
	* Gemma, Gemma 2 - Google
		* Has huge vocabulary, lightweight
	* Lamma - Meta
		* Reasoning, coding, safety enhancements
	* Mistral - Mistral AI
		* Math, coding, multilingual tasks
	* AI 01 - OpenAI
	* DeepSeek
		* Group relative optimization policy
	* Grock 3 - X AI

## Fine-Tuning (Cost x Performance x Efficiency)
All the above foundational models are built using the **Transformer Architecture**, but they need to be tailored for specific tasks

**The Training process :**
1. **Pre- Training**
	Feed the model tons of data just raw text, helps it learn the grammar and vocabulary of language<br>

	Take the pre-trained model with General knowledge, train it further with smaller more specific data in a particular domain <br>

	**SFT (Supervised Fine Tuning)**
	Main technique for training models on labelled examples. Helps model to learn and perform the specific task. Teaching it how to behave<br>

	**Reinforcement Learning With Human Feedback (RLHF)**
	Teaching it to generate responses that humans prefer. This reward model is used to fine tune the model using Reinforcement Learning<br>

	**Fine-Tuning can be so expensive ($)**
    To overcome this, **PFT** (Parameter Efficient Fine-Tuning: To only train a small part of the model leaving most of the pre-trained weights Frozen)
    1. **Adapter-based fine-tuning:** Add small modules called **Adapters** into the model and we only train the parameters within those adapters
    2. **Low-rank Adaptation (or) LoRA:** We use low-rank matrices to approximate the changes we would make to full fine tuning. Drastically reduces the number of parameters that we need to train
    3. **Soft Prompt :** The small set of trainable vectors **Soft prompt** which we add to the input, which we can specifically optimize without changing the original weights

## Prompt-Engineering
Once we have a find-tuned model, need **Prompt Engineering** to use it fully
* Prompt Engineering is about designing the **input** that we give to the model
* It makes a huge difference in the response of the model
1. **Zero shot Prompting**
	Give the model a direct instruction or question without any example
2. **Few shot Prompting**
	Give the model a few examples to tell what kind of response you are looking for 
3. **Chain Of Thought Prompting**
	For more complex reasoning tasks, we show the model how to think step-by-step

**Sampling Techniques** Way the model generates text <br>
1. **Greedy Search** Model always picks the most likely next token. Fast, but may lead to repetitive outputs
2. **Random Search** More random, can lead to more creative output. 
	**Higher Temperature - More Randomness**
	**Top K** Limits the model's choices to the top K most likely tokens, to control the output
	**Top P** Nucleus sampling - Uses dynamic threshold based on the probabilities of the tokens
	**Best of n** Generates multiples responses and picks best one based on some criteria

## Evaluating the LLM's
In the context of text generation (Something that is open-ended), we cannot use the traditional metrics like accuracy, f1 score etc.

**Requirements for a good Evaluation framework for LLM's:**
1. Must be multifaceted, need data specifically designed for the task we're evaluation. Should use real user interaction data, synthetic data to cover all kinds of situations
2. Cannot evaluate the model in isolation, should consider the whole system of which the model is a part of. For example, in cases of an Agent, should consider the entire agent's use case
3. Define what good actually means for our specific use case (Like, accuracy, creativity etc.)

**Methods used :**
1. BLEU (or) ROUGE like traditional metrics can still be used. But, they don't always capture the nuances of language. Sometimes a creative or unexpected response might be just good or even better than the expected one
2. Human Evaluation is good, but time consuming. So, people are using LLM powered autorater. We give the autorater model the task, the evaluation criteria and the response generated by the model, it then gives a score with reason for judgement. We need to calibrate the autorater regularly

## Accelerating the Inference of models
1. **Balance :** Balance the quality of output with the speed and cost of generating it
2. **Output Approximating Methods :** Changing the output slightly to gain efficiency.
	1. **Quantization :** Reducing the numerical precision of models's weights and activations.  Instead of using 32-bit integers, use 8 or 4 bit integers 
	2. **Distillation :** Train a smaller (Student - Faster and efficient) model to mimic a larger (Teacher) one
		1. Data distillation
		2. Knowledge distillation
		3. On Policy distillation
3. **Output Preserving Methods:** Keeps the output the exactly same, but tries to optimize the computations 
	1. **Flash Attention :** Designed to optimize the self attention calculations within the Transformer. Minimized the amount of data movement needed during those calculations which can be a bottle neck. Doesn't change the result of the attention computations, but just the way it's done
	2. **Prefix Caching:** Especially used in conversational applications. Saves time when we have repeated parts of input. Cache the results of attention calculations of parts of the input so that it need not be calculated again
	3. **Speculative Decoding:** Clever, use a smaller, faster drafter model to predict a bunch of future tokens. The main model checks the predictions, if the drafter is right, we can accept those tokens and skip the calculations for them which speeds up the decoding process
	4. **Batching:** Process multiple requests at the same time instead of doing it one by one
	5. **Parallelization:** Splitting up the computation across multiple processors and devices

## LLM Use Case in practice:

**Code and Math**
1. Code generation (**AlphaCode - Google**)
2. Completing code
3. Refactoring, debugging, documentation
4. Understand large codes
**Machine Translations**.
**Tech Summarization**.
**Question Answering Systems using RAG**.
**ChatBot systems**.
**Content Creation**.
**Natural Language Inference - Sentimental Analyis**.
**Text Classification - News, spam classification**.
**Autoraters**.
**Multimodal LLM's - Text + Audio + Video for education, business + more**.

---- 
# Prompt Engineering
## Output Length
The number of tokens the model generates directly impacts cost and processing time
* Need to engineer our prompt to be more targeted to get a concise response

## Sampling
### Temperature 
* Dial that controls the randomness
* **Low Temperature :** Predictable, Precision, deterministic output
* **High Temperature :** Introduced more randomness, to get a more creative, unexpected results

### Top K
* We consider only the top K most likely options for the output
* **Higher K :** More variety in the output
* **Lower K :** More focused
* **K = 1 :** Deterministic best guess

### Top P (Nucleus Sampling)
* Probability instead of fixed numbers, it selects the smallest set of words whose probabilities add up to at least the value of P
* **Lower P :** Makes output more restrictive
* **P closer to 1 :** Considers almost all possible words

### Case where we include all three in mix
1. **Temperature + Top P + Top K :** Model first looks for words that meet both Top P and Top K criteria, then **Temperature** setting influences the final choice among those filtered words
2. **Top P + Top K :** Just filters by which ever one is active, with no temperature setting, the model randomly choses from those that passes the filter 

> [!TIP]

| Value       | Benchmark Recommendation | More Variety | Single Answer |
| ----------- | ------------------------ | ------------ | ------------- |
| Temperature | 0.2                      | 0.9          | 0             |
| Top P       | 0.95                     | 0.99         |               |
| Top K       | 30                       | 40           |               |

## Prompting Techniques
### Zero shot prompting (or) General Prompting
* We're give the model a task description and input without any examples
### One shot (or) Few shot prompting
* We provide examples within the prompt to guide the model
* Model learns from the examples and gets a much clear understanding
* Quality and relevance of model are very important (GIGO)
* Also, can include examples of edge cases to make the solutions more robust
### System Prompting
* Can be used to specify output requirements like "Output all predictions as a Json object with specific keys"
* Setting the overall context and purpose of the prompt
### Role Prompting
* Giving the LLM a specific persona or identity
* Can prompt the model to be a Technical Writer to get a specific document
### Contextual Prompting
* Providing more specific background information that's relevant to the task at the hand
* Ex: To debug a code, we provide the code snippet, where the bug is, what libraries we are using
* The more context we provide, the more relevant the model will behave
### Step Back Prompting 
* First ask LLM to answer a broader question before diving into the detail of our specific question
### Chain Of Thought Prompting
* Idea is to prompt the model to explicitly generate the intermediate reasoning steps before giving the final answer or code solution
* Instead of just getting the solution, we also see the models thought process on how it arrived to the solution
* It uses more tokens -> Higher cost 
* **Self Consistency :** Make the model to generate multiple reasoning paths for the same prompt and then we choose the most consistent answer across those paths (Worth for high stake tasks)
### Tree Of Thought (2T)
* A generalization of COT, the LLM explores multiple reasoning paths simultaneously rather than just a single COT. The model branches out
* More creative problem solving
### ReAct (Reason And Act)
* Combining the LLM's reasoning capabilities with the ability to use external tools like search engines, code interpreters or even API's
* Example: A model uses a web search to gather some information and make decisions accordingly
### APE (Automatic Prompt Engineering)
* Automating the creating of essential prompts
* Ask the model to generate various prompt variations for a task and then we evaluate those variations based on their performance
### Code Prompting
* Prompts for writing particular codes
* Prompts for explaining codes
* Translating code from one language to another
* Prompts for debugging and reviewing code
### Multimodal Prompting
* Inputs like images, audios

## Best Practises
1. Provide Examples
2. Design with simplicity - Clear, simple, easy to understand
3. Be specific about the desired output
4. Use instructions over constraints (Focus on positive instructions)
5. Control max. token length
6. Use variable in Prompts (Dynamic prompts that we can use for various use cases)
7. Use schema if you are working with specific data formatting
8. Document the various prompt attempts - Allows to track our progress




