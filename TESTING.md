# Testing for The Wee Norn Irish Box

## Contents

- [Code Validation](#code-validation)
- [User Stories](#user-stories)
- [Branches](#branches)
- [Responsiveness](#responsiveness)
- [Performance](#performance)
- [Manual Testing](#manual-testing)
- [Known Bugs](#known-bugs)
- [Other Issues](#other-issues)

---

## Code Validation

The [W3C Markup Validator](https://validator.w3.org/) and the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) were used to validate the HTML and CSS files in the project and check there were no syntax errors. The following shows the results for each page:

[W3C Markup Validator](https://validator.w3.org/):

Products page displayed a bad value error for spaces in the subject line of mailto

- This was fixed by replacing all the spaces in the subject line with %20

After fixing the error on the products page, I ran all the pages through the validator again to check there were no other errors or warnings to show:

![Markup Validator Results](docs/images/html-validator.png)

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/):

There were no errors displayed after running all css files through the validator but there were warnings for the use of colour variables which can be ignored:

![CSS Validator Results](docs/images/css-validator.png)

[JS Hint](https://jshint.com/) was used to check that the JavaScript code in the project complies with coding rules and to check for any syntax errors:

Found one undefined variable in initialise_toasts.js:
![JS Hint Results](docs/images/toasts-js.png)

Found no errors in star_ratings.js:
![JS Hint Results](docs/images/stars-js.png)

Found one undefined variable in stripe_elements.js:
![JS Hint Results](docs/images/stripe-js.png)

[PEP8 Online](http://pep8online.com/) was used to check that the Python code meets PEP8 requirements:

![PEP8 Online Results](docs/images/pep8.png)

[Contents](#contents)

---

## User Stories

### First Time Visitor

As a **First Time Visitor**, I want to understand the main purpose of the site on my first visit:

- I've included a short description in the heading section below the navigation bar of the site as well as a section to explain how the site works

_Descriptions on Home Page_
![Site Description Screenshot](docs/images/home-page-description.png)

As a **First Time Visitor**, I want to be able to easily navigate the site:

- I've included a navigation bar at the top of all pages to provide links to other pages in the site
- I've also included various buttons throughout the site that also link to other pages
- I've added external links to social media pages in the footer that will open in a new tab/window

_Navigation Bar_
![Navigation Bar Screenshot](docs/images/navigation-bar.png)

As a **First Time Visitor**, I want to be able to easily view/use the site on my smartphone:

- I've used [Bootstrap 5](https://getbootstrap.com/) to make the site responsive across multiple devices including mobile and tablets
- The site has been tested across multiple devices to ensure it is [responsive](#responsiveness)

As a **First Time Visitor**, I want to be able to see what products are available to add to a snack box:

- I've included a link to the products page in the navigation bar that allows first time visitors see what products are available to add to a box before they register for an account to make a purchase

_Products Page_
![Products Screenshot](docs/images/products-page.png)

As a **First Time Visitor**, I want to know the snack box price:

- I've included the price of the box on the home page in the heading section as well as in the section that explains how the site works

As a **First Time Visitor**, I want to be able to read blog posts:

- I've included a link to the blog page in the navigation bar that allows first time visitors to read posts
- Without an account, they won't have permission to add any posts or comment on any posts

_Blog Post_
![Blog Page Screenshot](docs/images/blog-post.png)
_Comments Section_
![Blog Page Screenshot](docs/images/blog-comments.png)

As a **First Time Visitor**, I want to be able to easily register for an account:

- I've included a link to the sign up page in the navigation bar that allows first time visitors to create an account
- After signing up for an account, the user will receive a verification email which will allow them finish signing up for their account when they follow the link in the email

_Sign Up Form_
![Sign Up Form Screenshot](docs/images/signup.png)
_Verify Email_
![Verify Email Screenshot](docs/images/verify-email.png)

As a **First Time Visitor**, I want to read reviews from other users:

- I've included a reviews section on the home page so they can read about other peoples experience using the service

_Reviews_
![Reviews Screenshot](docs/images/reviews.png)

As a **First Time Visitor**, I want to be able to follow the company on social media platforms:

- I've included links to social media platforms in the footer of the site
- These links will open in a new tab/window when opened

_Footer_
![Footer Screenshot](docs/images/footer.png)

As a **First Time Visitor**, I want to be able to contact the company with any queries I might have:

- I've included an email link in the products page to allow users to contact the site owner to request any products they'd like to see available in the future

_Email Link_
![Email Link Screenshot](docs/images/email-link.png)

### Registered User

As a **Registered User**, I want to be able to easily login and logout of my account:

- I've included a link to the login page in the navigation bar and a link for logged in users to logout of their account

As a **Registered User**, I want to be able to easily add and remove items from my box:

As a **Registered User**, I want to be able to easily purchase my box:

As a **Registered User**, I want to receive an email confirming my purchase:

As a **Registered User**, I want to be able to easily update my delivery details in my profile:

As a **Registered User**, I want to be able to view my order history:

As a **Registered User**, I want to be able to easily submit blog posts:

As a **Registered User**, I want to be able to easily edit or delete any blog posts I've submitted:

As a **Registered User**, I want to be able to comment on other blog posts:

As a **Registered User**, I want to be able to leave a review on the site to let others know about my experience:

[Contents](#contents)

---

## Branches

Throughout the development process, different branches have been created to test different features and layouts which have now been merged with the master branch.

Reviews Branch:

- This branch was created to create the reviews app in the project and was also used to test the views in the home app to ensure that the reviews displayed properly on the home page

Stripe Branch:

- This branch was originally created to test stripe subscriptions
- After creating subscription models, views and adding stripe elements, I was unable to successfully setup stripe subscriptions so opted for a stripe one-time payment option instead

View Box Branch:

- This branch was created to test viewing the box items in the box app and also in the success toast when a user has successfully added an item to their box

[Contents](#contents)

---

## Responsiveness

As well as running each page through a validator and testing user stories to see if they were met, I also tested the responsiveness of the site across a number of different devices and browsers:

- Chrome DevTools was used during the development process to test the responsiveness of the site on different devices before pushing any changes to GitHub
- After pushing changes to GitHub, the site was also tested in Firefox and Safari
- The site was also tested across a number of personal devices including an iPad, iPhone 11 and MacBook Pro
- A desktop app called [Responsively](https://responsively.app/) was also used to check the responsiveness of the site on some additional android devices that I didn't have access to on Chrome DevTools

[Contents](#contents)

---

## Performance

As well as testing the responsiveness of the site, I also tested the performance of each page using [Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome DevTools.

[Contents](#contents)

---

## Manual Testing

Each page has been tested individually to check that:

- Images load properly
- Navigation buttons link to the correct pages in the site
- External links located in the footer open in a new tab/window and link to the correct site
- First time visitors only have access to the:
  - home page where they can only read reviews
  - sign up page
  - login page
  - blog page but are unable to add any posts or comments
  - products page but are unable to purchase/add products to a box
- Registered users have access to the:
  - home page where they can add a review
  - login page to login to their account
  - profile page to view their order history, blog drafts and to update their default delivery address
  - products page to add products to their box
  - box page to view products they have added to their box
  - checkout page to purchase their box followed by the checkout success page when they've completed a purchase
  - blog page to read, add and comment on posts as well as edit or delete any posts they've published
  - logout page to logout of their account
- The Site Owner/Superuser has access to the:
  - django admin panel
  - manage reviews page to manage reviews posted by users
  - products page to add, edit and delete products
  - blog page to edit and delete blog posts by all users

[Contents](#contents)

---

## Known Bugs

Reviews App:

- Currently, registered users are able to post more than one review

[Contents](#contents)

---

## Other Issues

Stripe Subscription:

- The original idea for this project was to create a subscription service that would allow subscribers to receive their snack box each month
- While trying to implement a stripe subscription plan, I was unable to generate any successful payments
- Due to work commitments/project submission deadline impending, I opted for my back-up plan of a one time payment option, keeping the same price of £10 per box that contains 6 items chosen by the user

[Contents](#contents)

---
