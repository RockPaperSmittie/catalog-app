# Catalog App

This application provides a catalog of clothing items which are sorted in different categories.
The application was made to fulfill the requirements of a project in Udacity's Fullstack Nanodegree course. 

## Aims

This application was created to practice creating applications that support CRUD operations and restful API design. Third party authentication is used to add login capabilities for users.

## Technologies used

* Python
* Flask
* SQLite
* SQLAlchemy
* Bootstrap
* jQuery
* Vagrant
* Virtual Box

Third party authentication via Google and Facebook is used to provide user login and allow for CRUD operations to be done by user.

## Application setup and run

Virtual Machine:
1. Download and install [vagrant](https://www.vagrantup.com/)
2. Download and install [Virtual Box](https://www.virtualbox.org/)
3. Clone this repository to a directory of your choice.
4. cd into directory containing the repository and run `vagrant up` in your terminal to install the virtual machine.
5. Log into your virtual machine by using the `vagrant ssh` command in your terminal.

Running app:

Once logged into your virtual machine, follow the steps below to run the application:

1. This app uses loremipsum as item descriptions. Please install the loremipsum generator through the terminal with the following command:

    `pip install loremipsum`

2. Use the following commands in the same order as seen below to run the application from the terminal:
    
    `python data.py`

    `python run.py`

4. The application can now be accessed through your browser at the following URL: http://localhost:8080

## Screenshot

This is what the app should look like upon visting http://localhost:8080.

![screen](ScreenShot.png)

## API endpoints

| Request | Result |
|--------- | ------ |
| `/catalog.json` | All categories and items |
| `/catalog/category_name.json` | Specific category with items |
| `/item/category_name/itemstyle/item_style.json` | Specific item |