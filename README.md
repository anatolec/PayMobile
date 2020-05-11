# Parktop
In Paris and a few other cities it is now possible to pay parking meter online on paybyphone.fr. This package 
allows you to automate this payment. It is based on the selenium web driver.

![](PayByPhone.PNG)

## Installation

```sh
pip install parktop
```

## Usage

```python
from parktop import topup

topup('0123456789', # Phone Number (= username)
      '123456',     # Password
      '75001',      # Zip code
      days=2)       # Parking time
```

## Release History

* 1.0.0
    * First stable version.

## Meta

Anatole Callies – anatole@callies.fr

Distributed under the Apache License 2.0. See ``LICENSE`` for more information.

[https://github.com/anatolec/](https://github.com/anatolec/)
