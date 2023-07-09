import pytest

from client.cbr_client import CBRClient
from client.currency_code_client import CurrencyCodeClient
from client.iso_currency_code_client import ISOCurrencyCodeClient

from constants import CBR_URL
from constants import CURRENCY_CODE_PATH
from constants import ISO_CURRENCY_CODE_PATH


@pytest.fixture(scope="session")
def cbr_client():
    return CBRClient(CBR_URL)


@pytest.fixture(scope="session")
def dictionary_currency_code():
    return CurrencyCodeClient(CURRENCY_CODE_PATH).get_dictionary_currency_code()


@pytest.fixture(scope="session")
def dictionary_iso_currency_code():
    return ISOCurrencyCodeClient(ISO_CURRENCY_CODE_PATH).get_dictionary_iso_currency_code()
