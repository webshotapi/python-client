from webshotapi import Client
import os
def test_screenshot_jpg(
    request_client: Client
):
    response = request_client.screenshot("https://example.com", {}, "jpg")
    assert response.status_code == 200
    save_path = '/tmp/screenshot.jpg'
    response.save(save_path)

    file_stat = os.stat(save_path)
    assert file_stat.st_size > 32000

def test_screenshot_png(
    request_client: Client
):
    response = request_client.screenshot("https://example.com", {}, "png")
    assert response.status_code == 200
    save_path = '/tmp/screenshot.png'
    response.save(save_path)

    file_stat = os.stat(save_path)
    assert file_stat.st_size > 32000

def test_screenshot_pdf(
    request_client: Client
):
    response = request_client.pdf("https://example.com", {})
    assert response.status_code == 200
    save_path = '/tmp/screenshot.pdf'
    response.save(save_path)

    file_stat = os.stat(save_path)
    assert file_stat.st_size > 32000