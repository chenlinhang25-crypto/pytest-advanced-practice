import pytest
import requests

BASE_URL = "http://192.168.31.117:5002"

def test_student_bitian(base_url):
        response =requests.post(
            f"{base_url}/api/student",
            json={}
        )
        assert response.json()["code"]==-1

def test_student_id_long(base_url):
    response =requests.post(
        f"{base_url}/api/student",
        json={"id" : "a" * 21 ,"name":"张三"}
    )
    assert response.json()["code"]==-1

@pytest.mark.parametrize("age",["-1","151","abc"])
def test_student_age(base_url,age):
    response =requests.post(
        f"{base_url}/api/student",
        json={"id":"001","name":"张三","age":age}
    )
    assert response.json()["code"]==-1

def test_student_same(base_url):
    response =requests.post(
        f"{base_url}/api/student",
        json={"id":"002","name":"张三"}
    )
    response = requests.post(
        f"{base_url}/api/student",
        json={"id": "002", "name": "李四"}
    )
    assert response.json()["code"]==-1
    assert response.status_code==409

def test_student_calculate(base_url):

    response =requests.post(
        f"{base_url}/api/calculate",
        json={"operation":"divide","num1":"10","num2":"0"}
    )
    assert response.json()["code"]==-1

def test_calculate_sqrt(base_url):
    response =requests.post(
        f"{base_url}/api/calculate",
        json={"operation":"sqrt","num1":"-4"}
    )
    assert response.json()["code"]==-1

@pytest.mark.parametrize("num1",["-1","171","3.5"])
def test_calculate_factorial(base_url,num1):
        response =requests.post(
            f"{base_url}/api/calculate",
            json={"operation":"factorial","num1":num1}

        )
        assert response.json()["code"]==-1

def test_student_notexist(base_url):
    request =requests.get(
        f"{base_url}/api/student/001",
        )
    assert request.json()["code"]==-1

    assert request.status_code==404

def test_order(base_url):
    response =requests.post(
        f"{base_url}/api/order",
        json={"order_id":"1","customer_id":"1","total_amount":"1"}
    )
    assert response.json()["code"]==-1

def test_order_total_amount(base_url):

    response =requests.post(
        f"{base_url}/api/order",
        json={
            "items": [{"product_id": "P001", "quantity": 1, "price": 100}],
        "order_id":"001","customer_id":"001","total_amount":200}

    )
    assert response.json()["code"]==-1
