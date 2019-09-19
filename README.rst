=======================
Intercom Take Home Test
=======================

This repository contains the code for the Intercom Take Home Test in which we invite guests within 100km of the Dublin offices to an event.

Have chosen Python 3.6 since it is a quick language to write, is well-supported, is well understood by most devs, and performance isn't critical. Something like this could be run in AWS Lambda which works well with Python.

Output is written to ./res/output.txt.


Assumptions
===========

Since this is meant to be run in production, the environment will be well known. If it was meant to be distributed amongst Intercom staff then we would have to modify for different versions of Python and OS's.

Assumptions:

- will be run in Ubuntu 18.04.
- 64 bit machine, accuracy should be enough to avoid using the numeric version to calculate great circle distance.
- Earth's diameter is 6371km.
- Assumed there will be a user model.
- Have hardcoded the Dublin office coordinates and distance threshold in a const file, could have also accepted them as program arguments.
- Throwing a custom IntercomExecption on any error cases
- Have used decimal.Decimal for better floating point accuracy.


Directory Structure
===================

| intercom_test/ - parent directory
| ├── config/ - where all your configuration goes
| │   ├── __init__.py
| │   └── config.py - variables that will change based on dev/prod env
| ├── models/ - where all your models go
| │   ├── __init__.py
| │   └── user.py - model for the Intercom user
| ├── res/ - contains resources
| │   ├── customers.txt - input file containing users
| │   └── output.txt - output of the program containing invited guests
| ├── src/ - contains feature related code
| │   ├── __init__.py
| │   ├── consts.py - variables that don't change run to run
| │   ├── food_and_drinks_events.py - code related to food and drinks events
| ├── tests/ - tests
| │   ├── __init__.py
| │   ├── test_maths_utils.py - tests for maths utility functions
| │   ├── test_food_and_drinks.py - tests for food and drinks events code
| │   └── test_file_utils.py - tests for file utility functions
| ├── utils/ - any utility functions
| │   ├── __init__.py
| │   ├── maths_utils.py - file for any maths related utility functions
| │   └── file_utils.py - file for any file related utility functions
| ├── .gitignore
| ├── main.py - main file for job server
| ├── requirements.txt - requirements for Python
| └── README.rst - this file


Pre-requisites
==============

- Ubuntu 18.04

- Python 3.6

To check you have this, enter the following into your command line:

.. code-block:: sh

   $ python3 --version

If you do not see something like `Python 3.6.8` then you will need to install it and return here afterwards.



Installation
============

In the parent directory (intercom_test), run:

.. code-block:: sh

   $ pip3 install -r requirements.txt


To Run
======
You can change whether messages are output to the console or not by modifying PRINT_MESSAGES in config/config.py. Once set, in the parent directory, run:

.. code-block:: sh

   $ python3 main.py


To Test
=======

In the parent directory, run:

.. code-block:: sh

   $ py.test


Improvements
============
 - Create pytest fixtures to create mock test files for file_utils testing.
 - Create a virtual environment for this.
 - Modify to run in Lambda and use boto to read from s3 bucket where customers are stored, then send emails to customers. Write results to different s3 bucket.
 - Open the lambda function to the rest of the Intercom application so it can be run by other scripts, teams, web servers, etc.


Author
======
Andrew Murtagh, amurtagh09@gmail.com, https://github.com/AndrewMurtagh


Licence
=======
Proprietary Intercom licence here.
