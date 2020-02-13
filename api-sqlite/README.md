# HTTP YoloV3 Object Recognizer - HTTPYOR

  A aplicação consiste na administração de banco de dados a partir de requests HTTP.

## Instalação

Use [pip](https://pip.pypa.io/en/stable/) para instalar as dependencias e rodar a aplicação:

```bash
pip install -r requirements.txt
python app.py
```

ou utilize o Docker (é preciso configurar o xhost para dar acesso a camera):

```bash
sudo docker build -t api-sqlal .
sudo docker run -p 8081:8081 api-sqlal
```

## Uso

### Items

Endpoint: '/item'  

Metodo: POST  
Content-Type: application/json ou ausente  
Body: 
```text
[{
	"name":"Pão Puma",
	"value_unit": 4.3
},
{
	"name":"Pão Psssuma",
	"value_unit": 4.3
},
{
	"name":"Pão Pumssa",
	"value_unit": 4.34
}]
```

