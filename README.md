# WebShotApi.com API client for Python

Capture and store website snapshots effortlessly with our SaaS service. 
Save images in popular formats such as JPG, PNG, and PDF. 
Additionally, extract selectors for every HTML element, 
complete with coordinates and CSS styles post-browser rendering. 
Utilize our API to create projects and seamlessly queue up all your URLs. 
Let our servers handle the workload, ensuring a hassle-free experience for you.

Full documentation about our api you can find in this website [Website screenshot API DOCS](https://webshotapi.com/docs/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/webshotapi) to install our client in Python.

```bash
pip install webshotapi
```

OR
```bash
pip3 install webshotapi
```

# Remove cookies popup before take sceenshot
![Remove cookies before take screenshot](https://raw.githubusercontent.com/webshotapi/webshotapi-website-screenshot-php-client/6681d3d38ea13391a30b2e43b8c37191e2d41bef/images/remove-cookies-before-take-screenshot.png)

Effortlessly remove annoying cookies pop-ups before capturing stunning screenshots. 
Let our advanced AI algorithm transform the way you visualize websites, ensuring a cookie-free snapshot every time! [Read more](http://webshotapi.com/blog/remove-cookies-before-take-screenshot/)


# API KEY
Api key you can generate after register.
[https://dashboard.webshotapi.com/api_keys](https://dashboard.webshotapi.com/api_keys)

# Usage

### Take screenshot and save jpg to file
```python
from webshotapi import Client

if __name__ == "__main__":
    try:
        TOKEN = 'YOUR TOKEN HERE'
        client = Client(TOKEN)
        
        result = client.screenshot(
            'https://www.example.com',{
            'remove_modals': True,
            'no_cache': True
        })

        if result.save('/tmp/testa.jpg'):
            print("File saved")
        else:
            print("Error with save file")

    except Exception as e:
        print("Error:")
        print(e)
```

### Take screenshot and save PDF to file
You can convert your html page to PDF. For example you can prepare html invoice template and convert that website to PDF
```python
from webshotapi import Client

if __name__ == "__main__":
    try:
        TOKEN = 'YOUR TOKEN HERE'
        client = Client(TOKEN)
        
        result = client.pdf(
            'https://www.example.com',{
                'no_cache': 1
        })

        if result.save('/tmp/test.pdf'):
            print("File saved")
        else:
            print("Error with save file")

    except Exception as e:
        print("Error:")
        print(e)
```

### Extract words map and HTML elements with css styles after rendering
Revolutionize your web development experience with our unparalleled software. Extract all selectors for HTML elements, complete with CSS styles, post-browser rendering. Furthermore, delve into the intricate details by extracting words along with their precise position data (x, y, width, height, offset from the previous word). This invaluable information allows you to construct a comprehensive words map of the entire website. Elevate your understanding and efficiency in website analysis and development like never before!
#### Sample script:
```python
from webshotapi import Client

if __name__ == "__main__":
    try:

        #create object
        TOKEN = 'YOUR TOKEN HERE'
        client = Client(TOKEN)

        #send request
        result = client.extract('https://www.example.com',{
            'no_cache': 1,
            'extract_selectors': 1,
            'extract_style': 1,
            'extract_words': 1,
            'extract_html': 1,
            'extract_text': 1
        })
        
        #print json data from result
        print(result.data())

    except Exception as e:
        print("Error:")
        print(e)
```
#### Results

```json
{
 "selectors": [
      {
         "xpath": "/html[1]",
         "css_selector": "html",
         "x": 0,
         "y": 0,
         "w": 1920,
         "h": 413,
         "style": {
            "visibility": "visible",
            "display": "block",
            "fontWeight": "400",
            "backgroundImage": "none",
            "backgroundColor": "rgba(0, 0, 0, 0)",
            "cursor": "auto",
            "fontSize": "16px",
            "color": "rgb(0, 0, 0)",
            "position": "static",
            "textDecoration": "none solid rgb(0, 0, 0)",
            "textDecorationLine": "none",
            "textDecorationColor": "rgb(0, 0, 0)",
            "textDecorationStyle": "solid",
            "textDecorationThickness": "auto",
            "bottom": "auto",
            "top": "auto",
            "left": "auto",
            "right": "auto",
            "zIndex": "auto",
            "opacity": "1",
            "backgroundRepeat": "repeat",
            "borderWidth": "0px",
            "textAlign": "start",
            "marginLeft": "0px",
            "marginRight": "0px",
            "marginTop": "0px",
            "marginBottom": "0px",
            "paddingLeft": "0px",
            "paddingRight": "0px",
            "paddingTop": "0px",
            "paddingBottom": "0px",
            "overflow": "visible",
            "textIndent": "0px",
            "textTransform": "none",
            "letterSpacing": "normal",
            "fontFamily": "\"Times New Roman\""
         },
         "attributes": {}
      }
  ],
  "words": [
     {
         "word": "permission.",
         "position": {
            "x": 660,
            "y": 231,
            "w": 92,
            "h": 19
         },
         "word_index": 26,
         "xpath": "/html[1]/body[1]/div[1]/p[1]",
         "offset": 145
      }
  ],
  "page_properties": {
      "viewport": {
         "width": 1920,
         "height": 1080
      },
      "document": {
         "width": 1920,
         "height": 1080
      }
   },
  "html": "<!doctype html><html lang='en' dir='ltr'><head><base hr...",
  "text": "Welcome in our page\nToday is Monday...",
  "screenshot_url": "https://api.webshotapi.com/v1/screenshot/?token=....&width=1920&height=960",
  "status_code": 200
}

```

## API docs
Full documentation about our api you can find in this website [API DOCS](https://webshotapi.com/docs/python/)

## About our service
You can use our service with free plan with 100 free requests 

## License
[MIT](https://choosealicense.com/licenses/mit/)