---
nav_title: Mensagem 
article_title: Mensagem 
alias: "/message_step/"
page_order: 5
page_type: reference
description: "Este artigo de referência aborda como criar uma mensagem autônoma usando a etapa Message."
tool: Canvas

---

# Mensagem 

> As etapas de mensagem permitem que você adicione uma mensagem independente onde quiser no Canvas.

\![Uma etapa de mensagem chamada "Promoção de almoço" usando o canal push.]({% image_buster /assets/img/canvas_components/message_step1.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

## Criar uma mensagem

Para criar um componente Message, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Mensagem**. 

### Etapa 1: Selecione seu canal de mensagens

Você pode selecionar entre os seguintes canais de mensagens: 
- Cartões de conteúdo
- E-mail
- LINHA
- Notificações push
- SMS/MMS/RCS
- Mensagens no aplicativo 
- Webhook
- WhatsApp

\![Uma lista de canais de mensagens disponíveis a serem selecionados para a etapa Mensagem.]({% image_buster /assets/img/canvas_components/message_step2.png %})

### Etapa 2: Editar configurações de entrega

Em seguida, você pode editar as configurações de Intelligent Delivery, substituições de Quiet Hours e validação de entrega.

#### Cronograma inteligente

Você pode ativar [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) com uma opção de fallback quando o perfil de um usuário não tiver dados suficientes para calcular um tempo ideal. Recomendamos ativar o Intelligent Timing e [a limitação de taxa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) como uma verificação adicional de qualquer atraso entre os usuários que entram na etapa de mensagem e o envio real da mensagem.

Selecione **Usando o Intelligent Timing** na guia **Delivery Settings (Configurações de entrega** ). Aqui, você pode selecionar o horário mais popular ou um horário alternativo específico. Se a opção Quiet Hours estiver ativada, a etapa Message (Mensagem) também permitirá que você substitua essa configuração.

#### Validações de entrega

As validações de entrega fornecem uma verificação adicional para confirmar que seu público-alvo atende aos critérios de entrega no envio da mensagem. Essa configuração é recomendada se Quiet Hours, Intelligent Timing ou rate limiting estiverem ativados. Você pode adicionar um segmento ou filtros adicionais para validar no momento em que a mensagem é enviada. Se um usuário não atender às validações de entrega definidas para uma etapa de Mensagem, ele sairá do Canvas na etapa.

A guia Configurações de entrega para as configurações do componente Mensagem. A opção Quiet Hours está ativada e a caixa de seleção Usar timing inteligente está marcada para entregar a mensagem em um horário ideal. As validações de entrega são ativadas para validar o público-alvo no envio da mensagem.]({% image_buster /assets/img/canvas_components/message_step4.png %}){: style="max-width:90%;"}

## Como os usuários avançam

Todos os usuários que entrarem na etapa Mensagem avançarão para a próxima etapa quando qualquer uma das seguintes condições for atendida:

- Qualquer mensagem é enviada
- Uma mensagem tem limite de frequência e não é enviada
- Uma mensagem é cancelada
- Um usuário não pode ser acessado pelo canal, portanto a mensagem não é enviada

{% raw %}
Se um Canvas baseado em ação for acionado por uma mensagem SMS recebida, você poderá fazer referência às propriedades de SMS na primeira etapa (etapa de Mensagem) ou em uma etapa de Mensagem aninhada em uma etapa de Caminho de ação. Por exemplo, na etapa Mensagem, você poderia usar `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## Referência a propriedades de entrada do Canvas

As propriedades de entrada do Canvas são configuradas na etapa **Entry Schedule (Programação de entrada)** da criação de um Canvas e indicarão o acionador que insere um usuário em um Canvas. Essas propriedades também podem acessar as propriedades de cargas úteis de entrada em Canvases acionados por API. Observe que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB. 

As propriedades de entrada podem ser usadas no Liquid em qualquer etapa da mensagem. Use o seguinte Liquid ao fazer referência a essas propriedades de entrada: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% alert note %}
Especificamente para canais de mensagens in-app, o `canvas_entry_properties` só pode ser referenciado no Canvas.
{% endalert %}

Use o seguinte Liquid ao fazer referência a essas propriedades de entrada: {% raw %}``canvas_entry_properties${property_name}``{% endraw %}. Observe que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você pode adicionar a palavra "shoes" (sapatos) a uma mensagem com o Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Você também pode aproveitar [as propriedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) em qualquer etapa da mensagem para orientar os usuários por meio de etapas personalizadas em todo o fluxo de trabalho do Canvas.

### Propriedades do evento

As propriedades do evento referem-se às propriedades que você define para eventos personalizados e eventos de compra. Essas propriedades de evento podem ser usadas em campanhas com entrega baseada em ação, bem como em Canvases. 

No Canvas, as propriedades de evento personalizado e evento de compra podem ser usadas no Liquid em qualquer etapa de mensagem que siga uma etapa [de Caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Por exemplo, ao fazer referência a `event_properties`, use este snippet do Liquid: {% raw %}``{{event_properties.${property_name}}}``{% endraw %} 

{% alert important %}
`event_properties` não pode ser usado independentemente das etapas dos Caminhos de Ação.
{% endalert %}

Na primeira etapa da mensagem após um caminho de ação, você pode usar o site `event_properties` relacionado ao evento referenciado nesse caminho de ação. Você pode ter outras etapas (que não sejam outros Caminhos de Ação ou etapa de Mensagem) entre essa etapa de Caminhos de Ação e a etapa de Mensagem. Observe que você só terá acesso a `event_properties` se a etapa Mensagem puder ser rastreada até um caminho que não seja Todos os outros em uma etapa Caminho de ação.

{% alert important %}
Não é possível usar `event_properties` na etapa de mensagem principal. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de Caminhos de Ação com o evento correspondente antes da etapa de Mensagem que inclui `event_properties`.
{% endalert %}

{% details Expand for original Canvas editor %}

Não é mais possível criar ou duplicar Canvases usando o editor original. Esta seção está disponível apenas para referência.

- `event_properties` não pode ser usado em etapas completas programadas. No entanto, você pode usar `event_properties` na primeira etapa completa de um Canvas baseado em ação, mesmo que a etapa completa esteja programada.
- `canvas_entry_properties` pode ser referenciado somente na primeira etapa completa de um Canvas.
- Especificamente para canais de mensagens in-app, o `canvas_entry_properties` pode ser referenciado no editor original do Canvas se você tiver propriedades de entrada persistentes ativadas como parte do acesso antecipado anterior.

{% enddetails %}

## Análises

Consulte a tabela a seguir para ver as definições das métricas do componente Message: 

| Métrico | Descrição |
| --- | --- |
| _Entradas_ | O número de vezes que a etapa foi inserida. Se o seu Canvas tiver reelegibilidade e um usuário inserir uma etapa de Mensagem duas vezes, duas entradas serão registradas. |
| _Prosseguiu para a próxima etapa_ | O número de entradas que prosseguiram para a próxima etapa do Canvas. |
| _Envia_ | O número total de mensagens que a etapa enviou. Se o seu Canvas for reelegível e um usuário inserir uma etapa de Mensagem duas vezes, duas entradas serão registradas. |
| _Destinatários exclusivos_ | O número de usuários que receberam mensagens dessa etapa. |
| _Evento de conversão primária_ | O número de vezes que um evento definido ocorreu após a interação ou a visualização de uma mensagem recebida de uma campanha do Braze. Você define esse evento ao criar a campanha. |
| _Receita_ | A receita total em dólares dos destinatários da campanha dentro da janela de conversão primária definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


