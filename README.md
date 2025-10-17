# PP4 - WebWorks
This project is a web development agency that provides tiered service packages — Bronze, Silver, Gold, and Platinum. Each package represents a different level of service, with Bronze offering essential entry-level support, Silver providing an enhanced and more comprehensive solution, Gold delivering advanced features and premium support, and Platinum serving as the ultimate top-tier option with the highest level of service and customisation.

## Table of Content

1. [Planning](#planning)
     * [User Stories](#user-stories)
     * [Wireframes](#wireframes)
     * [Entity Relationship Diagram](#entity-relationship-diagram)
     * [Colour Scheme](#colour-scheme)
2. [Final Design](#final-design)
3. [Features](#features)
4. [Deployment](#deployment)
5. [Testing](#testing)
6. [Feedback](#feedback)
7. [Tech Stack](#tech-stack)
8. [Resources](#resources)
9. [Credits / Tutotials](#credits--tutorials)
    * [Source used](#source-used)


## Planning

### User Stories
<img width="1193" height="489" alt="Screenshot 2025-09-09 at 21 31 32" src="https://github.com/user-attachments/assets/007e9734-5c6c-4aab-ba8d-7a0f7f8ee5e4" />



## Wireframes

### Home Wirefram - Desktop

This is the mock up of the home page when not signed in on desktop.
<img width="603" height="596" alt="home-wireframe" src="https://github.com/user-attachments/assets/8b7f59ea-5db0-476d-b924-2629445604a4" />

This is the mock up of the page when user is logged into their account.
<img width="603" height="596" alt="LoggedIn-Wireframe" src="https://github.com/user-attachments/assets/22953f83-d952-4fba-b5db-4a1400d284a4" />

### Wirefram - Mobile

<img width="301" height="1266" alt="Mobile Wireframe" src="https://github.com/user-attachments/assets/f02c428e-fe9a-4748-87b5-5d78c78ef6de" />


### Entity Relationship Diagram

Entity Relationship Diagram
Following on from designing the wireframes, I needed to think about a database structure to be used for the project. I opted for a comprehensive setup based around six core models: User, UserProfile, Order, Package, Review, and Rating.
The User model is composed of the following:

* ID (Primary Key)
* Username
* Email
* Password
* Date_joined

The UserProfile model is composed of the following:

* ID (Primary Key)
* User_id (Foreign Key)
* Default_phone_number
* Default_email
* Default_business_name

The Order model is composed of the following:

* ID (Primary Key)
* Order_number
* User_id (Foreign Key)
* Full_name
* Email
* Order_total
* Stripe_pid

The Package model is composed of the following:

* ID (Primary Key)
* Tier
* Name
* Slug
* Description
* Price
* Created_at

The Review model is composed of the following:

* ID (Primary Key)
* Package_id (Foreign Key)
* User_id (Foreign Key)
* Title
* Body

The Rating model is composed of the following:

* ID (Primary Key)
* Package_id (Foreign Key)
* User_id (Foreign Key)
* Rating
* Created_at

This structure allows for a one-to-one relationship between User and UserProfile, while enabling users to place multiple orders and create multiple reviews and ratings for different packages. Each package can have multiple reviews and ratings, keeping the relationships clear and easy to manage.

<img width="1143" height="703" alt="ERD" src="https://github.com/user-attachments/assets/90922d63-6a1f-4d9d-b158-4898806f1101" />

## Colour Scheme


## Final Design


## Features


## Deployment


## Testing


## Feedback


## Tech Stack

- HTML
- CSS / Bootstrap 5
- JavaScript
- Python / Django 

## Resources

- Code Institute
  - Boutique Ado

- Djnago 5 By Example by Antonio Mele

- Documentation for Django - <https://docs.djangoproject.com/en/5.2/>
  
- Stack Overflow


## Credits / Tutorials

### Newsletter
I used django-newsletter ([click here](https://dev.to/shubhamkshatriya25/how-to-build-a-email-newsletter-subscriber-in-django-j2p)) as a reference for the newsletter signup within the footer, and adapted the code to fit my project. This was just used as a guide.

## Invoice / Order History

This section was created with help from *Django 5 By Example* and the official Django documentation listed below:

- [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/)
- Django Models and Queries  
- Django Views  
- Django Templates



### Source Used
