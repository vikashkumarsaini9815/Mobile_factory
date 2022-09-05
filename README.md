# Mobile_Factory_Project

# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/car_rental_company.git
installation
pip install -r requairments.txt
create  factory_database.json
~~~
~~~
Runserver
python manage.py runserver
Rest api for createvehicales
http://127.0.0.1:8000/createvehicales
Request Body :
  {"car_type":"limo","registration":"2345","feature":["ABS","frond air bag","seat belt"]}
Response Body :
  {"succese":True}
Rest api for Booking
http://127.0.0.1:8000/bookingcar
Request Body : 
       {"car_type":"limo","feature":["abc","frond air bag","seat belat"]}
Response Body :
       {'is_available':True , "registration":"6534"}
Rest api for createuser
http://127.0.0.1:8000/createuser
Request Body :
        {"user_name":"vicky","contact":9509582321,"Email":"vicky9846@gmail.com}
Response Body :
        {"car_type":"limo","registration":"7474","feature":["abc","frond air bag","seat belat"]}
Web page for booking car
http://127.0.0.1:8000/selectcar
Web page for create vehicales
http://127.0.0.1:8000/registration
~~~
