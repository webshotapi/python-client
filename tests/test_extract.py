from webshotapi import Client

def test_extract(
    request_client: Client
):
    response = request_client.extract("https://example.com", {
        'extract_html': True,
        'extract_words': True,
    })
    assert response.status_code == 200

    payload = response.data()

    assert ' domain in literature without prior coordination or asking for permission.' in payload['html']
    assert payload['words'][0] == {
        'word': 'Example',
        'offset': 0,
        'position': {'h': 38, 'w': 153, 'x': 660, 'y': 133},
        'word_index': 0,
        'xpath': '/html[1]/body[1]/div[1]/h1[1]'
    }

