# django-televendas
Projeto Final da Aceleração Python para Web realizado pela Codenation  
[Descrição do Projeto](description.md)  

### INSTALL  
- Clone o repositório.  
`git clone https://github.com/codenation-dev/squad-6-ad-python-2.git`  
`cd squad-6-ad-python-2`  
- Instale as dependências.  
`pip install -r requirements.txt`  
- Construa o banco de dados.  
`python manage.py migrate`  
- Carregue os dados de exemplo  
`python manage.py loaddata televendas.json`  
- rode o servidor.  
`python manage.py runserver`  

### Test  
`python manage.py test`  


Recomendável criar um ambiente virtual para desenvolvimento.  
`python3 -m venv venv`  
`source venv/bin/activate`    

