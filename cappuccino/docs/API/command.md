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
## Django tests
All commands tests make use of the base `CommandTestCase` class, which sets up a `test directory` inside `local_settings.SHARED_PATH` (removed at the end of the test), and provides a method for directly retrieving the response from the API call.

```python
class CommandTestCase(TestCase):
	def setUp(self):
		self.TEST_DIRNAME = '_command-test-directory'
		self.SYSTEM_PATH_TEST_DIR = local_settings.SHARED_PATH + self.TEST_DIRNAME

		# Creating test dir
		if not os.path.exists(self.SYSTEM_PATH_TEST_DIR):
		    os.makedirs(self.SYSTEM_PATH_TEST_DIR)

	# Retrieves the Response object to the CommandRequest
	def sendCommandRequest(self, params):
		# Making ls request and checking response code
		c = Client()
		response = c.get('/command/', params)
		return response

	def tearDown(self):
		if not os.path.exists(self.SYSTEM_PATH_TEST_DIR):
			shutil.rmtree(self.SYSTEM_PATH_TEST_DIR)
```

The example test case for the `ls` command follows:

```python
class LsCommandTestCase(CommandTestCase):
	def setUp(self):
	  # call to the superclass for executing the general setup operations
		super(LsCommandTestCase, self).setUp()
    ... # ls command specific setup lines

	def test_ls_no_args(self):
		# Making ls request and checking response code
		params = CommandParams('ls', '/').toDict()
		response = super(LsCommandTestCase, self).sendCommandRequest(params)
		self.assertTrue(response.status_code, 200)
	
	  # If you created an example test file in the setUp,
	  # you could now check if that filename can be found
	  # in the response file list

	def tearDown(self):
	  # call to the superclass for executing the general setup operations
		super(LsCommandTestCase, self).tearDown()
    ... # ls command specific tearDown lines

```
