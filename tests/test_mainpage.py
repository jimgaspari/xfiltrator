path = '/'

def test_download_file_list(client):
    response = client.get(path, follow_redirects = True )
    assert response.status_code == 200