# Catalog App

This application provides a catalog of clothing items which are sorted in different categories.

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
4. cd into directory containing the repository and run `vagrant up` to install the virtual machine.
5. Log into your virtual machine with `vagrant ssh`.

Running app:
1. Install the loremipsum generator through the command line with the following command:
```bash
pip install loremipsum
```
2. Run the data.py file.
```bash
python data.py
```
3. Run the run.py file.
```bash
python run.py
```
4. The application can now be accessed through your browser at the following URL: http://localhost:8080

## Screenshot

This is what the app should look like upon visting http://localhost:8080.

![screen](ScreenShot.png)

## API endpoints

`/catalog.json` - All categories and items

`/catalog/category_name.json` - Specific category with items

`/item/category_name/itemstyle/item_style.json` - Specific item