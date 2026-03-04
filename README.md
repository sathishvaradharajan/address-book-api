# Address Book API

A minimal FastAPI application that allows users to create, update,
delete, and search addresses based on geographic distance.

The API stores addresses in a SQLite database and allows searching for
addresses within a specified radius using latitude and longitude.

------------------------------------------------------------------------

## Features

-   Create address
-   Update address
-   Delete address
-   Retrieve addresses within a given distance
-   SQLite database storage
-   Input validation using Pydantic
-   Distance calculation using geopy
-   Logging for API operations
-   Automated tests using pytest
-   Interactive API documentation via Swagger

------------------------------------------------------------------------

## Requirements

Python 3.10+

------------------------------------------------------------------------

## Setup Instructions

Clone the repository

git clone `<your-repository-url>`{=html}

Navigate into the project

cd address-book-api

Create virtual environment

python -m venv venv

Activate virtual environment

Windows (PowerShell)

venv`\Scripts`{=tex}`\Activate`{=tex}.ps1

Mac/Linux

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Running the Application

Start the FastAPI server

uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Running Tests

Run automated tests using pytest

python -m pytest -v

------------------------------------------------------------------------

## Example API Usage

### Create Address

POST /addresses

Example request body

{ "name": "Home", "street": "MG Road", "city": "Bangalore", "latitude":
12.9716, "longitude": 77.5946 }

------------------------------------------------------------------------

### Update Address

PUT /addresses/{address_id}

------------------------------------------------------------------------

### Delete Address

DELETE /addresses/{address_id}

------------------------------------------------------------------------

### Search Nearby Addresses

GET /addresses/nearby?lat=12.9716&lon=77.5946&distance_km=5

Returns addresses within a 5 km radius.

------------------------------------------------------------------------

## Logging

The application uses Python's built-in logging module to log important
events such as:

-   Address creation
-   Address updates
-   Address deletions
-   Nearby search requests
