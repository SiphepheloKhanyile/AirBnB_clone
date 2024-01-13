# 0x00. AirBnB clone - The console
## Background Context
## Welcome to the AirBnB clone project!
### First step: Write a command interpreter to manage the AirBnB objects.

This is the first step towards building a first full web application: the **AirBnB clone**. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:
- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
### What’s a command interpreter?
We want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Exaample Execution of command interpreter
- should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
- And also in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```