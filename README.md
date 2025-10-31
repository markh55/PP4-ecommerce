# PP4 - WebWorks

This project is a web development agency that provides tiered service packages — Bronze, Silver, Gold, and Platinum. Each package represents a different level of service, with Bronze offering essential entry-level support, Silver providing an enhanced and more comprehensive solution, Gold delivering advanced features and premium support, and Platinum serving as the ultimate top-tier option with the highest level of service and customisation.

[Project link (right click to open in new window)](https://pp4-webworks-8ba6fd0af6ed.herokuapp.com/)

## Table of Contents


  - [Planning](#planning)
    - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
    - [Home Wireframe - Desktop](#home-wireframe---desktop)
    - [Wireframe - Mobile](#wireframe---mobile)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Colour Scheme](#colour-scheme)
    - [Hero / Contact Image](#hero--contact-image)
  - [Final Design](#final-design)
  - [Features](#features)
    - [CRUD](#crud)
      - [Add review \& rating](#add-review--rating)
      - [Edit Review](#edit-review)
      - [Delete Review](#delete-review)
    - [Custom 404 Error Page](#custom-404-error-page)
  - [Deployment](#deployment)
    - [GitHub](#github)
    - [Heroku](#heroku)
    - [AWS](#aws)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
      - [Authentication](#authentication)
      - [Review/Rating](#reviewrating)
      - [Adding to the Bag](#adding-to-the-bag)
      - [Payment / Checkout](#payment--checkout)
      - [Access Control / Security](#access-control--security)
      - [Contact / Newsletter](#contact--newsletter)
      - [Responsive Design / UI](#responsive-design--ui)
    - [CI Python Linter](#ci-python-linter)
  - [Feedback](#feedback)
    - [Packages](#packages)
      - [Before](#before)
      - [After](#after)
  - [Tech Stack](#tech-stack)
  - [Resources](#resources)
    - [Walkthrough Project](#walkthrough-project)
    - [Books](#books)
    - [Documentation / Forums](#documentation--forums)
  - [Credits / Tutorials](#credits--tutorials)
    - [Newsletter](#newsletter)
    - [Invoice / Order History](#invoice--order-history)
    - [Sources Used](#sources-used)

## Planning

### User Stories

![User Stories](https://github.com/user-attachments/assets/007e9734-5c6c-4aab-ba8d-7a0f7f8ee5e4)

## Wireframes

### Home Wireframe - Desktop

This is the mock up of the home page when not signed in on desktop.

![Home Wireframe](https://github.com/user-attachments/assets/8b7f59ea-5db0-476d-b924-2629445604a4)

This is the mock up of the page when user is logged into their account.

![Logged In Wireframe](https://github.com/user-attachments/assets/22953f83-d952-4fba-b5db-4a1400d284a4)

### Wireframe - Mobile

![Mobile Wireframe](https://github.com/user-attachments/assets/f02c428e-fe9a-4748-87b5-5d78c78ef6de)

### Entity Relationship Diagram

Following on from designing the wireframes, I needed to think about a database structure to be used for the project. I opted for a comprehensive setup based around six core models: User, UserProfile, Order, Package, Review, and Rating.

**User model fields:**

* ID (Primary Key)
* Username
* Email
* Password
* Date_joined

**UserProfile model fields:**

* ID (Primary Key)
* User_id (Foreign Key)
* Default_phone_number
* Default_email
* Default_business_name

**Order model fields:**

* ID (Primary Key)
* Order_number
* User_id (Foreign Key)
* Full_name
* Email
* Order_total
* Stripe_pid

**Package model fields:**

* ID (Primary Key)
* Tier
* Name
* Slug
* Description
* Price
* Created_at

**Review model fields:**

* ID (Primary Key)
* Package_id (Foreign Key)
* User_id (Foreign Key)
* Title
* Body

**Rating model fields:**

* ID (Primary Key)
* Package_id (Foreign Key)
* User_id (Foreign Key)
* Rating
* Created_at

This structure allows for a one-to-one relationship between User and UserProfile, while enabling users to place multiple orders and create multiple reviews and ratings for different packages. Each package can have multiple reviews and ratings, keeping the relationships clear and easy to manage.

![ERD](https://github.com/user-attachments/assets/90922d63-6a1f-4d9d-b158-4898806f1101)

## Colour Scheme

![Colour Scheme](https://github.com/user-attachments/assets/9590b6f1-62b3-4d00-9a37-8af20383e892)

I wanted to keep WebWorks’ colour scheme simple and clean, avoiding too many colours that might distract users from the site’s content and offerings. Here’s the palette I’ve chosen:

* **#FFFFFF – White:** Main background colour, providing a clean, minimal canvas.
* **#00D9BB – Turquoise:** Accent colour to highlight key elements such as buttons or call-to-action areas.
* **#F8F9FA – Seasalt:** Soft neutral tone to separate different sections of the page.

### Hero / Contact Image

![Hero / Contact](https://github.com/user-attachments/assets/4844babe-b056-4251-942c-91a5c59f330a)

The hero and contact sections feature a purple gradient image. I chose this because it ties in nicely with the overall colour scheme while adding a subtle ‘pop’ of colour.

## Final Design

## Features

### CRUD

For the CRUD element of the project, users can leave, edit, and delete a review, as well as rate each service. Users can only edit their own reviews and ratings.

#### Add review & rating

![Add Review](https://github.com/user-attachments/assets/7604337b-5ef8-420a-be25-4fd631fe0be1)

#### Edit Review

![Edit Review](https://github.com/user-attachments/assets/3f05a009-ab2c-43dc-96cf-ce1a48f080ce)

#### Delete Review

![Delete Review](https://github.com/user-attachments/assets/1d0aae72-f6e8-4fd8-9e5b-14bd188dc024)

### Custom 404 Error Page

![404 Page](https://github.com/user-attachments/assets/8a65ade4-98f7-4809-a345-109488724ea6)

## Deployment

### GitHub

Created the PP4-ecommerce repository as the main deployment was handled via Heroku + AWS.

### Heroku

1. Created the pp4-webworks app within Heroku and adjusted the location to Europe.  
2. Linked GitHub repository under the “Deploy” tab.  
3. Clicked “Deploy Now” and confirmed deployment by opening the app.

### AWS

1. **Create S3 bucket:** Made bucket public and set region to Europe.  
2. **Upload files:** Uploaded static and media files, matching STATICFILES_DIRS structure.  
3. **Configure bucket permissions & policy:** Enabled public read access and CORS.  
4. **Link S3 to Django settings:** Updated `STATIC_URL` and `MEDIA_URL` using boto3 and django-storages.  
5. **Deploy backend:** Configured environment variables including `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `DATABASE_URL`, `DEBUG`, and `SECRET_KEY`.  
6. **Test live deployment:** Verified site and static files load correctly.

## Testing

### Manual Testing

Manual testing covered:

* Authentication
* Review/Rating
* Adding Items to the Bag
* Payment/Checkout
* Profile management
* Access Control/Security
* Contact/Newsletter
* Responsive Design/UI

#### Authentication

| Feature      | Test Performed                                                        | Outcome     |
| ------------ | ------------------------------------------------------------------- | ----------- |
| Login page   | Logged in as a user                                                   | Completed ✅ |
| Sign-up page | Completed sign up process                                             | Completed ✅ |
| Logout page  | Logged out of account                                                 | Completed ✅ |

#### Review/Rating

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Add review | Verified review added | ✅ |
| Edit review | Verified edit saved | ✅ |
| Delete review | Verified removal | ✅ |
| Add rating | Verified rating added | ✅ |
| Edit rating | Verified update | ✅ |
| Delete rating | Verified deletion | ✅ |
| Users only edit own | Confirmed system prevents edits on others | ✅ |

#### Adding to the Bag

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Add item | Added package to bag | ✅ |
| Remove item | Removed package | ✅ |
| View bag | Checked all package details | ✅ |

#### Payment / Checkout

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Enter payment | Entered valid card | ✅ |
| Process payment | Order instance created correctly | ✅ |
| Payment failure | Checked invalid card error | ✅ |
| Order confirmation | Verified order number and details | ✅ |

#### Access Control / Security

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Order access | Verified only own orders viewable | ✅ |
| Checkout protection | Verified login required | ✅ |

#### Contact / Newsletter

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Submit contact form | Submitted with all fields filled | ✅ |
| Field validation | Tested empty/invalid input | ✅ |
| Success feedback | Verified confirmation message | ✅ |

#### Responsive Design / UI

| Feature | Test Performed | Outcome |
| ------- | -------------- | ------- |
| Mobile layout | Verified on mobile devices | ✅ |
| Tablet layout | Verified tablet screen sizes | ✅ |
| Desktop layout | Verified desktop display | ✅ |
| Navigation | Checked menus/buttons | ✅ |
| Forms | Confirmed forms usable | ✅ |
| Images / media | Verified scaling | ✅ |

### CI Python Linter

Python Code Linting ran on:

* `profiles/views.py`  
* `packages/models.py`  
* `bag/views.py`  
* `checkout/views.py`  
* `home/forms.py`  

Images showing lint results:

* [Bag/Views.py](https://github.com/user-attachments/assets/5734ae93-ffe7-4a28-8d76-f10fb17e42e6)  
* [Checkout/Views.py](https://github.com/user-attachments/assets/5a147093-79b3-41cb-b96a-b7583cf95d49)  
* [Home/Form.py](https://github.com/user-attachments/assets/92f13438-94b7-4efb-a3d2-aa864c6ca471)  
* [Packages/Models.py](https://github.com/user-attachments/assets/c9897f98-168b-4ad7-811a-23da47b12f25)  
* [Profiles/View.py](https://github.com/user-attachments/assets/1a8e0760-fa8c-466f-9954-e3b2d025b02b)  

## Feedback

### Packages

* Fewer clicks for users  
* Clickable icons instead of buttons  
* Intuitive interactions

#### Before

Users had to click “More Details” to view package info.

![Before](https://github.com/user-attachments/assets/a7522871-7f0f-4646-866b-70b266c09f26)

#### After

Whole card is clickable; easier to tap on mobile/tablet.

![After](https://github.com/user-attachments/assets/07a4020c-6541-45f9-877a-af29b1685d67)

## Tech Stack

* HTML  
* CSS / Bootstrap 5  
* JavaScript  
* Python / Django  
* PostgreSQL

## Resources

### Walkthrough Project

* Code Institute  
* Boutique Ado walkthrough project

### Books

* Django 5 By Example by Antonio Melé  
* JavaScript from Beginner to Professional by Lautrnce Lars Svekis & Maaike Van Putten

### Documentation / Forums

* [Django Documentation](https://docs.djangoproject.com/en/5.2/)  
* [Stack Overflow](https://stackoverflow.com/)

## Credits / Tutorials

### Newsletter

Reference: django-newsletter ([newsletter guide](https://dev.to/shubhamkshatriya25/how-to-build-a-email-newsletter-subscriber-in-django-j2p))

### Invoice / Order History

Created with help from *Django 5 By Example* and official Django documentation:

### Sources Used

* [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/)  
* Django Models and Queries  
* Django Views  
* Django Templates
