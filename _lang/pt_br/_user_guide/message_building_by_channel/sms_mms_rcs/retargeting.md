---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens pelas interações de SMS e RCS de um usuário."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Redirecionamento de usuários

> Além de alterar o estado da inscrição do usuário e enviar respostas automáticas com base nas palavras-chave recebidas, o Braze também registrará as interações com o perfil do usuário para filtrar e disparar mensagens.<br><br>Esses filtros e disparos permitem filtrar ações com base nos usuários que receberam ou responderam a campanhas de SMS, MMS e RCS, ou engajar ainda mais os usuários que clicaram em URLs encurtados.

{% alert tip %}
Para saber mais sobre palavras-chave personalizadas e como configurar o envio de mensagens bidirecionais para aproveitar essas opções de redirecionamento, visite nosso artigo sobre [palavras-chave personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/).
{% endalert %}  

## Opções de redirecionamento

{% alert note %}
Ao criar públicos com redirecionamento de usuários, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a CUP. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canva e/ou da campanha.
{% endalert %}

### Filtre usuários por SMS, MMS e RCS

Os usuários podem ser filtrados pela última vez que receberam um SMS, MMS ou RCS ou se receberam um SMS, MMS ou RCS de uma campanha específica. Os filtros podem ser definidos na etapa de **públicos-alvo** do construtor de campanhas. 

**Filtrar por último recebido SMS/MMS/RCS**<br>
![Filtro de segmentação Último SMS recebido após 8 de dezembro de 2020.]({% image_buster /assets/img/sms/filter2.png %})

**Filtrar por mensagens recebidas da campanha SMS/MMS/RCS **<br>
Filtra os usuários que receberam uma mensagem de uma campanha específica. Com esse filtro, você também tem a opção de filtrar as pessoas que não receberam mensagens de uma campanha. <br>
![Filtro de segmentação Recebeu mensagem da campanha "SMS redirecionamento".]({% image_buster /assets/img/sms/filter1.png %})

### Disparar mensagens à medida que os usuários recebem SMS, MMS ou RCS {#trigger-messages}

Para disparar mensagens à medida que os usuários recebem mensagens SMS, MMS ou RCS de uma campanha específica, selecione **Interagir com a campanha** como a ação-gatilho para uma campanha baseada em ação. Em seguida, selecione **Receber SMS** e a campanha de SMS, MMS ou RCS que você gostaria de usar.

![]({% image_buster /assets/img/sms/trigger.png %})

### Filtrar por links de rastreamento avançado

Redirecione os usuários que clicaram em campanhas com [links de rastreamento avançados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).
Somente as campanhas que tiverem o rastreamento avançado ativado aparecerão nos seguintes menus suspensos:

**Redirecione os usuários que clicaram em uma campanha específica de SMS, MMS ou RCS**
1. Crie um segmento usando o filtro **Clicked/Opened Campaign (Campanha clicada/aberta** ).
2. Selecione **o link de sms encurtado clicado**.
3. Escolha a campanha desejada.

![]({% image_buster /assets/img/sms/retargeting5.png %})

**Redirecione os usuários que clicaram em uma etapa específica do Canva**
1. Crie um segmento usando o filtro **Etapa clicada/aberta**.
2. Selecione **o link de sms encurtado clicado**.
3. Escolha o canva e a etapa do canva desejados.

![]({% image_buster /assets/img/keyword_example1.jpg %})

## Redirecionamento específico por categoria de palavra-chave

Além das três categorias de palavras-chave padrão (Aceitação, Desaceitação e Ajuda), também é possível criar até 25 categorias de palavras-chave próprias, o que permite identificar palavras-chave e respostas arbitrárias. Essas categorias podem ser usadas para filtragem e redirecionamento. Para saber mais sobre as categorias de palavras-chave globais e como configurá-las, consulte [Processamento de palavras-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/). 

### Filtrar por recência

Filtre a recência de um usuário que responde ao seu programa de SMS, MMS ou RCS. Esse filtro avaliará a última data em que um usuário enviou uma mensagem de entrada que esteja dentro de uma das categorias de palavras-chave. 

![Filtro de segmentação Último SMS enviado ao grupo de inscrições "Marketing por SMS" com a palavra-chave "Aceitação" após 11 de agosto de 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrar por campanha ou atribuição do Canva

Filtre os usuários que responderam a uma campanha específica de SMS, MMS ou RCS ou a um componente do Canva, categoria de palavra-chave ou tag.

**Filtrar por respostas a uma campanha específica com categoria de palavra-chave**<br>
![Campanha com o filtro "Has replied to SMS" para a campanha "SMS-283" "Promotion". No filtro, o recurso menciona "Este filtro expirará 25 meses após o envio da última mensagem da "Promoção" se não estiver sendo usado em nenhuma campanha ativa."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**Filtrar por respostas a uma campanha ou canvas com uma tag específica**
![Campanha com o filtro "Has replied to SMS" para campanha ou Canvas com a tag "Curbside Messaging Service C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**Filtrar por resposta a uma etapa específica**
![Campanha com o filtro "Has replied to SMS" para a etapa "SMS Double Opt" "Step - Help".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Envio de mensagens por palavra-chave

As mensagens podem ser disparadas à medida que os usuários enviam mensagens de entrada com base em categorias de palavras-chave (o usuário enviou qualquer uma das palavras-chave) ou outras palavras-chave (o usuário enviou uma palavra-chave que não se enquadra em uma das categorias existentes). Esses disparos são definidos na etapa Entrega do criador de campanhas.

Ao avaliar se uma mensagem de entrada atende a um evento de gatilho definido, os espaços à esquerda e à direita são removidos antes do início da avaliação.

{% alert tip %}
Se um Canvas baseado em ação for disparado por uma mensagem SMS ou MMS recebida, você poderá fazer referência às [propriedades do SMS Liquid suportadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) em qualquer etapa do Canva até a próxima jornada de ação.
{% endalert %}

**Disparar por categoria de palavra-chave de entrada**<br>
![Campanha de SMS baseada em ações com o filtro de segmentação Enviou a palavra-chave "Aceitação" para o grupo de inscrições "Marketing por SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**Disparar por palavras-chave arbitrárias**<br>
Note que, ao disparar uma mensagem em uma resposta de palavra-chave "Outra", você terá a oportunidade de avaliar o corpo da palavra-chave em uma correspondência de texto exata. Essa correspondência segue as mesmas regras a seguir: Somente a **mensagem exata, de uma única palavra,** será processada ( _não diferencia maiúsculas_ de _minúsculas_). Uma palavra-chave enviada de `Hello Braze!` não corresponderia aos critérios mostrados no exemplo a seguir.
![Campanha de SMS baseada em ação com categoria de palavra-chave como "Outro", em que o corpo da mensagem é exatamente "Olá" ou "Ei".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**Palavras-chave do modelo**<br>
Ao disparar uma campanha ou um componente do Canvas em um SMS ou MMS de entrada, é possível modelar opcionalmente o texto ou os anexos de mídia que o usuário enviou para o corpo da campanha ou do Canvas com o Liquid. Isso o capacitará a acessar a resposta do usuário, que poderá ser incluída em sua resposta, aplicar lógica condicional ou qualquer outra coisa que possa ser feita com o Liquid. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
