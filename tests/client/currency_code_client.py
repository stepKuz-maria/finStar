import xml.etree.ElementTree as ET

from constants import CURRENCY_ATTRIBUTE_ID


class CurrencyCodeClient:
    def __init__(self, path):
        self.path = path

    def get_dictionary_currency_code(self):
        catalog = ET.parse(self.path)
        dictionary_currency_code = {}
        for item in catalog.getroot():
            dictionary_currency_code[item.attrib[CURRENCY_ATTRIBUTE_ID]] = item
        return dictionary_currency_code
