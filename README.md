# Conversor de Moedas e Notificações via WhatsApp

Este projeto consiste em dois serviços principais: um conversor de moedas que utiliza a API da AwesomeAPI para consultar taxas de câmbio em tempo real, e um serviço de envio de notificações via WhatsApp usando a API do CallMeBot. Ele converte o valor de moedas, como o Bitcoin para o Real, e envia o resultado para um número de WhatsApp especificado.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Conta no [CallMeBot](https://www.callmebot.com/) para enviar mensagens via WhatsApp
- Chave de API da [AwesomeAPI](https://docs.awesomeapi.com.br/) para realizar consultas de conversão de moedas

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/PedroTomasini/conversor-moedas.git
cd conversor-moedas
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate  # Para Windows
```

3. Instale as dependências necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuração

Antes de executar o projeto, você precisará configurar suas credenciais API. Renomeie o arquivo `.env.example` para `.env` e insira suas chaves de API:

```
CALLMEBOT_API_KEY=your_callmebot_api_key
PHONE_NUMBER=your_whatsapp_number
```

- `CALLMEBOT_API_KEY`: Chave de API do CallMeBot.
- `PHONE_NUMBER`: Número de telefone para o qual a mensagem será enviada (no formato internacional).

## Execução

Para executar o projeto, basta rodar o script Python principal. Ele realizará a conversão da moeda especificada e enviará uma mensagem WhatsApp com o valor atual.

```bash
python main.py
```

A mensagem será enviada para o número configurado com o valor da cotação do Bitcoin (ou outra moeda) em Reais.

## Estrutura do Projeto

```
.
├── clients
│   ├── callmebot_service.py      # Serviço responsável por enviar mensagens via WhatsApp
│   ├── conversor_service.py      # Serviço responsável por realizar conversão de moedas
├── .env.example                  # Arquivo de exemplo para configurar variáveis de ambiente
├── main.py                       # Arquivo principal para execução do projeto
├── README.md                     # Este arquivo
└── requirements.txt              # Dependências do projeto
```

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você tiver alguma sugestão ou encontrar algum bug, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Este projeto é uma solução simples para acompanhar a cotação de moedas e receber notificações diretamente no WhatsApp.
