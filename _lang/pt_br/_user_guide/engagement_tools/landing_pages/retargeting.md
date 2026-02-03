---
nav_title: Redirecionamento de usuários
article_title: Redirecionar usuários através de uma landing page
description: "Aprenda como redirecionar usuários que enviaram um formulário através de uma landing page."
page_order: 3
---

# Redirecionar usuários através de uma landing page

> Saiba como redirecionar os usuários que enviaram um formulário por meio de uma landing page, criando um segmento dedicado ou enviando uma mensagem quando o formulário for enviado.

## Pré-requisitos

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Redirecionamento de usuários

O Braze rastreia automaticamente quando um usuário envia um formulário de landing page. Você pode visualizar o número total de envios de um formulário na [análise de dados da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). No entanto, para redirecionamento específico do usuário, será necessário redirecionar os usuários por meio do formulário da landing page usando um dos seguintes métodos:

- **Usando um segmento:** É possível criar um novo segmento para identificar automaticamente os usuários que enviaram ou não um formulário da landing page.
- **Usando um disparador de mensagens:** É possível configurar um disparador de mensagens para enviar mensagens automaticamente aos usuários ou inseri-los em um Canva depois que eles enviarem o formulário.

{% tabs local %}
{% tab Using a segment %}
Quando você [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), no grupo "Redirecionamento", escolha **Formulário enviado na Landing Page**.

![Criação de segmento com o Grupo de Filtro selecionado como "Formulário Enviado na Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

A partir daqui, você pode segmentar usuários com base em se eles enviaram ou não um formulário de landing page para sua landing page.
{% endtab %}

{% tab Using a message trigger %}
Quando você escolher sua opção de entrega para sua [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ou [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), selecione **Entrega Baseada em Ação**, então **Formulário Enviado da Landing Page**.

Todos os usuários que enviarem um formulário por meio desse formulário da landing page receberão um envio de mensagens pelo canal de envio de mensagens escolhido ou entrarão no Canva escolhido.

![Ação-gatilho da landing page na mensagem.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
A opção de entrega baseada em ação para landing pages não está disponível para mensagens no app. Para direcionar usuários que enviaram um formulário em uma landing page com uma mensagem no app, selecione o filtro **Formulário Enviado na Landing Page** nas **Opções de Direcionamento** da sua campanha.
{% endalert %}

{% endtab %}
{% endtabs %}
