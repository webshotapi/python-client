import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi.ApiClient import ApiClient
from webshotapi.ApiException import ApiException

def on_request_completed(res, req, index):
    print("OK",index)
    print(res.save('/tmp/job_'+str(index)))

def on_request_error(res, req,index):
    print(res.body)
    print("no OK",index)

if __name__ == "__main__":
    try:

        #create object
        TOKEN = 'PLACE HERE YOU TOKEN'
        client = ApiClient(TOKEN)

        #create multi concurrency requests
        pipeline = client.multi()

        #add request to multi query
        pipeline.extract('https://www.google.com',{
            'extract_html': 1,
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        # add request to multi query
        pipeline.screenshot_jpg('https://www.o2.pl', {
            'remove_modals': 1,
            'no_cache': 1,
        })

        # add request to multi query
        pipeline.screenshot_jpg('https://www.kaggle.com', {
            'remove_modals': 1,
            'no_cache': 1,
        })

        # add request to multi query
        pipeline.screenshot_png('https://www.cnn.com', {
            'remove_modals': 1,
            'no_cache': 1,
        })



        # add request to multi query
        pipeline.extract('https://www.google.com', {
            'extract_html': 1,
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        # add request to multi query
        pipeline.extract('https://www.google.com', {
            'extract_html': 1,
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        # add request to multi query
        pipeline.extract('https://www.google.com', {
            'extract_html': 1,
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        # add request to multi query
        pipeline.extract('https://www.google.com', {
            'extract_html': 1,
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1
        })

        # execute all requests
        pipeline.exec(on_request_completed, on_request_error)

    except ApiException as e:
        print("Error:")
        print(e)
    #print(result)



