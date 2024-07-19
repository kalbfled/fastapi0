from locust import HttpUser, task


class StatusUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get('/status')
