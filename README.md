# API - SQLAlchemy - Payments

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

O script para a criação das tabelas encontra-se no arquivo create_tables.py. São trẽs tabelas: items, payments e uma associativa payment_items.

### Items

Endpoint: '/item'  
Metodo: POST  
Content-Type: application/json
Body: 
```text
[{
	"name":"Pão Puma",
	"value_unit": 6.3
},
{
	"name":"Bolacha traquinas",
	"value_unit": 2.5
},
{
	"name":"Macarrão",
	"value_unit": 2.34
}]
```

Endpoint: '/item/<item_id>'
Metodo: DELETE  
Content-Type: application/json
Body: Não aplicável


Endpoint: '/item'  
Metodo: PUT  
Content-Type: application/json
Body: 
```text
{
	"id": 2,
	"name": "Doritos"
}
```

Endpoint: '/item'  
Metodo: GET  
Content-Type: application/json
Body: 
```text
{
	"name": "Doritos"
}
``` 

### Payments

Endpoint: '/payment'  
Metodo: POST  
Content-Type: application/json
Body: 
```text
[{
    "id_item": 3,
    "count_items": 3,
    "total_value": 30.4
}]
```

Endpoint: '/payment'  
Metodo: DELETE   
Content-Type: application/json 
Body:  
```text
{
    "id_payment": 2 
}
```  


Endpoint: '/payment'   
Metodo: PUT  
Content-Type: application/json
Body: 
```text
{
	"id_payment": 2,
    "count_items": 600,
    "total_value": 30.4
}
```

Endpoint: '/item'  
Metodo: GET  
Content-Type: application/json
Body: 
```text
{
    "id": 1
}
``` 
