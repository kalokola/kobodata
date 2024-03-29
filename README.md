<samp>

# [kobodata](https://pypi.org/project/kobodata/)

[![Made in Tanzania](https://img.shields.io/badge/made%20in-tanzania-008751.svg?style=flat-square)](https://github.com/Tanzania-Developers-Community/made-in-tanzania)
[![Downloads](https://pepy.tech/badge/kobodata)](https://pepy.tech/project/kobodata)
[![Downloads](https://pepy.tech/badge/kobodata/month)](https://pepy.tech/project/kobodata)
[![Downloads](https://pepy.tech/badge/kobodata/week)](https://pepy.tech/project/kobodata)

A python wrapper for [**Kobo Data Tool Kit**](https://www.kobotoolbox.org/)

## Why Kobodata

- This helps get remote data collected easily via kobo forms via consuming the APIS from [*.kobotoolbox.org](https://www.kobotoolbox.org/) sites.

There are several accounts , you can signup for one:

- [Humanitarian Organisation Accounts](https://kobo.humanitarianresponse.info/)
- [Researchers, Aid Workers & Everyone Else Accounts](https://kf.kobotoolbox.org/)

## Getting started

To get started with **kobodata**, you have to firstly install the library either directly or using *pip*.

### Installation directly

Use git to clone or you can also manually download the project repository just as shown below;

```bash
$ git clone https://github.com/kalokola/kobodata
$ cd kobodata
kobodata $ python setup.py install 
```

### Installing from pip

```bash
# For Windows 

pip install  --upgrade kobodata

#For Linux | MAC 

pip3 install --upgrade kobodata
```

# Get Account Credentials
1. You have to sign up at [Kobo ToolBox](https://www.kobotoolbox.org/) and create your first form. 
2. To obratin [account_token]() got to your account settings and you will see an API Token section, view the token and copy it to your cip board. The API Token looks like [bd1f68af664306q82d62w1412873d3b76b4321]()
3. To obtain the [dataset_uuid]() navigate to your kobo project, select [DATA] to view the table. Inspect the link to your table and copy a section that looks like [agLCVHnDkbXRkEuhtp4oUF]()
4. Specify the [account_domain]() for your account [kf.kobotoolbox.org]() or [kobo.humanitarianresponse.info]()

Once you have got the credentials you can proceed as follows. 

## How to Use (Code Exmaple).

Here how to fetch real time data

```python
>>> from kobodata import KoboData 
>>> account_token = "bd1f68af664306q82d62w1412873d3b76b4321"
>>> dataset_uuid = "agLCVHnDkbXRkEuhtp4oUF"
>>> account_domain = "kf.kobotoolbox.org"
>>> dataset = KoboData(
            account_subdomain,
            dataset_uuid,
            account_token     
        )

# get number observations
>>> dataset.counts
    784 rows

# return a dictionary of results
>>> dataset.get_data
```

## All the credit

1. [kalokola](https://github.com/kalokola)
2. All other contributors
</samp>
