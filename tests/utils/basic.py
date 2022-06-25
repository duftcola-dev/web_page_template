def check_default_response(response:dict):
    assert response.status_code == 200
    assert isinstance(response.json,dict)
    assert response.json == {"OK":1}

def check_200(response:dict):
     assert response.status_code == 200

def check_201(response:dict):
     assert response.status_code == 200

def check_400(response:dict):
     assert response.status_code == 400

def check_404(response:dict):
     assert response.status_code == 404

def check_412(response:dict):
     assert response.status_code == 412