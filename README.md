The AirBnB Clone Project is a Python-based project that simulates the backend of the AirBnB website. It includes a command-line interface (CLI) where users can interact with the backend functionalities. Here's a breakdown of the project components and how to use them:


#Project Components:

console.py: This is the main executable of the project, serving as the command interpreter.
models/engine/file_storage.py: Manages serialization of instances to a JSON file and deserialization from JSON to instances.
models/init.py: Initializes a unique FileStorage instance for the application.
models/base_model.py: Defines common attributes/methods for other classes.
models/user.py: Represents the User class which inherits from BaseModel.
models/state.py: Represents the State class which inherits from BaseModel.
models/city.py: Represents the City class which inherits from BaseModel.
models/amenity.py: Represents the Amenity class which inherits from BaseModel.
models/place.py: Represents the Place class which inherits from BaseModel.
models/review.py: Represents the Review class which inherits from BaseModel.

#Usage Modes:

*/Interactive Mode: Users can input commands directly into the console. After executing a command, the prompt appears again, awaiting further input.
*/Non-interactive Mode: Commands can be piped into the shell's execution. In this mode, no prompt appears, and commands are executed immediately.

#Format of Command Input:

Commands should be separated by spaces.
In non-interactive mode, commands need to be piped through an echo.
Interactive mode allows direct keyboard input.

#Available Commands:

quit or EOF: Exits the program.
help: Provides information about command usage.
create: Creates a new instance of a valid class (e.g., BaseModel, User) and saves it to the JSON file.
show: Prints the string representation of an instance based on class name and ID.
destroy: Deletes an instance based on class name and ID and saves the changes into the JSON file.
all: Prints string representations of all instances based on class name.
update: Updates an instance's attribute based on class name and ID and saves changes to the JSON file.
count: Retrieves the number of instances of a class.
How to Start:
Clone the repository from GitHub: git clone https://github.com/jzamora5/AirBnB_clone.git
Navigate to the cloned directory: cd AirBnB_clone
Run the console program: ./console.py

#Examples:
*/Interactive Mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

*/Non-interactive Mode:

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

This setup allows users to interact with the backend functionalities of the AirBnB Clone Project, facilitating actions such as creating, updating, and deleting instances, as well as retrieving counts and representations of instances.
