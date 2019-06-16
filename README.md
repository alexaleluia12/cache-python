```txt
Extrutura base
{"nome": "","endereco":"","descricao":"","outros":"","id":1}


mock-server - retorna json statico (1MB - genJSON.py) criado com http-server (Node.js)
http://127.0.0.1:8080/cache/ref.json


Request
GET localhost:5000/person/1/police/CTN?attrs=id


NO -> Network Only
CTN -> Cachen then Network

---
**Tempo**

CTN
1   (cat miss) -> 0.77 seg
n+1 (cat hit)  -> 0.024 seg

NO
0.034 seg


TODO(Alex)
Adicionar Logger
Outras politicas de cache
Ferramenta automatizada de teste de extresse geração de relatorio
Async melhora alguma coisa
```txt