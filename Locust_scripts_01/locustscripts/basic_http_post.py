from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://the-internet.herokuapp.com/"

    @task
    def launch_URL(self):
        self.client.get("/abtest",name="heroku");
        # self.client.post("/login.php",name="login",data={"username":"xyz",
        # "password":"mukul","action":"process"})
