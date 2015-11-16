This is the www.emfcamp.org web site

[![Build Status](https://travis-ci.org/emfcamp/Website.svg?branch=master)](https://travis-ci.org/emfcamp/Website)

Requirements
=======

* [Python 2.7](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/latest/installing.html)
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/installation.html)
* [SQLite3](https://www.sqlite.org/download.html)


Starting
========
```
sudo apt-get install -y python-dev python-virtualenv libxml2-dev libxslt1-dev libffi-dev postgresql-server-dev-9.4 git
make init
make update # may take a few minutes if you don't have cached .whl files
make data
```

Alt method using 'easy\_install'
=======
To set up easy\_install go [here](https://pythonhosted.org/setuptools/easy_install.html#installing-easy-install "pythonhosted.org")
```
sudo easy_install virtualenv
make init
```

Using vagrant
=======

```
vagrant up
vagrant ssh
cd /vagrant
```
This is running all the necassary provisioning steps (see ```provision.sh```), only the final ```make``` and
```make admin``` is needed. Port 5000 is forwarded.

Running
=======
```
make update
make data
make
```

Now create a user (go to [http://localhost:5000/signup](http://localhost:5000/signup)) and then run:

```
make admin
```

This will make your user an administrator.

If you want to clean out the database and start again then:

```
rm var/test.db
make update
make data
```

Viewing
=======
The site will run by default on [http://localhost:5000](http://localhost:5000).

If you would like to change the port that the site uses you can set this in development.cfg by adding:

```python
    PORT=8888
```

You can also make the site accessible outside of your computer.
Only do this if you're sure you know what you're doing.

```python
    HOST='0.0.0.0'
    PORT=8888
```

You may also like to set `LOG_COLOR=True`, which makes it easier to distinguish SQLAlchemy log lines.

Payments for tickets
====================
We have (currently) three payment systems: bank transfer, Stripe and GoCardless.

#### Bank Transfer
These are manually resolved via scripts and the admin panel.

#### Stripe
This is the easiest method to "pay" for a ticket when you're developing. The details for a successful payment are:

- **email**: what ever you want
- **card number**: 4242 4242 4242 4242
- **expiry**: anything that's in the future
- **cvc**: anything

If you want to test specific modes please check [their documentation](https://stripe.com/docs/testing 'Stripe testing docs')

#### GoCardless
Unfortunately GoCardless don't offer a simple method of setting up a developer system. If you want to test this payment method you'll have to:

1. Make a copy of 'config/development.cfg' and name it 'config/live.cfg'
2. Set up your own merchant account (go to [https://gocardless.com/merchants/new](https://gocardless.com/merchants/new)).
3. Enable Sandbox mode (button at the top right)
4. Enable developer mode: 'More...' (top left) > Developer (this should take you straight to the [API Keys](https://dashboard-sandbox.gocardless.com/developer/api-keys)). 
5. Copy the following values from the API Keys to the appropriate environment variable in 'live.cfg':
    - 'App Identifier' -> `GOCARDLESS_APP_ID`
    - 'App secrets' -> `GOCARDLESS_APP_SECRET`
    - 'Merchant access token' -> `GOCARDLESS_ACCESS_TOKEN`
    - 'Merchant id' -> `GOCARDLESS_MERCHANT_ID`
6. From Developer go to [URI Settings](https://dashboard-sandbox.gocardless.com/developer/uri-settings) (left hand menu block)
7. Set the following:
    - **Redirect URI**: `http://localhost:5000/pay/gocardless/`
    - **Cancel URI**: `http://localhost:5000/pay/gocardless/`

In theory you should now be able to use GoCardless to checkout. You should see the payments under [payments](https://dashboard-sandbox.gocardless.com/payments) (top left)

Links to Documentation
======================

N.B. the version might be wrong for some of these, check against requirements.txt

## Flask

* [Flask](http://flask.pocoo.org/docs/)
* [Flask-Script](http://packages.python.org/Flask-Script/)

## Templates

* [Jinja2](http://jinja.pocoo.org/docs/)
* [Bootstrap](http://twitter.github.com/bootstrap/)

## Forms

* [Flask-WTF](http://packages.python.org/Flask-WTF/)
* [WTForms](http://wtforms.readthedocs.org/en/latest/)

## Database

* [Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy/)

