import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi.ApiClient import ApiClient
from webshotapi.ApiException import ApiException

if __name__ == "__main__":
    try:
        TOKEN = 'PLACE HERE YOU TOKEN'
        client = ApiClient(TOKEN)
        result = client.extract('https://www.example.com',{
            'extract_html': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        print(result.save('/tmp/test_extract.json'))


    except ApiException as e:
        print("Error:")
        print(e)
    #print(result)



