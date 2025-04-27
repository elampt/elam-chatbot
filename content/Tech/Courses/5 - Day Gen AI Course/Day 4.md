# Domain Specific LLMs
# Cybersecurity - SecLM
## Applications
* **Security Analysts** LLMs could translate natural language into the syntax of complex query languages so that the analysts need not take hours doing it. It could help and automate the investigation and categorization of alerts
* **Chief Information Security Officer (CISO)** could use LLMs to generate clear summarizes of the threat landscape specific to their organization
* **IT Administrators and Security Teams** can use LLMs to get insights into potential attack pathways and get recommendations on the most effective preventative measures

## SecLM standards to be meet for security
* The threat landscape changes so rapidly, so they have to keep the model up to date #timeliness
* Has to be able to analyze sensitive user specific data without any risk of the data being exposed to the environment
* Has to be capable of multi-step reasoning

## Why are General Purpose LLMs fall-short when it comes to security needs
1. There's not a lot of publicly available high quality security data to train on the details of real world incidents, they are usually confidential
2. The sheer breadth and depth of security knowledge is another major obstacle

## SecLM Design
1. It starts with a very targeted training approach, they begin with a strong general purpose foundation model, needs to have multi-lingual support
2. Further pre-training with cyber security specific contents like blogs, threat reports, detection rules, full IT security textbooks etc.
3. **Supervised Fine Tuning :** Here, they train the model on tasks that mirror what security experts actually do in the real world do (User specific data is kept separate and only used within very specific fine-tuning tasks)
	* Analyzing potentially malicious groups
	* Explaining command line instructions
	* Inspecting security report logs
	* Summarizing complex threat reports
	* Generating queries for security management platforms

## Evaluation Metrics
1. Multifaceted approach for task where there's a clear right or wrong answer like classifying malware. Standard classification metrics are used
2. For more open-ended tasks, the model's outputs are compared to expert provided answers using different metrics to measure how similar the generated text is (**ROUGE, BERTScore**)
3. Human Valuators for qualitative feedback

## Fine-tuning
* Imagine we have a brand new security platform that wasn't part of the training data: 
	**In Context Learning :** We can give the model a few examples of how to interact with that platform and it can adapt really quickly

* If we want to incorporate our organization's unique network configurations or align the model's analysis with our internal expertise
	**PET (Prompt Engineering Tuning)** let's us do the lightweight customization without having to retrain the whole model

* **RAG :** Important for keeping the model up to date on the latest threat intelligence. It lets the model pull in information from external sources in real time

# Healthcare - MedLM
## GenAI in Healthcare
* Personalizing the patient experience
* Provide real-time feedback during consultation helping both the patient and clinician understand the key points

## Med-PaLM
**V1 :** First AI to surpass the passing score on USMLE style medical license exam
**V2 :** Further achieving expert level performance on the same exam. Significant improvements in the quality and depth of its long form answers as evaluated by physicians

## Evaluation Strategy
* Combine **Quantitative metrics** with **Qualitative assessments**. Use the USMLE style questions as a benchmark
* **MedPaLM** gave 67% passing score, **MedPaLM2** gave a 86.5% passing score
* **Qualitative Assessments** on things like the factual correctness on the information, the appropriate use of medical knowledge, the helpfulness of the response potential biases and the potential for harm
* Comparison with human experts for the same questions

## How is MedPaLM 2 trained ?
* It builds upon the base LLM **PaLM 2** and it's fine-tuned using a ton of medical question answering data
* They use a bunch of different prompting techniques for multiple choice questions 
	* **Few Shot Prompting**
	* **Chain Of Thought Prompting :** Encourages the model to show it's reasoning step which improves the accuracy
* **Ensemble Refinement :** Technique where the model takes into account it's own generated explanations and uses them to refine it's final answer. Learning from itself
