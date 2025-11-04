---
nav_title: Mensagens para usuários
article_title: Mensagens para Usuários
description: "Este artigo de referência cobre como a Braze lidará com mensagens de usuários."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Mensagens de usuários

> O WhatsApp é um canal de comunicação bidirecional. Não apenas sua marca pode enviar mensagens para os usuários, mas eles também podem participar de conversas usando campanhas e Canvases modelados. Existem várias maneiras de fazer isso, incluindo respostas rápidas do WhatsApp, mensagens de lista e palavras-chave. Respostas rápidas e mensagens de lista com chamadas para ação (CTAs) são uma ótima maneira de incentivar o engajamento dos usuários com suas mensagens no WhatsApp.

## Gatilhos baseados em ação 

Tanto campanhas quanto Canvases podem iniciar, ramificar e ter mudanças no meio da jornada a partir de uma mensagem recebida do WhatsApp (um usuário enviando uma mensagem para o seu WhatsApp), como uma palavra-chave. 

Certifique-se de que sua palavra-chave corresponda ao que você espera dos usuários.

**Coisas a saber:**
- Cada letra da sua palavra-chave deve ser capitalizada quando configurada. A Braze não exige que as palavras-chave recebidas enviadas pelos usuários sejam capitalizadas. Por exemplo, enviar "jOin2023" ainda acionará o Canvas ou a campanha.
- Se nenhuma palavra-chave for especificada na ação de agendamento de entrada baseada em gatilho, a campanha ou Canvas será executada para TODAS as mensagens recebidas do WhatsApp. Isso inclui mensagens que corresponderam a frases em campanhas e Canvases ativas, caso em que o usuário receberá duas mensagens do WhatsApp.

{% tabs %}
{% tab Campaign %}

\![Opções de agendamento de campanha baseada em ação.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

\![Opções de agendamento baseadas em ação.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Respostas não reconhecidas

Recomendamos que você inclua uma opção para respostas não reconhecidas em Canvases interativos. Isso orienta os usuários a entender quais são os prompts disponíveis e define expectativas para o canal. O gerenciamento de expectativas pode ser especialmente útil se você tiver canais do WhatsApp com chat de agente ao vivo. 
- Na etapa de ação, após criar os grupos de ação para as frases de filtro personalizadas, adicione um grupo de ação adicional para "Enviar mensagem pelo WhatsApp", mas **não marque Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas dos usuários, semelhante a uma cláusula "else". 
- Recomendamos que você siga com uma mensagem pelo WhatsApp informando ao usuário que este canal não está atendido e orientando-o para um canal de suporte, se necessário. 

## Respostas rápidas 

\![Tela do telefone mostrando um botão de chamada à ação que responderá ao texto do botão clicado.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

As respostas rápidas aparecem como opções de botão clicáveis dentro da conversa, mas agem como se um usuário tivesse respondido com texto. O Braze então processa essas como mensagens recebidas e pode enviar de volta respostas definidas com base no botão clicado. Use a etapa "Ação de mensagem recebida pelo WhatsApp" ao criar e filtrar respostas de seus usuários.

\![Uma mensagem do WhatsApp mostrando texto e três botões de chamada à ação.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configure a experiência de resposta rápida no Canvas

#### Passo 1: Crie CTAs

Primeiro, crie seus CTAs de Resposta Rápida no [Gerenciador de Modelos de Mensagem do WhatsApp](https://business.facebook.com/wa/manage/message-templates/) dentro de um modelo de mensagem. 

\![A interface do gerenciador de modelos de mensagem do WhatsApp mostrando como criar um botão CTA, fornecendo o tipo de botão (personalizado) e o texto do botão.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Uma vez que seu modelo tenha sido enviado e aprovado pelo WhatsApp, você pode usá-lo para construir um Canvas dentro do Braze. 

{% alert tip %}
Você pode construir o Canvas antes de receber a aprovação do seu modelo de mensagem.
{% endalert %}

#### Passo 2: Construa seu Canvas

Em seguida, construa um Canvas com um passo de mensagem que inclua seu modelo criado. 

\![Compositor de mensagem do passo WhatsApp com um modelo de resposta rápida preenchido.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Crie um passo de ação que siga o passo de mensagem. Crie um grupo por opção de resposta rápida neste passo de ação.

\![Um Canvas onde a ação de avaliação é "enviar uma mensagem recebida do whatsapp".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Para cada grupo de opção de resposta rápida, especifique o texto exato como o botão que você está correspondendo. Observe que as palavras-chave devem estar em maiúsculas. 

\![Um passo de Canvas onde a ação "enviar uma mensagem recebida do whatsapp" é configurada para enviar quando um corpo de mensagem específico é recebido.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Se você quiser uma resposta padrão para usuários que respondem à mensagem com texto em vez de respostas rápidas, crie um grupo adicional sem corpo de mensagem correspondente.

Continue construindo o Canvas como você faria normalmente a partir deste ponto em diante.

### Respostas

Você provavelmente vai querer uma mensagem de resposta para cada resposta. Recomendamos ter uma opção de captura para respostas fora dos limites das respostas rápidas (como para clientes que respondem com uma mensagem geral em vez de um prompt pré-determinado). Por exemplo, "Desculpe, não reconhecemos sua resposta. Para questões de suporte, por favor, envie uma mensagem para <support channel>."

\![Um Canvas construído mostrando as respostas para cada botão de chamada à ação.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Observe que você pode usar quaisquer ações subsequentes que o Canvas Braze oferece, como mensagens em resposta, atualizações de perfil de usuário ou webhooks Braze-to-Braze. 

## Listar mensagens

As mensagens da lista aparecem como uma mensagem de corpo com uma lista de opções clicáveis. Cada lista pode ter várias seções, e cada lista pode ter até 10 linhas.

\![Exemplo de uma mensagem de lista do WhatsApp com linhas para diferentes estilos de moda.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configure a experiência da mensagem de lista no Canvas

#### Passo 1: Crie ou edite um Canvas baseado em ações existente

Você só pode adicionar mensagens de lista do WhatsApp a Canvases que são baseados em ações, pois precisam ser em resposta a uma mensagem do usuário.

#### Passo 2: Crie um passo de Mensagem do WhatsApp

Adicione um passo de [Mensagem do WhatsApp]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), e então selecione o layout da mensagem de resposta de **Mensagem de Lista**.

\![Uma coleção selecionável dos diferentes tipos de mensagens de resposta do WhatsApp que você pode criar, incluindo "Mensagem de Lista".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Adicione um nome de **Botão de lista** que os usuários selecionarão para exibir sua lista. Em seguida, use os campos em **Conteúdo da lista** para criar sua lista:

- **Seção:** Adicione até 10 seções para agrupar e organizar seus itens de lista. Por exemplo, um varejista de roupas poderia usar seções para organizar por estilos sazonais (como primavera, verão, outono e inverno) ou itens de vestuário (como blusas, calças e sapatos).
- **Linha:** Adicione até 10 linhas, ou itens de lista, em todas as seções.
- **Descrição da linha (opcional):** Adicione uma descrição opcional a todas as linhas (itens de lista).

\![A seção "Conteúdo da lista" preenchida com duas seções, e várias linhas e descrições de linha.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Altere a ordem das seções e linhas selecionando e arrastando o ícone ao lado de seus nomes.

\![Arrastando uma seção de lista para um novo local.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De volta ao compositor do Canvas, adicione um [Caminho de Ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) após a etapa Mensagem que possui um grupo para cada resposta da lista. Em cada grupo:

1. Adicione um gatilho para **Grupo de assinatura do WhatsApp recebido** e selecione o respectivo grupo de assinatura do WhatsApp.
2. Marque a caixa **Onde o corpo da mensagem**.
3. Especifique o conteúdo para uma linha (ou item da lista).

\![Compositor para um caminho de Ação com grupos para diferentes estilos de roupas.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continue a construir seu Canvas.

### Criando caminhos de ação para descrições longas

Se você tiver descrições de linha, deve usar **Corresponde a regex** para especificar uma linha. Por exemplo, se você quiser especificar uma linha com a descrição, "Nosso novo estilo que se encaixa sobre seu par favorito de botas de tornozelo", você pode usar [regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) com "botas de tornozelo".

\![Um gatilho do WhatsApp usando o filtro para "Corresponde a regex" para capturar mensagens de resposta com "botas de tornozelo".]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Considerações para mensagens de resposta

As mensagens de resposta precisam ser enviadas dentro de 24 horas após receber a mensagem de um usuário. Para ajudar a construir experiências bem-sucedidas, a Braze verifica a lógica da mensagem para confirmar que há uma mensagem de usuário recebida a montante que desbloqueia a mensagem de resposta. 

Os seguintes eventos desbloqueiam mensagens de resposta: 

- Mensagem recebida 
  - [Caminho de Ação]({{site.baseurl}}/action_paths/) ou [entrada baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) com o gatilho **Enviar uma mensagem recebida do WhatsApp**.

\![Uma etapa de entrada baseada em ação com o gatilho "Enviar uma mensagem recebida do WhatsApp".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrada acionada pela API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Mensagem de produto de entrada 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) evento

\![Um Caminho de Ação com o gatilho de um evento personalizado realizado `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

