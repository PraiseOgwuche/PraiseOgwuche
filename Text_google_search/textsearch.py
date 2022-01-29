import bs4
import json
import requests
import googlesearch
import os
os.system("clear")




class Paragraph:
    def __init__(self, paragraph):
        self.text = paragraph
        self.length = len(self.text)
    def __repr__(self) -> str:
        return f"Paragraph({self.length})"

class Result:
    def __init__(self, link):
        self.link = link
        result = requests.get(self.link).text
        soup = bs4.BeautifulSoup(result, "lxml")
        paragraphs = soup.find_all("p")

        self.paragraphs = [Paragraph(p.text) for p in paragraphs]
    def __len__(self):
        return len(self.paragraphs)
    def __repr__(self):
        return f"Result{len(self.paragraphs)}"

class JointResult:
    def __init__(self, query):
        self.query = query
        q = "+".join(self.query.split())
        url = f"https://www.google.com/search?q={q}"
        self.links = googlesearch.search(url,num_results=3)
        #print(self.links)
        self.results = [Result(l) for l in self.links]

if __name__ == "__main__":
    
    query = "top 10 anime"
    jr = JointResult(query)
    #print(jr.results[0].paragraphs) 
    for p in jr.results[0].paragraphs:
        print(p.text)


