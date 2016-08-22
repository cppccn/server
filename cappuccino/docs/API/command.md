## /command/ EntryPoint

| Information | Value |
| ----------- |:-------------:|
| URL      | `/command/`        |
| Method   |           GET      |
| Url Params | ***command(STRING)***, ***currentDir(STRING)***      |

### Success Response

```python
{ 
  'data':
  [{'last_modified': 'Mon Aug 15 12:53:31 2016', 'type': 'dir', 'name': u'.X11-unix', 'size': '0.0 Mb'},
   {'last_modified': 'Mon Aug 15 12:53:36 2016', 'type': 'dir', 'name': u'.ICE-unix', 'size': '0.0 Mb'},
   {'last_modified': 'Mon Aug 15 12:53:31 2016', 'type': 'file', 'name': u'.X0-lock', 'size': '11 b'},
  'type': true
}
```         
### Error Response
```python
{'type': false, 'data': "Path not correct, file does not exist"}           |
```

### Sample Call

```javascript
$http.get("/command/", {
        params: {
            "command": "ls",
            "currentDir": "/",
        }
    }).success(callback).error(callback); |
```

or by using `curl` utility:
```bash
curl 'http://localhost:8000/command=ls&currentDir=/'
```
