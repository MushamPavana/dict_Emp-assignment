


employee_dict = {}
def add_employee(domain, name, empid, email):
    employee_info = {
        "Name": name,
        "Employee ID": empid,
        "Email": email
    }

    employee_dict[domain] = employee_info

add_employee("python", "pavana", "02143", "pavana.marolix@gmail.com")

if "python" in employee_dict:
    employee_info = employee_dict["python"]
    print("Employee Details:")
    print("Domain: python")
    for key, value in employee_info.items():
        print(key + ":", value)
else:
    print("Employee not found in the dictionary.")
