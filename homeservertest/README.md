# homeservertest

## homeservertest server

Server development for science news site SPA.
Start of development


### Process

**Django** server gets its data from three web-sources through scraping. Loads this data into the **Postgresql** database.
At the client's request the server renders and responce **html** template.
The **html** template has a **JS** script. It requests the **Vue.js** application on the server to pass data to fill the article containers.
The **Vue.js** script receives data in **json** format from **Django Rest Framework** and passes it to the **html** template for rendering.


### Composition

* *Djangoproject*
* *datasite.py* - scraping module
* *Vue.js* - script gets the data from *Django Rest Framework* the  and passes it to the client side
* *Postgresql* - data base


### Basic tools
* Django
* PostgreSQL
* Beautifulsoup
* Django Rest Framework
* Vue.js


### Packages(pip_requirements.txt):
* asgiref==3.5.2
* beautifulsoup4==4.11.1
* certifi==2022.5.18.1
* charset-normalizer==2.0.12
* Django==4.0.4
* djangorestframework==3.13.1
* idna==3.3
* lxml==4.8.0
* Pillow==9.1.1
* psycopg2==2.9.3
* python-dateutil==2.8.2
* pytz==2022.1
* requests==2.27.1
* six==1.16.0
* soupsieve==2.3.2.post1
* sqlparse==0.4.2
* urllib3==1.26.9
