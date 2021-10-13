from logging import exception
from unittest import main, TestCase
import requests

URL_BASE = "http://viacep.com.br/ws"
def get_cep_data(cep, type_return):

    try:
        payload={}
        headers = {}
        url = URL_BASE + '/' + cep + '/' + type_return
        response = requests.request("GET", url, headers=headers, data=payload)

        if(response.status_code == 200):
            return response.json()
        
        return False
    
    except exception:
        return "Error"


class TestRequest(TestCase):
  teste_mock = {
            "cep": "01001-000",
            "logradouro": "Praça da Sé",
            "complemento": "lado ímpar",
            "bairro": "Sé",
            "localidade": "São Paulo",
            "uf": "SP",
            "ibge": "3550308",
            "gia": "1004",
            "ddd": "11",
            "siafi": "7107"
  }

  def test_if_request_returns_ok(self):
    # my_house = get_cep_data("26325170","json")
    # expected_response = dict()
    self.assertEqual(type(self.teste_mock), type(dict()))

if __name__ == '__main__':
    main()