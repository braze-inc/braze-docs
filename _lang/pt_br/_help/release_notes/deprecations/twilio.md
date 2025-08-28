---
nav_title: Parceria Twilio
alias: /partners/twilio/

description: "Este artigo descreve a parceria entre Braze e Twilio."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Observe que o suporte para a Integração Twilio Webhook será descontinuado em 31 de janeiro de 2020. Se você deseja continuar acessando os serviços de SMS com a Braze, consulte nossa [documentação de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).
{% endalert %}

Para este exemplo, configuraremos o canal de webhook do Braze para enviar SMS e MMS aos seus usuários, via [API de envio de mensagens](https://www.twilio.com/docs/api/rest/sending-messages) da Twilio. Para sua conveniência, um modelo de webhook do Twilio está incluído no dashboard.

## URL HTTP

A URL do Webhook é fornecida pela Twilio no seu dashboard. Este URL é único para sua conta Twilio, pois contém seu ID de conta Twilio (`TWILIO_ACCOUNT_SID`).

No nosso exemplo da Twilio, o URL do webhook é `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Você pode encontrar este URL na seção *Primeiros Passos* do console do Twilio.

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Corpo da solicitação

A API do Twilio espera que o corpo da solicitação seja codificado em URL, então temos que começar alterando o tipo de solicitação no criador de webhook da Braze para `Raw Text`. Os parâmetros necessários para o corpo da solicitação são *Para*, *De* e *Corpo*.

A captura de tela a seguir é um exemplo de pode ser a sua solicitação se você estiver enviando um SMS para o número de telefone de cada usuário, com o corpo "Olá da Braze!".

- Você precisará ter números de telefone válidos em cada perfil de usuário no seu público-alvo.
- Para atender ao formato de solicitação do Twilio, use o filtro `url_param_escape` Liquid no conteúdo da sua mensagem. Este filtro codifica uma string para que todos os caracteres sejam permitidos em uma solicitação HTML; por exemplo, o caractere de mais (`+`) no número de telefone `+12125551212` é proibido em dados codificados em URL e será convertido para `%2B12125551212`.

![Corpo do webhook]({% image_buster /assets/img_archive/Webhook_Body.png %})

## Cabeçalhos e Método da Solicitação

O Twilio requer dois cabeçalhos de solicitação, o Content-Type da solicitação e um cabeçalho de [autenticação básica HTTP](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Adicione-os ao seu webhook clicando no ícone de engrenagem ao lado do criador de webhook, depois clicando em *Adicionar Novo Par* duas vezes.

Nome do Cabeçalho | Valor do Cabeçalho
--- | ---
Content-Type | `application/x-www-form-urlencoded`
Autorização | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Substitua `TWILIO_ACCOUNT_SID` e `TWILIO_AUTH_TOKEN` com valores do seu dashboard do Twilio. Por fim, o endpoint da API do Twilio está esperando uma solicitação HTTP POST, então escolha essa opção no menu suspenso para *HTTP Method*.

![Método Webhook]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Faça uma prévia da sua solicitação

Use o criador de webhook para prévia a solicitação de um usuário aleatório, ou de um usuário com credenciais específicas, para garantir que a solicitação esteja sendo renderizada corretamente.

![Prévia do Webhook]({% image_buster /assets/img_archive/Webhook_Preview.png %})

