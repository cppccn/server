## ***/download/*** Entry Point

| Information | Value |
| ----------- |:-------------:|
| URL      | `/download/`        |
| Method   |           GET      |
| Url Params | ***command(STRING)***, ***currentDir(STRING)***      |

### Success Response
Try to visit the following url with your browser and you should see a `download/open file window` prompting:

    http://localhost:8000/download/?command=dw mattia&currentDir=/


### Error Response
coming soon ...

### Sample Call

```javascript
$http.get("/command/", {
        params: {
            "command": "dw filename.txt",
            "currentDir": "/",
        }
    }).success(callback).error(callback); |
```

The above mentioned command will force your browser to have the user choose wether to download or open `filename.txt` which is supposed to be in `currentDir` directory.

or by using `curl` utility:
coming soon ...
