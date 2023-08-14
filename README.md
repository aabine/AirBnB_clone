# HBNB Command Line Interface (CLI)

## Project Description

This project is an Airbnb-like clone that focuses on building a command-line interface (CLI) for managing different data models. The CLI allows you to interact with the application, create, read, update, and delete instances of various classes such as User, State, City, Amenity, Place, Review, etc.

## Command Interpreter

The Command Interpreter is the core of the project, providing an interactive interface for managing and manipulating the data models. It supports various commands for managing instances, searching, updating, and more.

### How to Start

To start the Command Interpreter, navigate to the project directory and run the `console.py` script:

```bash
python console.py
```

### How to Use

Once the Command Interpreter is running, you'll see a prompt `(hbnb) `. You can enter commands to perform various actions on the data models.

### Examples

- Creating a new instance:
  ```bash
  (hbnb) create User
  ```

- Showing an instance:
  ```bash
  (hbnb) show User 12345
  ```

- Updating an instance:
  ```bash
  (hbnb) update User 12345 first_name "John"
  ```

- Deleting an instance:
  ```bash
  (hbnb) destroy User 12345
  ```

- Listing all instances of a class:
  ```bash
  (hbnb) all User
  ```

## Authors

- Austine Abine (kendoaustine@yahoo.com)
- Josiah Jonathan Segun (jothamjosiah10@gmail.com)

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`
3. Make changes and commit: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin new-feature`
5. Create a pull request.

```
