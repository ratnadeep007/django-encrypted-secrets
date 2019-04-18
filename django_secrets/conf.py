import os

SECRETS_ROOT = os.environ.get('DJANGO_SECRETS_ROOT',  os.getcwd())

ENCRYPTED_SECRETS_KEY_PATH = f'{SECRETS_ROOT}/master.key'

key_file_exists = os.path.isfile(ENCRYPTED_SECRETS_KEY_PATH)

if key_file_exists:
    ENCRYPTED_SECRETS_KEY = open(f'{SECRETS_ROOT}/master.key').read()
else:
    ENCRYPTED_SECRETS_KEY = None

# Allow an override with env variable:
ENCRYPTED_SECRETS_KEY = os.environ.get('DJANGO_MASTER_KEY', ENCRYPTED_SECRETS_KEY)

ENCRYPTED_SECRETS_PATH = f'{SECRETS_ROOT}/secrets.yml.enc'
