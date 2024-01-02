import json

def jsonChecker(jsonFile, jsonSchema, exact=True):

    assert type(jsonFile) == str, "jsonFile must be a string"
    assert type(jsonSchema) == dict, "jsonSchema must be a dictionary"

    jsonFile += ".json" if jsonFile.endswith(".json") == False else ""

    with open(jsonFile) as json_file:
        jsonData = json.load(json_file)

        if exact:
            if len(jsonData) != len(jsonSchema):
                return False
        
        for key in jsonData:
            if key not in jsonSchema:
                return False
            else:
                if type(jsonData[key]) != jsonSchema[key]:
                    return False
        
        return True
