#!/usr/bin/python3
"""the airbnb console."""
import cmd
import re
from shlex import split
from models import storage


def parse(arg):
    brances = re.search(r"\{(.*?)\}", arg)
    brakt = re.search(r"\[(.*?)\]", arg)
    if brances is None:
        if brakt is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brakt.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brakt.group())
            return retl
    else:
        lexer = split(arg[:brances.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(brances.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """the airbnb command console.

    Attributes:
        prompt (str): the input qury.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing."""
        pass

    def default(self, arg):
        """when input qury is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """the quit function."""
        return True

    def do_EOF(self, arg):
        """to singla exit program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        create and print class id
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: display the srtring representation of class with the id
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy the class and its ID."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: display all instance of all classes and there ID."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: give the count of nbr of all instance of classes."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update a class by its given id to update a vlaue or attribute."""
        qarg = parse(arg)
        objdict = storage.all()

        if len(qarg) == 0:
            print("** class name missing **")
            return False
        if qarg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(qarg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(qarg[0], qarg[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(qarg) == 2:
            print("** attribute name missing **")
            return False
        if len(qarg) == 3:
            try:
                type(eval(qarg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(qarg) == 4:
            obj = objdict["{}.{}".format(qarg[0], qarg[1])]
            if qarg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[qarg[2]])
                obj.__dict__[qarg[2]] = valtype(qarg[3])
            else:
                obj.__dict__[qarg[2]] = qarg[3]
        elif type(eval(qarg[2])) == dict:
            obj = objdict["{}.{}".format(qarg[0], qarg[1])]
            for k, v in eval(qarg[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
