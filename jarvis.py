import speech
import queryprocessor
import groqai as g
speech.say(g.fakeReply("you have to reply user a line of text its for when the ai asistant loads firstly"))
# import requests
# def askAi(q):
#    r = requests.post("https://api.groq.com/openai/v1/chat/completions",
#     json = {
#         "model" : "openai/gpt-oss-20b",
#         "messages": [{
#             "role":"user",
#             "content" : 
#         },{
#             "role" : "System",
#             "content" : ""
#         }]
        
#     },
#     headers={
#             "Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx"
#     }
#     )
#    response = r.json()['choices'][0]['message']['content']
#    response = response.replace("*","")
#    return response

while True:
    # valid = False 
    q = speech.query().lower()
    queryprocessor.processquery(q)
    