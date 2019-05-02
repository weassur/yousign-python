[![Build Status](https://travis-ci.org/weassur/yousign-python.svg?branch=master)](https://travis-ci.org/weassur/yousign-python)
[![codecov](https://codecov.io/gh/weassur/yousign-python/branch/master/graph/badge.svg)](https://codecov.io/gh/weassur/yousign-python)

# yousign

Python client for the YouSign REST api

# Usage

You'll need to get an `api_key` from YouSign to authenticate.

```
from yousign.yousign import YouSign

api_key = os.environ.get('YOUSIGN_API_KEY')
## choose to use the production or the development endpoints
production = True

yousign_client = YouSign(api_key=api_key, production=production)
yousign_client.authenticate()

print(yousign_client.users())

```

# Tests

intall requirements.txt

`pip install -r requirements.txt`

run tests

`py.tests`

watch for changes

`ptw -- --testmon`
