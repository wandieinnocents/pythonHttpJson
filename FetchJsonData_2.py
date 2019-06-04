import json



def main():


    with open('datasetsfille.json') as f:

     data = json.load(f)


     for dataitem in data['dataset']:

         print(json.dumps(dataitem))


if __name__ == '__main__':main()