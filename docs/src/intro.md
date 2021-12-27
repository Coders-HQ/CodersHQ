Introduction Coders Headquarters
===================

Coders Headquarters (CodersHQ) is a social platform for developers to
network, do challenges and gain points by contributing and helping
others.

Currently the platform is at the alpha stage with a lot of the
foundations being set. It is built using django and deployed using
docker.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


The Wiki
--------

Have a look at the [wiki](https://github.com/Coders-HQ/CodersHQ/wiki),
we document everything over there. We plan to migrate from the wiki to
something more established, like readthedocs, once we have enough
material to work with.

We also document the tasks in the
[project](https://github.com/Coders-HQ/CodersHQ/projects) section and
have a look at the
[issues](https://github.com/Coders-HQ/CodersHQ/issues) section to find
out what we are working on.

Quick Setup
-----------

add the missing environment variables values in
\'.envs/.local/.django\', such as the following values:

    GITHUB_TOKEN=
    GITHUB_CLIENT_ID=
    GITHUB_CLIENT_SECRET=
    SLACK_TOKEN=

These can be obtained from github\'s settings section and slack\'s api
section if you create a bot.

To build the stack and update the databse run :

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Follow the rest of the README for more information and use `/admin` to
edit and create challenges.

Getting Up and Running Locally With Docker
==========================================

The steps below will get you up and running with a local development
environment. All of these commands assume you are in the root of your
generated project.

Note

If you\'re new to Docker, please be aware that some resources are cached
system-wide and might reappear if you generate a project multiple times
with the same name.
:::

Prerequisites
-------------

-   Docker; if you don\'t have it yet, follow the [installation
    instructions](https://docs.docker.com/install/#supported-platforms);
-   Docker Compose; refer to the official documentation for the
    [installation guide](https://docs.docker.com/compose/install/).
-   (Windows) This repository can run on windows and was tested on
    [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
    Once you have WSL2, and a linux kernel, installed and running you
    need to install docker and you should be good to go. (Tested on
    Docker version 20.10.7, build f0df350 and Windows OS Build:
    19042.1052)

Build the Stack
---------------

This can take a while, especially the first time you run this particular
command on your development system:

    $ docker-compose -f local.yml build

Generally, if you want to emulate production environment use
`production.yml` instead. And this is true for any other actions you
might need to perform: whenever a switch is required, just do it!

Run the Stack
-------------

This brings up both Django and PostgreSQL. The first time it is run it
might take a while to get started, but subsequent runs will occur
quickly.

Open a terminal at the project root and run the following for local
development:

    $ docker-compose -f local.yml up

You can also set the environment variable `COMPOSE_FILE` pointing to
`local.yml` like this:

    $ export COMPOSE_FILE=local.yml

And then run:

    $ docker-compose up

To run in a detached (background) mode, just:

    $ docker-compose up -d

Execute Management Commands
---------------------------

As with any shell command that we wish to run in our container, this is
done using the `docker-compose -f local.yml run --rm` command: :

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Here, `django` is the target service we are executing the commands
against.

(Optionally) Designate your Docker Development Server IP
--------------------------------------------------------

When `DEBUG` is set to `True`, the host is validated against
`['localhost', '127.0.0.1', '[::1]']`. This is adequate when running a
`virtualenv`. For Docker, in the `config.settings.local`, add your host
development server IP to `INTERNAL_IPS` or `ALLOWED_HOSTS` if the
variable exists.

Basic Commands
--------------

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out
    the form. Once you submit it, you\'ll see a \"Verify Your E-mail
    Address\" page. Go to your console to see a simulated email
    verification message. Copy the link into your browser. Now the
    user\'s email should be verified and ready to go.

-   To create an **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and
your superuser logged in on Firefox (or similar), so that you can see
how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy codershq

### Test coverage

To run the tests, check your test coverage, and generate an HTML
coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    $ pytest

### Celery

This app comes with Celery.

To run a celery worker:

``` {.bash}
cd codershq
celery -A config.celery_app worker -l info
```

Please note: For Celery\'s import magic to work, it is important *where*
the celery commands are run. If you are in the same folder with
*manage.py*, you should be right.

### Email Server

In development, it is often nice to be able to see emails that are being
sent from your application. For that reason local SMTP server
[MailHog](https://github.com/mailhog/MailHog) with a web interface is
available as docker container.

Container mailhog will start automatically when you will run all docker
containers. Please check [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)
for more details how to start all containers.

With MailHog running, to view messages that are sent by your
application, open your browser and go to `http://127.0.0.1:8025`

Deployment
----------

The following details how to deploy this application.

### Heroku

See detailed [cookiecutter-django Heroku
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html).

### Docker

See detailed [cookiecutter-django Docker
documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with
variables of your choice. Bootstrap v4 is installed using npm and
customised by tweaking your variables in
`static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap
source](https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss),
or get explanations on them in the [Bootstrap
docs](https://getbootstrap.com/docs/4.1/getting-started/theming/).

Bootstrap\'s javascript as well as its dependencies is concatenated into
a single file: `static/js/vendors.js`.

Slack
-----

This project has an associated slack page that is used when a new
challenge is created and discussions which relates to challenges in
general. The slack page is located at
\[codershq-challenge.slack.com\](<https://codershq-challenge.slack.com>).
