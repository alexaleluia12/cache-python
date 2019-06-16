```txt
Extrutura base
{"nome": "","endereco":"","descricao":"","outros":"","id":1}


mock-server - retorna json statico (1MB - genJSON.py) criado com http-server (Node.js)
==Dockerfile==
FROM node:8
# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

#RUN npm install
# If you are building your code for production
RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080
CMD [ "./node_modules/.bin/http-server", "-c-1", "." ]
====
.
├── cache
│   └── ref.json
├── Dockerfile
├── node_modules
├── package.json
├── package-lock.json
└── README.md

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