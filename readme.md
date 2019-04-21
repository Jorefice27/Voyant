# Python Setup
* Navigate to voyant/ and create a python virtual environment (this was written using python 3.5.2)
    * `python -m virtualenv venv`
* Activate the environment
    * `souce venv/bin/activate`
* Install the required packages with pip
    * `python -m pip install -r requirements.txt`
        * This will install the required packages for "requests" and "Django"
        * Note: The latest windows update has made my computer practically useless so I developed this using my linux partition, however I apparently didn't bother using virtual environments in school so just using `pip freeze` added about 50 packages you won't need so I had to comb through that manually, but I believe that these are the only packages that need to be installed

# Password Check
## Simple Password Check
* To run this program, navigate to voyant/ and enter python checkpassword_set.py
* Once the program starts, enter "checkpassword" followed by any string to see if it is a common password
* When this program first loads, it reads all passwords from the file and places them into a hashset for constant lookup times on each query
* Enter "exit" at any time to exit the program

## Radix Password Check
* To run this program, navigate to voyant/ and enter python checkpassword_trie.py
* Once the program starts, enter "checkpassword" followed by any string to see if it is a common password
* When this program first loads, it reads all passwords from the file and places them into a trie for O(m) lookup times, where m is the lenght of the pasword, on each query
* Enter "exit" at any time to exit the program

# FizzBuzz Web Service
* Navigate to voyant/djangoServer/
* Run ```python manage.py migrate```
* Run ```python manage.py runserver```
* Make a request to http://localhost/fizzbuzz using your browser, curl, etc and provide values for "begin" and "end"

# Weather Client
* Navigate to voyant/
* Run `python weather.py`
* Enter "weather" followed by a zip code to retrieve the weather for that area
* If your zipcode is from outside of the USA, add the country code after the zip code (ex: `$weather 75000 fr`)
* Enter "exit" at any time to exit the program