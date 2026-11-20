
import requests
import json

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch all posts
response = requests.get(url)

# Validate response status code
assert response.status_code == 200, f"API request failed: {response.status_code}"

print("Status Code:", response.status_code)
print("API request successful!")

# Convert response to JSON
posts = response.json()

# Verify required keys in every post
required_keys = {"userId", "id", "title", "body"}

for post in posts:
    assert required_keys.issubset(post.keys()), (
        f"Missing keys in post ID: {post.get('id')}"
    )

print(f"Validated {len(posts)} posts successfully!")

# Save the first 5 posts into a JSON file
first_five_posts = posts[:5]

with open("first_5_posts.json", "w", encoding="utf-8") as file:
    json.dump(first_five_posts, file, indent=4)

print("First 5 posts saved to first_5_posts.json")
