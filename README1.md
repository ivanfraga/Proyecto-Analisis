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


Temática Libre (Kaggle)- David Cacuango

Para este punto se extrajeron datasets de kaggle, después se subió manualmente todos los archivos .csv a la base de datos de MySql,
en este caso se extrajeron tres datasets los cuales son: Medallas, Atletas, Equipos. Posteriormente con la herramienta de logstash 
atreves del archivo de configuración “creacion_indices-Mysql_Elastic,JuegosOlimpicos.conf” se pasaron todos los datos a elasticsearch 
el punto importante que tenemos que tener en cuenta es que se debedescargar el conector de .jar que nos provee MySql, y dentro del
archivo de configuración poner la ruta de donde se encuentra.

Una vez pasado los datos, procedio a visualizar mediante la herramienta de Tableau, lo cual nos permitió sacar unas breves conclusiones 

Pulso político por provincias en Ecuador(Web scraping) – Luis Catota

La extracción de datos se realizó a través de un script de Python. El cual se encargó de extraer los títulos y una corta descripción de noticias
del portal oficial de “EL comercio”(Diario nacional y empresa de medios de comunicacion en Ecuador) acerca de la inclinación política en varias provincias del país. 

Los datos recopilados fueron dirigidos hacia una base de datos NOSQL (MongoDB). EL proceso se repitió en varias ocasiones para obtener más datos. 
Una vez extraídos los datos se creó el plugin “webmongodb.conf“, el cual sirve para  cargar los datos por medio de logstash además se levantaron los servicios de
“cerebro”, y dentro de una terminal ubicada en la carpeta bin de logstash se ejecuta el siguiente comando 'logstash -f webmongodb.conf', de este modo se visualizaron
los datos dentro de cerebro.

Finalmente para analizar y presentar los datos de mejor manera usamos herramientas más completas como lo son elasticsearch y tableau public las cuales nos 
proporcionaron resultados satisfactorios. 


Temática Juegos por el Mundo - Erick Andrade

Se descargo un dataset en la pagina oficial de Kaggle que luego se paso los datos hacia Sql Server y verificar que el dataset me servia para el proposito. Hecho la carga se verifico que los datos no esten corrompidos, para lo cual se corrio una sentencia para determinar la información de los datos. Puesto, que no se encontro impurezas en el dataset se exporto el archivo para phpMyAdmin para darle un mejor control de la información al crear un usuario y contraseña para la información a traves de la plataforma de phpMyAdmin. Despues, se configuro el archivo de logstash para su subida para elasticsearch que previamente se incializo desde las carpetas y bin con la posterior conexión local. Tal y como se ve en la figura:
```json
input {
	jdbc {
		jdbc_connection_string => "jdbc:mysql://localhost:3306/erick"
		jdbc_user => "erick2"
		jdbc_password => "erick2"
		jdbc_driver_class => "com.mysql.jdbc.Driver"
		jdbc_driver_library => "X:\ELK\logstash-7.14.0\lib\Connector J 8.0 (1)\Connector J 8.0\mysql-connector-java-8.0.7-dmr-bin.jar"
		statement => "SELECT * FROM ps4_gamessales"
	}
}
output {
	stdout { codec => json_lines }
	elasticsearch {
		"hosts" => "localhost:9200"
		"index" => "mysql"
		"document_type" => "data" 
	}
}
```
Es importante escoger el conector de la libreria oficial de jdbc, luego que este codigo se ejecute en el bin de logstash ```logstash -f json.conf``` se procede a utilizar la herramienta de Power BI Desktop para posteriormente escoger la data en la opcion de ODBC y conseguir "elasticsearch" como local. A partir de allí se manipula la data, tomando sumo cuidado cuales valores son los necesarios para evaluar sin necesidad de colocar toda la data. Ahora con las grafícas resaltadas las que son por el caso de estudio se evaluan y saca concluciones certeras. 

