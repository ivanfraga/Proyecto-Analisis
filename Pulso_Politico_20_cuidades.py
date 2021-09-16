#!/usr/bin/env python
# coding: utf-8

# In[5]:


from facebook_scraper import get_posts
import couchdb
import json
import time


# In[6]:


couch=couchdb.Server('http://CUMBAL:12345@127.0.0.1:5984')


# In[7]:


db = couch.create('guano3')


# In[8]:


i=1
#for post in get_posts('ecuarauz2021', pages=1000, extra_info=True):
#for post in get_posts('RodrigoFajardoAsamblea12', pages=1000, extra_info=True):cuenca
#for post in get_posts('fernanda.mashi.ec', pages=1000, extra_info=True):machala
#for post in get_posts('pameaguirreoficial', pages=1000, extra_info=True):ibarra1
#for post in get_posts('patriciocervantesCREO', pages=1000, extra_info=True):ibarra2
#for post in get_posts('byronmaldonado21', pages=1000, extra_info=True):loja
#for post in get_posts('HumbertoAlavaradoEspinel', pages=1000, extra_info=True):los rios
#for post in get_posts('JoaoAcunaF', pages=1000, extra_info=True):manabi
#for post in get_posts('FerCabascangoOficial', pages=1000, extra_info=True):quito
#for post in get_posts('RicardoChavez.Valencia79', pages=1000, extra_info=True):santo domingo
#for post in get_posts('RositaBelenMayorgaT', pages=1000, extra_info=True):Ambato
#for post in get_posts('RinaCampainAsambleista', pages=1000, extra_info=True):esmeraldas
#for post in get_posts('RafaelLuceroASAMBLEISTA', pages=1000, extra_info=True):riombamba
#for post in get_posts('LuisAlmeidaMoran', pages=1000, extra_info=True):guayaquil
#for post in get_posts('sofiaespinrc', pages=1000, extra_info=True):daule
#for post in get_posts('RonnyAleagaSantos', pages=1000, extra_info=True):duran
#for post in get_posts('DaltonBacigalupoB', pages=1000, extra_info=True):Latacunga
#for post in get_posts('AnaHerrera.RC', pages=1000, extra_info=True):Salcedo
#for post in get_posts('PeterCalo2021', pages=1000, extra_info=True):la mana
#for post in get_posts('marjoriechavezm', pages=1000, extra_info=True):sangolqui
#for post in get_posts('RocioGuanoluisaAsambleista', pages=1000, extra_info=True):pedro moncayo
#for post in get_posts('MarceHolguinec', pages=1000, extra_info=True):cayambe
for post in get_posts('jorgeyundamachado', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




