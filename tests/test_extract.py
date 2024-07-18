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
    assert 'domain in literature without prior coordination or asking for permission.' in payload['html']
    assert payload['words'][0] == {
        'word': 'Example',
        'position': {'x': 660, 'y': 133, 'w': 124, 'h': 51},
        'word_index': 0,
        'xpath': '/html[1]/body[1]/div[1]/h1[1]',
        'offset': 0
    }

