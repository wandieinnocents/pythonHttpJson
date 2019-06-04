import json
import requests

#get data from url
request = requests.get('https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=mHuskLpVFsLoDfmHzRk5')

#convert data to string
#json data is read from the string format using json.loads
request_text = request.text

#get data
data = json.loads(request_text)


#serialize the data
data_serialized = json.dump(data,open("jsonDdata","w",) , indent=4)

