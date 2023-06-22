from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Define the prompt template for weapon selection recommendation
weapon_template = '''Recommend a suitable weapon for the following scenario:
Scenario: {scenario}
Requirements: {requirements}'''

weapon_prompt = PromptTemplate(
    input_variables=["scenario", "requirements"],
    template=weapon_template
)

# Format the weapon selection recommendation prompt
weapon_prompt.format(
    scenario="Close-quarters combat",
    requirements="Stealth, high lethality"
)

# Initialize the language model and chain
llm = OpenAI(temperature=0.7)
weapon_chain = LLMChain(llm=llm, prompt=weapon_prompt)

# Run the weapon selection recommendation chain
weapon_chain.run({
    "scenario": "Close-quarters combat",
    "requirements": "Stealth, high lethality"
})
