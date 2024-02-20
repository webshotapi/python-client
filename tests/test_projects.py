from webshotapi import Client

shared_data = {
    "new_project_id": None,
    "saved_urls": []
}

def test_create_project(
    request_client: Client,
):
    response = request_client.projects().create({
        "name": "Test python project",
        "status": "active"
    })
    assert response.status_code == 201
    shared_data['new_project_id'] = response.data()['id']


def test_get_project(
    request_client: Client,
):
    response = request_client.projects().get(shared_data['new_project_id'])
    assert response.status_code == 200

def test_get_projects(
    request_client: Client,
):
    response = request_client.projects().get_all(1)
    assert response.status_code == 200
    assert len(response.data()['projects']) > 0


def test_update_project(
    request_client: Client,
):
    response = request_client.projects().update(
        shared_data['new_project_id'],
        {
            "name": "abc",
            "status": "disabled"
        }
    )

    assert response.status_code == 200
    assert response.data()['name'] == 'abc'

def test_add_url(
    request_client: Client,
):
    response = request_client.projects().url_add(
        shared_data['new_project_id'],
        "screenshot",
        [
            "https://example.com/blog",
            "https://example.com/blog/page-3"
        ],
        {
            "image_type": "png",
            "remove_modals": True,
            "premium_proxy": True,
        }
    )

    shared_data['saved_urls'] = response.data()
    assert response.status_code == 201

def test_url_delete(
    request_client: Client,
):
    response = request_client.projects().url_delete(
        shared_data['new_project_id'],
        shared_data['saved_urls'][0]['id']
    )

    #shared_data['saved_urls'] = response.data()['urls']
    assert response.status_code == 200
    assert response.data()['deleted'] == True

def test_get_urls(
    request_client: Client,
):
    response = request_client.projects().urls_get(
        shared_data['new_project_id'],
    )

    assert response.status_code == 200
    assert len(response.data()['urls']) == 1
    assert response.data()['urls'][0]['id'] == shared_data['saved_urls'][1]['id']


def test_delete_project(
    request_client: Client,
):
    response = request_client.projects().remove(shared_data['new_project_id'])

    assert response.status_code == 200
    assert response.data()['deleted'] == True
