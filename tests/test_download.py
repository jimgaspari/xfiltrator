from ntpath import join


path = '/downloads/'

def test_download_file(client):
    filename = "collect.sh"
    response = client.get(join(path,filename))
    assert response.status_code == 200

def test_download_file_list(client):
    response = client.get(path, follow_redirects = True )
    assert response.status_code == 200
