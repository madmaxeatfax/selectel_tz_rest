# REST API

The REST API to the example app is described below.


## Get my jokes
### Request
`GET /api/v1/jokes`

	curl -i "http://localhost:5000/api/v1/jokes?login=Gunter"

### Response

	HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 577
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:58:26 GMT

	{
	  "jokes": [
		{ "content": "Chuck Norris can multiply length x width x heigth when finding the circumference of a circle.",  "id": 2 },
		{ "content": "In the Bible, Jesus turned water into wine. But then Chuck Norris turned that wine into beer.", "id": 4 },
		{ "content": "Chuck Norris can make a single female cheat.",  "id": 5 }
	  ],
	  "user": { "id": 1, "login": "Gunter" }
	}


## Create new joke
### Request
`POST /api/v1/jokes`

	curl -X POST -F joke="some joke" -i "http://localhost:5000/api/v1/jokes?login=Gunter"

### Response

    HTTP/1.0 201 CREATED
	Content-Type: application/json
	Content-Length: 115
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:14:52 GMT

	{
	  "joke": { "content": "some joke", "id": 1 },
	  "user": { "id": 1, "login": "Gunter" }
	}


## Get my joke
### Request
`GET /api/v1/jokes/:id`

	curl -i "http://localhost:5000/api/v1/jokes/1?login=Gunter"

### Response

    HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 78
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:30:19 GMT

	{
	  "joke": { "content": "some joke", "id": 1 },
	  "user_id": 1
	}


## Update my joke
### Request
`PUT /api/v1/jokes/:id`

	curl -X PUT -F joke="another joke" -i "http://localhost:5000/api/v1/jokes/1?login=Gunter"

### Response

    HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 81
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:33:17 GMT

	{
	  "joke": { "content": "another joke",  "id": 1 },
	  "user_id": 1
	}


## Delete my joke
### Request
`DELETE /api/v1/jokes/:id`

	curl -X DELETE -i "http://localhost:5000/api/v1/jokes/1?login=Gunter"

### Response

    HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 81
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:36:18 GMT

	{
	  "joke": { "content": "another joke", "id": 1 },
	  "user_id": 1
	}


## Get random joke
### Request
`GET /api/v1/jokes/random`

	curl -i "http://localhost:5000/api/v1/jokes/random?login=Gunter"

### Response

	HTTP/1.0 200 OK
	Content-Type: application/json
	Content-Length: 162
	Server: Werkzeug/0.16.0 Python/3.7.3
	Date: Sun, 13 Oct 2019 12:53:05 GMT

	{
	  "joke": { "content": "Chuck Norris can multiply length x width x heigth when finding the circumference of a circle.", "id": 2 },
	  "user_id": 1
	}