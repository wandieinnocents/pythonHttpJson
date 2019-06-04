
#working module for json data consumption

import urllib.request,json
import requests




def main():

    print("showing api consumption for exchange rates..")

    #api, url
    url = "http://api.exchangeratesapi.io/latest"

    r = requests.get(url)
    rates_json = json.loads(r.text)['rates']

    print(rates_json)

    print("cad values here ... ")

    val_1 = rates_json['CAD']
    print("this is value one")
    print(val_1)
    print("sum is here")
    sum = val_1*2
    print(sum)


    print(type(rates_json))






if __name__ == '__main__':main()
