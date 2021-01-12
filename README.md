# The Reading
Welcome to the MoMo README file.

This is a school project with the main focus to display my skills in HTML, CSS, JavaScript,
Python, Flask, MongoDB and Materialize. This website's goal is for users to create, read,
update and delete book reviews. Also for the owner/owners to include affiliated sales links
to monetize the webpage and make a profit through the webpages popularity and usage. 


## UX/UI


### User Stories (UX)

As a user type, I want:

-   to be able to create, read, update and delete book reviews.

-	the webpage to be intuitive, to make usage easier and more appealing.

-   to see clear separations between my own book reviews and others.

-	to be able to purchase the book either directly via the webpage or through affiliated links.


### Owner Stories (UX)

As an owner type, I want:

-   to create a webpage that will allow users and owners to create, read, update and delete book reviews.

-   the webpage to be intuitive and appealing, which in turn will make the user want to use it
    on several accounts.

-   to be able to monetize the webpage by providing users with either selling the book directly
    on the webpage or by adding affiliated links.


### Wireframes (UI)
![Image of Home Page and Footer](assets/wireframes/home-page-and-footer.png)

![Image of Sort Function](assets/wireframes/sort-function.png)

![Image of Sort and Filter chosen](assets/wireframes/sort-and-filter-chosen.png)

![Image of Log In and Register](assets/wireframes/log-in-and-register.png)

![Image of Profile](assets/wireframes/profile.png)

![Image of Manage Categories and New Review](assets/wireframes/manage-catagories-and-new-review.png)

![Image of Add Category and Edit Review](assets/wireframes/ass-category-and-edit-review.png)

![Image of Full Sized Review](assets/wireframes/full-size-review.png)

![Image of Drop down menu for mobile, User](assets/wireframes/drop-down-user.png)

![Image of Drop down menu for mobile, Admin](assets/wireframes/drop-down-menu-admin.png)

## Features
In this section the features of the different parts of this project
    will be described.

### Existing Features

- Feature 1 - base.html - base template that extends to all other html files.
    The base template contains three different sections. 
    - Header - navbar - The navbar contains the company logo image, home button,
        Log in button and register button.
    - Main section, when there is no user logged in there is a welcome message
        spanned across the top of the page, underneath the navbar. Underneath
        the welcome text there is a place for flash message that is unique per
        each html page.
    - Footer - the footer contains four social link icons (facebook, instagram,
        twitter and linkedin), the company logo image, links to information.html
        (about us, terms, privacy and FAQ), copyright text and company email
        (thereading@readerz.null).
- Feature 2 - login.html - lets the user enter their username, password and press
    a button that logs in the user into the webpage. Beneath the log in card-panel
    there is a link called 'Register here!' that redirects the user to the
    registration page. 
- Feature 3 - register.html - lets the user enter a username, password and press
    a button that registers and logs in the user into the webpage. Beneath the
    log in card-panel there is a link called 'Log In here!' that redirects
    the user to the log in page.
- Feature 4 - reviews.html - 'Home' - this page lets the user see all the reviews
    that the webpage contains. The reviews are displayed underneath each other.
- Feature 5 - review card-panel - the review card panel contains:
    - book image (currently the same image for all reviews)
    - review headings (book title, author name, genre category, language,
        page length, date of publishing, grade, created by whom)
    - review description, that lets the users read a truncated version of the
        review description of the book.
    - teal button stating 'Full review' wich lets the user access the full review 
        where the description text is not truncated.
- Feature 6 - search and filter bar
    - search
    - filter 
    - search button - one blue button with label 'Search'. When pressed it activates
        a function that makes a search to the database taking the text field and 
        sort by filter as parameters and returns a corresponding value. 
    - reset button - returns the user to the home page (reviews.html).
- Feature 7 - base.html - navbar - when logged in as a generic user the navbar
    contains four nav items (home, profile, new review and log out).
- Feature 8 - base.html - navbar - when logged in as a admin the navbar contains 
    five navbar items (home, profile, new review, manage categories and log out).
- Feature 9 -
- Feature 10 -
- Feature 11 -
- Feature 12 -
- Feature 13 -
- Feature 14 -
- Feature 15 -
- Feature 16 -
- Feature 17 -
- Feature 18 -
- Feature 19 -
- Feature 20 -




    Feature 1 - allows users X to achieve Y, by having them fill out Z
    ...





### Features Left to Implement

- Future implementetion that would increase monetization would be to add adds to the webpage. That is not
the current focus with this project and therefore not Implemented.


## Technologies Used


### Languages


### Framework


### Library


### Other Technologies


## Testing


### Manual Testing


### Webpage images


### W3C vaildator


### w3 validator


### jshint


### Automated Testing


### Bugs fixed


### Known issues


## Deployment



## Credits


### Content

Book reviews:

- Review description summary for the book Frankenstein:
[www.wikipedia.org/frankenstein](https://en.wikipedia.org/wiki/Frankenstein)

- Review description summary for the book Dr. Jekyll and Mr. Hyde:
[www.bbc.co.uk](https://www.bbc.co.uk/bitesize/guides/z88wjxs/revision/1)

- Review description summary for the book Dracula:
[www.wikipedia.org/dracula](https://en.wikipedia.org/wiki/Dracula)

- Review description summary for the book Alice in Wonderland:
[en.wikipedia.org](https://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland)

Code:

- Code for date in python was retrived from w3schools.com
[www.w3schools.com](https://www.w3schools.com/python/python_datetime.asp)

- Integer converter retrived from careerkarma.com
[careerkarma.com](https://careerkarma.com/blog/python-string-to-int/)

- Range for jinja was adapted from jinja.palletsprojects.com
[jinja.palletsprojects.com](https://jinja.palletsprojects.com/en/2.11.x/templates/)


### Media

- The logo for The Reading was created by me with the website
    [hatchful](https://hatchful.shopify.com/).

![alt](/static/images/the-reading-logo.png)


- The review image with the text "BOOK IMAGES" was made by me with paint.

![alt](/static/images/book-image.jpg)

- The background image of books is created by Annie Spratt and has been retrived
    from [unsplash.com](https://unsplash.com/photos/lIWF2uHxs0Q).

![alt](/static/images/books.jpg)


### Acknowledgements

This project received inspiration for this project from 3 following websites:

- [Readsy](https://reedsy.com/discovery/blog/book-review-examples)
- [Bookpage](https://bookpage.com/reviews?page=2)
- [Goodreads](https://www.goodreads.com/)

