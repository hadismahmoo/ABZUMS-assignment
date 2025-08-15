
from openai import OpenAI

try:
    with open("APIkey.txt","r") as file:
        OpenAI_API_key=file.read()
except FileNotFoundError:
    OpenAI_API_key=[]

AVALAI_base_URL= "https://api.avalai.ir/v1"

client=OpenAI(api_key=OpenAI_API_key,base_url=AVALAI_base_URL)

tone=input('Enter a tone for the conversation (e.g.,sarcastically,cheerfully,angrily.): ')


if tone.strip()=="":
    print("The input is empty.")
    

prompts=[
    {"role":"system","content":f"Respond {tone}"}
]

Exit_words={"quit","exit","stop"}

while True:
    user_message=input("\n enter your message (or quit or exit or stop ):  ")

    if user_message.lower() in Exit_words:
        print("End of conversation ")
        break

    if user_message.strip()=="":
        print("Your message is empty try again ")
        continue

    prompts.append({"role":"user","content":user_message})

    history=[]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=prompts
        )

        
        # print(response.choices[0].message.content)
        
        ai_message=response.choices[0].message.content
        history.append({"role":"assisstant","content":ai_message})
        print(history)


        

    except Exception as e:
        print("Error getting AI response:", str(e))

