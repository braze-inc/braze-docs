---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários por meio de uma página de destino
description: "Saiba como redirecionar os usuários que enviaram um formulário por meio de uma página de destino."
page_order: 3
---

# Redirecionamento de usuários por meio de uma página de destino

> Saiba como redirecionar os usuários que enviaram um formulário por meio de uma página de destino, criando um segmento dedicado ou acionando uma mensagem quando o formulário é enviado.

## Pré-requisitos

Antes de começar, você precisará criar uma [página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Redirecionamento de usuários

O Braze rastreia automaticamente quando um usuário envia um formulário de página de destino. Você pode visualizar o número total de envios de um formulário na [análise da página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). No entanto, para o redirecionamento específico do usuário, você precisará redirecionar os usuários por meio do formulário da sua landing page usando um dos seguintes métodos:

- **Usando um segmento:** Você pode criar um novo segmento para identificar automaticamente os usuários que enviaram ou não um formulário de landing page.
- **Usando um acionador de mensagem:** Você pode configurar um acionador de mensagens para enviar mensagens automaticamente aos usuários ou inseri-los em um Canvas depois que eles enviarem o formulário.

{% tabs local %}
{% tab Using a segment %}
Quando você [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), no grupo "Retargeting", escolha **Formulário enviado na página de destino**.

Criação de segmento com o grupo de filtros selecionado como "Formulário enviado na página de destino".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

A partir daí, você pode segmentar os usuários com base no fato de eles terem ou não enviado um formulário para a sua página de destino.
{% endtab %}

{% tab Using a message trigger %}
Quando você escolher a opção de entrega para sua [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), selecione **Action Based Delivery (Entrega baseada em ação**) e, em seguida, **o formulário Submitted Landing Page (Página de destino enviada**).

Todos os usuários que enviarem um formulário por meio desse formulário da página de destino receberão uma mensagem por meio do canal de mensagens escolhido ou entrarão no Canvas escolhido.

\![Ação de acionamento da página de destino em mensagens.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
A opção de entrega baseada em ação para páginas de destino não está disponível para mensagens in-app. Para segmentar usuários que enviaram um formulário em uma página de destino com uma mensagem in-app, selecione o filtro **Formulário enviado na página de destino** nas **Opções de segmentação** da sua campanha.
{% endalert %}

{% endtab %}
{% endtabs %}
