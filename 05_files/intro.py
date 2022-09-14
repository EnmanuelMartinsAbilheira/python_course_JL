import json


with open('copia.json') as json_file: 
               data = json.load(json_file) 

#print(data)
print(len(data['Employees']))
print(data['Employees'][0]['userId'])


data['Employees'].append( 
{
      "userId": input("userid: "),
      "jobTitle": input("jobTitle: "),
      "firstName":input("firstName: "),
      "lastName": input("lastName"),
      "employeeCode": input("employeeCode: "),
      "region": input("Region: "),
      "phoneNumber": input("phoneNumber: "),
      "emailAddress": input("emailAddress: ")
}
)

x = input("Cual indice quere imprimir: ")
print(data['Employees'][int(x)])

with open('copia.json','w') as json_file: 
               json.dump(data,json_file,indent=4, separators=(", ", ": "), sort_keys=True)