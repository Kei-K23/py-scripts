from dotenv import dotenv_values
import requests
import argparse
import datetime

env_vars = dotenv_values('.env')
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%m/%d/%Y')

API_KEY = env_vars.get('API_KEY')

BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

# Remove the extra comma after the list definition
CON_CURRENCIES = [
    "USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK",
    "NZD", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "ZAR", "BRL",
    "TRY", "HKD"
]


def get_currencies(base, base_currencies):
    try:
        currencies = base_currencies.strip()
        url = f'{BASE_URL}&base={base}&currencies={currencies}'
        res = requests.get(url=url)
        data = res.json()
        return data['data']
    except Exception as e:
        print(e)
        return None


def validate_argument(args):
    if args.base not in CON_CURRENCIES:
        print(f'{args.base} is not a valid base currency')
        return False

    currencies = args.currencies.split(',')

    for currency in currencies:
        if currency not in CON_CURRENCIES:
            print(f'{currency} is not a valid currency')
            return False

    return True


parser = argparse.ArgumentParser(
    description="Currency exchange rate CLI by Kei-K"
)

parser.add_argument(
    '-b', '--base', metavar='base', required=True,
    help='Name of the base currency'
)

parser.add_argument(
    '-c', '--currencies', metavar='currencies',
    required=True,
    help='Comma separated value without space of currency e.g USD,EUR,AUD'
)

args = parser.parse_args()

if validate_argument(args):
    currencies_data = get_currencies(args.base, args.currencies)

    if currencies_data:
        if args.base in currencies_data.keys():
            del currencies_data[args.base]

        title = f" Curreny for {formatted_time} based on {
            args.base}\n".center(35, '=')
        print(title)
        for currency, value in currencies_data.items():
            formatted_value = "{:.2f}".format(value)
            print(currency.ljust(30, '-'), formatted_value.rjust(5))
        print('')
        print('Enjoy your day')

    else:
        print('Failed to retrieve the currencies data!')
