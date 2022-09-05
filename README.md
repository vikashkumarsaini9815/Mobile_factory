# Mobile_Factory

# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/Mobile_Factory_Project
~~~
# installation
~~~
pip install -r requairments.txt
~~~~
# Setup DB migration
~~~
create  factory_database.json and edit following metadata
{
    "A": [10.28, "ED Screen"],
    "B": [24.07, "OLED Screen"],
    "c": [33.3, "AMOLED Screen"],
    "D": [25.94, "Wide-Angle Camera"],
    "E": [32.39, "Ultra-Wide-Angle Camera"],
    "F": [18.77, "USB-C Port"],
    "G": [15.13, "Micro-USB Port"],
    "H": [20.0, "Lightning Port"],
    "I": [42.31, "Android os"],
    "J": [45.0, "ios os"],
    "K": [45.0, "Metallic Body"],
    "L": [30.0, "Plastic Body"]
}

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

