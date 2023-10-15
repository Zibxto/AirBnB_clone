# ALX Project - AirBnB clone

## Description

A project by ALX to create a simplified version of the popular Airbnb platform. It involves building a command-line interpreter that allows users to manage various objects within the AirBnB project, such as users, states, cities, and places. The project implements a parent class, `BaseModel`, for object initialization, serialization, and deserialization. Additionally, the project includes comprehensive unit tests to ensure the functionality and reliability of all classes and the storage engine.

## Command Interpreter

The command interpreter serves as a simplified version of the Shell, tailored to manage specific objects within the AirBnB project. The interpreter enables users to perform the following operations:

- Create a new object (e.g., User, Place)
- Retrieve an object from a json file.
- Update attributes of an object
- Delete an object

## How to Start It

To start the AirBnB command interpreter, follow these steps:

1. Clone the project repository from GitHub link.
2. Navigate to the project directory.
3. Run the `console.py` file to start the command-line interpreter using `./console.py` or `python3 console.py`.

## How to Use It

The command interpreter provides a set of commands that can be used to manage AirBnB objects. Some basic commands include:

- `create` - Creates a new instance of a specified class.
- `show` - Displays the details of a specific object.
- `destroy` - Deletes a specified object.
- `update` - Updates the attributes of a specified object.
- `all` - Display all objects.

The command-line interface also provides various options and functionalities for managing the AirBnB project efficiently.

## Examples

Here are some examples of how to use the command interpreter:

To create a new User:
```python3
(hbnb) create User
```

To display the details of a specific Place:
```python3
(hbnb) show Place 1234-1234-1234
```

To update the name of a State:
```python3
(hbnb) update State 9876-9876-9876 name "Abuja"
```

To display all object for specific Review:
```python3
(hbnb) all Review
```

To delete details of a specific Amenity
```python3
(hbnb) destroy Amenity 1234-1234-1234
```

These examples demonstrate the basic usage of the command interpreter for managing AirBnB objects.
