# **AirBnB clone - The console**
________________________________________
<img src="https://github.com/jegomezV/holbertonschool-AirBnB_clone/blob/master/hbnbnn%20creyk.png?raw=true">


*In this project we will develop a simple copy of the [AirBnB](https://www.airbnb.com.co/) website, starting now until the end of the first year. In this first part we developed the console.*
________________________________________

## **The console**

________________________________________
- Create our data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to a file (JSON file)
________________________________________

## **Usage**
````./console.py

(hbnb) help

Documented commands (type help <topic>):
======================================== 
EOF  help  quit

(hbnb)

(hbnb)

(hbnb) quit

$
````

They should pass in non-interactive mode: <code>$ echo "python3 -m unittest discover tests" | bash</code>
________________________________________

## **How to use it**

| File | Description | Attributes |
| :---         |     :---:      |          ---: |
| <code>help   | Display all commands available  | <code>help     |
| <code>create | Creates new object   | <code>create (class here)<code> |
| <code>update | Updates attribute of an object|<code>User.update('123', {'name': 'Greg_n_Mel'})|
| <code>all   | Display all objects in class  | <code>user.all    |
| <code>show  | Retrieve an object from a file | <code>user.show |
| <code>destroy  | Destroy specified object |  <code>User.destroy('123') |
| <code> quit | Exits     | <code> quit    |






