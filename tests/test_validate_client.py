import pytest
import xmlschema
from xmlschema import XMLSchemaValidationError

from constants import CURRENCY_EXCHANGE_XSD_ORIGINAL
from constants import CURRENCY_EXCHANGE_WITH_ERROR_XSD_ORIGINAL
from constants import EXCHANGE_RATE_DATE


def test_validation_xml_to_xsd_positive(cbr_client):
    xsd = xmlschema.XMLSchema(CURRENCY_EXCHANGE_XSD_ORIGINAL)
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    assert xsd.is_valid(exchange_rate)


def test_validation_xml_to_xsd_negative(cbr_client):
    xsd = xmlschema.XMLSchema(CURRENCY_EXCHANGE_WITH_ERROR_XSD_ORIGINAL)
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    with pytest.raises(XMLSchemaValidationError):
        xsd.validate(exchange_rate)
