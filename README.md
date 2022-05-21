<samp>
# KOBODATA DOCUMENTATION

## Contents

**Step(1) Installation**
```$ pip3 install kobodata```

## How to Use

**Step(1) : import KoboData class**

```python
from kobodata import KoboData
```

**Step(2) : Specify Authentication credentials**

- (i) your authentocation token obtained from kobo account settings eg "768fe18a0c1xxxxxxa0c1977a4xxx6ed88

```python
account_token = "xxxxxxxxxxxxxxxxxxxxxxxxx"
```

- (ii) unique identifier for your dataset e.g "agLCVHnDkbXRkEuhtp4oUF"

```python
dataset_uuid = "xxxxxxxxxxxxxxx"
```

- (iii) depends on your kobo account type eg: "kf.kobotoolbox.org" or "kobo.humanitarianresponse.info"

```python
account_domain = "xxxxxxxxxxxxxxx"
```

**Step(3) : Access data**

- (i) import the class and specify your credentials

```python
dataset = KoboData(
    account_domain,
    dataset_uuid,
    account_token     
)
```


- (ii) to get data, it returns a dictionary of your data

```python
my_data = dataset.kobo_data
```

- (iii) you can convert into a pandas data frame for further analyses

```python
import pandas as pd
table = pd.DataFrame(my_data)
print(table)
```


- (iv) total number of data collected

```python
print(dataset.counts)
```


## Contacts
> Programmed by Brightius Kalokola

[Email](brightiuskalokola@gmail.com)

[Twitter](https://twitter.com/kalokolabr)

[Github](https://github.com/kalokola)

`I code to Spread Ideas and make things easier for people.`
</samp>