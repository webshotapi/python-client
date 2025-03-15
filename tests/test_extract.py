from webshotapi import Client

def test_extract(
    request_client: Client
):
    response = request_client.extract("https://example.com", {
        'extract_html': True,
        'extract_words': True,
    })

    assert 'his domain is for use in illustrative examples in documen' in response['html']
    assert response['words'][0] == {
        'word': 'Example',
        'position': {'x': 660, 'y': 133, 'width': 124, 'height': 51},
        'word_index': 0,
        'xpath': '/html[1]/body[1]/div[1]/h1[1]',
        'offset': 0
    }

