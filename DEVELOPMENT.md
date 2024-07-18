# Dev mode
If you want to run api-server client with own mock server set for local env

```sh
export WEBSHOTAPI_ENDPOINT=http://localhost:3000
```
Then client will connect with localhost:3000. With this host you can mock original server.


# Internal test api key for dev environment
```sh
export WEBSHOTAPI_TEST_API_KEY=7815696ecbf1c96e6894b779456d330e7815696ecbf1c96e6894b779456d330d
```

# Prepare tests
```sh
source venv/bin/activate
python -m pip install -r ./requirements.txt
python -m pip install pytest
```

# Test
```sh
source venv/bin/activate
venv/bin/pytest ./tests
```

# Build Docs
```sh
python -m pip install sphinx
sphinx-apidoc -o docs-source webshotapi/
sphinx-build -b html docs-source ./docs
```

# Release
```sh
bin/release.sh
```