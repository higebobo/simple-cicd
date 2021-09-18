# Simple CI/CD

Simple CI/CD sample with GNU Make and Python.

## Usage

```shell
python -m app
```

test

```shell
pytest -v
```

## Deployment


Edit .env.fabric

```shell
cp .env.fabric.sample .env.fabric
vi .env.fabric
...
```

See the deployment task in [Makefile](./Makefile)


## Note

When trying this sample at your own risk.
