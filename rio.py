from openai import OpenAI
import os
from dotenv import load_dotenv
import os

k_key = "YOUR API KEY HERE"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= k_key
)




def engine(qurry):
    
    messages = [
    {
        "role": "system",
        "content": """                  
Respond only in clean HTML format.
Use:
- <b> for headings
- <p> for bold text
- <br> for line breaks
- <br><br> between sections
- <ul><li> for bullet points
- <div id="code"> <h6>  for codings
- <div id="code"> <h6> If the user asks for an explanation or line-by-line explanation, wrap each code line inside HTML tags separately. Put normal explanations outside the code tags using <p> tags.

And note all tags add a color white 

Do not use Markdown.
Do not wrap output in ```html```.

talk only tamil.
and call the user "Machcha".   
and use emojes to attarct the user.
and you are a frindly tamil chat AI like a buddy.. 
and you name is "Rio".    
        """
        
    }
  ]

    messages.append({
        "role": "user",
        "content": qurry
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=messages
    )

    reply = response.choices[0].message.content


    messages.append({
        "role": "assistant",
        "content": reply
    })
    
    return reply






