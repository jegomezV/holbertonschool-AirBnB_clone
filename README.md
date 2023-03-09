<p align="center"> 
<img src="https://github.com/jegomezV/holbertonschool-AirBnB_clone/blob/master/hbnbnn%20creyk.png?raw=true">
</p>

*In this project we will develop a simple copy of the [AirBnB](https://www.airbnb.com.co/) website, starting now until the end of the first year. In this first part we developed the console.*
________________________________________

## **The console description** 
Command interpreter based in cmd to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)


- Create our data model
- Manage (create, update, destroy, etc) objects via a console/command interpreter
- Store and persist objects to a file (JSON file).

The first piece (the console) is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later.

________________________________________

## **Usage**
````
./console.py

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
| <code> quit | Close the console | <code> quit|
________________________________________


## **Class Models**

| File | Description | Attributes |
| :---         |     :---:      |          ---: |
| <code>base_model.py  | 	BaseModel class for all the sub-classes  | <code>id, created_at, updated_at     |
| <code>user.py | User class for user information.  | <code>email, password, first_name, last_name<code> |
| <code>amenity.py | Amenity class for information about amenities.|<code>name|
| <code>city.py   | City class for information about the city.  | <code>state_id, name    |
| <code>state.py  | State class for information about the state. | <code>name |
| <code>place.py | Place class for details of the AirBnB apartments for rent. |  <code>city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| <code> review.py | Review class for review information from the user/client. | <code> place_id, user_id, text|
________________________________________
## **How to Install** 
### Clone the repository in [this](https://github.com/jegomezV/holbertonschool-AirBnB_clone) link or copy the text bellow.

```` 
git@github.com:jegomezV/holbertonschool-AirBnB_clone.git
````
________________________________________

## **Testing**
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

````
$ python3 unittest -m discover tests
````
````
$ python3 unittest -m tests/test_console.py
````
________________________________________

## **Authors**
- [Cristhian Andres Jurado](https://github.com/Chrs-creyk)

- [Juan Eduardo Gomez](https://github.com/jegomezV)
