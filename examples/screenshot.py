import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi.ApiClient import ApiClient
from webshotapi.ApiException import ApiException

if __name__ == "__main__":
    try:
        TOKEN = 'PLACE HERE YOU TOKEN'
        client = ApiClient(TOKEN)
        result = client.screenshot_jpg('https://www.cnn.com',{
            'remove_modals': 1
        })

        if result.save('/tmp/testa.jpg'):
            print("File saved")
        else:
            print("Error with save file")

    except ApiException as e:
        print("Error:")
        print(e)
    #print(result)



