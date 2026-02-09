---
nav_title: Propriedades de entrada da tela e propriedades de evento
article_title: Propriedades de Entrada da Canva e Propriedades de Evento
page_order: 4.2
page_type: reference
description: "Este artigo de referência descreve as diferenças entre as propriedades de entrada do Canva e as propriedades de evento, e quando usar cada propriedade."
tool: Canvas
---

# Propriedades de entrada da tela e propriedades de evento

> Este artigo de referência aborda informações sobre `canvas_entry_properties` e `event_properties`, incluindo quando usar cada propriedade e as diferenças de comportamento. <br><br> Para saber mais sobre propriedades de eventos personalizados em geral, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

As propriedades de entrada do Canva e as propriedades de evento funcionam de forma diferente em seus fluxos de trabalho do Canva. As propriedades de eventos ou chamadas de API que disparam a entrada de um usuário em um Canva são conhecidas como `canvas_entry_properties`. As propriedades dos eventos que ocorrem à medida que um usuário percorre uma jornada do Canva são conhecidas como `event_properties`. A principal diferença é que o `canvas_entry_properties` se concentra em mais do que apenas eventos, acessando também as propriedades das cargas úteis de entrada em Canvas disparados por API.

Consulte a tabela a seguir para obter um resumo das diferenças entre as propriedades de entrada do Canva e as propriedades do evento.

| | Propriedades de entrada do canva | Propriedades do evento
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistência** | Pode ser referenciado por todas as etapas [de mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante a duração de um Canvas criado usando o Canvas. | \- Só pode ser referenciado uma vez. <br> \- Não pode ser referenciado por nenhuma etapa de Mensagem subsequente. |
| **Comportamento da tela** | Pode fazer referência a `canvas_entry_properties` em qualquer etapa de um Canva. Para o comportamento pós-lançamento, consulte [Editando Canvas após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Pode fazer referência a `event_properties` na primeira etapa de mensagem **após** uma etapa [de jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) em que a ação realizada é um evento personalizado ou um evento de compra. <br> \- Não pode estar após a jornada Restante do público da etapa Jornadas de ação. <br> \- Pode ter outros componentes que não sejam de mensagens entre as jornadas de ação e as etapas de mensagens. Se um desses componentes que não são de mensagens for uma etapa de jornadas de ação, o usuário poderá passar pela jornada Everyone Else desse caminho de ação. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Este artigo está disponível para referência ao usar as propriedades de entrada do Canvas e as propriedades de evento para o fluxo de trabalho anterior do Canvas.

**Propriedades de entrada da tela:**
- As propriedades de entrada persistente devem estar ativadas. 
- Só pode fazer referência a `canvas_entry_properties` na primeira etapa completa de um Canva. O Canva deve ser baseado em ação ou disparado por API.

**Propriedades de entrada:**
- Pode fazer referência a `event_properties` em qualquer etapa completa que use a entrega baseada em ação em um Canva.
- Não pode ser usado em etapas completas programadas que não sejam a primeira etapa completa de um Canva baseado em ação. No entanto, se um usuário estiver usando um [componente do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), o comportamento seguirá as regras atuais do fluxo de trabalho do Canvas para `event_properties`.

**Propriedades do evento:**
- Não é possível usar `event_properties` na etapa de envio de mensagens. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.

{% enddetails %}

### Coisas para saber

- As propriedades de entrada da tela estão disponíveis apenas para referência no Liquid. Para filtrar as propriedades na tela, use [a segmentação de propriedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para canais de envio de mensagens no app, você pode fazer referência a `canvas_entry_properties` e `event_properties` em um Canvas. `event_properties` pode ser acessado quando incluído na primeira etapa do Canvas porque é baseado em disparo.
- Não é possível usar `event_properties` na etapa de envio de mensagens. Em vez disso, você pode usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.
- Quando uma etapa do caminho da ação contém um disparador "Enviou uma mensagem de entrada SMS" ou "Enviou uma mensagem de entrada WhatsApp", as etapas subsequentes do Canva podem incluir uma propriedade Liquid do SMS ou do WhatsApp. Isso reflete o funcionamento das propriedades de eventos nas telas. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e envio de mensagens de conversação.

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Carimbos de data e hora para propriedades de eventos

Se estiver usando carimbos de [data]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) e hora com um [tipo de data e hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) das [propriedades de eventos de gatilho]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em Canvas baseados em ação, os carimbos de data e hora serão normalizados para UTC. Algumas exceções estão detalhadas abaixo.

Devido a esse comportamento, a Braze recomenda enfaticamente o uso de um filtro de fuso horário Liquid, como o exemplo a seguir, para garantir que suas mensagens sejam enviadas com o fuso [horário de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) sua [preferência]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter).

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### Exceções

- Os registros de data e hora não são normalizados para UTC na primeira etapa de um Canva se essa etapa for uma etapa do Message.
- Os carimbos de data/hora não são normalizados para UTC em nenhuma etapa de mensagens usando o canal de envio de mensagens no app, independentemente de sua ordem no Canvas.

## Caso de uso

![Uma etapa de caminho de ação seguida de uma etapa de postergação e uma etapa de mensagem para usuários que adicionaram um item à lista de desejos, e uma jornada para todos os outros.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para entender melhor as diferenças entre `canvas_entry_properties` e `event_properties`, vamos considerar este cenário em que os usuários entram em um Canva baseado em ação se executarem o evento personalizado "adicionar item à lista de desejos". 

O `canvas_entry_properties` é configurado na etapa do [Entry Schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) da criação de um Canva e corresponde a quando um usuário entra em um Canvas. Esses `canvas_entry_properties` também podem ser referenciados em qualquer etapa do Message.

Nesta tela, temos uma jornada de usuário que começa com uma etapa das jornadas de ação para determinar se um usuário adicionou um item à sua lista de desejos. A partir daqui, se o usuário tiver adicionado um item, ele terá uma postergação antes de receber a mensagem "Novo item na sua lista de desejos!" da etapa Mensagem. 

A primeira etapa de mensagens em uma jornada do usuário tem acesso ao `event_properties` personalizado da etapa de jornadas de ação. Nesse caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` nessa etapa de Mensagem como parte do conteúdo da mensagem. Se um usuário não adicionar um item à sua lista de desejos, ele acessará a jornada Everyone Else, o que significa que o site `event_properties` não pode ser referenciado e reflete um erro de configurações inválidas.

Observe que você só terá acesso a `event_properties` se a etapa de mensagem puder ser rastreada até uma jornada que não seja "Restante do público" em uma etapa de jornada de ação. Se a etapa da mensagem estiver conectada a uma jornada Everyone Else, mas puder ser rastreada até uma etapa das jornadas de ação na jornada do usuário, você também terá acesso a `event_properties`. Para saber mais sobre esses comportamentos, consulte a [etapa Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

