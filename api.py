
import requests
import pytest
import time

from pydantic import BaseModel, ValidationError
from typing import List


BASE_URL = "https://jsonplaceholder.typicode.com"


# -------------------------------
# Pydantic Schema Models
# -------------------------------

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str


# -------------------------------
# Test 1: Response Status Code
# -------------------------------

def api_posts_status_code():
    response = requests.get(f"{BASE_URL}/posts", timeout=5)

    assert response.status_code == 200


# -------------------------------
# Test 2: Response Time
# -------------------------------

def api_posts_response_time():
    start_time = time.perf_counter()

    response = requests.get(f"{BASE_URL}/posts", timeout=5)

    end_time = time.perf_counter()

    response_time = end_time - start_time

    assert response.status_code == 200
    assert response_time < 2, (
        f"Response took {response_time:.2f} seconds"
    )


# -------------------------------
# Test 3: Post Schema Validation
# -------------------------------

def api_posts_schema():
    response = requests.get(f"{BASE_URL}/posts", timeout=5)

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)

    for post in posts:
        validated_post = Post(**post)

        assert validated_post.id is not None


# -------------------------------
# Test 4: Parameterized Endpoint Testing
# -------------------------------

@pytest.mark.parametrize(
    "endpoint, expected_model",
    [
        ("posts", Post),
        ("comments", Comment),
        ("users", User),
    ]
)
def api_multiple_endpoints(endpoint, expected_model):

    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        timeout=5
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    # Validate schema for every returned record
    for item in data:
        validated_data = expected_model(**item)

        assert validated_data is not None


# -------------------------------
# Test 5: Validate First 5 Posts
# -------------------------------

def api_first_five_posts():

    response = requests.get(f"{BASE_URL}/posts", timeout=5)

    assert response.status_code == 200

    posts = response.json()

    first_five = posts[:5]

    assert len(first_five) == 5

    for post in first_five:
        validated_post = Post(**post)

        assert validated_post.userId > 0
        assert validated_post.id > 0
