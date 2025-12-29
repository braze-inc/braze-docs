---
nav_title: Propriedades de entrada de tela e propriedades de evento
article_title: Propriedades de entrada de tela e propriedades de evento
page_order: 4.2
page_type: reference
description: "Este artigo de referência descreve as diferenças entre as propriedades de entrada do Canvas e as propriedades de evento, e quando usar cada propriedade."
tool: Canvas
---

# Propriedades de entrada de tela e propriedades de evento

> Este artigo de referência aborda informações sobre `canvas_entry_properties` e `event_properties`, incluindo quando usar cada propriedade e as diferenças de comportamento. <br><br> Para obter informações sobre propriedades de eventos personalizados em geral, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

As propriedades de entrada do Canvas e as propriedades de evento funcionam de forma diferente em seus fluxos de trabalho do Canvas. As propriedades de eventos ou chamadas de API que acionam a entrada de um usuário em um Canvas são conhecidas como `canvas_entry_properties`. As propriedades dos eventos que ocorrem à medida que um usuário percorre uma jornada do Canvas são conhecidas como `event_properties`. A principal diferença é que o `canvas_entry_properties` se concentra em mais do que apenas eventos, acessando também as propriedades das cargas úteis de entrada em Canvases acionados por API.

Consulte a tabela a seguir para obter um resumo das diferenças entre as propriedades de entrada do Canvas e as propriedades do evento.

| | Propriedades de entrada do Canvas | Propriedades do evento
|----|----|----|
| **Líquido** | `canvas_entry_properties` | `event_properties` |
| **Persistência** | Pode ser referenciado por todas as etapas [da mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) durante a duração de um Canvas criado usando o Canvas. | \- Só pode ser referenciado uma vez. <br> \- Não pode ser referenciado por nenhuma etapa subsequente da Mensagem. |
| **Comportamento do Canvas** | Pode fazer referência a `canvas_entry_properties` em qualquer etapa de um Canvas. Para obter informações sobre o comportamento pós-lançamento, consulte [Edição de telas após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Pode fazer referência a `event_properties` na primeira etapa de Mensagem **após** uma etapa [de Caminhos de Ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) em que a ação realizada é um evento personalizado ou um evento de compra. <br> \- Não pode estar após o caminho Todos os outros da etapa Caminhos de ação. <br> \- Pode ter outros componentes que não sejam de mensagem entre os caminhos de ação e as etapas de mensagem. Se um desses componentes não relacionados a mensagens for uma etapa de caminhos de ação, o usuário poderá passar pelo caminho Todos os outros desse caminho de ação. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Não é mais possível criar ou duplicar Canvases usando o editor original. Este artigo está disponível para referência ao usar as propriedades de entrada do Canvas e as propriedades de evento para o fluxo de trabalho anterior do Canvas.

**Propriedades de entrada da tela:**
- As propriedades de entrada persistente devem estar ativadas. 
- Só pode fazer referência a `canvas_entry_properties` na primeira etapa completa de um Canvas. O Canvas deve ser baseado em ações ou acionado por API.

**Propriedades de entrada:**
- Pode fazer referência a `event_properties` em qualquer etapa completa que use o fornecimento baseado em ação em um Canvas.
- Não pode ser usado em etapas completas programadas que não sejam a primeira etapa completa de um Canvas baseado em ação. No entanto, se um usuário estiver usando um [componente do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), o comportamento seguirá as regras atuais do fluxo de trabalho do Canvas para `event_properties`.

**Propriedades do evento:**
- Não é possível usar `event_properties` na etapa de mensagem principal. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de Caminhos de Ação com o evento correspondente **antes da** etapa de Mensagem que inclui `event_properties`.

{% enddetails %}

### Coisas para saber

- As propriedades de entrada do Canvas estão disponíveis apenas para referência no Liquid. Para filtrar as propriedades dentro do Canvas, use [a segmentação de propriedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Para canais de mensagens in-app, `canvas_entry_properties` só pode ser referenciado em um Canvas. `event_properties` não pode ser usado para canais de mensagens in-app.
- Não é possível usar `event_properties` na etapa de mensagem principal. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de Caminhos de Ação com o evento correspondente **antes da** etapa de Mensagem que inclui `event_properties`. 
- Quando uma etapa do Caminho de ação contém um acionador "Enviou uma mensagem de entrada de SMS" ou "Enviou uma mensagem de entrada do WhatsApp", as etapas subsequentes do Canvas podem incluir uma propriedade SMS ou WhatsApp Liquid. Isso reflete como as propriedades de eventos funcionam no Canvases. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e mensagens de conversação.

### Carimbos de data e hora para propriedades de eventos

Se você estiver usando carimbos de [data e hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) com um [tipo de data e hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de [propriedades de eventos de acionamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) em Canvases baseados em ação, os carimbos de data e hora serão normalizados para UTC. Algumas exceções estão detalhadas abaixo.

Devido a esse comportamento, a Braze recomenda enfaticamente que você use um filtro de fuso horário Liquid como o exemplo a seguir para garantir que suas mensagens sejam enviadas com o fuso [horário de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) sua preferência.

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### Exceções

- Os registros de data e hora não são normalizados para UTC na primeira etapa de um Canvas se essa etapa for uma etapa de Mensagem.
- Os carimbos de data/hora não são normalizados para UTC em nenhuma etapa de mensagem usando o canal de mensagens no aplicativo, independentemente de sua ordem no Canvas.

## Caso de uso

Uma etapa do Caminho de ação seguida por uma etapa de Atraso e uma etapa de Mensagem para usuários que adicionaram um item à lista de desejos e um caminho para todos os outros.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para entender melhor as diferenças entre `canvas_entry_properties` e `event_properties`, vamos considerar este cenário em que os usuários entrarão em um Canvas baseado em ação se executarem o evento personalizado "add item to wishlist" (adicionar item à lista de desejos). 

O `canvas_entry_properties` é configurado na etapa [Entry Schedule (Programação de entrada)]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) da criação de um Canvas e corresponderá a quando um usuário entrar no Canvas. O site `canvas_entry_properties` também pode ser consultado em qualquer etapa do Message.

Neste Canvas, temos uma jornada do usuário que começa com uma etapa de Caminhos de ação para determinar se um usuário adicionou um item à sua lista de desejos. A partir daqui, se o usuário tiver adicionado um item, ele sofrerá um atraso antes de receber a mensagem "New item in your wishlist!" (Novo item na sua lista de desejos!) da etapa Message (Mensagem). 

A primeira etapa da Mensagem em uma jornada do usuário terá acesso ao `event_properties` personalizado da etapa Caminhos de ação. Nesse caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` nessa etapa da mensagem como parte do conteúdo da mensagem. Se um usuário não adicionar um item à sua lista de desejos, ele passará pelo caminho Everyone Else, o que significa que o site `event_properties` não pode ser referenciado e refletirá um erro de configurações inválidas.

Observe que você só terá acesso a `event_properties` se a etapa Mensagem puder ser rastreada até um caminho que não seja Todos os outros em uma etapa Caminhos de ação. Se a etapa da mensagem estiver conectada a um caminho Everyone Else (Todos os outros), mas puder ser rastreada até uma etapa Action Paths (Caminhos de ação) na jornada do usuário, você também terá acesso a `event_properties`. Para obter mais informações sobre esses comportamentos, confira a [etapa Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

