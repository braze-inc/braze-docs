---
nav_title: Usuários de envio de mensagens
article_title: Envio de mensagens aos usuários do LINE
page_order: 2
description: "Este artigo de referência aborda como conversar com os usuários usando modelos de campanhas e Canvas."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Envio de mensagens aos usuários do LINE

> O LINE é um canal de comunicação bidirecional. É possível ir além do envio de mensagens aos usuários e se engajar em conversas com eles usando campanhas de modelos e Canvas. Este artigo cobre os detalhes do envio de mensagens para os usuários, como definir palavras disparadoras para mensagens recebidas e respostas não reconhecidas.

Há vários métodos para conversar com os usuários pelo LINE, como o uso de palavras disparadoras do LINE. Também é possível usar chamadas para ação (CTAs) para incentivar o engajamento do usuário com o envio de mensagens LINE.

## Gatilhos baseados em ações

É possível criar campanhas e Canvas que iniciam, ramificam e têm alterações no meio do caminho quando você recebe uma mensagem LINE de entrada (uma mensagem enviada por um usuário) que contém uma palavra disparadora. Certifique-se de escolher palavras disparadoras que correspondam ao que você espera que os usuários enviem.

### Campanha interrompida

Defina suas palavras de disparo ao programar uma campanha de entrega baseada em ação.

![Disparador baseado em ação de "Enviar esta campanha para usuários que enviaram LINE de entrada para o grupo de inscrições onde o corpo da mensagem é" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canva

Defina suas palavras-gatilho em [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) em seu Canva.

![Caminho de ação com um disparador de "Enviar esta campanha para usuários que enviaram LINE de entrada para o grupo de inscrições onde o corpo da mensagem é" e um campo em branco.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Solicitações

Cada letra de sua palavra de disparo deve ser maiúscula ao criar sua campanha ou canva, embora a Braze não exija que as palavras de disparo de entrada sejam maiúsculas. Por exemplo, se sua palavra de acionamento for "JOIN2023", uma mensagem de entrada "jOin2023" ainda disparará o Canva ou a campanha.

Se nenhuma palavra disparadora for especificada, a campanha ou o Canva será executado para *todas as* mensagens LINE recebidas. Isso inclui mensagens com frases correspondentes em campanhas ativas e Canvas, caso em que o usuário receberá duas mensagens LINE.

## Respostas não reconhecidas

Você deve incluir uma opção de disparo para respostas não reconhecidas em telas interativas. Isso informa os usuários sobre os prompts disponíveis (ou palavras disparadoras) e define suas expectativas em relação ao canal.

### Criação de um disparador para respostas não reconhecidas

Depois de criar grupos de ação para as frases de filtro personalizadas, adicione outro grupo de ação à jornada de ação para **Enviar mensagem LINE** e não verifique **Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas do usuário, semelhante a uma cláusula "else".

Para essa mensagem, você deve enviar uma mensagem LINE informando ao usuário que esse canal não é monitorado por um humano e, se necessário, orientá-lo para um canal de suporte.

