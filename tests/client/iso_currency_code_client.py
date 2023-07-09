import xml.etree.ElementTree as ET

from constants import ISO_CURRENCY_ATTRIBUTE_ITEM

from constants import ISO_CURRENCY_ATTRIBUTE_ID
from constants import ISO_CURRENCY_ATTRIBUTE_NAME
from constants import ISO_CURRENCY_ATTRIBUTE_NOMINAL
from constants import ISO_CURRENCY_ATTRIBUTE_ISO_NUM_CODE
from constants import ISO_CURRENCY_ATTRIBUTE_ISO_CHAR_CODE


class ISOCurrencyCodeClient:
    def __init__(self, path):
        self.path = path

    def get_dictionary_iso_currency_code(self):
        catalog = ET.parse(self.path)
        dictionary_iso_currency_code = {}
        for item in catalog.findall(ISO_CURRENCY_ATTRIBUTE_ITEM):
            dictionary_iso_currency_code[item.attrib[ISO_CURRENCY_ATTRIBUTE_ID]] = [
                item.find(ISO_CURRENCY_ATTRIBUTE_NAME).text,
                item.find(ISO_CURRENCY_ATTRIBUTE_NOMINAL).text,
                item.find(ISO_CURRENCY_ATTRIBUTE_ISO_NUM_CODE).text,
                item.find(ISO_CURRENCY_ATTRIBUTE_ISO_CHAR_CODE).text]
        return dictionary_iso_currency_code
