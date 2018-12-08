import requests

"""
Test for get method for Rest Webservice

url=" http://localhost:3000/posts/1"
response=requests.get(url=url)
print(response.status_code)
print(type(response.text))
print(response.headers["Content-Type"])
"""
postData = """{
      "id": 101,
      "title": "json-server",
      "author": "typicode"
    }"""
"""
this block is used for testing the post method data used in postData available above
url="http://localhost:3000/posts"

headers={"Content-Type": "application/json"}
postResponse=requests.post(url=url,data=postData,headers=headers)
print(postResponse.status_code)
print(postResponse.text)
"""

"""
this block is used to test the delete method, replace id with any appropriate id value 
url="http://localhost:3000/posts/id"
delResponse=requests.delete(url=url)
print(delResponse.text)
"""

putData = """{
      "id": 101,
      "title": "updatedVal1",
      "author": "updatedVal2"
    }"""
"""
this block of works to test the put method used data is above putData
url="http://localhost:3000/posts/1"

headers={"Content-Type": "application/json"}
putResponse=requests.put(url=url,data=putData,headers=headers)
print(putResponse.status_code)
"""

# test the dufference between put and patch method
putDataTest = """{
      "id": 10,
      "title": "updatedVal1",
      "author": "updatedVal2"
    }"""
url = "http://localhost:3000/posts/1"

headers = {"Content-Type": "application/json"}
putResponse = requests.patch(url=url, data=putDataTest, headers=headers)
print(putResponse.status_code)
