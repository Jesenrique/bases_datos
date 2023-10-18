import pymongo
import json

# Establecer una conexión con la base de datos MongoDB
mongo_uri="mongodb+srv://jesusenriquegarciag:G8sH0yWAlC2yj9Kg@trabajofinal.bxyhmdg.mongodb.net"

client = pymongo.MongoClient(mongo_uri)
# No es necesario especificar una base de datos por defecto en MongoDB Atlas

db = client.sample_mflix
coleccion = db["movies"]

pipeline = [
{
    "$match":{"directors":{"$exists":True},
              "runtime":{"$type":"number"}}
},
{
    "$unwind": "$directors"
},
{
    "$group":{
       "_id":{"director":"$directors"},
       "total":{"$sum":1},
       "duration":{"$avg":"$runtime"} 
    }
}
]


# Realizar la consulta de agregación
result = coleccion.aggregate(pipeline)

output_file = "resultado1.json"

# Guardar el resultado en un archivo JSON
with open(output_file, "w") as json_file:
    for document in result:
        json.dump(document, json_file)
        json_file.write('\n')