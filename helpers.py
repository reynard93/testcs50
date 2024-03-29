from functools import wraps
from flask import redirect, session

def login_required(f):
  # this is to decorate routes to need login
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("username") is None:
      return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function