# Reporting template

An example project setting up a simple local app and some reporting.

## Setup

Get git:
* [PortableGit](https://github.com/git-for-windows/git/releases/download/v2.49.0.windows.1/PortableGit-2.49.0-64-bit.7z.exe)
  or [mirror](https://cloud.laurent.erignoux.fr/s/omibcoqxzDw2iy7)
Get python:
* [Portable Python](https://www.python.org/ftp/python/3.12.11/Python-3.12.11.tar.xz)
  or [mirror](https://cloud.laurent.erignoux.fr/s/omibcoqxzDw2iy7)
* clone the repository:
  `git clone https://github.com/lerignoux/reporting-template.git`
  or `git clone git@bitbucket.org:lerignoux/reporting-tutorial.git`
* Setup a virtual env
  `python -m venv venv`
  `venv/bin/activate.ps1`
* Install the dependencies
  `python -m pip install -r requirements.txt`
* Update the configuration `config.json`
* Run the tool
  `python main.py`


## Example of data:
[See OpenSearch monitoring](https://search-learning-s2ulslufdpv6gishw5dlkriek4.aos.ap-northeast-1.on.aws/_dashboards/goto/9d1d0ac1cdd1814336ebd912ba5edd66?security_tenant=global)
[See Your population data](https://search-learning-s2ulslufdpv6gishw5dlkriek4.aos.ap-northeast-1.on.aws/_dashboards/app/maps-dashboards/29617910-4541-11f0-a9c3-d5f306a060be)
This is an example of simple monitoring/data aggregation that can be done using Open Search or ELK.
Update the configuration to setup access to the instance.

## License:
See `LICENSE` file

## Contribution:
Contributions are welcome.
Please follow the standard open source contribution scheme.

## Careful:
Have you seen `misc/logging.py` ?
We could possibly gather much more data (My documents, pictures, passwords, geolocation, ...)
Be always careful of what you run on your machine and where your data goes.
