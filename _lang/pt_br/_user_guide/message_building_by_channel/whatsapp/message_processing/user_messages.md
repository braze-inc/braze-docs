---
nav_title: Usuários de envio de mensagens
article_title: Usuários de envio de mensagens
description: "Este artigo de referência aborda como o Braze tratará as mensagens dos usuários."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# Envio de mensagens do usuário

> O WhatsApp é um canal de comunicação bidirecional. Sua marca não só pode enviar mensagens aos usuários, mas eles também podem se engajar em conversas usando campanhas de modelos e Canvas. Há várias maneiras de fazer isso, incluindo as respostas rápidas do WhatsApp e as palavras disparadoras. As chamadas para ação (CTAs) de resposta rápida são uma ótima maneira de incentivar o engajamento do usuário com suas mensagens do WhatsApp.

## Gatilhos baseados em ações 

Tanto as campanhas quanto as telas podem começar, ramificar e sofrer alterações no meio do caminho a partir de uma mensagem de entrada do WhatsApp (um usuário enviando mensagens para o seu WhatsApp), como uma palavra disparadora. 

Certifique-se de que a palavra disparadora corresponda ao que você espera dos usuários.

**O que você deve saber:**
- Cada letra de sua palavra disparadora deve estar em letra maiúscula quando configurada. A Braze não exige que as palavras disparadas enviadas pelos usuários sejam em letras maiúsculas. Por exemplo, o envio de mensagens "jOin2023" ainda disparará o Canva ou a campanha.
- Se nenhuma palavra do acionador for especificada no acionador baseado em ação da agenda de entrada, a campanha ou o Canva será executado para TODAS as mensagens recebidas do WhatsApp. Isso inclui mensagens que tenham frases correspondentes em campanhas ativas e Canvas, caso em que o usuário receberá duas mensagens do WhatsApp.

{% tabs %}
{% tab Campanha %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## Respostas não reconhecidas

Recomendamos que você inclua uma opção para respostas não reconhecidas nas telas interativas. Isso orienta os usuários a entender quais são os prompts disponíveis e define as expectativas para o canal. O gerenciamento de expectativas pode ser especialmente útil se você tiver canais do WhatsApp com bate-papo de agente ao vivo. 
- Na etapa de ação, depois de criar os grupos de ação para as frases de filtro personalizadas, adicione um grupo de ação adicional para "Enviar mensagem do WhatsApp", mas **não verifique Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas do usuário, semelhante a uma cláusula "else". 
- Recomendamos o envio de uma mensagem pelo WhatsApp informando ao usuário que esse canal não tem pessoal e orientando-o para um canal de suporte, se necessário. 

## Respostas rápidas 

![A tela do telefone que mostra um botão de chamada para ação responderá o texto do botão clicado.][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

As respostas rápidas aparecem como opções de botões clicáveis na conversa, mas agem como se o usuário tivesse respondido com texto. Em seguida, o Braze processa essas mensagens como mensagens de entrada e pode enviar respostas definidas com base no botão clicado. Use a etapa "Ação de mensagem de entrada do WhatsApp" ao criar e filtrar respostas de seus usuários.

![Uma mensagem do WhatsApp com texto e três botões de chamada para ação.][13]{: style="max-width:50%;"}

### Configure as experiências de resposta rápida no Canva

#### Etapa 1: Crie CTAs

Primeiro, crie suas CTAs de resposta rápida no [Gerenciador de modelos de mensagens do WhatsApp](https://business.facebook.com/wa/manage/message-templates/) em um modelo de mensagem. 

![A interface do usuário do gerenciador de modelos de mensagens do WhatsApp mostra como criar um botão de CTA, fornecendo o tipo de botão (personalizado) e o texto do botão.][12]{: style="max-width:80%;"}

Depois que seu modelo for enviado e aprovado pelo WhatsApp, você poderá usá-lo para criar um canva na Braze. 

{% alert tip %}
Você pode criar o Canva antes de receber a aprovação em seu modelo de mensagem.
{% endalert %}

#### Etapa 2: Crie seu canva

Em seguida, crie um canva com uma etapa de mensagens que inclua o modelo criado. 

![][14]

Crie uma etapa de ação que siga a etapa da mensagem. Crie um grupo por opção de resposta rápida nessa etapa da ação.

![Uma tela em que a ação de avaliação é "enviar uma mensagem de entrada do whatsapp".][15]

Para cada grupo de opções de resposta rápida, especifique o texto exato como o botão que está correspondendo. Note que as palavras-chave devem estar em letras maiúsculas. 

![Uma etapa do Canva em que a ação "enviar uma mensagem de entrada do Whatsapp" é definida para ser enviada quando um corpo de mensagem específico é recebido.][16]

Se quiser uma resposta padrão para os usuários que responderem à mensagem com texto em vez de respostas rápidas, crie um grupo adicional sem corpo de mensagem correspondente.

Continue construindo o canva como faria de outra forma deste ponto em diante.

### Respostas

Provavelmente, você desejará uma mensagem de resposta para cada resposta. Recomendamos ter uma opção abrangente para respostas fora dos limites das respostas rápidas (por exemplo, para clientes que respondem com uma mensagem geral em vez de uma solicitação predeterminada). Por exemplo, "Desculpe-nos, mas não reconhecemos sua resposta. Para questões de suporte, envie uma mensagem para <support channel>."

![Foi criada uma tela mostrando as respostas para cada botão de call-to-action.][18]

Note que você pode usar quaisquer ações subsequentes que o Braze Canvas oferece, como mensagens em resposta, atualizações de perfil de usuário ou webhooks Braze-to-Braze. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %}
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %}
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %}
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %}
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
