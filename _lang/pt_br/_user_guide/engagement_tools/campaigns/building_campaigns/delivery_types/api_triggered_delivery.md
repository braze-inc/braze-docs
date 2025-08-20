---
nav_title: Entrega disparada por API
article_title: Entrega disparada por API
page_order: 2
page_type: reference
description: "Este artigo de referência descreve como agendar e configurar uma campanha disparada por API."
tool: Campaigns
platform: API

---

# Entrega acionada por API

> Campanhas disparadas por API ou campanhas disparadas por servidor são ideais para casos de uso transacionais mais avançados. As campanhas acionadas por API da Braze permitem que os profissionais de marketing gerenciem a cópia da campanha, testes multivariantes e regras de re-eligibilidade no dashboard da Braze, enquanto acionam a entrega desse conteúdo a partir de seus próprios servidores e sistemas. A solicitação da API para disparar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real.

## Configuração de uma campanha acionada por API

Configurar uma campanha disparada por API leva algumas etapas. Primeiro, crie uma nova campanha multicanal ou de canal único (com testes multivariantes).

{% alert note %}
Uma campanha acionada por API é diferente de uma [campanha de API]({{site.baseurl}}/developer_guide/rest_api/api_campaigns/#api-campaigns).
{% endalert %}

Em seguida, configure sua cópia e notificações da mesma forma que faria normalmente para notificações agendadas e selecione **Entrega Acionada por API**. Para saber mais sobre o disparo dessas campanhas a partir do seu servidor, confira este artigo [envio de campanha acionada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

![]({% image_buster /assets/img_archive/api_triggered_campaign_delivery.png %})

## Usando o conteúdo modelado incluído com uma solicitação de API

Além de acionar a mensagem, você também pode incluir conteúdo com a solicitação da API para ser modelado na mensagem dentro do objeto `trigger_properties`. Este conteúdo pode ser referenciado no corpo da mensagem. Por exemplo, você pode incluir:
``{% raw %} {{ api_trigger_properties.${ some_value_included_with_request }}} {% endraw %}`` Veja o seguinte exemplo de notificação social para contexto adicional:

![A propriedade de disparar mencionada incluída na mensagem para preencher automaticamente o nome do usuário seguida do texto: "curtiu sua foto!" Clique aqui para ver o que eles têm feito.".]({% image_buster /assets/img_archive/api_triggered_photo_social_example_1.png %}){: style="max-width:70%;"}

## Re-eligibilidade com campanhas acionadas por API

O número de vezes que um usuário recebe uma campanha acionada por API pode ser limitado usando as configurações de re-eligibilidade. Isso significa que o usuário receberá a campanha apenas uma vez ou uma vez em uma janela específica, independentemente de quantas vezes o disparo da API for acionado.

Por exemplo, digamos que você está usando uma campanha acionada por API para enviar ao usuário uma campanha sobre um item que ele visualizou recentemente. Neste caso, você pode limitar a campanha para enviar no máximo uma mensagem por dia, independentemente de quantos itens eles visualizaram enquanto disparavam o gatilho da API para cada item. Por outro lado, se sua campanha acionada por API for transacional, você vai querer garantir que o usuário receba a campanha toda vez que fizer a transação, definindo a postergação para zero minutos.

![]({% image_buster /assets/img_archive/api_triggered_reeligible.png %})


