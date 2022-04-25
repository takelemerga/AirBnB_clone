<center> <h2>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Author | https://github.com/takelemerga/AirBnB_clone
<br>
<br>
 <table>
  <tr>
    <th>File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>models/base_model: <a href = "https://github.com/takelemerga/AirBnB_clone/blob/master/models/base_model.py"> BaseModel</a>  
    <td>defines all common attributes/methods for other classes</td>
  </tr>
  <tr>
    <td><a href="https://github.com/takelemerga/AirBnB_clone/tree/master/models"> models</a></td>
    <td>contains project class modules</td>
  </tr>
  <tr>
    <td>models/engine/<a href="https://github.com/takelemerga/AirBnB_clone/tree/master/models/engine">file_storage</a></td>
    <td>serializes instances to a JSON file and deserializes JSON file to instances</td>
  </tr>
  <tr>
    <td><a href="https://github.com/takelemerga/AirBnB_clone/blob/master/console.py">console</a></td>
    <td>entry point of the command interpreter</td>
  </tr>
  <tr>
    <td><a href="https://github.com/takelemerga/AirBnB_clone/tree/master/models/tests">tests/</a></td>
    <td>All files, classes, functions must be tested with unit tests</td>
  </tr>
</table>
<h1><center>Usage</center></h1>
<p>

    First clone this repository. once the repository is cloned locate the "console.py" file and run it as follows:

<code>/AirBnB_clone$ ./console.py</code>

    When this command is run the following prompt should appear:

<code>(hbnb)</code>

    This prompt designates you are in the "HBnB" console.
 </p>
<h3><center>commands<center></h3>
create - Creates an instance based on given class

destroy - Destroys an object based on class and UUID

show - Shows an object based on class and UUID

all - Shows all objects the program has access to, or all objects of a given class

update - Updates existing attributes an object based on class name and UUID

quit - Exits the program (EOF will as well)

help - display documented commands(methods)
<h3>examples</h3>
1. create an object: create className
<hr>
(hbnb) create User
b5fc79ad-0f9f-4864-ac5c-c74278b8e21d
(hbnb) create Use
** class name doesn't exist **
(hbnb)

2.show an object: show className id
<hr>
(hbnb) show User b5fc79ad-0f9f-4864-ac5c-c74278b8e21d
[User] (b5fc79ad-0f9f-4864-ac5c-c74278b8e21d) {'id': 'b5fc79ad-0f9f-4864-ac5c-c74278b8e21d', 'created_at': datetime.datetime(2022, 4, 25, 11, 6, 20, 390648), 'updated_at': datetime.datetime(2022, 4, 25, 11, 6, 20, 390701)}
(hbnb)
