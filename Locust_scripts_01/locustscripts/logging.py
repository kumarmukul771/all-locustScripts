from locust import HttpUser,task,between
import logging

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "http://suprdaily-staging-2.ap-south-1.elasticbeanstalk.com/v2/products/sku-attributes/"

    @task
    def launch_URL(self):
        response = self.client.get("/", headers= {
  "Authorization": "Token a639ddbd593911108d194431c730bd01992c5895",
})

        print(response.status_code)
        logging.info("Log message")
        # print(response.text)
