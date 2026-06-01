import pytest
import requests


@pytest.fixture
def created_student(base_url):
    student_id = "fix_001"
    requests.post(
        f"{base_url}/api/student",
        json={"id": "fix_001", "name": "fixture测试"},
    )
    yield student_id
    requests.delete(
        f"{base_url}/api/student/fix_001",
    )


def test_create_student(base_url, created_student):
    response = requests.get(
        f"{base_url}/api/student/fix_001"
    )
    assert response.json()["code"] == 0


@pytest.fixture
def student_with_score(created_student, base_url):
    response = requests.post(
        f"{base_url}/api/calculate",
        json={"operation": "add", "num1": 80, "num2": 10}
    )
    result = response.json()
    yield result


def test_student_with_score(student_with_score):
    assert student_with_score["data"]["result"] == 90


@pytest.fixture(scope="module")
def shared_student(base_url):
    student_id = "share_001"
    requests.post(
        f"{base_url}/api/student",
        json={"id": "share_001", "name": "作用域测试"}
    )
    yield student_id
    requests.delete(
        f"{base_url}/api/student/share_001",
    )


def test_get_shared_student(base_url, shared_student):
    response = requests.get(
        f"{base_url}/api/student/share_001",
    )
    assert response.json()["code"] == 0


def test_update_shared_student(base_url, shared_student):
    response = requests.put(
        f"{base_url}/api/student/share_001",
        json={"name": "新名字"}
    )
    assert response.json()["code"] == 0