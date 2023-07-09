from constants import EXCHANGE_RATE_DATE


def test_check_currency_iso_name(cbr_client, dictionary_iso_currency_code):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    error_name = ''
    for valuta in exchange_rate.findall("Valute"):
        find_in_dictionary = dictionary_iso_currency_code.get(valuta.attrib['ID'])
        if find_in_dictionary is not None:
            if find_in_dictionary[0] != valuta.find("Name").text:
                error_name = error_name + find_in_dictionary[0] + ' != ' + valuta.find("Name").text + '\n'
    assert error_name == '',  error_name


def test_check_currency_iso_nominal(cbr_client, dictionary_iso_currency_code):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    error_nominal = ''
    for valuta in exchange_rate.findall("Valute"):
        find_in_dictionary = dictionary_iso_currency_code.get(valuta.attrib['ID'])
        if find_in_dictionary is not None:
            if find_in_dictionary[1] != valuta.find("Nominal").text:
                error_nominal = error_nominal + find_in_dictionary[1] + ' != ' + valuta.find("Nominal").text + '\n'
    assert error_nominal == '', error_nominal


def test_check_currency_iso_num_code(cbr_client, dictionary_iso_currency_code):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    error_num_code = ''
    for valuta in exchange_rate.findall("Valute"):
        find_in_dictionary = dictionary_iso_currency_code.get(valuta.attrib['ID'])
        if find_in_dictionary is not None:
            if int(find_in_dictionary[2]) != int(valuta.find("NumCode").text):
                 error_num_code = error_num_code + find_in_dictionary[2] + ' != ' + valuta.find("NumCode").text + '\n'
    assert error_num_code == '', error_num_code


def test_check_currency_iso_char_code(cbr_client, dictionary_iso_currency_code):
    exchange_rate = cbr_client.get_exchange_rate_on_date(EXCHANGE_RATE_DATE)
    error_char_code = ''
    for valuta in exchange_rate.findall("Valute"):
        find_in_dictionary = dictionary_iso_currency_code.get(valuta.attrib['ID'])
        if find_in_dictionary is not None:
            if find_in_dictionary[3] != valuta.find("CharCode").text:
                error_char_code = error_char_code + find_in_dictionary[3] + ' != ' + valuta.find("CharCode").text + '\n'
    assert error_char_code == '', error_char_code
