## Installation guide

Note: This project will work with python 3. You also need to have MySQL Database running
- Install 'pdfminer' for python 3
```
    $ pip3 install pdfminer.six
```
- Install Masonite-CLI
```
    $ pip3 install masonite-cli
```
- Install the necessary files in the copied directory
```
    $ craft install
```
Then you need to create a database in MySQL called 'masonite' and add database username and password to the .env file accordingly and then migrate the migations for database
```
    $ craft migrate
```
after migration is finished you need to start the server using:
```
    $ craft serve
```
Now you will be able to access the app using the address 127.0.0.1:8000