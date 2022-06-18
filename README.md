# packaging-with-mypy-b

This Python package is to remind me how to build and distributes packages that contain type stubs built with the `stubgen` tool from [`mypy`](https://github.com/python/mypy).

See <https://github.com/austinjp/packaging-with-mypy-a>.

<hr/>

## What to do?

Generate stubs for 3rd party packages.

```
python3.9 -m venv venv
source venv/bin/activate
stubgen -o ./stubs -p gunicorn # Note: -p for packages, -m for modules
```

Ensure the stubs are bundled with *this* package; see `setup.py`.

Add to source version control, and distribute.

In the *importing* package (here, `packaging-with-mypy-a`), ensure env var `MYPYPATH` includes the installation location of *this* package. For example:

```
export MYPYPATH=venv/lib/python3.9/site-packages
```
