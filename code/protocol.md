# Backend Communication Protocol
If you want to use the backend service, you need to follow the protocol to communicate with the backend.
## POST
```
url = "http://127.0.0.1:5000/start/"

data = {
    "query": "your query here",
    "start_time": "frontend query start time"
}
```
Return message:
* successfully start 
```json
{
   "code": 200 ,"message": "Task started successfully" 
}
```

* missing params or start failed
```json
{
    "code": 500 ,"error": "Internal Server Error"
}
```
* error method
```json
{
    "code": 405 ,"error": "Invalid request method"
}
```
## GET
```
url = "http://127.0.0.1:5000/log/"

params = {
    "query": "your query here",
    "start_time": "frontend query start time"
}
```
Return message:
* successfully get log
```json
{
    "code": 200 ,"log":"log of the task(json)"
}
```
* successfully get log
```json
{
    "code": 500 ,"error": "Internal Server Error"
}
```
* error method
```json
{
    "code": 405 ,"error": "Invalid request method"
}
```