#  Copyright 2020 WebShotApi. All right reserved
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi import Client

if __name__ == "__main__":
    try:
        API_TOKEN = os.environ['WEBSHOTAPI_API_KEY']
        client = Client(API_TOKEN)

        #create new project
        result = client.projects().create({
            "name": "Test project added from api",
            "status": "active"
        })

        if(result.status_code == 201):
            new_project_id = result.data()['id']
            print(f"Project id: {new_project_id} created")

            # add urls to project
            urls_result = client.projects().url_add(
                new_project_id,
                "screenshot",
                [
                    'https://www.example.com',
                    'https://www.example2.com',
                    'https://www.example3.com'
                ],
                {
                    "response_type": "image",
                    "image_type": "png",
                    "remove_modals": 1,
                    "ads": 1,
                    "width": 1440,
                    "height": 960,
                    "no_cache": 0,
                    "scroll_to_bottom": 1,
                    "retina": 0,
                    "delay": "",
                    "wait_for_selector": "",
                    "wait_for_xpath": "",
                    "image_quality": 75,
                    "transparent_background": 1,
                    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "accept_language": "en/GB",
                    "cookies": "user=1&last_visit=2020-12-09",
                    "headers": "X-hello=value;X-var=value",
                    "full_page": 1,
                    "timezone": "Europe/Paris",
                    "fail_statuscode": "403,404, 500-511",
                    "extract_selectors": 1,
                    "extract_words": 0,
                    "extract_style": 0,
                    "extract_text": 1,
                    "extract_html": 0,
                    "capture_element_selector": "",
                    "injection_css": ".price{color:red;}",
                    "injection_css_url": "",
                    "injection_js": "document.querySelector(\"#ads\").style.display=\"none\";",
                    "thumbnail_width": 128
                })

            print("New urls added")
            print(urls_result.data())
        else:
            print("Error with create project")


    except Exception as e:
        print("Error:")
        print(e)
    #print(result)



