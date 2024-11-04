---
title: Sandbox Python SDK reference
excerpt: Reference guide to the Sandbox Python SDK on how to authorize, instantiate and use its service classes to access the Open Gateway APIs.
category: 66d5624a492663000f4ed527
---

> 📘 To try out our APIs, visit the [Sandbox](https://opengateway.telefonica.com/developer-hub/unirse).

The current scope of the Sandbox SDK is limited since it is meant to showcase how an SDK integration is like. Check the [API Integration guide](/docs/apiintegration) to understand the pros and cons of using an SDK when compared to implement HTTP requests.

Available languages:
- Python

Available service classes (per Open Gateway API product):
- SIM Swap

## Installation

The Sandbox SDK is available as a Python package in the [Python Package Index (PyPI)](https://pypi.org/project/opengateway-sandbox-sdk/). You can install it using `pip`:

```bash
pip install opengateway-sandbox-sdk
```

## Service class reference

#### Class constructor

```Python
SimSwap(client_id: str, client_secret: str, phone_number: str)
```

Instantiates a SIM Swap service class authorizing the instance with the [CIBA flow](/docs/backend).

Required parameters:
- client_id (str): Your application's client ID as obtained from the Sandbox console
- client_secret (str): Your application's client secret obtained along with the client ID
- phone_number (str): Phone Number to check SIM Swap status, with country prefix. Example: '+346xxxxxxxx'

#### Class functions

###### Check for a SIM Swap
```Python
SimSwap.check(self, max_age:int) → bool
```

Required parameters:
- max_age (int): Period in hours to be checked for a SIM Swap

Returns:
- bool, true if the SIM was swapped during the "max_age" period

###### Retrieve last SIM Swap date
```Python
SimSwap.retrieve_date(self) → datetime
```
Returns:
- datetime, with the Timestamp of latest SIM swap performed

## Usage sample

> 📘 These are code examples
> 
> Check other examples in the [catalog](../../catalog/available.md)

```python
import sys
from opengateway_sandbox_sdk import SimSwap

APP_CLIENT_ID = "obtained-from-the-sandbox-console"
APP_CLIENT_SECRET = "obtained-from-the-sandbox-console"

def main() -> None:
    phone_number = sys.argv[1]
    max_age = int(sys.argv[2]) if len(sys.argv) > 2 else 2400

    simswap_client = SimSwap(APP_CLIENT_ID, APP_CLIENT_SECRET, phone_number)
    print(f'CIBA auth success')

    if simswap_client.check(max_age=2400):
        print(f'A SIM card swap happened in the last {max_age // 24} days')
    else:
        print(f'No SIM card swap in the last {max_age // 24} days')

    last_swap = simswap_client.retrieve_date()
    print(f'Last SIM card swap happened {last_swap}')

if __name__ == "__main__":
    main()
```
