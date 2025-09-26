---
nav_title: Pypestream
article_title: Pypestream
description: "Este artigo de referência descreve a parceria entre a Braze e a Pypestream, uma plataforma de IA conversacional full-stack que permite aprimorar o engajamento digital com sua marca."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> A [Pypestream](https://www.pypestream.com) é uma plataforma de IA conversacional full-stack que oferece envio de mensagens patenteado e completo na nuvem para transformar marcas em entidades digitais "sempre ativas". Com a Pypestream, as marcas agora podem se engajar em conversas omnicanais em escala com cada cliente, aproveitando uma experiência de usuário imersiva, recursos avançados de NLU e integrações em tempo real com sistemas back-end.

_Essa integração é mantida pela Pypestream._

## Sobre a integração

A integração entre a Braze e a Pypestream permite orquestrar com perfeição o ciclo de vida do cliente de ponta a ponta, desde o contato inicial, encaminhado para uma experiência de conversação, até o(s) acompanhamento(s) omnicanal(is) por meio de redirecionamento inteligente. 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Pypestream | É necessário ter uma [conta Pypestream](https://www.pypestream.com/contact-us/) para usar a parceria.<br><br>Uma vez inscrito, a equipe da Pypestream o ajudará a configurar seu ambiente dedicado para começar a criar sua solução de IA conversacional para integração com o Braze. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

A parceria entre a Braze e a Pypestream pode ser usada nos seus canvas para satisfazer a casos de uso comuns, como:
* **Redirecionamento inteligente**: Redirecione os usuários com o Braze Canvas após o engajamento de conversação com a sua marca, aproveitando todos os pontos de dados avançados coletados por meio do Pypestream.
* **Direcionamento dinâmico**: Entre em contato com clientes existentes e potenciais com base em seus coortes e segmentos específicos, atendendo-os com experiências de conversação personalizadas por meio da Pypestream.
* **Insights contextuais sobre o cliente**: Depois que um usuário final (cliente existente ou potencial) se engajar em seu site, combine as tags de página da Web ingeridas pelo Pypestream Event Listener com os dados de cliente armazenados no Braze para fornecer uma interação de conversação contextual e totalmente personalizada.

## Integração

A Pypestream utiliza uma camada de integração sem servidor para realizar integrações personalizadas em várias plataformas. Essa camada é usada para fazer interface com serviços ou sistemas para dar suporte aos requisitos de dados do fluxo de conversação que está sendo criado. Essas integrações, chamadas de integrações de Action Node, geralmente são escritas em Python e implantadas usando a plataforma Pypestream. Depois que um nó de ação é instanciado, ele oferece a flexibilidade de se integrar a qualquer endpoint da API do Braze e permite que os resultados sejam avaliados de várias maneiras. 

{% alert note %}
Acesse este [artigo do Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) para obter uma visão geral e as etapas de configuração dos nós de ação do Pypestream. Você deve ser cliente da Pypestream para acessar essa documentação.
{% endalert %}

### Etapa 1: Definir configurações de ponto de extremidade

Os valores de configuração primária, como o URL do endpoint REST da Braze e as chaves da API da Braze, devem ser definidos no arquivo `app.py` da solução: 

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### Etapa 2: Desenvolver modelo de nó de ação

Os nós de ação aproveitam o ambiente com o qual a solução é implantada para interagir, com os respectivos endpoints Braze definidos na etapa anterior. Essa etapa desenvolve um nó de ação para integrar endpoints específicos do Braze. Use o modelo a seguir como um guia para desenvolver as integrações: 

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### Etapa 3: atualize os projetos de solução

A etapa final da integração com a Braze REST API envolve a configuração dos fluxos no [Design Studio](https://platform.pypestream.com/design-studio/) da Pypestream para usar o nó de ação que foi desenvolvido na etapa anterior. 

{% alert note %}
Acesse este [artigo da Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) para obter uma visão geral de como configurar modos no Design Studio. Você deve ser cliente da Pypestream para acessar essa documentação.
{% endalert %}

## Caso de uso de integração

Depois que os pré-requisitos forem atendidos e uma estrutura de nó de ação tiver sido criada, o desenvolvedor terá uma tela em branco para trabalhar ao interagir com os pontos de extremidade da API do Braze. Este exemplo mostra as etapas necessárias para integrar um nó de ação ao [endpoint `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) do Braze - especificamente para criar um perfil de usuário para rastrear um usuário específico que entra em um fluxo de conversação Pypestream.

### Etapa 1: Colete dados de usuários em conversas

Quando um usuário entra em uma sessão da Pypestream, as especificidades dos dados coletados dependem inteiramente do caso de uso em questão. Para poder criar um perfil de usuário no Braze, a conversa deve coletar os campos necessários
exigido pelo ponto de extremidade desejado.

Por exemplo, se a solução coletou as seguintes informações do usuário durante a conversa para o endpoint `/user/track` da Braze: 

* Nome
* Sobrenome
* Endereço de e-mail
* Data de nascimento
* Cidade de residência
* Sistema operacional

Esses dados agora podem ser enviados para a plataforma da Braze para rastrear o engajamento desse usuário com a capacidade de redirecioná-lo no futuro. Confira a [lista de casos de uso](#use-cases) para ver os aplicativos comuns.

### Etapa 2: Preencher os dados na estrutura do nó de ação

Aproveitando a mesma estrutura para desenvolver nós de ação, os dados coletados do usuário podem ser preenchidos no nó de ação para serem enviados ao Braze por meio do nosso endpoint `/user/track`.

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### Etapa 3: Atualizar os fluxos de solução para redirecionar após o sucesso/falha do nó de ação

Por fim, no design de cada solução, você pode encaminhar os usuários para os nós com base no sucesso da chamada à API do nó de ação. Se o nó de ação receber uma mensagem de erro, o usuário final deverá ser tratado com cuidado. 

