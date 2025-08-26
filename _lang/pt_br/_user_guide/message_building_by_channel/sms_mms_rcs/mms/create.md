---
nav_title: Criação de uma campanha MMS
article_title: Criação de uma campanha MMS
page_order: 2
description: "Este artigo de referência aborda as etapas envolvidas na criação, no envio e na prévia de uma mensagem MMS."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Criação de uma campanha MMS

> Este artigo contém informações específicas sobre a composição de MMS, que faz parte do criador de SMS. Para saber mais informações detalhadas sobre o criador de SMS/MMS, consulte o [criador de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## Noções básicas de envio de MMS

### Selecione seu grupo de inscrições

É necessário designar um grupo de inscrições com números de telefone ativados para MMS para direcionamento (podem ser códigos curtos ou longos).

### Corpo da mensagem de entrada

Insira tipos de imagem PNG, JPEG, GIF e VCF da biblioteca de mídia ou especifique um URL. Somente uma imagem é suportada.

### Entenda o envio de MMS

Os MMS são cobrados em uma taxa diferente dos SMS somente de texto, e nem todas as operadoras aceitam MMS. Nesses casos, o Twilio converterá automaticamente o MMS em um link de imagem no qual o usuário poderá clicar.

### Use cartões de contato

Os cartões de contato (às vezes conhecidos como vCard ou Virtual Contact Files (vcf)) são um formato de arquivo padronizado para o envio de informações comerciais e de contato que podem ser facilmente importadas para catálogos de endereços ou de contatos. Esses cartões podem ser criados de [forma programática](https://www.twilio.com/blog/send-vcard-twilio-sms) e feitos upload para a biblioteca de mídia do Braze ou criados por meio do nosso [gerador de cartões de contato]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) integrado.

## Criação de uma mensagem MMS

A criação de uma mensagem MMS requer que seu grupo de inscrições esteja configurado para o envio de MMS. Isso é indicado pela visualização da tag MMS ao selecionar um grupo de inscrições. Ao selecionar um grupo de inscrições habilitado para MMS, você poderá fazer upload de uma imagem, fazer referência a um URL de imagem ou incluir um cartão de contato.

![A guia "Compose" para escrever sua mensagem.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Especificações da imagem

| **Especificações da imagem** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Tamanho                     | Até 600 KB        |
| Tipos de arquivos               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-visualização de uma mensagem MMS

A Braze fornece uma prévia da imagem que você fez upload no painel **Pré-visualização** do criador de mensagens. 

{% alert note %}
Não é possível personalizar a ordem dos ativos de SMS/MMS. O pedido depende do fato de o telefone receber essa mensagem.
{% endalert %}

![Um exemplo de mensagem "Ready to hit the gym...at home?" (Pronto para ir para casa?). A prévia mostra a mensagem e a imagem enviadas como textos.]({% image_buster /assets/img/sms/mms_preview.png %})
