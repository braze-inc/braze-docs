---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários por SMS
description: "Este artigo de referência aborda como os usuários podem redirecionar suas mensagens por meio de interações de SMS dos usuários."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# Redirecionamento de usuários

> Além de alterar o estado da inscrição do usuário e enviar respostas automáticas com base nas palavras-chave recebidas, o Braze também registrará as interações com o perfil do usuário para filtrar e disparar mensagens.<br><br>Esses filtros e disparadores permitem filtrar os usuários que receberam mensagens SMS, receberam mensagens SMS de uma campanha de mensagens específica e disparar mensagens à medida que os usuários recebem mensagens SMS de uma campanha de mensagens específica. 

{% alert tip %}
Para saber mais sobre palavras-chave personalizadas e como configurar o envio de mensagens bidirecionais para aproveitar essas opções de redirecionamento, visite nosso artigo sobre [palavras-chave personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}  

## Opções de redirecionamento

{% alert note %}
Ao criar públicos com redirecionamento de usuários, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a CUP. Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canva e/ou da campanha.
{% endalert %}

### Filtrar usuários por SMS

Os usuários podem ser filtrados por quando receberam um SMS pela última vez ou se receberam um SMS de uma campanha de SMS específica. Os filtros podem ser definidos na etapa Usuários-alvo do criador de campanhas. 

**Filtrar pelo último SMS recebido**<br>
![Filtro de segmentação Último SMS recebido após 8 de dezembro de 2020.][2]

**Filtrar por mensagens recebidas de uma campanha de SMS**<br>
Filtra os usuários que receberam uma mensagem de uma campanha específica de SMS. Com esse filtro, você também tem a opção de filtrar as pessoas que não receberam mensagens de uma campanha de mensagens SMS. <br>
![Filtro de segmentação Recebeu mensagem da campanha "SMS redirecionamento".][1]

### Envio de mensagens à medida que os usuários recebem SMS {#trigger-messages}

Para disparar mensagens à medida que os usuários recebem mensagens SMS de uma campanha específica, selecione **Interagir com a campanha** como a ação-gatilho para uma campanha baseada em ação. Em seguida, selecione **Receive SMS (Receber SMS)** e a campanha de SMS que você gostaria de usar.

![][3]

### Filtrar por links de rastreamento avançado

Redirecione os usuários que clicaram em campanhas com [links de rastreamento avançados]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).
Somente as campanhas que tiverem o rastreamento avançado ativado aparecerão nos seguintes menus suspensos:

**Redirecionamento de usuários que clicaram em uma campanha de SMS específica**
1. Crie um segmento usando o filtro **Clicked/Opened Campaign (Campanha clicada/aberta** ).
2. Selecione o **sms clicado**.
3. Escolha a campanha desejada.

![][15]

**Redirecione os usuários que clicaram em uma etapa específica do Canva**
1. Crie um segmento usando o filtro **Etapa clicada/aberta**.
2. Selecione o **sms clicado**.
3. Escolha o canva e a etapa do canva desejados.

![][16]

## Redirecionamento específico por categoria de palavra-chave

Além das três categorias de palavras-chave padrão (Aceitação, Desaceitação e Ajuda), também é possível criar até 25 categorias de palavras-chave próprias, o que permite identificar palavras-chave e respostas arbitrárias. Essas categorias podem ser usadas para filtragem e redirecionamento. Para saber mais sobre as categorias de palavras-chave de SMS e como configurá-las, consulte [Redirecionamento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Filtrar por recência

Filtre a frequência com que um usuário responde ao seu programa de SMS. Esse filtro avaliará a última data em que um usuário enviou um SMS de entrada que esteja dentro de uma das categorias de palavras-chave. 

![Filtro de segmentação Último SMS enviado ao grupo de inscrições "Marketing por SMS" com a palavra-chave "Aceitação" após 11 de agosto de 2020.][6]

### Filtrar por campanha ou atribuição do Canva

Filtre os usuários que responderam a uma campanha de SMS específica ou a um componente do Canva, categoria de palavra-chave ou tag.

**Filtrar por respostas a uma categoria de campanha específica**<br>
![Campanha com o filtro "Has replied to SMS" para a campanha "SMS-283" "Promotion". No filtro, o recurso menciona "Este filtro expirará 25 meses após o envio da última mensagem da "Promoção" se não estiver sendo usado em nenhuma campanha ativa".][12]

**Filtrar por respostas a uma campanha ou canvas com uma tag específica**
![Campanha com o filtro "Has replied to SMS" para campanha ou Canva com a tag "Curbside Messaging Service C".][13]

**Filtrar por resposta a uma etapa específica**
![Campanha com o filtro "Respondeu o SMS" para a etapa "Aceitação dupla de SMS" "Etapa – Ajuda".][11]

### Envio de mensagens por palavra-chave

As mensagens podem ser disparadas à medida que os usuários enviam mensagens de entrada com base em categorias de palavras-chave (o usuário enviou qualquer uma das palavras-chave) ou outras palavras-chave (o usuário enviou uma palavra-chave que não se enquadra em uma das categorias existentes). Esses disparos são definidos na etapa Entrega do criador de campanhas.

Ao avaliar se uma mensagem de entrada atende a um evento de gatilho definido, os espaços à esquerda e à direita são removidos antes do início da avaliação.

{% alert tip %}
Se um Canvas baseado em ação for disparado por uma mensagem SMS recebida, você poderá fazer referência às propriedades do SMS em qualquer etapa do Canva até a próxima jornada de ação.
{% endalert %}

**Disparar por categoria de palavra-chave de entrada**<br>
![Campanha de SMS baseada em ações com o filtro de segmentação Palavra-chave enviada "Aceitação" para o grupo de inscrições "Marketing por SMS".][7]{: style="margin-top:10px;"}

**Disparar por palavras-chave arbitrárias**<br>
Note que, ao disparar uma mensagem em uma resposta de palavra-chave "Outra", você terá a oportunidade de avaliar o corpo da palavra-chave em uma correspondência de texto exata. Essa correspondência segue as mesmas regras a seguir: Somente a **mensagem exata, de uma única palavra,** será processada ( _não diferencia maiúsculas_ de _minúsculas_). Uma palavra-chave enviada de `Hello Braze!` não corresponderia aos critérios mostrados no exemplo a seguir.
![Campanha de mensagens SMS baseada em ações com categoria de palavra-chave como "Outros", em que o corpo da mensagem é exatamente "Olá" ou "Ei".][8]{: style="margin-top:10px;"}

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

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %}
[15]: {% image_buster /assets/img/sms/retargeting5.png %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
