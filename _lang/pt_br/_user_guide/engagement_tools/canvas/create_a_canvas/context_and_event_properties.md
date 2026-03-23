---
nav_title: Propriedades de contexto e eventos
article_title: Propriedades de Contexto e Evento
page_order: 4.2
page_type: reference
description: "Este artigo de referência descreve as diferenças entre propriedades de contexto e de evento, e quando usar cada propriedade."
tool: Canvas
---

# Propriedades de contexto e eventos

> Este artigo de referência aborda informações sobre `context` e `event_properties`, incluindo quando usar cada propriedade e as diferenças de comportamento. <br><br> Para saber mais sobre propriedades de eventos personalizados em geral, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

As propriedades de contexto e as propriedades de evento funcionam de maneira diferente dentro dos seus fluxos de trabalho no Canvas. As propriedades de eventos ou chamadas de API que disparam a entrada de um usuário em um Canva são conhecidas como `context`. As propriedades dos eventos que ocorrem à medida que um usuário se move dentro de uma jornada no Canvas são conhecidas como `event_properties`. A principal diferença é que `context` foca em mais do que apenas eventos, acessando também as propriedades das cargas de entrada em Canvases acionados por API.

Consulte a tabela a seguir para um resumo das diferenças entre propriedades de contexto e de evento.

| | Propriedades de contexto | Propriedades do evento |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistência** | Podem ser referenciadas por todos os passos [Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante a duração de um Canvas construído usando Canvas. | \- Só pode ser referenciado uma vez. <br> \- Não pode ser referenciado por nenhuma etapa de Mensagem subsequente. |
| **Comportamento do Canvas** | Pode fazer referência a `context` em qualquer etapa de um Canva. Para o comportamento pós-lançamento, consulte [Editando Canvas após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Pode fazer referência a `event_properties` na primeira etapa de mensagem **após** uma etapa [de jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) em que a ação realizada é um evento personalizado ou um evento de compra. <br> \- Não pode estar após a jornada Restante do público da etapa Jornadas de ação. <br> \- Podem ter outros componentes que não sejam Mensagem entre as Jornadas de Ação e os passos de Mensagem. Se um desses componentes que não são de mensagens for uma etapa de jornadas de ação, o usuário poderá passar pela jornada Everyone Else desse caminho de ação. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Observe que o Contexto do Canvas não é suportado no editor original do Canvas, portanto, esta seção está disponível para referência ao usar propriedades de entrada do Canvas e propriedades de evento para o fluxo de trabalho anterior do Canvas.

**Propriedades de entrada do Canvas:**
- Deve ter as propriedades de entrada persistentes ativadas. 
- Só pode referenciar `canvas_entry_properties` no primeiro passo completo de um Canvas. O Canva deve ser baseado em ação ou disparado por API.

**Propriedades de entrada:**
- Pode referenciar `event_properties` em qualquer passo completo que use entrega baseada em ação em um Canvas.
- Não pode ser usado em passos completos agendados, exceto no primeiro passo completo de um Canvas baseado em ação. No entanto, se um usuário estiver usando um [componente do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), o comportamento segue as regras atuais do fluxo de trabalho do Canvas para `event_properties`.

**Propriedades de evento:**
- Não é possível usar `event_properties` na etapa de mensagem principal. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.

{% enddetails %}

### Coisas para saber

- O contexto está disponível apenas para referência no Liquid. Para filtrar as propriedades dentro do canva, use [a segmentação de propriedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para canais de mensagem no app, você pode referenciar `context` e `event_properties` em um Canva. `event_properties` pode ser acessado quando incluído na primeira etapa do Canva, pois é baseado em gatilho.
- Não é possível usar `event_properties` na etapa de envio de mensagens. Em vez disso, você pode usar `context` ou adicionar uma etapa de Jornadas de Ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.
- Quando uma etapa do caminho da ação contém um disparador "Enviou uma mensagem de entrada SMS" ou "Enviou uma mensagem de entrada WhatsApp", as etapas subsequentes do Canva podem incluir uma propriedade Liquid do SMS ou do WhatsApp. Isso reflete como as propriedades de evento funcionam nos Canvases. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e envio de mensagens de conversação.

{% alert note %}
A elegibilidade do público é avaliada uma vez na entrada do Canva. Se um usuário for mesclado durante a entrada, o usuário identificado continua pelo Canva e não é reavaliado em relação aos critérios do segmento do Canva.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Carimbos de data/hora para gatilhos

Se você estiver usando carimbos de data/hora com um [tipo de data/hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de eventos que acionam Canvases baseados em ação, que são referenciados usando [contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties), os carimbos de data/hora são normalizados para UTC.

Dado esse comportamento, a Braze recomenda fortemente que você use um filtro de fuso horário Liquid como o exemplo a seguir para garantir que suas mensagens sejam enviadas com seu [fuso horário preferido]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### Exceções

- Os carimbos de data/hora não são normalizados para UTC na primeira etapa de um Canva se essa etapa for uma etapa de Mensagem.
- Os carimbos de data/hora não são normalizados para UTC em qualquer etapa de Mensagem usando o canal de mensagem no app, independentemente da sua ordem no Canva.

## Caso de uso

![Uma etapa de Caminho de Ação seguida por uma etapa de Postergação e uma etapa de Mensagem para usuários que adicionaram um item à sua lista de desejos, e um caminho para todos os outros.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para entender melhor as diferenças para `context` e `event_properties`, vamos considerar este cenário onde os usuários entram em um Canva baseado em ação se realizarem o evento personalizado "adicionar item à lista de desejos". 

O contexto é configurado na etapa [Agenda de Entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) de criação de um Canva e corresponde ao momento em que um usuário entra em um Canva. O contexto também pode ser referenciado em qualquer etapa de Mensagem.

Nesta tela, temos uma jornada de usuário que começa com uma etapa das jornadas de ação para determinar se um usuário adicionou um item à sua lista de desejos. A partir daqui, se o usuário adicionou um item, ele experimenta uma postergação antes de receber uma mensagem "Novo item na sua lista de desejos!" da etapa de Mensagem. 

A primeira etapa de Mensagem em uma jornada do usuário tem acesso ao `event_properties` personalizado da sua etapa de Jornadas de Ação. Nesse caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` nessa etapa de Mensagem como parte do conteúdo da mensagem. Se um usuário não adicionar um item à sua lista de desejos, ele passa pelo caminho de Todos os Outros, o que significa que `event_properties` não pode ser referenciado e reflete um erro de configurações inválidas.

Observe que você só terá acesso a `event_properties` se a etapa de mensagem puder ser rastreada até uma jornada que não seja "Restante do público" em uma etapa de jornada de ação. Se a etapa de Mensagem estiver conectada a um caminho de Todos os Outros, mas puder ser rastreada de volta a uma etapa de Jornadas de Ação na jornada do usuário, então você ainda terá acesso a `event_properties`. Para saber mais sobre esses comportamentos, veja [Mensagem etapa]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

