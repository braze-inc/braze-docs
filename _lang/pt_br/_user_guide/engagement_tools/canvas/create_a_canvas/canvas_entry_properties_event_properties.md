---
nav_title: Propriedades de entrada de tela e propriedades de evento
article_title: Propriedades de entrada de tela e propriedades de evento
page_order: 4.2
page_type: reference
description: "Este artigo de referência descreve as diferenças entre as propriedades de entrada do Canva e as propriedades de evento, e quando usar cada propriedade."
tool: Canvas
---

# Propriedades de entrada da tela e propriedades de evento

> Este artigo de referência aborda informações sobre `canvas_entry_properties` e `event_properties`, incluindo quando usar cada propriedade e as diferenças de comportamento. <br><br> Para saber mais sobre propriedades de eventos personalizados em geral, consulte [Propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% alert important %}
Desde 28 de fevereiro de 2023, não é mais possível criar ou duplicar canvas usando o editor original. Este artigo está disponível para referência ao usar `canvas_entry_properties` e `event_properties` para o fluxo de trabalho original do canva.
{% endalert %}

As propriedades de entrada do Canva e as propriedades de evento funcionam de forma diferente em seus fluxos de trabalho do Canva. As propriedades de eventos ou chamadas de API que disparam a entrada de um usuário em um Canva são conhecidas como `canvas_entry_properties`. As propriedades dos eventos que ocorrem à medida que um usuário percorre uma jornada do Canva são conhecidas como `event_properties`. A principal diferença aqui é que o `canvas_entry_properties` se concentra em mais do que apenas eventos, acessando também as propriedades das cargas úteis de entrada em canvas disparados por API.

No editor de canvas original e no Canvas Flow, não é possível usar `event_properties` na etapa do canva. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.

O comportamento também varia entre os fluxos de trabalho criados com o Canvas Flow e o editor original. Por exemplo, no editor original do Canva, você pode usar `event_properties` na primeira etapa completa se for uma etapa baseada em ação. No Canvas Flow, não há suporte para etapas completas, portanto, isso não se aplica.

Consulte a tabela a seguir para obter um resumo das diferenças entre `canvas_entry_properties` e `event_properties`.

| | Propriedades de entrada do canva | Propriedades do evento
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistência** | Pode ser referenciado por todas as etapas [de mensagens][1] durante a duração de um Canvas criado usando o Canvas Flow. | \- Só pode ser referenciado uma vez. <br> \- Não pode ser referenciado por nenhuma etapa de Mensagem subsequente. |
| **Comportamento da tela original** | \- As propriedades de entrada persistente devem estar ativadas. <br> \- Só pode fazer referência a `canvas_entry_properties` na primeira etapa completa de um Canva. O Canva deve ser baseado em ação ou disparado por API. | \- Pode fazer referência a `event_properties` em qualquer etapa completa que use a entrega baseada em ação em um Canva. <br> \- Não pode ser usado em etapas completas programadas que não sejam a primeira etapa completa de um Canva baseado em ação. No entanto, se um usuário estiver usando um [componente de canvas][2], o comportamento seguirá as regras do Canvas Flow para `event_properties`. |
| **Comportamento do Canvas Flow** | Pode fazer referência a `canvas_entry_properties` em qualquer etapa de um Canva. Para o comportamento pós-lançamento, consulte [Editando Canvas após o lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Pode fazer referência a `event_properties` na primeira etapa de mensagem **após** uma etapa [de jornadas de ação][3] em que a ação realizada é um evento personalizado ou um evento de compra. <br> \- Não pode estar após a jornada Restante do público da etapa Jornadas de ação. <br> \- Pode ter outros componentes do canva que não sejam de mensagem entre as jornadas de ação e as etapas de mensagem. Se um desses componentes que não são de mensagens for uma etapa de jornadas de ação, o usuário poderá passar pela jornada Everyone Else desse caminho de ação. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Note que as propriedades de entrada do canva só estão disponíveis para referência no Liquid. Para filtrar as propriedades dentro do canva, use [a segmentação de propriedades de eventos]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

{% alert note %}
Para canais de envio de mensagens no app, o `canvas_entry_properties` só pode ser referenciado no Canvas Flow e no editor original do Canvas se [as propriedades de entrada persistente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) estiverem ativadas no editor original como parte do acesso antecipado anterior. No entanto, `event_properties` não pode ser usado para canais de envio de mensagens no app.
{% endalert %}

Quando uma etapa do caminho da ação contém um disparador "Enviou uma mensagem de entrada SMS" ou "Enviou uma mensagem de entrada WhatsApp", as etapas subsequentes do Canva podem incluir uma propriedade Liquid do SMS ou do WhatsApp. Isso reflete o funcionamento das propriedades do evento no Canvas Flow. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e envio de mensagens de conversação.

## Caso de uso

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Para entender melhor as diferenças entre `canvas_entry_properties` e `event_properties`, vamos considerar este cenário em que os usuários entrarão em um Canva baseado em ação se executarem o evento personalizado "adicionar item à lista de desejos". 

O `canvas_entry_properties` é configurado na etapa [Entry Schedule (Programação de entrada)]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) da criação de um Canva e corresponderá a quando um usuário entrar no Canvas. Esses `canvas_entry_properties` também podem ser referenciados em qualquer etapa de mensagens no Canvas Flow, pois o Canvas Flow oferece suporte a propriedades de entrada persistentes. 

Nesta tela, temos uma jornada de usuário que começa com uma etapa das jornadas de ação para determinar se um usuário adicionou um item à sua lista de desejos. A partir daqui, se o usuário tiver adicionado um item, ele sofrerá uma postergação antes de receber a mensagem "New item in your wishlist!" (Novo item na sua lista de desejos!) da etapa Message (Mensagem). 

A primeira etapa da mensagem em uma jornada do usuário terá acesso ao `event_properties` personalizado da etapa Jornadas de ação. Nesse caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` nessa etapa de Mensagem como parte do conteúdo da mensagem. Se um usuário não adicionar um item à sua lista de desejos, ele acessará a jornada Restante do público, o que significa que o `event_properties` não pode ser referenciado e refletirá um erro de configurações inválidas.

Observe que você só terá acesso a `event_properties` se a etapa de mensagem puder ser rastreada até uma jornada que não seja "Restante do público" em uma etapa de jornada de ação. Se a etapa da mensagem estiver conectada a uma jornada Restante do público, mas puder ser rastreada até uma etapa das jornadas de ação na jornada do usuário, você também terá acesso a `event_properties`. Para saber mais sobre esses comportamentos, consulte [Etapa da mensagem][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
