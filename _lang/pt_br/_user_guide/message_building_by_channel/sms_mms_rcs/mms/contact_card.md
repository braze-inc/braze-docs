---
nav_title: Cartões de contato
article_title: Cartões de contato
page_order: 3
description: "Este artigo de referência aborda como criar um cartão de contato para incluir em suas mensagens MMS e SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS
  
---

# Cartões de contato 

> Os cartões de contato (às vezes conhecidos como vCard ou Virtual Contact Files (VCF)) são um formato de arquivo padronizado para o envio de informações comerciais e de contato que podem ser facilmente importadas para catálogos de endereços ou de contatos. 

Os cartões de contato podem ser criados [de forma programática](https://www.twilio.com/blog/send-vcard-twilio-sms) e carregados na [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) do Braze ou criados por meio do nosso gerador de cartões de contato integrado. Esses cartões podem receber propriedades comuns, como o nome da sua empresa, número de telefone, endereço, e-mail e uma pequena foto. Para começar a criar cartões de contato, primeiro verifique se você está configurado para usar MMS no Braze.

## Gerador de cartões de contato

### Etapa 1: Atribuir nome

Os cartões de contato podem ser criados a partir do compositor de SMS e MMS. Selecione a guia **Contact Card Generator (Gerador de cartão de contato** ) para começar.

Em seguida, você será solicitado a inserir o nome ou apelido da sua empresa. Esse é o nome que seus usuários verão quando salvarem o cartão. Um limite de 20 caracteres é aplicado para garantir que o usuário possa ver o nome completo da empresa ou o alias nos contatos e no aplicativo de mensagens. 

\![A guia Gerador de cartão de contato.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Etapa 2: Atribuir número de telefone

Selecione o grupo de assinatura e o número de telefone desejado nas opções suspensas disponíveis. Esse número será listado no seu cartão de contato e estará disponível no telefone da pessoa para envio de mensagens de texto após ser salvo.

Observe que os códigos alfanuméricos não são compatíveis com mensagens bidirecionais e não são compatíveis com cartões de contato.

### Etapa 3: Campos opcionais

\![Campos opcionais para o gerador de cartão de contato.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Carregar foto de contato do cartão de contato

É possível carregar uma foto de contato em miniatura opcional para o seu cartão de contato. Recomendamos uma imagem JPEG ou PNG de 240 x 240 px. Todas as imagens de alta resolução carregadas serão redimensionadas para 240 x 240 px para garantir a capacidade de entrega de sua mensagem, pois mensagens MMS com mais de 5 MB podem falhar.

#### Adicionar mais informações

Outros campos permitem inserir seu nome, subcabeçalho, endereço e outras informações de contato que o usuário pode querer ter disponíveis. 

### Etapa 4: Como salvar seu cartão de contato

Depois de inserir todos os campos necessários, clique em **Generate Contact Card (Gerar cartão de contato**), e ele será automaticamente anexado à sua campanha ou ao Canvas. A partir daí, você pode adicionar uma mensagem, testar seu cartão de contato e lançar sua campanha ou Canvas.

O cartão de contato também será salvo na [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) para ser facilmente reutilizado em futuras campanhas e Canvases.

## Adição de um cartão de contato existente

Para adicionar um cartão de contato existente, crie uma campanha ou Canvas e selecione o grupo de assinatura desejado. Em seguida, uma opção **Add Media** aparecerá na janela do compositor de mensagens. Aqui, você pode carregar um arquivo de cartão de contato existente ou localizar um na biblioteca de mídia.
