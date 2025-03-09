import json

file =open("C:\\Users\\DMcCo\\Downloads\\student (1).json","r")
json_string =file.read()
file.close()

student_json =json.loads(json_string)

student_json ["name"]= "Carl"

file =open("C:\\Users\\DMcCo\\Downloads\\student (1).json","w")
file.write(json.dumps(student_json))
file.close()

print("Change Successful")