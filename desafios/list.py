def execFunction(function, list, element = None,index = None):
    if(element is not None):
        element = int(element)
    if(index is not None):
        index = int(index)
    list_function = {
        "insert": list.insert, 
        "remove": list.remove, 
        "append": list.append, 
        "sort": list.sort,
        "pop": list.pop,
        "reverse": list.reverse,
        "print" : print}
    if(function in list_function):
        if(function == "insert"):
            list_function[function](index,element)
        elif(function == "remove" or function == "append"):
            list_function[function](element)   
        elif(function == "print"):
            list_function[function](list)
        else:
            list_function[function]() 
    else:
        return False


if __name__ == '__main__':
    N = int(input())
    values = list()

    for i in range(N):
        command = input().split()
        if(command[0] == "insert"):
            execFunction(command[0],values,command[2], command[1])
        elif(command[0] == "remove" or command[0] == "append"):
            execFunction(command[0],values,command[1])
        else:
            execFunction(command[0],values)

        
    

         