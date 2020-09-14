def create(data):
    array = []
    file = open(data,"r")
    content = file.readlines()

    for each in content:
        temp = each.replace("\n","").split(",")
        array.append(temp)

    file.close()
    return array




