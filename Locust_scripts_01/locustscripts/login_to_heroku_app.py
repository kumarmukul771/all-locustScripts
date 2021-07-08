from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://the-internet.herokuapp.com/"

    @task
    def launch_URL(self):
        response = self.client.post("/authenticate", data=
        {
            "username": "tomsmith",
            "password": "SuperSecretPassword",
        }  )

        print("Testing")
        print(response.status_code)
        print(response.text)
