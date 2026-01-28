# inloggningsfunktion – Testautomatisering

Detta projekt är en del av kursen **Testautomatisering** och innehåller automatiserade tester
för en inloggningsfunktion på en färdig webbsida, skrivna i **Python** med **Selenium WebDriver**
och **pytest** samt ett integrationstest/API som kontrollerar att API går att anropa. I GitHub actions
är det väntat att detta test misslyckas med statuskod 403.

## Testobjekt
Webbsidan som testas:
https://www.saucedemo.com/
Externt API som testas:
https://fakestoreapi.com/

## Tekniker och verktyg
- Python 3.13
- Selenium WebDriver
- pytest
- requests för API tester
- PyCharm
- GitHub + GitHub actions

## Projektstruktur
inloggningsfunktion/
│└──.venv
├── tests/
│ └── test_api_integration.py
│ └── test_login.py
├── requirements.txt
└── README.md
