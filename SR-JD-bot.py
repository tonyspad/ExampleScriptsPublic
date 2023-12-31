
import os
import openai
from openai import OpenAI

client = openai.OpenAI(
    api_key= ('OPEN-AI-KEY-HERE'),
    organization= ('org-KEY-HERE')
)

def MLE():
    header = "Staff Machine Learning Engineer"
    subheader = "New York, New York | San Francisco, CA"
    about = (
        "About the Role\n"
        "A marketplace can grow if there is a balance between supply and demand. Selection is the key differentiating factor which will bring more eaters to the platform and create a flywheel effect of generating order volume which will add value to merchants to stay and grow with Uber. The team’s mission is to improve selection from both eater and merchant lens by executing on strategic growth and profitability levers which will keep the flywheel moving and create the network effect.\n"
        
    )
    comp = (
        "Compensation\n"
        "FOr San Francisco, CA-based roles: The base salary range for this role is $174,000 per year - $193,500 per year./n" 
        "For New York, NY-based roles: The base salary range for this role is USD$207,000 per year - USD$230,000 per year./n"
        "You will be eligible to participate in Uber's bonus program, and may be offered an equity award & other types of comp. You will also be eligible for various benefits. More details can be found at the following link https://www.uber.com/careers/benefits.\n"
        
    )
    qualifications = (
        "* Bachelor in Computer Science, Engineering, Mathematics or related field and 8-years full-time as a Machine Learning Engineer or Software Engineer, working on building data pipelines, training and deploying machine learning models in production on a daily basis\n"
        "* Experience with writing, releasing, and working in large distributed systems, deep learning or/and natural language processing is a big plus.\n"
        "* Experience analyzing a feature in production using analytics and experiments.\n"
        "* Experience in using Python (pandas, scipy, or numpy, etc) for scientific computations and object-oriented programming.\n"
        "* Experience in using SQL (Presto, Hive, or Spark, etc) for data querying and ETL.\n"
        "* Experience in applying machine learning models to solve real-world problems.\n"
        
    )
    


    return f"{header}\n\n{subheader}\n\n{about}\n\n{comp}\n\n{qualifications}"


def job_desc(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        temperature=0.4,
        messages=[
            {"role": "system", "content": "You are a Recruiting assistant for a software company called Uber that is in the ridesharing and delivery space. You create job descriptions of open roles to attract potential candidates to apply."},
            {"role": "user", "content": "Staff Machine Learning Engineer"},
            {"role": "assistant", "content": MLE()},
            {"role": "user", "content": prompt}
    ]
)


    reply_content = completion.choices[0].message.content
    print(reply_content)

job_desc("Operations Manager")
