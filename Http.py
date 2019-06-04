

#working module for json data consumption

import urllib.request,json



def main():

    print("showing daa")

    url = "http://dummy.restapiexample.com/api/v1/employees"
    data = urllib.request.urlopen(url).read()


    #json data format
    jsonDataFormat = json.loads(data.decode("utf-8"))

    #this is the only varying code the rest works
    #to print data use this
    #print(json.dumps(jsonDataFormat))

    #or use print(jsonDataFormat)
    print(jsonDataFormat [0]["employee_name"] )


if __name__ == '__main__':main()
