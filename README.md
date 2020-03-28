# Satang Pro Python

A Python library for [satang.pro](https://docs.satang.pro/) API


## Releases
  - ```1.0.0``` releases first version


## Table of Contents

  - [Installation](#installation)
  - [Usage](#usage)
    - [Initial a Object]($initobj)
    - [Viewing Orders](#viewingorder)
    - [Viewing Orderbook Tickers](#viewingorderbooktickers)
    - [Viewing User Info](#viewinguserinfo)


## Installation <a name="installation"></a>

    pip install satang-pro

## Usage <a name="usage"></a>

    from satang_pro import SatangPro

### Initial a object <a name="initobj"></a>

#### Parameter:

  * ```api_key``` <b>string</b>
  * ```secret_key``` <b>string</b>

#### Function:

    API_KEY = "live-9700657ce6984..."
    SECRET_KEY = "ctyf9ZW2QO6ejpFU..."

    sp = SatangPro(api_key=API_KEY, secret_key=SECRET_KEY)

### Viewing Orders <a name="viewingorder"></a>

#### Parameter:

  * ```pair``` <b>string</b> a pair symbol, such as 'btc_thb', 'eth_thb'

#### Function:

    sp.orders(pair='btc_thb')

#### Response:

    {
      'bid': [
        {
          'price': '221000',
          'amount': '0.15473'
        },
        {
          'price': '219456.001',
          'amount': '0.32597'
        }
      ],
      'ask': [
        {
          'price': '221400',
          'amount': '0.02607'
        },
        {
          'price': '221480.99324974',
          'amount': '0.99999'
        }
      ]
    }


### Viewing Orderbook Tickers <a name="viewingorderbooktickers"></a>

#### Function:

    sp.orderbook_tickers()

#### Response:

    {
      'BCH_THB': {
        'bid': {
          'price': '7011',
          'amount': '19.2023'
        },
        'ask': {
          'price': '8000',
          'amount': '0.0209'
        }
      },
      'BNB_THB': {
        'bid': {
          'price': '400',
          'amount': '25'
        },
        'ask': {
          'price': '419.9999978',
          'amount': '200'
        }
      }



  ### Viewing User Info <a name="viewinguserinfo"></a>

  #### Function:

      sp.users()

  #### Response:

    {
      "id": 999,
      "email": "satang-user@satang.com",
      "identity_verification_level": "level_1",
      ...
    }
