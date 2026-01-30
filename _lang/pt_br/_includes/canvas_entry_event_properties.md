Você pode usar as propriedades de entrada do Canvas e as propriedades de evento em suas jornadas de usuário do Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

[As propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) são as propriedades que você mapeia para Canvas que são baseadas em ações ou disparadas por API. Note que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB.

{% alert note %}
Para canais de mensagem no app especificamente, `canvas_entry_properties` só pode ser referenciado no Canvas.
{% endalert %}

Você pode referenciar `canvas_entry_properties` em qualquer etapa de Mensagem com este formato Liquid: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

#### Caso de uso

{% raw %}
Digamos que uma loja de varejo, RetailApp, tenha a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 

RetailApp pode puxar o nome do produto (sapatos) para uma mensagem com este Liquid: `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

O RetailApp também pode disparar o envio de mensagens específicas para diferentes propriedades do `product_name` em um Canva que direciona os usuários depois que eles acionam um evento de compra. Por exemplo, eles podem enviar mensagens diferentes para os usuários que compraram sapatos e para os usuários que compraram outra coisa, adicionando o seguinte Liquid em uma etapa de Mensagem.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expand for original Canvas editor %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência. Para os Canvases construídos com o editor original, as propriedades de entrada do Canvas podem ser referenciadas na primeira etapa completa de um Canvas apenas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

As propriedades de eventos referem-se às propriedades que você define para eventos e compras personalizados. Esses `event_properties` podem ser usados em campanhas com entrega baseada em ação e Canvas.

{% alert important %}
Você não pode usar `event_properties` na primeira etapa de Mensagem do seu Canvas. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes da** etapa de mensagem que inclui `event_properties`.
{% endalert %}

No Canvas, propriedades de evento personalizado e de evento de compra podem ser usadas em Liquid em qualquer etapa de Mensagem que siga uma etapa de Jornadas de Ação. Certifique-se de usar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} se você estiver referenciando essas propriedades de evento. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente Message.

Na primeira etapa de Mensagem que segue uma Jornada de Ação, você pode usar propriedades de evento relacionadas ao evento referenciado nessa Jornada de Ação. No entanto, essas propriedades de evento só podem ser usadas se o usuário realmente realizou a ação (e não foi classificado no grupo Todos os Outros). Você pode ter outras etapas (que não sejam outros caminhos de ação ou etapa de mensagem) entre esses caminhos de ação e a etapa de mensagem.

{% details Expand for original Canvas editor %}

Não é mais possível criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência. Para o editor original do Canvas, propriedades de evento não podem ser usadas em etapas completas agendadas. No entanto, você pode usar propriedades de evento na primeira etapa completa de um Canvas baseado em ação, mesmo que a etapa completa esteja agendada.

{% enddetails %}

{% endtab %}
{% endtabs %}

Consulte as [propriedades de entrada do Canva e as propriedades de evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para obter mais informações e exemplos.