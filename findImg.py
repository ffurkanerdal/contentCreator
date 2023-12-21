import requests,random

unsplash_api    =   "" # Write your Unsplash API

class Unsplash:
    def __init__(self,query):
        self.url        =   "https://api.unsplash.com/search/photos"
        self.params     =   {
            "query" :   query,
            "page"  :   5,
            "per_page":   20,
            "order_by"  :   "relevant"
        }
        self.headers    =   {
            "Authorization" :   f"Client-ID {unsplash_api}"
        }

    def getPhoto(self):
        self.response = requests.get(self.url, headers=self.headers, params=self.params)
        
        if self.response.status_code == 200:
            data = self.response.json()
            url_list = []
            
            if "results" in data:
                for photo_info in data["results"]:
                    photo_url = photo_info["urls"]["regular"]
                    url_list.append(photo_url)
                return url_list
            else:
                return "NotFound"
        else:
            return self.response.status_code
    
    def downPhoto(self):
        urls = self.getPhoto()
        k = min(3, len(urls))
        photos  =   random.sample(urls,k=k)
        for i in photos:
            try:
                response    =   requests.get(i)
                if response.status_code==200:
                    with open(f"file{random.randint(1,100)}.webp","wb") as file:
                        file.write(response.content)
                        
                else:
                    return "Dont Download"

            except Exception as e:
                return "Hata"+str(e)


image = Unsplash





