#disct data={"key":value} value = anything, key = string only

data = {
    "name":"dang",
    "class":"rrr"
}

#print(type(data))
#print(data)

#dictionary doesnt accept duplicate data = case sensitive(only key not name)

student = {
    'id': 101,
    'name': 'sudan',
    'age': 22,
    'course': 'Sudan',
    'marks': [78, 85, 90],
    'is_active': True,
    'address':'dharan',
}

#print(student['name'])

#printing keys and values
#print(student.keys())
#print(student.values())

#add in dictionary
student['num']=98062

#update new data in dict
student['name']='prashanna'

#update function
student.update({'name':'hari', 'num':123})
#print(student)

#removing data

del student['course'] 
student.pop('name')
student.popitem() #remove last item
student.clear() #clear dictionary

#get function(way to manipulate error message)
print(student.get('age', 'not found')) #sends not found if no key called age

#nested disctionary
student = {
    'id': 101,
    'name': 'sudan',
    'age': 22,
    'course': 'Sudan',
    'marks': [78, 85, 90],
    'is_active': True,
    'address':'dharan',
    'num':{
        'ntc':980,
        'ncell':{
            'telecome':'nepal'
        }
    }
}
print(student['num']['ncell']['telecom']) #taking values from nested dict

print(f"{student['name']}'s total marks is {student['marks'][0]+student['marks'][1]+student['marks'][2]} and his best course is {student['course']}")

