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

## Architecture
When the server receives a request to this API end point, the `CommandView` is called, analyses the request and asks `CommandFactory` to create the corresponding command object, call its method `execute()` and sends back a `JsonResponse` to the client:

```python
currentDir = request.GET.get('currentDir', '/')
command = request.GET.get('command', 'ls')
commandObject = CommandFactory().createCommand(command)
response = commandObject.execute(currentDir + '/')
return JsonResponse(response, safe="False")
```

The factory instanciates modules classes dinamically by looking into the `modules` directory, since the class which handles a specific command, has the same name as the file it's declared in:

```python
class CommandFactory:
    def __init__(self):
        self.name = "factory"

    def createCommand(self, command):
        command_name = command.split(" ")[0]

        if command_name in constants.ALLOWED_COMMANDS:
            for entry in constants.ALLOWED_COMMANDS:
                if entry == command_name:
                    class_name = command_name[0].capitalize() + command_name[1:] + "Command"
                    module = __import__("cappuccino.apps.command.modules." + class_name, globals(), locals(), [class_name], 0)
                    class_ = getattr(module, class_name)(command)
                    return class_
        else:
            return commands.ErrorCommand(command)
```

`CommandFactory` takes the full command from `CommandView`, checks if the user has rights to execute that command, and if that's the case, it returns an instance of the `command object` needed.

## Extension
The above explained architecture easily allows to extend our server for it to be able handling a new command, by following these few steps.
If you want to add a command that counts pdf files with the following syntax:
```bash
count_pdf dirname
```

- add a `Count_pdfCommand.py` file into `modules` directory
- declare `Count_pdfCommand` class inside it (First char needs to be `uppercase`)
- the above mentioned class needs to inherit from `BaseCommand` class
- overright the `execute()` method
- the `execute()` method must return a `CommandResponse` object

Here's a command class declaration example:
```python
class CdCommand(BaseCommand):
    def __init__(self, full_name):
        self.full_name = full_name

    def execute(self, currentDir):
        # Sending a list of json FileEntry objects
        return self.cd(currentDir)

    # Returns a CommandResponse object with an ErrorMessage or the currentDir value after the command execution
    def cd(self, currentDir):
        if self.full_name == "cd .": # Case no arguments
            return CommandResponse(True, currentDir)
        elif self.full_name == "cd":
            return '/'
        else: # Case with arguments
            if self.full_name == "cd ..": # Case go back to parent
                parentDir = self.parentDir(currentDir)
                if parentDir:
                    path =  local_settings.SHARED_PATH + parentDir
                    return CommandResponse(True, path)
                else:
                    return CommandResponse(True, currentDir)
            else: # Case ls path
                return CommandResponse(True, local_settings.SHARED_PATH + self.full_name.split(' ')[1])

    def parentDir(self, currentDir):
	...
```


