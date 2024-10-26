from pymongo import MongoClient

#Conexão no banco
connection_string = 'mongodb://localhost:27017'
client = MongoClient(connection_string)
db_connection = client['whatsapp']

#Acessando a coleção
collection = db_connection.get_collection('nome_e_numeros') 

#Buscando todos os elementos
elementos = collection.find()

#Acessando cada elemento por vez
nomes = []
numeros = []
ids = []

for doc in elementos: 
    nome = nomes.append(doc['nome'])
    numero = numeros.append(doc.get("numero"))
    id = ids.append(doc['_id'])
    #Depois deste 'for' pode fechar a conexaõ com  o MongoDB e rodar o programa de mensagens
client.close()