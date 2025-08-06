---
nav_title: Prévia dinâmica de link para SMS
article_title: Prévia dinâmica de link para SMS
description: "Este artigo de referência descreve como ativar e usar o recurso de prévia de links para SMS da Movable Ink."
page_type: partner
search_tag: Partner
---

# Prévia dinâmica de link para SMS

> Com a prévia dinâmica de para SMS da Movable Ink, você tem acesso à imersão do MMS pelo custo do SMS. Isso permite usar a Braze e a Movable Ink para oferecer experiências de mensagens ricas, personalizadas e econômicas.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para usar a parceria. |
| Fonte de dados | Você precisa conectar uma fonte de dados ao Movable Ink. Isso pode ser feito por CSV, importação do site ou API. |
| Recursos de envio de MMS | Confirme que você está configurado para MMS por meio do Braze.
| [Encurtamento de links]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) | Confirme se o encurtamento de links está ativado. | 
| Cartão de contato | Sua marca (o remetente) deve ser salva como um contato no telefone do usuário para que a prévia do link funcione no iOS. Isso pode ser feito com um cartão de contato ou outro método. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Siga as respectivas etapas abaixo para enviar links dinâmicos de SMS para os sistemas operacionais iOS e Android.

### iOS

{% alert important %}
Para permitir imagens prévias de links para iOS, os usuários devem adicionar sua marca (o remetente) como um contato.
{% endalert %}

#### Etapa 1: Crie uma campanha de cartões de contato

Depois que os usuários salvarem a sua marca como um contato, seja por meio de um [cartão de contato]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) ou outro método, eles poderão ver os prompts **Tap to Load Preview** e os links do Movable Ink.

![1]{: style="max-width:30%;"}

#### Etapa 2: enviar links da Movable Ink

1. Crie uma campanha de SMS na Movable Ink e gere seu URL de cliques.
2. No dashboard do Braze, acesse **Campaigns (Campanhas** ) e configure uma nova campanha de SMS/MMS no menu suspenso **Create Campaign (Criar campanha** ).
3. No criador da campanha de SMS:
    - Defina o grupo de inscrições.
    - Digite sua mensagem.
    - Adicione o link da Movable Ink **por último**, depois de todos os outros textos no corpo da mensagem. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
Dê uma olhada no [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para saber mais sobre a personalização Liquid.  
{% endalert %}

{: start="4"}
4\. Você está pronto para testar e lançar sua campanha de prévia de links dinâmicos de SMS.

![3]{: style="max-width:70%;"}

Depois que os usuários carregarem a prévia do link, uma imagem personalizada será renderizada com a capacidade de criar um link para o seu site, app ou landing page.

![4]{: style="max-width:30%;"}

### Android (dispositivos Google e Samsung)

Os usuários do Android não precisam salvar sua marca como um contato para receber prévias de links dinâmicos de SMS. No entanto, isso ainda é recomendado para que o dispositivo possa carregar automaticamente as prévias dos links.

![5]{: style="max-width:30%;"}

Os usuários que não salvaram a sua marca como um contato e ativaram as prévias automáticas terão que selecionar **Toque para carregar a prévia** para carregar a imagem da prévia.

![6]{: style="max-width:30%;"}

## Considerações

- Inclua apenas um link de prévia em sua mensagem. O conteúdo não será gerado com vários links no corpo do SMS. 
- Não inclua nenhum caractere após o link da prévia ou a experiência poderá ser interrompida.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}
