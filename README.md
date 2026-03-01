Altius QA Automation Assignment

This project contains automated REST API tests implemented in Python using pytest and requests.

Scope

The tests cover:

Login API

Verify successful login

Verify error handling for invalid credentials

Deals List API

Call POST /api/v0.0.2/deals-list

Verify the response is successful

Verify exactly one deal is returned

Verify the deal title matches the expected value

Authentication is handled via the Authorization2 cookie returned by the login API and reused using a shared requests.Session().

Setup

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file (see .env.example) with the following variables:

BASE_URL=https://fo1.api.altius.finance

EMAIL=your_email_here

PASSWORD=your_password_here
DEALS_VIEW=task-manage
EXPECTED_DEAL_TITLE=Shared deal for home assignment

Run Tests

pytest -v

Notes

The login flow uses POST /api/v0.0.2/login.
Authentication is session-based and relies on the Authorization2 cookie.
Configuration is handled via environment variables for flexibility.