SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

ADMIN_USERNAME="admin"
ADMIN_PASSWORD="1234"
SECRET_KEY = ["dvgfatnbfghgtdtd44fghvwk23232v2154ntdhrhb"]


PAYMENT_MERCHANT = 'sandbox'
PAYMENT_CALLBACK = 'http://localhost:5000/verify'
PAYMENT_FIRST_URL = 'https://sandbox.shepa.com/api/v1/token'
PAYMENT_VERIFY_URL = 'https://sandbox.shepa.com/api/v1/verify'
