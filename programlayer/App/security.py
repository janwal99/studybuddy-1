from passlib.context import CryptContext

# Setup the CryptContext to use the bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Takes a plain text password and returns a secure hash.
    Use this when a new user registers.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares a plain text password against the hashed version in the database.
    """
    return pwd_context.verify(plain_password, hashed_password)