
import  json

people_string = '''

{
    "people":

     [
         {
        "name":"wandie innocent",
        "phone":"0706382817",
        "email":["wandieinnoc@gmail.com","kavumawena@gmail.com"],
         "has_licence": false
        },
        
        {
        "name":"Obwot Solon",
        "phone":"0788992222",
        "email":["solo@gmail.com","juliusrano@gmail.com"],
         "has_licence": true

        }

        ]

}

'''


data = json.loads(people_string)

#look through peole and access them individualy

for person in data['people']:
    del person['phone']

new_string = json.dumps(data,indent=2, sort_keys=True)
print(new_string)


