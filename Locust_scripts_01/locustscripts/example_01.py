from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://jsonplaceholder.typicode.com"

    # making post request with json data and extracting data
    # @task
    # def launch_URL(self):
    #     response = self.client.post("/posts", json=
    #     {
    #         "title": "Silence of the Lambs",
    #         "body": "Thriller Book",
    #         "userId": 1
    #     }
    #                                 )
    #     json_var = response.json()
    #     request_id = json_var['title']
    #     print('Post title is ' + request_id)

    # making post request with formdata and extracting data
    @task
    def launch_URL2(self):
        response = self.client.post("/posts", data=
        {
            "title": "Silence of the Lambs",
            "body": "Thriller Book",
            "userId": 1
        }
                                    )
        json_var = response.json()
        request_id = json_var['title']
        print('Post title is ' + request_id)
