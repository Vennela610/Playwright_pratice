import json 
def write_json(path,data):
    with open(path,"w",encoding="UTF-8") as file:
        json.dump(data,file,indent = 4)