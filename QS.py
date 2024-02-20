'''kwargs'''
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # print("Name: ", name, "Power: ", power)


print_kwargs(name="shaktiman", power="lazer", enemy="dr .jhatka")
