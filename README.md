# agsconfig  &middot; [![GitHub](https://img.shields.io/badge/license-BSD--3--Clause-green.svg)](LICENSE)

agsconfig is a Python library for editing ArcGIS Server configuration, either before deployment by editing a Service Definition Draft, or after deployment by editing the JSON configuration provided by ArcGIS Server.

## Installation

agsconfig is made available on PyPi, simply install it with `pip`.

```
> pip install agsconfig
```

## Development

To get started on developing agsconfig, simply fork the repository and get it with your favourite Git client.  In the root of the repository is a standalone task runner, [`pie.py`](https://github.com/adamkerz/pie), that can excute tasks contained in `pie_tasks.py`.

You'll need a Python install with `pip` and `virtualenv`, but other than that, no pre-installed dependencies are necessary.

On a shell, simply run the setup task as follows to create a virtual environment for development work:

```
> python .\pie.py setup
```

To get a list of all available tasks, exceute the following:

```
> python .\pie.py -l
```
