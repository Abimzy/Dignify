# Project: Dignify®

Electronic medical records (EMR) or electronic health records (EHR) have been shown to improve quality patient care and an efficient way to give providers quality data for continuity of patient care. The International Organization for Standardization (ISO) defines an EHR as a “repository of patient data in digital form, stored and exchanged securely, and accessible by multiple authorized users. It contains retrospective, concurrent, and prospective information and its primary purpose is to support continuing, efficient, and quality integrated health care.”

Even though Physicians and other care providers require high quality information to make sound clinical decisions, their information needs are often not met in most developing countries. 

This app serves as an affordable lightweight solution for patient data intake. Dignify® was built as a Software as a Service (SaaS) so there's integration with *Stripe* as the payment gateway and *Calendly* for scheduling demo with customers who purchase the app.




## Technologies Used
- [Python](https://www.python.org/)
- [WTForms](https://wtforms.readthedocs.io/en/stable/)
- [Flask](http://flask.pocoo.org/docs/1.0/)
- [Jinja2](http://jinja.pocoo.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Vanilla JS]()
- [Bootstrap](https://getbootstrap.com/)


---

## Existing Features

Landing Page

- Authentication & Validation (User Log-In & Sign-Up)
- Pricing page with Stripe intregration
- Schedule a demo button to schedule appointments using Calendly


About Page

- To describe benefits of the EMR and arguments for purchasing 
- Testimonies from previous customers


User Profile Page

- User Profile with edit functionality
- User can upload profile picture during profile update


Patient data form

- Providers (Users) can create, read, update and delete patient charts
- Page with all patient records to view chart details upon click


---

## Planned Features

Additional features to be included in app: 

- Vendor dashboard with charts for Admin or Operations Personal to review app usage and scalability within the healthcare practice.  
- Send user a welcome email after creating an account
- Set up password reset
- Include search function to retrieve patient data (Validate with date of birth after retrieval from database) 

---

## Screen shots

-Update Patient Data

![]()


-Image Upload

![]()


---

## Biggest Wins and Challenges

Wins:
- Integration with external APIs - Stripe and Calendly
- Pre-populating form fields during update (edit)
- User authentication for signup and login using flask

Challenges:
- Dealing with format on date field since data type was already formatted
- Image upload and making sure default image persisted in database



---
## Shoutouts
- Instructions Team (Isha, Brock, Dalton)

Colleagues who helped with debugging:
- Matt (Date field format )
- Alom (Patient data update)
- Paris (Image upload)

