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
    - [Authentication](#authentication) 
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

### Authentication

For the authentication sign-up, I’ve decided to disable verification emails. Without paying for a service my options are very limited, so this simplifies the process. Users are only required to provide their details and a verification email is not sent. This keeps the authentication process lightweight and functional for the scope of this project.

<img width="676" height="736" alt="Screenshot 2025-11-01 at 18 37 26" src="https://github.com/user-attachments/assets/addccd18-7e08-4162-a458-6ce64b3bcac2" />


### Contact Form

For the contact form, once it is submitted, users immediately see a thank you message and no additional email confirmations are sent; for the purpose of this project, setting up emails to be sent out is very limited and would cost me if the free allowance were exceeded. For a real store or live site, a confirmation email would be sent to the user.

<img width="1493" height="956" alt="Screenshot 2025-11-01 at 18 55 58" src="https://github.com/user-attachments/assets/16909208-5a43-4330-a05c-ce5dc088dcb3" />


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

with this project all i needed to do on github was create the PP4 repository as the main deployment was handled via Heroku & AWS (steps below)

### Heroku

1. First step i did was create the app within Heroku by creating the app name and ajusting the location to europe, once they was done i clicked create app.

<img width="1262" height="937" alt="Screenshot 2025-10-31 at 21 47 40" src="https://github.com/user-attachments/assets/b7033e9c-644d-4d44-bfd3-ce2f39b56246" />

2. Second step was to navigate to the 'Deploy" tab and link my Github account once that was linked i could then search for my repository i would like to link.

<img width="1255" height="751" alt="Screenshot 2025-10-31 at 21 48 25" src="https://github.com/user-attachments/assets/14f3d50e-664c-4cf4-8af5-5cf804899de3" />

  
3. Following on from step two once that was all linking up i go to the bottom of the page and click "deploy now".

<img width="1256" height="956" alt="Screenshot 2025-10-31 at 21 48 58" src="https://github.com/user-attachments/assets/f1ecb42d-67bf-41f3-b03e-c60a00babbf1" />

4. Then when they deployment is compeleted it would go back to the top of the page to click "open app" to ensure my project was all linked and working as it should.
   
<img width="1266" height="184" alt="Screenshot 2025-10-31 at 21 49 13" src="https://github.com/user-attachments/assets/a16287f4-9cec-466e-95b4-24e1a2f3ad09" />


To complete the deployment of my Django app, I updated the ALLOWED_HOSTS list in the settings.py file to include my local development addresses and my deployed Heroku domain. This ensures that Django will accept requests from both environments.

<img width="653" height="53" alt="Screenshot 2025-11-02 at 13 50 57" src="https://github.com/user-attachments/assets/c20a2620-abb8-4625-a08c-d0ae7e422382" />

This tells Django which hosts are allowed to make requests to the app.

* "127.0.0.1" and "localhost" allow the app to run locally without triggering errors during development.

* The Heroku domain ("pp4-webworks-8ba6fd0af6ed.herokuapp.com") allows the deployed version of the app to respond to incoming requests on Heroku.

If a request comes from a host not listed here, Django will block it and return a “400 Bad Request” error for security reasons.



### AWS

For AWS i didnt get any screenshots of the process but all i did was set up S3, IAM, and linked everything to Django. Steps below:

1. Create S3 bucket: I logged into AWS, created a new S3 bucket, set it to public, and chose the Europe region.

2. Set up IAM user: I created an IAM user specifically for the project, gave it programmatic access, and attached a policy that allowed full S3 access to my bucket only. I saved the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY for Django.

3. Upload files: I uploaded static and media files, keeping the folder structure consistent with STATICFILES_DIRS.

4. Configure bucket permissions & policy: I enabled public read access and set up CORS so the site could fetch the files.

5. Link S3 to Django settings: I updated STATIC_URL and MEDIA_URL using boto3 and django-storages so Django would serve files from the bucket.

5. Deploy backend: I configured environment variables in AWS (like AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, DEBUG, SECRET_KEY) so the app could run securely.

7. Test live deployment: I opened the site to make sure everything loaded correctly and static/media files were working.

## Testing

### Manual Testing

To ensure the quality and performance of my project, I performed comprehensive manual testing. My testing covers the following main components:  

* Authentication
* Review/Rating
* Adding Items to the Bag
* Payment/Checkout
* Profile management
* Access Control/Security
* Contact/Newsletter
* Responsive Design/UI

Each component was tested to ensure it functions correctly and provides a smooth, user-friendly experience.


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

Python Code Linting: I ran a CI linter on key Python files to catch style and syntax issues. The files tested include:

* profiles/views.py → represents Authentication/Profile
* packages/models.py → represents Review/Rating
* bag/views.py → represents Adding Items to the Bag
* checkout/views.py → represents Payment/Stripe
* home/forms.py → represents Contact/Newsletter

The screenshots show the code follows PEP8 standards, is clean, and is easier to read, reducing the likelihood of bugs.

### Bag/Views.py

<img width="1261" height="981" alt="Screenshot 2025-10-31 at 20 12 43" src="https://github.com/user-attachments/assets/5734ae93-ffe7-4a28-8d76-f10fb17e42e6" />

### Checkout/Views.py

<img width="1216" height="775" alt="Screenshot 2025-10-31 at 20 20 52" src="https://github.com/user-attachments/assets/5a147093-79b3-41cb-b96a-b7583cf95d49" />

### Home/Form.py

<img width="1265" height="904" alt="Screenshot 2025-10-31 at 20 22 08" src="https://github.com/user-attachments/assets/92f13438-94b7-4efb-a3d2-aa864c6ca471" />

### Packages/Models.py

<img width="1273" height="833" alt="Screenshot 2025-10-31 at 20 25 27" src="https://github.com/user-attachments/assets/c9897f98-168b-4ad7-811a-23da47b12f25" />

### Profiles/View.py

<img width="1277" height="816" alt="Screenshot 2025-10-31 at 20 27 31" src="https://github.com/user-attachments/assets/1a8e0760-fa8c-466f-9954-e3b2d025b02b" /> 

### Lighthouse

**Desktop**

<img width="444" height="158" alt="Desktop" src="https://github.com/user-attachments/assets/4870d4ff-e632-446a-b0c6-02ba74d5f391" />

**Mobile**

<img width="435" height="158" alt="Mobile" src="https://github.com/user-attachments/assets/5b960c70-fdfe-483b-9f44-f48b07835094" />

I performed lighthouse testing on my project to ensure that the performance was optimal for each device as you can see the scores come in as:

* **Performance**

  - Desktop - 99
  - Mobile - 94

* **Accessibility**

  - Desktop - 90
  - Mobile - 90

* **Best Practice**

  - Desktop - 78
  - Mobile - 79

* **SEO**
  
   - Desktop - 91
   - Mobile - 91
 
From these findings, the Best Practices scores are in the high 70s on both desktop and mobile. While this could be improved, the main factor affecting the score is Stripe, a third-party payment API. Stripe injects scripts and sets third-party cookies (e.g., from js.stripe.com and m.stripe.com), which are flagged in Chrome DevTools. These are part of Stripe’s functionality and cannot be controlled or removed from my side, so the slightly lower score is expected and does not indicate an issue with the project itself.

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
