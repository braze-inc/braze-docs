---
nav_title: Usuários de envio de mensagens
article_title: Usuários de mensagens
description: "Este artigo de referência aborda como o Braze tratará as mensagens dos usuários."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Envio de mensagens do usuário

> O WhatsApp é um canal de comunicação bidirecional. Sua marca não só pode enviar mensagens aos usuários, mas eles também podem se engajar em conversas usando campanhas de modelos e Canvas. Há várias maneiras de fazer isso, incluindo respostas rápidas do WhatsApp, mensagens em lista e palavras disparadoras. As chamadas para ação (CTAs) de resposta rápida e de lista de mensagens são uma ótima maneira de incentivar o engajamento do usuário com seu envio de mensagens do WhatsApp.

## Gatilhos baseados em ações 

Tanto as campanhas quanto as telas podem começar, ramificar e sofrer alterações no meio do caminho a partir de uma mensagem de entrada do WhatsApp (um usuário enviando mensagens para o seu WhatsApp), como uma palavra disparadora. 

Certifique-se de que a palavra disparadora corresponda ao que você espera dos usuários.

**O que você deve saber:**
- Cada letra de sua palavra disparadora deve estar em letra maiúscula quando configurada. A Braze não exige que as palavras disparadas enviadas pelos usuários sejam em letras maiúsculas. Por exemplo, o envio de mensagens "jOin2023" ainda disparará o Canva ou a campanha.
- Se nenhuma palavra do acionador for especificada no acionador baseado em ação da agenda de entrada, a campanha ou o Canva será executado para TODAS as mensagens recebidas do WhatsApp. Isso inclui mensagens que tenham frases correspondentes em campanhas ativas e Canvas, caso em que o usuário receberá duas mensagens do WhatsApp.

{% tabs %}
{% tab Campaign %}

![Opções de agendamento de campanhas baseadas em ações.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Opções de agendamento do Canva baseadas em ações.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Respostas não reconhecidas

Recomendamos que você inclua uma opção para respostas não reconhecidas nas telas interativas. Isso orienta os usuários a entender quais são os prompts disponíveis e define as expectativas para o canal. O gerenciamento de expectativas pode ser especialmente útil se você tiver canais do WhatsApp com bate-papo de agente ao vivo. 
- Na etapa de ação, depois de criar os grupos de ação para as frases de filtro personalizadas, adicione um grupo de ação adicional para "Enviar mensagem do WhatsApp", mas **não verifique Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas do usuário, semelhante a uma cláusula "else". 
- Recomendamos o envio de uma mensagem pelo WhatsApp informando ao usuário que esse canal não tem pessoal e orientando-o para um canal de suporte, se necessário. 

## Respostas rápidas 

![A tela do telefone que mostra um botão de chamada para ação responderá o texto do botão clicado.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

As respostas rápidas aparecem como opções de botões clicáveis na conversa, mas agem como se o usuário tivesse respondido com texto. Em seguida, o Braze processa essas mensagens como mensagens de entrada e pode enviar respostas definidas com base no botão clicado. Use a etapa "Ação de mensagem de entrada do WhatsApp" ao criar e filtrar respostas de seus usuários.

![Uma mensagem do WhatsApp com texto e três botões de chamada para ação.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configure a experiência de resposta rápida no Canva

#### Etapa 1: Crie CTAs

Primeiro, crie suas CTAs de resposta rápida no [Gerenciador de modelos de mensagens do WhatsApp](https://business.facebook.com/wa/manage/message-templates/) em um modelo de mensagem. 

![A interface do usuário do gerenciador de modelos de mensagens do WhatsApp mostra como criar um botão de CTA, fornecendo o tipo de botão (personalizado) e o texto do botão.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Depois que seu modelo for enviado e aprovado pelo WhatsApp, você poderá usá-lo para criar um canva na Braze. 

{% alert tip %}
Você pode criar o Canva antes de receber a aprovação em seu modelo de mensagem.
{% endalert %}

#### Etapa 2: Crie seu canva

Em seguida, crie um canva com uma etapa de mensagens que inclua o modelo criado. 

![Criador de mensagens por etapas do WhatsApp com um modelo de resposta rápida preenchido.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Crie uma etapa de ação que siga a etapa da mensagem. Crie um grupo por opção de resposta rápida nessa etapa da ação.

![Uma tela em que a ação de avaliação é "enviar uma mensagem de entrada do whatsapp".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Para cada grupo de opções de resposta rápida, especifique o texto exato como o botão que está correspondendo. Note que as palavras-chave devem estar em letras maiúsculas. 

![Uma etapa do Canva em que a ação "enviar uma mensagem de entrada do Whatsapp" é definida para ser enviada quando um corpo de mensagem específico é recebido.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Se quiser uma resposta padrão para os usuários que responderem à mensagem com texto em vez de respostas rápidas, crie um grupo adicional sem corpo de mensagem correspondente.

Continue construindo o canva como faria de outra forma deste ponto em diante.

### Respostas

Provavelmente, você desejará uma mensagem de resposta para cada resposta. Recomendamos ter uma opção abrangente para respostas fora dos limites das respostas rápidas (por exemplo, para clientes que respondem com uma mensagem geral em vez de uma solicitação predeterminada). Por exemplo, "Desculpe-nos, mas não reconhecemos sua resposta. Para questões de suporte, envie uma mensagem para <support channel>."

![Foi criada uma tela mostrando as respostas para cada botão de call-to-action.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Note que você pode usar quaisquer ações subsequentes que o Braze Canvas oferece, como mensagens em resposta, atualizações de perfil de usuário ou webhooks Braze-to-Braze. 

## Envio de mensagens

As mensagens de lista aparecem como um corpo de mensagem com uma lista de opções clicáveis. Cada lista pode ter várias seções, e cada lista pode ter até 10 linhas.

![Exemplo de uma mensagem de lista do WhatsApp com linhas para diferentes estilos de moda.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configurar a experiência de mensagens da lista no Canva

#### Etapa 1: Crie ou edite uma tela baseada em ação existente

Só é possível adicionar mensagens da lista do WhatsApp a Canvas que sejam baseadas em ações, pois elas precisam ser uma resposta a uma mensagem do usuário.

#### Etapa 2: Criar uma etapa de envio de mensagens do WhatsApp

[Etapa]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) Adicionar uma [mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) do WhatsApp e, em seguida, selecione o layout da mensagem de resposta de **List Message**.

![Uma coleção selecionável dos diferentes tipos de mensagens de resposta do WhatsApp que você pode criar, incluindo "Mensagem de lista".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Adicione um nome de **botão de lista** que os usuários selecionarão para exibir sua lista. Em seguida, use os campos no **conteúdo da lista** para criar sua lista:

- **Seção:** Adicione até 10 seções para agrupar e organizar os itens da lista. Por exemplo, um varejista de roupas pode usar seções para organizar por estilos sazonais (como primavera, verão, outono e inverno) ou itens de vestuário (como blusas, calças e sapatos).
- **Fila:** Adicione até 10 linhas, ou itens de lista, em todas as seções.
- **Descrição da linha (opcional):** Adicione uma descrição opcional a todas as linhas (itens de lista).

![A seção "List content" foi preenchida com duas seções e várias linhas e descrições de linhas.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Altere a ordem das seções e linhas selecionando e arrastando o ícone ao lado de seus nomes.

![Arrastar uma seção da lista para um novo local.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De volta ao criador do Canvas, adicione uma [jornada de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) após a etapa de mensagem que tenha um grupo para cada resposta de lista. Em cada grupo:

1. Adicione um disparo para o **grupo de inscrições do WhatsApp de entrada enviado** e selecione o respectivo grupo de inscrições do WhatsApp.
2. Marque a caixa de seleção **Onde o corpo da mensagem**.
3. Especifique o conteúdo de uma linha (ou item de lista).

![Criador de uma jornada de ação com grupos para diferentes estilos de roupas.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continue a desenvolver seu Canva.

### Criação de jornadas de ação para descrições longas

Se você tiver descrições de linhas, deverá usar o **regex Matches** para especificar uma linha. Por exemplo, se você quiser especificar uma linha com a descrição "Nosso novo estilo que se ajusta ao seu par favorito de botas de cano alto", poderá usar [regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) com "ankle boots".

![Um disparo do WhatsApp usando o filtro para "Matches regex" para capturar mensagens de resposta com "ankle boots".]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Considerações sobre o envio de mensagens de resposta

As mensagens de resposta precisam ser enviadas dentro de 24 horas após o recebimento da mensagem de um usuário. Para ajudar a criar experiências bem-sucedidas, o Braze verifica a lógica da mensagem para confirmar se há uma mensagem do usuário de entrada upstream que desbloqueie a mensagem de resposta. 

Os seguintes eventos desbloqueiam as mensagens de resposta: 

- Envio de mensagens 
  - [Jornada de ação]({{site.baseurl}}/action_paths/) ou [entrada baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) com o disparo **Enviar uma mensagem de entrada do WhatsApp**.

![Uma etapa de entrada baseada em ação com o disparo "Enviar uma mensagem de entrada do WhatsApp".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrada disparada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Envio de mensagens de entrada do produto 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) evento

![Uma jornada de ação com o disparo de um evento personalizado realizado `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

