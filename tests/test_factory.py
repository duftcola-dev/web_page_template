from app import App 

def test_config():
    print("Testing ")
    assert not App().init_app().testing
    assert App().init_app(test=True).testing
