import openai
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


openai.api_key = "YOUR_OPENAI_API_KEY"

# Define the prompt template with placeholders for company, challenge, as I discussed above
template = """ 
Did you know...? [Insert relevant statistic]

Learn how [Company Name] successfully addressed [the challenge faced] through their partnership with [Partner Organization]. 

* [Outcome/Benefit 1]
* [Outcome/Benefit 2]
* [Outcome/Benefit 3]

"[Insert impactful quote or testimonial]" - [Name], [Title],  [Company Name]

[Insert Call-to-action related to the specific case study] 
#[Relevant Hashtag 1] #[Relevant Hashtag 2] 
"""

# Create a PromptTemplate object
prompt_template = PromptTemplate(input_variables=["Company Name", "challenge", "Outcome/Benefit 1", "Outcome/Benefit 2", "Outcome/Benefit 3", "statistic", "quote", "Name", "Title", "Call-to-action", "Hashtag 1", "Hashtag 2"], template=template)

# Data input (tailor this based on your case study)
data_input = {
    "Company Name": "Sodexo",
    "challenge": "scalable leadership development across APMEA",
    "Outcome/Benefit 1": "Scalable coaching programs with AI/analytics",
    "Outcome/Benefit 2": "Access to diverse, certified coaches",
    "Outcome/Benefit 3": "Unlimited coaching for a hybrid workforce",
    "statistic": "75% of classroom-style training is forgotten if not implemented within 6 days.",
    "quote": "Our partnership with CoachHub has been transformative...",
    "Name": "Jean Baptiste CALEMARD",
    "Title": "Head of FMCG Accounts",
    "Call-to-action": "Join others on a journey of growth!",
    "Hashtag 1": "ExploreTheGreaterYou",
    "Hashtag 2": "leadershipdevelopment"
}

# Create LLM instance (feel free to adjust the OpenAI model as needed)
llm = OpenAI(temperature=0.5)  

# Generate the tailored social media post
response = prompt_template.format(data_input)
print(response)
