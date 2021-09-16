# Proyecto-Analisis

El presente trabajo trata de implementar las distintas maneras de extraer datos de varias fuentes de información tales como web, bases de datos SQL y No SQL. 
El análisis es relacionado con el manejo de Elasticsearch y varias herramientas de visualización.

Pulso político por provincias en Ecuador(Tweets) - Iván Fraga

La extracción de datos se realizó mediante el script de Python Cosecha_TwitterPovincial.py
El cual se encargo de extraer los tweets de Twitter por geolocalización de varias provincias hacia CouchDB
EL proceso se repitío varias veces, debido a que se quería obtener un numero similar de tweets por provincia 

Una vez extraidos los tweets se realizo la configuración del archivo creacion_indices_couch_provincia.conf, el cual sirve para la carga de datos por medio de logstash.
Se levanta los servicios de cerebro, y dentro de una terminal ubicada en la carpeta bin de logstash se ubica el siguiente comando 'logstash -f creacion_indices_couch_provincia.conf'.
El archivo creacion_indices_couch_provincia.conf se modifico por cada base de datos almacenada en CouchDB.

La visualización de los datos presentados ahora en Cerebro, selo realizó por medio de Kibana, para ello se hizo una indexación por cada provincia y una indexación general,
posteriormente se crearon diversas visualizaciones tales como: tablas, nubes de palabras, diagramas, etc. Para un análisis óptimo de la información obtenida 

Pulso Politico en 20 cuidades del Ecuador (Facebook)-Denisse Cumbal

La extracion de  datos fue de la plataforma de Facebook mediante un script de Python 
El cual se encargo de extraer los datos de Facebook de las personas que estas en el política - diputados, presidente y mas por cuidad 
El proceso fue repetitivo para poder extraer lo datos (
Se analizo inicialmente ¿Quienes estan representando o trabajando por la cuidad, luego se busco perfil por perfil cuidad por ciudad extrayendo los datos
)
Una vez los datos recopilados y enviados a la base de Datos no estructurada Couchdb , mediante la herramienta de logstash , es posible envviar los datos de Coudb a elasticsearch que se encuentra en la nube para esto se configuro de antemano (Se habilito la cuenta de  elasticsearch en la nube para obtener las credenciales , luego en un block de notas ponemos un input {
  couchdb_changes {
    username => "******"
    password => "******"
    db => "guayaquil3"
  }
}output {
  elasticsearch {
    	
        hosts => "https:***************"
        user => "elastic"
        password => "*********"
        index => "couchdb_guayaquil"
    }
}
De esa forma podemos enviar los datos de una base de datos a otra base de Datos, para que funcione es importante que en la carpeta bin de logstash ejecutamos nuestro input y nuestro output, luego para la visualizacion usamo Power BI , se analizo los like por cuidad y podemos decir que las conclusiones son interesantes.
