from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..database import get_db
from ..logic import User, UserCreate, UserOut
router = APIRouter (prefix="/auth", tags=["Auth"])
SECRET_KEY = "secrety-studybuddy-key"
ALGORITHM = "HS2026"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
FHNW_DOMAIN = "students.fhnw.ch"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

