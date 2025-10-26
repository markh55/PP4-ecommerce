# PP4 - WebWorks
This project is a web development agency that provides tiered service packages — Bronze, Silver, Gold, and Platinum. Each package represents a different level of service, with Bronze offering essential entry-level support, Silver providing an enhanced and more comprehensive solution, Gold delivering advanced features and premium support, and Platinum serving as the ultimate top-tier option with the highest level of service and customisation.

[Project link (right click to open in new window)](https://pp4-webworks-8ba6fd0af6ed.herokuapp.com/)

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
     * [Walkthrough Project](#walkthrough-project)
     * [Books](#books)
     * [Documention / forums](#documention--forums)
10. [Credits / Tutotials](#credits--tutorials)
     * [Sources used](#sources-used)


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


<img width="1600" height="1200" alt="Webworks (2)" src="https://github.com/user-attachments/assets/9590b6f1-62b3-4d00-9a37-8af20383e892" />


I wanted to keep WebWorks’ colour scheme simple and clean, avoiding too many colours that might distract users from the site’s content and offerings. With that in mind, here’s the palette I’ve chosen and the reasoning behind each colour:

#FFFFFF – White: This serves as the main background colour, providing a clean, minimal canvas for the rest of the site.

#00D9BB – Turquoise: Used as an accent colour to highlight key elements such as buttons or call-to-action areas, helping them stand out without being overwhelming.

#F8F9FA – Seasalt: This soft neutral tone is used to separate different sections of the page, such as “What We Offer” and “What Our Clients Say.” The subtle contrast creates a clear visual distinction while maintaining a cohesive look.

### Hero / Contact Image

<img width="1000" height="562" alt="hero copy" src="https://github.com/user-attachments/assets/4844babe-b056-4251-942c-91a5c59f330a" />

The hero and contact sections feature a purple gradient image. I chose this because it ties in nicely with the overall colour scheme while adding a subtle ‘pop’ of colour. The image helps the site stand out visually, yet still maintains a clean and minimal look that fits the WebWorks style.

If I were to change something, this would be the one area I’d revisit — I think I could recreate a very similar effect using CSS alone for a more lightweight and flexible solution.

## Final Design


## Features

### Authentication

I configured Django’s email backend to use Gmail SMTP for sending authentication-related emails. This setup supports features like:

* Account verification and confirmation during user registration

* Password reset functionality using secure, time-limited links

## Deployment

### Git Hub 
with this project all i needed to do on github was create the PP4-ecommerce repository as the main deployment was handled via Heroku + AWS (steps below)

### Heroku
1. First step i did was create the pp4-webworks app within Heroku by creating the app name and ajusting the location to europe, once they was done i clicked create app.

<img width="1782" height="1032" alt="Screenshot 2025-10-21 at 21 37 47" src="https://github.com/user-attachments/assets/9d3f5130-109e-472e-abdc-4d722d9c8621" />

2. Second step was to navigate to the 'Deploy" tab and link my Github account once that was linked i could then search for my repository i would like to link.

<img width="1788" height="975" alt="Screenshot 2025-10-21 at 21 40 14" src="https://github.com/user-attachments/assets/c9708643-0018-4282-b4d2-00c3eb90a24c" />

3. Following on from step two once that was all linking up i go to the bottom of the page and click "deploy now".

<img width="1782" height="1031" alt="Screenshot 2025-10-21 at 21 40 48" src="https://github.com/user-attachments/assets/85c49abd-b3ab-4de5-afd2-36f1fba3d638" />

4. Then when they deployment is compeleted it would go back to the top of the page to click "open app" to ensure my project was all linked and working as it should.

<img width="1259" height="186" alt="Screenshot 2025-10-21 at 21 43 24" src="https://github.com/user-attachments/assets/11a8aee2-36aa-4fe9-bf75-65b01d3483e1" />


### AWS

1. Create an S3 bucket
First, I logged into my AWS account and navigated to S3. I clicked Create bucket, gave it a unique name (pp4-webworks), and selected the region closest to me (Europe). I also ensured the bucket was publicly accessible so my static files could be served.

2. Upload project files to S3
Next, I uploaded all static and media files to the bucket. This included CSS, images, and JavaScript files. I made sure the folder structure matched STATICFILES_DIRS from my Django project to prevent broken links.

3. Configure bucket permissions & policy
After uploading, I added a bucket policy to allow public read access, ensuring users could access static files directly. I also enabled CORS to allow cross-origin requests if needed.

4. Link S3 bucket to Django settings
I updated settings.py in my Django project to point STATIC_URL and MEDIA_URL to the S3 bucket using boto3 and django-storages. This ensures all static files and media are served from AWS.

5. Deploy backend
To deploy the full site, I configured environment variables in AWS, including AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to connect to AWS services, DATABASE_URL for the PostgreSQL database, and other project-specific settings such as DEBUG and SECRET_KEY. This setup allowed the Django project to run online and be publicly accessible.

6. Test live deployment
Finally, I accessed the site’s public URL to ensure it was live and that all static files were loading correctly from the S3 bucket.

As this was my first time setting up and using AWS, I did not take any screenshots of the step-by-step setup process, but I have explained in detail above what I did and how.

## Testing


## Feedback

When my PP4 project was tested by family and friends, I received the following feedback:

### Packages:

Fewer clicks: Make it easier for users to complete actions without having to search for buttons.
Clickable icons: Allow icons to perform the same actions as buttons, so users can click the icon instead of scrolling for a “More Details” button.
Intuitive interactions: Ensure the design feels natural and users instinctively know what can be clicked.

### Before:

Users had to click the “More Details” button to view package information and add it to their bag.

<img width="1248" height="637" alt="Screenshot 2025-10-26 at 22 37 51" src="https://github.com/user-attachments/assets/a7522871-7f0f-4646-866b-70b266c09f26" />

### After
After taking the feedback, I updated my project to remove the “More Details” button and make the whole card a clickable object. This has several benefits, especially as the majority of web browsing now happens on mobile and tablet devices: it provides larger, easier-to-tap areas, reduces the chance of users missing small buttons, and makes navigation feel more intuitive and seamless across different screen sizes.

<img width="1225" height="587" alt="Screenshot 2025-10-26 at 23 03 06" src="https://github.com/user-attachments/assets/07a4020c-6541-45f9-877a-af29b1685d67" />

## Tech Stack

- HTML
- CSS / Bootstrap 5
- JavaScript
- Python / Django 

## Resources

### Walkthrough Project
- Code Institute
  - Boutique Ado

### Books
- Djnago 5 By Example by Antonio Mele
- JavaScript from Beginner to Professional by Lautrnce Lars Svekis & Maaike Van Putten

### Documention / forums
- Documentation for Django - <https://docs.djangoproject.com/en/5.2/>  
- Stack Overflow


## Credits / Tutorials

### Sources Used

### Newsletter
I used django-newsletter ([click here](https://dev.to/shubhamkshatriya25/how-to-build-a-email-newsletter-subscriber-in-django-j2p)) as a reference for the newsletter signup within the footer, and adapted the code to fit my project. This was just used as a guide.

### Invoice / Order History

This section was created with help from *Django 5 By Example* and the official Django documentation listed below:

- [Django 5.2 Documentation](https://docs.djangoproject.com/en/5.2/)
- Django Models and Queries  
- Django Views  
- Django Templates

