import pyttsx3
import os
import sys
from groqai import askAi,fakeReply
import webbrowser as wb
from speech import say
websites = ["instagram","youtube","facebook","chatgpt","deepseek","tiktok","messenger"]
apps = ["vs code"]



def  processAi(q):
        ai = askAi(q)
        if ai == None:
            return
        if "[system]" in ai:
            try:
               ai = ai.replace("```","#")
            #    compiled_code = compile(ai, "<dynamic-string>", "exec")
               exec(ai)
               say(fakeReply(f"ai has completed query : {q} give a line of text like task done sir that will be sent to user to notify this "))
               print(ai)
               return
            except BaseException as se:
               say(askAi(f"the ai provided this {ai} and it gave syntax err {se} notify user their query : {q}"))
               print(f"{ai} error : {se}")
               return 
 
        return say(ai)
       

def processquery(q):          
    if q and "open" in q:

        for app in apps:
            if app in q:
                say(f"Opening {app}")
                os.startfile(r"C:\Users\Saugat\OneDrive\Desktop\Visual Studio Code.lnk")
                return
        for site in websites:
            if site in q:
              say(f"Opening {site}")
              wb.open(site + ".com")
              return
        # say("Sorry i cant open that")
        # return   
    processAi(q)