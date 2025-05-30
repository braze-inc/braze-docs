---
nav_title: Redirecionamento de usuários
article_title: Redirecionamento de usuários por meio de uma landing page
description: "Saiba como redirecionar os usuários que enviaram um formulário por meio de uma landing page."
page_order: 3
---

# Redirecionamento de usuários por meio de uma landing page

> Saiba como redirecionar os usuários que enviaram um formulário por meio de uma landing page, criando um segmento dedicado ou enviando uma mensagem quando o formulário for enviado.

## Pré-requisitos

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Redirecionamento de usuários

O Braze rastreia automaticamente quando um usuário envia um formulário de landing page. Você pode visualizar o número total de envios de um formulário na [análise de dados da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). No entanto, para redirecionamento específico do usuário, será necessário redirecionar os usuários por meio do formulário da landing page usando um dos seguintes métodos:

- **Usando um segmento:** É possível criar um novo segmento para identificar automaticamente os usuários que enviaram ou não um formulário da landing page.
- **Usando um disparador de mensagens:** É possível configurar um disparador de mensagens para enviar mensagens automaticamente aos usuários ou inseri-los em um Canva depois que eles enviarem o formulário.

{% tabs local %}
{% tab Usando um segmento %}
Quando você [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), no grupo "Redirecionamento", escolha **Formulário enviado na landing page**.

![Criação de segmento com o grupo de filtros selecionado como "Formulário enviado na landing page"]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

A partir daí, é possível segmentar os usuários com base no fato de eles terem ou não enviado um formulário para sua landing page.
{% endtab %}

{% tab Uso de um disparador de mensagens %}
Ao escolher a opção de entrega para sua [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/), selecione **Entrega baseada em ação** e, em seguida, **Formulário da landing page enviada**.

Todos os usuários que enviarem um formulário por meio desse formulário da landing page receberão um envio de mensagens pelo canal de envio de mensagens escolhido ou entrarão no Canva escolhido.

![Ação-gatilho da landing page no envio de mensagens]({% image_buster /assets/img/landing_pages/trigger.png %})
{% endtab %}
{% endtabs %}
