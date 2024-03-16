import json

def verify_json_resource(file): #checks whether atleast one resource field equals to single asterisk
    # opening JSON file
    f = open(file)

    # loading json data from file
    data = json.load(f)

    found = False

    # iterating through statements and checking resource field
    for statement in data['PolicyDocument']['Statement']:
       if statement['Resource'] == '*':
            found = True
            break

    # Closing file
    f.close()

    if found:
        return False
    else:
        return True

def main():
    print(verify_json_resource("awsPolicy.json"))

if __name__ == "__main__":
    main()