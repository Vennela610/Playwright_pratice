import pytest
from Utilities.config_reader import Config


# @pytest.mark.api
# @pytest.mark.regression
def test_valid_login(api_login):

    response = api_login.get(
        "/login.htm",
        params={
            "username": Config.parabank_API_username,
            "password": Config.parabank_API_password
        }
    )

    print("STATUS:", response.status_code)
    print("URL:", response.url)
    print("RESPONSE:", response.text)

    assert response.status_code == 200
    
# def test_invalid_login(api_login):
#     response = api_login.post( 
#         "/login.htm", 
#         data={ "username": "invalid_user", 
#               "password": Config.parabank_API_password } ) 

    
#     print("STATUS:", response.status_code) 
#     print("URL:", response.url) 
#     print("RESPONSE:", response.text) 
#     assert response.status_code == 200 
#     assert "The username and password could not be verified." in response.text