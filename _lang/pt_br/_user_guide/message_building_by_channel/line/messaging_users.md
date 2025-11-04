---
nav_title: Usuários de mensagens
article_title: Mensagens para usuários do LINE
page_order: 2
description: "Este artigo de referência aborda como conversar com os usuários usando modelos de campanhas e Canvases."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Mensagens para usuários do LINE

> O LINE é um canal de comunicação bidirecional. Você pode ir além do envio de mensagens aos usuários e participar de conversas com eles usando modelos de campanhas e Canvases. Este artigo aborda os detalhes do envio de mensagens aos usuários, por exemplo, como definir palavras de acionamento para mensagens recebidas e respostas não reconhecidas.

Há vários métodos para conversar com os usuários por meio do LINE, como o uso de palavras de acionamento do LINE. Você também pode usar chamadas para ação (CTAs) para incentivar o envolvimento do usuário com as mensagens do LINE.

## Gatilhos baseados em ações

Você pode criar campanhas e Canvases que iniciam, ramificam e têm alterações no meio do caminho quando você recebe uma mensagem LINE de entrada (uma mensagem enviada por um usuário) que contém uma palavra de gatilho. Certifique-se de escolher palavras de gatilho que correspondam ao que você espera que os usuários enviem.

### Campanha

Defina suas palavras de gatilho ao programar uma campanha de entrega baseada em ação.

Gatilho baseado em ação de "Enviar esta campanha aos usuários que enviaram LINE de entrada para o grupo de assinatura onde está o corpo da mensagem" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Tela

Defina suas palavras-gatilho dentro de [caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) em seu Canvas.

Caminho de ação com um acionador de "Enviar esta campanha aos usuários que enviaram LINE de entrada para o grupo de assinatura onde está o corpo da mensagem" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Requisitos

Cada letra de sua palavra de gatilho deve ser maiúscula ao criar sua campanha ou Canvas, embora o Braze não exija que as palavras de gatilho de entrada sejam maiúsculas. Por exemplo, se sua palavra de acionamento for "JOIN2023", uma mensagem de entrada "jOin2023" ainda acionará o Canvas ou a campanha.

Se nenhuma palavra de acionamento for especificada, a campanha ou o Canvas será executado para *todas as* mensagens LINE recebidas. Isso inclui mensagens com frases correspondentes em campanhas ativas e Canvases, caso em que o usuário receberá duas mensagens LINE.

## Respostas não reconhecidas

Você deve incluir uma opção de acionamento para respostas não reconhecidas em telas interativas. Isso informa os usuários sobre os prompts disponíveis (ou palavras de gatilho) e define suas expectativas em relação ao canal.

### Criação de um acionador para respostas não reconhecidas

Depois de criar grupos de ação para as frases de filtro personalizadas, adicione outro grupo de ação ao caminho de ação para **Enviar mensagem LINE** e não verifique **Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas do usuário, semelhante a uma cláusula "else".

Para essa mensagem, você deve enviar uma mensagem LINE informando ao usuário que esse canal não é monitorado por um ser humano e, se necessário, orientá-lo para um canal de suporte.

