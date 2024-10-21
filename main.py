from clients.conversor_service import CoinConversorService
from clients.callmebot_service import CallMeBot


conversor_service = CoinConversorService()
convesion = conversor_service.converter('BTC', 'BRL')

wpp_service = CallMeBot()
wpp_service.send_message(
    message=f'Cotação do Bitcoin: R$ {round(float(convesion), 2)}'
)
