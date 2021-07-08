from locust import HttpLocust , TaskSet , task

class WebSiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/login",{
            "username": "test_user",
            "password": ""
        })

        @task
        def index(self):
            self.client.get("/")

        @task
        def about(self):
            self.client.get("/about")

class WebSiteUSer(HttpLocust):
    task_set = WebSiteTasks
    min_wait = 5000
    max_wait = 15000
