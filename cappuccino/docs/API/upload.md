## /upload/ EntryPoint

| Information | Value |
| ----------- |:-------------:|
| URL      | `/upload/`        |
| Method   |           POST      |
| Url Params | ***upl[](Array of STRING of local filepaths)***|

### Success Response

### Error Response

### Sample Call

By using `curl` utility:
```bash
curl -F 'upl[]=@/tmp/test/testfile' http://127.0.0.1:8000/upload/
```