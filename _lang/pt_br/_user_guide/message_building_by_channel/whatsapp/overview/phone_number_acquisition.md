---
nav_title: Aquisição de número de telefone
article_title: Aquisição de número de telefone
page_order: 3
description: "Este artigo de referência aborda como adquirir um número de telefone da Twilio e da Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Aquisição de número de telefone

> Para usar o canal de envio de mensagens do WhatsApp, você precisará de um número de telefone que atenda aos requisitos do WhatsApp para sua [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Você mesmo deve adquirir seu número de telefone, pois o Braze não fornecerá o número para você. Você pode comprar um telefone físico com um cartão SIM por meio de sua operadora de telefonia comercial ou usar um de nossos parceiros: Twilio ou Infoblip. **Você deve ter sua própria conta Twilio ou Infobip, pois isso não pode ser feito pela Braze.**

## Requisitos da API do WhatsApp

Seu número de telefone deve atender a esses requisitos da API do WhatsApp:

- De propriedade de sua empresa 
- Ter um código de país e de área (como números de telefone fixo e celular)
- Capacidade de receber chamadas de voz ou SMS
- Acessível durante a configuração da conta (para receber códigos de verificação)
- Não é um código curto
- Não usado anteriormente com a plataforma WhatsApp Business
- Não conectado a uma conta pessoal do WhatsApp

## Aquisição de um número de telefone Twilio

### Etapa 1: Compre um número de telefone no console ou na API do Twilio

1. No console do Twilio, acesse **Desenvolver** > **Números de telefone** > **Gerenciar** > **Comprar um número**. Se você não vir essa opção, selecione **Explore Products (Explorar produtos**), role até **Super Networks (Super redes**) e selecione **Phone Number (Número de telefone** ) > **Buy a number (Comprar um número)**. <br><br>![Console do Twilio com a guia "Develop" (Desenvolvimento) aberta e a opção "Buy a number" (Comprar um número).]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Digite o código de área ou a localização desejada (se houver). Encontre um número e selecione **Comprar**. <br><br> ![Um botão para comprar o número de telefone listado.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Depois de comprar o número de telefone, acesse **Números ativos** e selecione o número de telefone que acabou de comprar. <br><br>!["Active Numbers" (Números ativos) mostrando o número de telefone comprado.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Etapa 2: Configure seu número de telefone

Siga as instruções do Twilio para [configurar seu número de telefone do Twilio para receber o código de verificação por e-mail usando a transcrição do correio de voz](https://www.twilio.com/docs/whatsapp/self-sign-up#setting-up-your-twilio-phone-number-to-receive-the-verification-code-via-email-using-voicemail-transcription). **Não siga as instruções em nenhuma outra etapa, pois isso conectará seu número de telefone ao Twilio, não à Braze.**

{% alert warning %}
**Siga apenas as instruções do Twilio para receber um código de verificação.**

Se seguir as próximas etapas das instruções do Twilio, você conectará seu número de telefone ao Twilio. Isso significa que você não pode conectar esse número ao Braze, a menos que faça uma migração ou compre um número diferente.
{% endalert %}

### Etapa 3: Conclua o fluxo de trabalho de inscrição incorporado

1. Depois que o Twilio estiver configurado, vá para o dashboard do Braze > **Parceiros de tecnologia** > **WhatsApp** e selecione **Iniciar integração** ou **Adicionar conta do WhatsApp Business**, o que aparecer, para disparar o [fluxo de trabalho de inscrição incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>Na etapa **Adicionar um número de telefone para o WhatsApp**, selecione **Chamada telefônica** para verificar seu número de telefone. <br><br>![Seção com as opções para verificar seu número de telefone por meio de mensagem de texto ou chamada telefônica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Aguarde alguns minutos para que o código de verificação seja enviado para sua caixa de entrada de e-mail e, em seguida, insira o código de verificação e conclua a configuração.

## Aquisição de um número de telefone da Infobip 

1. No console da Infobip, acesse **Channels and Numbers** e selecione **Numbers**.<br><br>![Seção "Canais e números" da Infoblip com "Números" listados abaixo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecione **Comprar número** > o país para o qual deseja enviar mensagens > **SMS**.<br><br>![Botão para comprar um número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependendo do país selecionado, talvez seja necessário concluir um processo de registro adicional (como selecionar uma opção de 10 DLC ou ligação gratuita para números de telefone dos EUA). Certifique-se de selecionar a opção disponível.<br><br>![Uma página solicita que você selecione o tipo de número: 10 DLC ou gratuito.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecione a oferta disponível, prossiga com as demais etapas e aguarde o processamento de sua solicitação. Você pode verificar o status acessando **Números** > **Minha solicitação**. <br><br>![Uma oferta com informações que incluem taxas e cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependendo do país selecionado, aguarde a equipe da Infobip entrar em contato para obter os detalhes do registro (como no caso do 10DLC nos EUA).<br><br>

6. Quando seu número de telefone estiver pronto na Infobip, vá para o dashboard do Braze > **Technology Partners** > **WhatsApp** e selecione **Begin integration (Iniciar integração** ) ou **Add WhatsApp Business Account (Adicionar conta do WhatsApp Business**), o que aparecer, para disparar o [fluxo de trabalho de inscrição-se incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> Na etapa **Adicionar um número de telefone para o WhatsApp**, selecione **Mensagem de texto** para saber como deseja verificar seu número de telefone.<br><br>![Seção com as opções para verificar seu número de telefone por meio de mensagem de texto ou chamada telefônica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Verifique [os registros de análise](https://www.infobip.com/docs/analyze/analyze-logs) da Infobip no portal do cliente para obter o código de verificação, que pode levar alguns minutos para aparecer; em seguida, insira o código de verificação e conclua a configuração.




