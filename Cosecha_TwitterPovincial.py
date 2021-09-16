import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
###API ########################
ckey = "JZzE4yYhd8kTJtutN3vvYUWkM"
csecret = "dJZCd2ioRdZGUPyAF3SeMrdCajMNUR9HQyyrzmvcE4eVqO3n9h"
atoken = "1420136431176015872-5oEJ6oVjzunqzcXFWzIrCV6rsZbnLl"
asecret = "tL1l2SHUGpmlwA90m9nFuLDP3jW8V1gQuC2s8SGzYvmWP"
#####################################
class listener(StreamListener):
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True
    def on_error(self, status):
        print(status)
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
'''========couchdb'=========='''
server = couchdb.Server('http://admin:1233tana@localhost:5984/')  #Conexion a couchdb
try:
    db = server.create('stadomingo')#si no esta creada esa base de datos se crea
except:
    db = server['stadomingo']#si a esta creada se trabaja con la misma

'''===============LOCATIONS=============='''


#twitterStream.filter(locations=[-80.1895,0.0058,-78.4625,1.203])#Tweets de esmeraldas
#twitterStream.filter(locations=[-78.9761,-0.38,-78.0986,0.1665])#Tweets de pichincha
#twitterStream.filter(locations=[-80.5454,-2.6936,-79.1355,-1.2032])#Tweets de guayas
#twitterStream.filter(locations=[-79.5875,-4.9818,-78.3016,-3.4528])#Tweets de zamora
#twitterStream.filter(locations=[-78.8536,0.0987,-77.9058,0.6344])#Tweets de imbabura
#twitterStream.filter(locations=[-81.1272,-2.5707,-80.1917,-1.6161])#Tweets de staelena
#twitterStream.filter(locations=[-80.8691,-1.8516,-79.7429,0.3615])#Tweets de manabi

twitterStream.filter(locations=[-79.6392,-0.6991,-78.7629,0.162])#Tweets de stadomingo
