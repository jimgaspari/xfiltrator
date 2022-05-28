path = '/fileupload/'

def test_upload_file(client):
    filename = "tests/files/os_info.txt"
    data = {
        'file': (open(filename, 'rb'), filename)
    }
    response = client.post(path, data=data, follow_redirects = True )
    assert response.status_code == 200