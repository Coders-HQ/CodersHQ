# Platform

This document lists the more import features of Coders HQ. The list and details should be updated and match the live version of CHQ.

### User System
[//]: # (user)
There should be a way for users to join through the landing page. The creation of users should be done using the industry standard when dealing with password and user data. Users should be able to look into their own details within their own profile page.

### Chat Feature
[//]: # (chat)

The website should have a way for users to communicate with each other and this feature should be self contained, i.e, it should not be an API to another external server but should be part of the docker stack.
This feature can be a simple direct message chat function where all the data is saved in a local database. The user should be able to view his/her history and communicate with other users.

### Scoring Feature
[//]: # (scoring)

There should be a basic scoring system where a user is scored continuously based on the following:
* Open source contribution, i.e. github score. This is currently in effect but should be improved
* Hackathon contribution (more details in the hackathon section)
* Challenge engagement and completion (more details in the challenge section)
* General activity with other users (social score)

### Challenges
[//]: # (challenges)

Challenges are defined as a method for users to join an event where a specific problem is set by an entity with a time limit. Then users can attempt to solve the problem and upload their work for the admins/companies to select the winners.

Challenges can also be broken down into smaller parts, called sprints, each of which comes with its own time limit.

Challenges should have the following features:
- Optional multiple sprints each sprint can be more specific
- Can join with a team or as a single user
- Companies should have a lot of freedom when creating challenges
- companies should be able to do the following:
	- add logo
	- choose number of sprints
	- allocate prize
	- give/ recommend cloud provider computational power
- If a cloud provider is chosen then time must be allocated for the users to get used 

### Hackathons
[//]: # (hackathons)

Hackathons are similar to challenges, however, they will have a much smaller time-frame. 

### Blogging Feature
[//]: # (blogging)

There should be a page where admins can create entries to a blog and have users like it and save it.

### Companies System
[//]: # (companies)

Companies can be created by users and each company should have a specific set of privileges that users don't. These are:
* To create/edit their own hackathons
* To create/edit their own challenges
* To view hackathon/challenge contributions and select desired winners

### Landing Page
[//]: # (landing_page)

The landing page should be a single page with basic information on the website and a login/signup redirect. The design of the landing page should be similar to the current draft landing page

### Dashboard
[//]: # (dashboard)

The website should be built similar to a dashboard where the users have the ability to navigate to any section on the website and view new messages as a notification. The design should be intuitive and based on modern aesthetics

#### What is in the dashboard

These are the items that need to be part of the dashboard

* score
* basic info (maybe a card)
* number of live hackathons
* number of completed challenges
* news
* Upcoming events
* Interactions with user’s blog posts/comments 

### Email System

The email should be integrated with django and an email should be sent when a user joins (this currently works using mailhog as a test bed). Admins should also have an easy way to send emails to multiple users or a single user.
