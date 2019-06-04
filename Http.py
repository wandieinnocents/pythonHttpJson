import urllib.request,json



def main():

    print("showing daa")

    url = "http://dummy.restapiexample.com/api/v1/employees"
    data = urllib.request.urlopen(url).read()


    #json data format
    jsonDataFormat = json.loads(data.decode("utf-8"))

    print(jsonDataFormat [0]["employee_name"],[1]["id"] )


if __name__ == '__main__':main()
