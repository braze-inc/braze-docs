---
nav_title: Aquisição de número de telefone
article_title: Aquisição de número de telefone
page_order: 4
description: "Este artigo de referência aborda como adquirir um número de telefone da Twilio e da Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Aquisição de número de telefone

> Para usar o canal de envio de mensagens do WhatsApp, você precisará de um número de telefone que atenda aos requisitos do WhatsApp para sua [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Você mesmo deve adquirir seu número de telefone, pois a Braze não fornecerá o número para você. Você pode comprar um telefone físico com um cartão SIM por meio de sua operadora de telefonia comercial ou usar um de nossos parceiros: Twilio ou Infobip. **Você deve ter sua própria conta Twilio ou Infobip, pois isso não pode ser feito pela Braze.**

## Requisitos da API do WhatsApp

Seu número de telefone deve atender a estes requisitos da API do WhatsApp:

- Ser de propriedade da sua empresa 
- Ter um código de país e de área (como números de telefone fixo e celular)
- Ser capaz de receber chamadas de voz ou SMS
- Estar acessível durante a configuração da conta (para receber códigos de verificação)
- Não ser um código curto
- Não ter sido usado anteriormente com a plataforma WhatsApp Business
- Não estar conectado a uma conta pessoal do WhatsApp

## Aquisição de um número de telefone Twilio

### Etapa 1: Compre um número de telefone no console ou na API do Twilio

1. No console do Twilio, acesse **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Se você não vir essa opção, selecione **Explore Products**, role até **Super Networks** e selecione **Phone Number** > **Buy a number**. <br><br>![Console do Twilio com a guia "Develop" aberta e a opção "Buy a number".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Digite o código de área ou a localização desejada (se houver). Encontre um número e selecione **Buy**. <br><br> ![Um botão para comprar o número de telefone listado.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Depois de comprar o número de telefone, acesse **Active Numbers** e selecione o número de telefone que acabou de comprar. <br><br>!["Active Numbers" mostrando o número de telefone adquirido.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Etapa 2: Configure seu número de telefone

Siga as instruções do Twilio para configurar seu número de telefone Twilio para receber o código de verificação por e-mail usando **apenas** o [Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number). **Não siga as instruções de nenhuma outra etapa.**

{% alert warning %}
Siga apenas as instruções do Twilio para receber um código de verificação.
Se seguir as próximas etapas, você conectará seu número de telefone ao Twilio, o que significa que não poderá conectar esse número à Braze, a menos que faça uma migração ou compre um número diferente.
{% endalert %}

1. No console do Twilio, acesse a [página Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) e selecione o número de telefone que você comprou.
2. Acesse a seção **Voice Configuration** e, no menu suspenso **Configure with**, selecione **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Na linha **A call comes in**, selecione **Webhook** e defina a URL como `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, substituindo `YOUR_EMAIL_ADDRESS` pelo seu endereço de e-mail.
4. No console do Twilio, acesse **2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register** e selecione **Copy** ao lado do número de telefone.
5. Na janela **Self Sign-up**, na página **Add your WhatsApp phone number**, selecione **Add a new phone number** e cole o número de telefone.
6. Selecione **Phone call** como método de verificação e, em seguida, selecione **Next**.
7. Você receberá o código de verificação no seu e-mail em até 10 minutos.

### Etapa 3: Conclua o fluxo de trabalho de inscrição incorporado

1. Depois que o Twilio estiver configurado, acesse o dashboard da Braze > **Technology Partners** > **WhatsApp** e selecione **Begin integration** ou **Add WhatsApp Business Account**, o que aparecer, para disparar o [fluxo de trabalho de inscrição incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>Na etapa **Add a phone number for WhatsApp**, selecione **Phone call** para verificar seu número de telefone. <br><br>![Seção com as opções para verificar seu número de telefone por meio de mensagem de texto ou ligação telefônica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Aguarde alguns minutos para que o código de verificação seja enviado para sua caixa de entrada de e-mail e, em seguida, insira o código de verificação e conclua a configuração.

## Aquisição de um número de telefone da Infobip 

1. No console da Infobip, acesse **Channels and Numbers** e selecione **Numbers**.<br><br>![Seção "Channels and Numbers" da Infobip com "Numbers" listado abaixo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecione **Buy Number** > o país para o qual deseja enviar mensagens > **SMS**.<br><br>![Botão para comprar um número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependendo do país selecionado, talvez seja necessário concluir um processo de registro adicional (como selecionar uma opção de 10 DLC ou toll-free para números de telefone dos EUA). Certifique-se de selecionar a opção disponível.<br><br>![Uma página solicita que você selecione o tipo de número: 10 DLC ou toll-free.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecione a oferta disponível, prossiga com as demais etapas e aguarde o processamento da sua solicitação. Você pode verificar o status acessando **Numbers** > **My Request**. <br><br>![Uma oferta com informações que incluem taxas e cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependendo do país selecionado, aguarde a equipe da Infobip entrar em contato com você para informar os detalhes de registro (como para 10DLC nos EUA).<br><br>

6. Quando seu número de telefone estiver pronto na Infobip, acesse o dashboard da Braze > **Technology Partners** > **WhatsApp** e selecione **Begin integration** ou **Add WhatsApp Business Account**, o que aparecer, para disparar o [fluxo de trabalho de inscrição incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> Na etapa **Add a phone number for WhatsApp**, selecione **Text message** para verificar seu número de telefone.<br><br>![Seção com as opções para verificar seu número de telefone por meio de mensagem de texto ou ligação telefônica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Verifique os [registros de análise](https://www.infobip.com/docs/analyze/analyze-logs) da Infobip no portal do cliente para obter o código de verificação, que pode levar alguns minutos para aparecer; em seguida, insira o código de verificação e conclua a configuração.