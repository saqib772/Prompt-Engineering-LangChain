# **Lang Chain and Prompt Engineering**

This repository contains source code for Lang Chain and Prompt Engineering, aimed at providing a user-friendly interface for non-technical users to interact with advanced language models. The code simplifies the process of generating human-like responses and performing language-related tasks using OpenAI's GPT-3.5 model.


## **Universe Advisor**

The LangChain library allows you to harness the power of the language model by acting as a universe advisor for common people. With just a few lines of code, you can easily explain various topics related to the universe that people commonly inquire about. By providing a simple prompt and specifying the desired universe topic, such as "Time travel," you can receive informative responses in a way that is easy for non-technical users to understand.

Example:

```
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Define the prompt template
temp = '''I want you to act as a Universe Advisor for Common People. In an easy way, explain the topics people ask about {universe_topic}'''

#See The Prompt_eng.ipynb file for code

```
## **Language Translation**

In addition to providing universe-related information, the LangChain library also enables easy language translation. With a simple template, you can translate a given sentence into the target language of your choice.

Example:

```
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Define the prompt template
temple = '''In an easy way, translate the following context {sentence} into {target_language}'''
language_prompt = PromptTemplate(input_variables=["sentence","target_language"], template=temple)

#See The Code File For More
```

## **Prompt Engineering with Few-Shot Learning**

Prompt engineering is an essential technique to improve the performance of language models. The LangChain library provides support for prompt engineering with few-shot learning, allowing you to ask questions and receive informative answers. You can easily set up prompt templates with examples and generate accurate responses.

Example:
```
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Define examples for few-shot learning
examples = [
    {
        "question": "Who lived longer, Muhammad Ali or Alan Turing?",
        "answer": """
        Are follow-up questions needed here: Yes.
        Follow-up: How old was Muhammad Ali when he died?
        ## ......
    }]

# See the code for more

```

