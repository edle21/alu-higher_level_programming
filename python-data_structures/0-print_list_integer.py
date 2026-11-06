
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        if type(number) is not int:
            raise TypeError("List must contain only integers")
        print("{:d}".format(number))

