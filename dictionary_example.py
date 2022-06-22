country_code_dict = {"India":91,"US":1, "UK":4}
print(country_code_dict)

print(country_code_dict["India"])
print(country_code_dict.get("India"))

keys = country_code_dict.keys()
print(keys)

values = country_code_dict.values()
print(values)

#print(country_code_dict["Indai"])
country_code_dict["US"]=100
country_code_dict.update({"UK":400})

print(country_code_dict)

dep1= {"wife":"Pooja","son":"ram"}
emp1= {"name":"Peter", "active": True, "emp_mail":"a@c.com", "depedent": dep1}
emp2= {"name":"John", "active": False, "emp_mail":"b@c.com"}
emp3= {"name":"Gita", "active": True, "emp_mail":"c@c.com"}

country_code_dict = {"India":91,"US":1, "UK":4}

org_dict={100: emp1, 200: emp2, 300: emp3}

#org_list={emp1, emp2, emp3}

print(org_dict)

emp = org_dict[200]
print("-------------")
print(emp)
name_emp = emp["name"]
print(name_emp)
print(org_dict[100]["name"])
print(org_dict[100]["depedent"]["son"])
print(org_dict[200]["depedent"]["son"]) # Has error, because emp2 does npt have depedent.
#print(org_list)



