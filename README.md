# Welcome to linkversity

Learn from links. [#7 featured product](https://www.producthunt.com/products/contriblearn#contriblearn) on ProductHunt. free & opensource!

## QuickStart


1.

```
python -m pip install -r requirements.txt
```

2.

Create .env with the following (or add the following environment variables) or add those to instance/config.py

```.env
SQLALCHEMY_DATABASE_URI = "sqlite:///linkversity.db"

SALT = "some-salt"

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY= ''
SECRET_KEY = 'secret-secret'
```

Optional

```
APP_NAME = ''
ACTIVE_FRONT_THEME = ''
ACTIVE_BACK_THEME = ''
```

If using gunicorn locally, use this

```py
import os
from dotenv import load_dotenv

for env_file in ('.env', '.flaskenv'):
    env = os.path.join(os.getcwd(), env_file)
    if os.path.exists(env):
        load_dotenv(env)
```

3.

Add config.json file in root dir with content

```json
{
    "admin_user": {
      "username": "appinv",
      "email": "admin@domain.com",
      "password": "pass"
    },
    "settings": {
      "APP_NAME": "Demo",
      "ACTIVE_FRONT_THEME": "blogus",
      "ACTIVE_BACK_THEME": "boogle",
      "CURRENCY": "MUR"
    }
}
```

4.

Run

```
shopyo initialise
flask run --debug
```
