import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# Cryptographic key for generating tokens or signatures
# Protection against Cross-Site Request Forgery (CSRF)
