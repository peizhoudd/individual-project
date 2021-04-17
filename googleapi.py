import requests as req
import re
class GoogleNavigation():
    def __init__(self):
        self.apikey="AIzaSyAni6-Fnvcn5lPL4ktloi3epdBYyHvP1aw"

    def getdirect(self,paramStarts,paramEnd):
        dir=req.post("https://maps.googleapis.com/maps/api/directions/json?origin="+paramStarts+"&destination="+paramEnd+"&key="+self.apikey).json()
        htmlre=re.compile('>(.*?)<')
        i=dir["routes"][0]["legs"][0]["steps"]
        ret=""
        for tem in i:
            rtn=rtn+"---"+''.join(htmlre.findall(tem["html_instructions"]))
        return rtn
