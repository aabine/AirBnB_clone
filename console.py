#!/usr/bin/python3
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF (Ctrl+D)"""
        return True

    def do_help(self, arg: str):
        """Displays help documentation"""
        print("Custom help message for HBNBCommand:")
        print("- quit: Exit the program")
        print("- EOF: Exit the program on EOF (Ctrl+D)")

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and save it to the JSON file"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        class_name = arg.split()[0]

        try:
            class_module = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        new_instance = class_module()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        # Get the class module
        try:
            class_module = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)

        all_objs = storage.all()
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        # Get the class module
        try:
            class_module = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)

        all_objs = storage.all()
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints string representation of all instances based on class name"""
        objects = storage.all().values()

        if args:
            try:
                filtered_objects = [str(obj) for obj in objects
                                    if type(obj).__name__ == args]
                if not filtered_objects:
                    print("** class doesn't exist **")
                    return
                print(filtered_objects)
            except NameError:
                pass
        else:
            result = [str(obj) for obj in objects]
            print(result)

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        args = line.split()
        print("Args:", args)

        # Check if the correct number of arguments is provided
        if len(args) < 4:
            print("Usage: update <class name> <id>"
                  "<attribute name> <attribute value>")
            return

        class_name = args[0]
        obj_id = args[1]
        attribute_name = args[2]
        attribute_value = " ".join(args[3:])
        # Remove the double quotes from the attribute value
        attribute_value = attribute_value.strip('"')
        try:
            # Get the class module using the provided class name
            class_module = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        # Retrieve all objects
        all_objs = storage.all()
        obj_key = "{}.{}".format(class_name, obj_id)

        # Check if the instance exists
        if obj_key not in all_objs:
            print("** no instance found **")
            return

        instance = all_objs[obj_key]

        # Check if the instance is a dictionary or an object
        if not isinstance(instance, dict):
            if not hasattr(instance, attribute_name):
                # Convert the attribute value to the appropriate data type
                try:
                    if attribute_value.isdigit():
                        converted_value = int(attribute_value)
                    else:
                        converted_value = float(attribute_value)
                except ValueError:
                    converted_value = attribute_value
            else:
                converted_value = attribute_value
            setattr(instance, attribute_name, converted_value)
        else:
            # Handle dictionary case
            instance[attribute_name] = attribute_value

        # Save the updated instance
        instance.save()
        print("Attribute updated successfully")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Execute non-interactive command and exit
        cmd_args = " ".join(sys.argv[1:])
        HBNBCommand().onecmd(cmd_args)
    else:
        # Enter interactive command loop
        HBNBCommand().cmdloop()
