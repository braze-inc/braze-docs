---
nav_title: Criação de uma campanha MMS
article_title: Criação de uma campanha MMS
page_order: 2
description: "Este artigo de referência aborda as etapas envolvidas na criação, no envio e na visualização de uma mensagem MMS."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Criação de uma campanha MMS

> Este artigo contém informações específicas sobre a composição de MMS, que faz parte do compositor de SMS. Para obter informações mais detalhadas sobre o compositor de SMS/MMS, consulte o [compositor de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## Noções básicas de envio de MMS

### Selecione seu grupo de assinaturas

Você deve designar um grupo de assinaturas com números de telefone habilitados para MMS a serem direcionados (podem ser códigos curtos ou longos).

### Corpo da mensagem de entrada

Insira tipos de imagem PNG, JPEG, GIF e VCF da biblioteca de mídia ou especifique um URL. Somente uma imagem é suportada.

### Compreender o envio de MMS

Os MMS são cobrados a uma taxa diferente dos SMS somente de texto, e nem todas as operadoras aceitam MMS. Nesses casos, o Twilio converterá automaticamente o MMS em um link de imagem no qual o usuário poderá clicar.

### Use cartões de contato

Os cartões de contato (às vezes conhecidos como vCard ou Virtual Contact Files (vcf)) são um formato de arquivo padronizado para o envio de informações comerciais e de contato que podem ser facilmente importadas para catálogos de endereços ou de contatos. Esses cartões podem ser criados [de forma programática](https://www.twilio.com/blog/send-vcard-twilio-sms) e carregados na biblioteca de mídia do Braze ou criados por meio do nosso [gerador de cartões de contato]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) integrado.

## Criação de uma mensagem MMS

A criação de uma mensagem MMS requer que seu grupo de assinaturas esteja configurado para envio de MMS. Isso é indicado pela exibição da tag MMS ao selecionar um grupo de assinatura. Ao selecionar um grupo de assinatura habilitado para MMS, você poderá carregar uma imagem, fazer referência a um URL de imagem ou incluir um cartão de contato.

\![A guia "Compose" para escrever sua mensagem.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Especificações da imagem

| **Especificações da imagem** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Tamanho                     | Até 600 KB        |
| Tipos de arquivo               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pré-visualização de uma mensagem MMS

O Braze fornece uma visualização da imagem que você carregou no painel de **visualização** do compositor de mensagens. 

{% alert note %}
A ordenação dos ativos de SMS/MMS não pode ser personalizada. A ordem depende do telefone que está recebendo a mensagem.
{% endalert %}

\![Um exemplo de mensagem "Ready to hit the gym... at home?" (Pronto para ir à academia... em casa?). A visualização mostra a mensagem e a imagem enviadas como textos.]({% image_buster /assets/img/sms/mms_preview.png %})
