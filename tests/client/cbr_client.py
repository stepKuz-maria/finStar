import requests
import xml.etree.ElementTree as ET

from constants import CBR_REQUEST_PATH


class CBRClient:
    def __init__(self, url):
        self.url = url

    def get_exchange_rate_on_date(self, date_req):
        res = requests.get(f"{self.url}{CBR_REQUEST_PATH}{date_req}")
        xml_format = ET.fromstring(res.text)
        return xml_format
