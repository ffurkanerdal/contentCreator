import requests

api = "" # Write your API

class AskMe:
    def __init__(self) -> None:
        self.url        =   'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='+api
        self.headers    =   {
            "Content-Type"  :   "application/json"
        }
        
    def getText(self,que):
        data       =   {
            "contents"  :   [{
                "parts" :   [{
                    "text" :   que
                }]
            }]
        }
        response    =   requests.post(self.url,headers=self.headers,json=data)
        text        =   response.json()["candidates"][0]["content"]["parts"][0]["text"]

        
        return text


create = AskMe().getText
