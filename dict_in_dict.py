my_dict = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main Street",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
    },
}

# Access the street address
street_address = my_dict["address"]["street"]
name1 = my_dict["name"]
# Print the street address
print(street_address)  # Output: 123 Main Street
print(name1)
