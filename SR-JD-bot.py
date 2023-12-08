Last login: Thu Dec  7 20:57:36 on ttys000
anthonyspadafino@anthonys-mbp-2 ~ % mkdir Python1
anthonyspadafino@anthonys-mbp-2 ~ % cd Python1
anthonyspadafino@anthonys-mbp-2 Python1 % vim SR-JD-bot.py




































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

job_desc("Sr. Product Manager"")
Entering Ex mode.  Type "visual" to go to Normal mode.
:
E501: At end-of-file
:.wq
E140: Use ! to write partial buffer
:
