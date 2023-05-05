import openai

openai.api_key="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"

def chat(mesg):
    res=openai.Completion.create(
        model='text-davinci-002',
        prompt=mesg,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7
    )

    return res.choices[0].text.strip()

while True:
    user=input("you : ")
    mesg = f"Me : {user} \nYou : "
    print("AI : ", chat(mesg))


