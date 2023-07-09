from constants import EXCHANGE_RATE_DATE


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def test_value_is_number(cbr_client):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    for valute in exchange_rate.findall("Valute"):
        value = valute.find("Value").text
        assert is_number(value.replace(",", "."))


def test_numcode_is_number(cbr_client):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    for valute in exchange_rate.findall("Valute"):
        numcode = valute.find("NumCode").text
        assert numcode.isnumeric()
