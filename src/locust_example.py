import logging
import random

from locust import HttpUser, SequentialTaskSet, constant, tag, task

city_list = []


class MyScript(SequentialTaskSet):
    @task
    @tag("get", "root")
    def get_root(self):
        with self.client.get(url="/", catch_response=True, name="ROOT") as response:
            if response.status_code == 200:
                city_list.append(response.text)
                response.success()
                logging.info(">>>Root")
            else:
                response.failure("Failure !")

    @task
    @tag("get", "cities")
    def get_cities(self):
        with self.client.get(
            url="/cities", catch_response=True, name="GET"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info(">>>Cities")
            else:
                response.failure("Failure !")

    @task
    @tag("get", "cities_by_id")
    def get_cities_by_id(self):
        id = random.randint(0, 3)
        with self.client.get(
            url=f"/cities/{id}", catch_response=True, name="GET_BY_ID"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info(">>>Cities by id")
            else:
                response.failure("Failure !")

    @task
    @tag("post")
    def create_city(self):
        logging.info("Post")
        with self.client.post(
            url="/cities", json={"name": "POSTED"}, catch_response=True, name="POST"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info(">>>Post")
            else:
                response.failure("Failure !")

    @task
    @tag("put")
    def update_city(self):
        id = random.randint(0, 3)
        with self.client.put(
            url=f"/cities/{id}", catch_response=True, name="UPDATE"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info(">>>Put")
            else:
                response.failure("Failure !")

    @task
    @tag("delete")
    def delete_city(self):
        id = random.randint(0, 3)
        with self.client.delete(
            url=f"/cities/{id}", catch_response=True, name="DELETE"
        ) as response:
            if response.status_code == 200:
                response.success()
                logging.info(">>>Delete")
            else:
                response.failure("Failure !")


class MyLoadTest(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = constant(1)
    tasks = [MyScript]
