# import requests 

# class APIlogin:
#     def __init__(self,base_url):
#         self.base_url = base_url.rstrip("/") 

#     def get(self,endpoint,params = None): 
#         return requests.get(f"{self.base_url}{endpoint}",params = params) 

#     def post(self,endpoint,params = None):
#         return requests.post(f"{self.base_url}{endpoint}",params = params)

#     def put(self,endpoint,params = None):
#         return requests.put(f"{self.base_url}{endpoint}",params = None) 

#     def patch(self,endpoint,params=None):
#         return requests.patch(f"{self.base_url}{endpoint}",params = params)

#     def delete(self,endpoint,params = None):
#         return requests.delete(f"{self.base_url}{endpoint}",params = params)
         


import requests


class APILogin:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def post(self, endpoint, data=None, json=None, headers=None):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            data=data,
            json=json,
            headers=headers
        )

    def put(self, endpoint, params=None, **kwargs):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            params=params,
            **kwargs
        )

    def patch(self, endpoint, params=None, **kwargs):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            params=params,
            **kwargs
        )

    def delete(self, endpoint, params=None, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            params=params,
            **kwargs
        )