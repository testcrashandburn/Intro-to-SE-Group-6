# Group 6
Team Members:
* David Zetterholm,	Team Lead, dz101,	dz101@msstate.edu,  username: testcrashandburn
* Reshma Devi Mandli	rm2478	rm2478@msstate.edu Team member
* Enang Imowo  ije25 ije25@msstate.edu Team member
* Fisher Mason mcf325 mcf325@msstate.edu Team member
* Megan Tucker mpt133 mpt133@msstate.edu Team member

[Sprint 1 Meeting Minutes](https://github.com/testcrashandburn/Intro-to-SE-Group-6/wiki/Meeting)

# Tradex: Group 6's Intro-to-SE Ecommerce Project

This repo is for designing and developing an e-commerce platform that will have a number of functionalities
based on the customer (TA) expectations. 

[We use continuous integration (CI)](https://github.com/testcrashandburn/Intro-to-SE-Group-6/actions/workflows/django.yml)

[Here are some User Stories](https://github.com/testcrashandburn/Intro-to-SE-Group-6/blob/main/user-stories)

[Here is the project's website](http://20.115.44.153:8000/polls/)

Tradex is a web application using a collection of platforms in multiple languages, with a version control system, and live cloud server for testing and presentation. Specifically: 
1. Backend: The web server logic uses the webserver package Django 5.0 
2. Database: The various databases use SQLite 3.38, with Python 3.9 bindings  
3. Frontend: The front end utilizes HTML, CSS, and JavaScript 
4. Version Control: Git with the web-GUI platform GitHub 
5. Cloud Server: Microsoft Azure Standard B1s (1 vcpu, 1 GiB memory), Debian Linux 11 

IDEs: Microsoft Visual Studio Code, Emacs, Micro, Nano


# Tradex Description:

The Tradex application provides a seamless online shopping experience, empowering customers to leverage the Tradex website for convenient and secure online purchases. At its core, the system caters to three primary roles: buyer, seller, and admin should be able to login and perform different actions and logout. Customers can effortlessly browse the website, utilizing the key features of searching for items and comparing them, ensuring a user-friendly experience. The browse and search items functionality serve as the primary use case for customers seeking to explore and view products. 
This search and compare use case extends into several scenarios, allowing customers not only to compare items but also to make purchases and, if needed, initiate returns. This enhances the overall flexibility and user satisfaction within the platform. On the seller's side, the application introduces a set of features facilitating the addition of items, selling processes, and the seamless handling of payments for their listed products. The sell-use case streamlines the seller's journey, ensuring a straightforward and efficient selling experience. Administrators, like another key user group, are equipped with features that enable them to oversee and manage the platform effectively. This includes the crucial ability to approve or block new user accounts and products, contributing to the platform's integrity and security.

# Tradex Features:

* Product Databases
  - There will be a base product class involving product information as well as databases containing the list of products and user interactions with products.
  
* User Accounts and Roles
  - There will be a base user class that involves account login information and class extensions for each role (buyer, seller, administrator).

* Payment Management System
  - There will be a base product class that involves transaction information such as users involved and product information necessary for identifying transactions.
  
* Admin Dashboard
  - The Administrator class extension of the user class will hold a dashboard of administrative actions such as approving/denying account creation as well as monitoring user support/report tickets.
