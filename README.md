# Mobile_Factory_Project

# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/car_rental_company.git
~~~
# installation
~~~
pip install -r requairments.txt
~~~~
# Setup DB migration
~~~
create  factory_database.json
~~~
# Runserver
~~~
python manage.py runserver
~~~
# Rest api for mobile
~~~
http://127.0.0.1:8000/mobile/
Request Body :
  {"components":["A","B","C"]}
Response Body :
  {
    "order_id": 286,
    "Total": 92.67,
    "parts": [
        "ED Screen",
        "Ultra-Wide-Angle Camera",
        "Plastic Body",
        "Lightning Port"
    ]
}
~~~

