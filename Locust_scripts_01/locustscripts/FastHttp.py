from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

class MyUser(FastHttpUser):
    wait_time = between(2, 5)
    host = "http://suprdaily-staging-2.ap-south-1.elasticbeanstalk.com/v2/products/sku-attributes/"

    @task
    def index(self):
        response = self.client.get("/", headers={
            "Authorization": "Token a639ddbd593911108d194431c730bd01992c5895",
        })

        print(response.status_code)