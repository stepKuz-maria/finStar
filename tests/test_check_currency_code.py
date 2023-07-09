from constants import CURRENCY_ATTRIBUTE_ID
from constants import EXCHANGE_RATE_DATE


def test_check_currency_code(cbr_client, dictionary_currency_code):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    miss_currency_code = ''
    for valuta in exchange_rate:
        if dictionary_currency_code.get(valuta.attrib[CURRENCY_ATTRIBUTE_ID]) is None:
            miss_currency_code += valuta.attrib[CURRENCY_ATTRIBUTE_ID] + ' '
    error_message = 'Коды валют, которых нет в справочнике: ' + miss_currency_code
    assert miss_currency_code == '', error_message
