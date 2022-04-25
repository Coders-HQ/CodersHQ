<p align="center">
 <img width="500" src="https://cdn-az.allevents.in/events5/banners/2ef3aa159dfbd7f5fe3707f4d7ef64ae30b70e298136f8ce3123990f0bd18720-rimg-w1000-h349-gmir.png?v=1644048442">

<h1 align="center">Coders Headquarters</h1>

</p><p align="center"><a href="https://github.com/pydanny/cookiecutter-django/">
<img width="200" src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter">
</a><a href="https://github.com/ambv/black">
<img width="100" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a><a href="https://opensource.org/licenses/MIT">
<img width="80" src="https://img.shields.io/badge/License-MIT-red.svg"></a><a href="https://discord.gg/CPQHAZrg8b0">
<img width="80" src="https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white"> 
</a>
</p>


 ## :wave: Introduction
 
  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-9-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Coders Headquarters (CodersHQ) is a social platform for developers to grow, network, challenge themselves, and gain points by contributing and helping others in this community. This platform was built by the community and for the community. The essence of CodersHq is to inspire everyone to learn to code, share knowledge and learn together.

Currently the platform is at the alpha stage with a lot of the
foundations being set. It is built using django and deployed using
docker.

## 📄 The Docs


Have a look at the [docs](https://coders-hq.github.io/CodersHQ), we document everything over there.
We plan to migrate from the docs to something more established, like readthedocs, once we have enough material
to work with.

We also document the tasks in [notion](https://suwaidi.notion.site/Coders-HQ-ae1356125bdc4b36b2b5b1973d09d609) and you can have a look at the [issues](https://github.com/Coders-HQ/CodersHQ/issues) section to find out what we are working on.


## ⚙️ Quick Setup


Make sure you have Docker version 2+ and then do the following to build the stack and update the databse :

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Follow the rest of the README for more information and use ``/admin`` to edit and create challenges.


## 🧑‍💻 Getting Up and Running Locally With Docker



The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your generated project.


#### Note

If you're new to Docker, please be aware that some resources are cached system-wide
and might reappear if you generate a project multiple times with the same name.


## Prerequisites


* Docker; if you don't have it yet, follow the [installation instructions](https://docs.docker.com/install/#supported-platforms);
* Docker Compose; refer to the official documentation for the [installation guide](https://docs.docker.com/compose/install/).
* (Windows) This repository can run on windows and was tested on [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10). Once you have WSL2, and a linux kernel, installed and running you need to install docker and you should be good to go. (Tested on Docker version 20.10.7, build f0df350 and Windows OS Build: 19042.1052)



## 🏗️ Build the Stack


This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build

Generally, if you want to emulate production environment use ``production.yml`` instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!


## Run the Stack


This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

You can also set the environment variable ``COMPOSE_FILE`` pointing to ``local.yml`` like this::

    $ export COMPOSE_FILE=local.yml

And then run::

    $ docker-compose up

To run in a detached (background) mode, just::

    $ docker-compose up -d


## Execute Management Commands


As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f local.yml run --rm`` command: ::

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Here, ``django`` is the target service we are executing the commands against.


## (Optionally) Designate your Docker Development Server IP


When ``DEBUG`` is set to ``True``, the host is validated against ``['localhost', '127.0.0.1', '[::1]']``. This is adequate when running a ``virtualenv``. For Docker, in the ``config.settings.local``, add your host development server IP to ``INTERNAL_IPS`` or ``ALLOWED_HOSTS`` if the variable exists.



## Basic Commands


### Setting Up Your Users


* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command:
``` python
    $ python manage.py createsuperuser
```
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks


Running type checks with mypy:

``` python
    $ mypy codershq
```

### Test coverage


To run the tests, check your test coverage, and generate an HTML coverage report:
``` html
    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html
```

Running tests with py.test

``` python
    $ pytest
```

### Celery


This app comes with Celery.

To run a celery worker:

``` shell
    cd codershq
    celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.


### Email Server


In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation` for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

## Stargazers ⭐

### Thanks to all of our   `Stargazers` ⭐ 🔭 who are supporting CodersHQ project

[![Stargazers repo roster for @Coders-HQ/CodersHQ](https://reporoster.com/stars/Coders-HQ/CodersHQ)](https://github.com/Coders-HQ/CodersHQ/stargazers)

# Contributors ✨

We would like to thank and appreciate our extraordinary contributors :clap:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/ralsuwaidi"><img src="https://avatars.githubusercontent.com/u/22400032?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rashed Suwaidi</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=ralsuwaidi" title="Code">💻</a> <a href="#design-ralsuwaidi" title="Design">🎨</a> <a href="#projectManagement-ralsuwaidi" title="Project Management">📆</a> <a href="#infra-ralsuwaidi" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-ralsuwaidi" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://abdulrahmanalblooshi.com"><img src="https://avatars.githubusercontent.com/u/34681035?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdulrahman Alblooshi</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=gitanimous" title="Code">💻</a> <a href="#design-gitanimous" title="Design">🎨</a></td>
    <td align="center"><a href="https://abdulkarim-suleiman.github.io/data-ninja.github.io"><img src="https://avatars.githubusercontent.com/u/77554371?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Abdulkarim Suleiman</b></sub></a><br /><a href="#content-Abdulkarim-Suleiman" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/Musab0"><img src="https://avatars.githubusercontent.com/u/6482739?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Musab</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=Musab0" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/arsxl"><img src="https://avatars.githubusercontent.com/u/69077626?v=4?s=100" width="100px;" alt=""/><br /><sub><b>arsxl</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=arsxl" title="Code">💻</a> <a href="#plugin-arsxl" title="Plugin/utility libraries">🔌</a></td>
    <td align="center"><a href="https://github.com/DerpySmurf"><img src="https://avatars.githubusercontent.com/u/59332297?v=4?s=100" width="100px;" alt=""/><br /><sub><b>DerpySmurf</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=DerpySmurf" title="Code">💻</a> <a href="#design-DerpySmurf" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/haralali"><img src="https://avatars.githubusercontent.com/u/74138203?v=4?s=100" width="100px;" alt=""/><br /><sub><b>haralali</b></sub></a><br /><a href="#projectManagement-haralali" title="Project Management">📆</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/kajaldoshi"><img src="https://avatars.githubusercontent.com/u/14121077?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kajal Doshi</b></sub></a><br /><a href="https://github.com/Coders-HQ/CodersHQ/commits?author=kajaldoshi" title="Code">💻</a> <a href="#infra-kajaldoshi" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    <td align="center"><a href="https://github.com/khushboo-gehi"><img src="https://avatars.githubusercontent.com/u/69520097?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Khushboo Gehi</b></sub></a><br /><a href="#projectManagement-khushboo-gehi" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
