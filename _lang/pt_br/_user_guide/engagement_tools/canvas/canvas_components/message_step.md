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

> As etapas de mensagens permitem que você adicione uma mensagem independente onde quiser no Canvas Flow.



## 

Para criar um componente Message, primeiro adicione uma etapa do canva.  

###  

 
- 
- 
- 
- 
- 
-  
- 
- 



###  Editar configurações de entrega



#### 

É possível ativar [o Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) com uma opção de fallback quando o perfil de um usuário não tiver dados suficientes para calcular um tempo ideal. Recomendamos ativar o Intelligent Timing e [o limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) como uma verificação adicional de qualquer postergação entre os usuários que entram na etapa Mensagem e o envio real da mensagem.

Selecione **Usar Intelligent Timing** na guia **Configurações de entrega**. Aqui, você pode selecionar o horário mais popular ou um horário de fallback específico. Se o Horário de silêncio estiver ativado, a etapa Mensagem também permitirá que você substitua essa configuração.

#### 

As validações de entrega fornecem uma verificação adicional para confirmar que seu público atende aos critérios de entrega no envio de mensagens. Essa configuração é recomendada se o Horário de silêncio, o Intelligent Timing ou o limite de frequência estiverem ativados. Você pode adicionar um segmento ou filtros adicionais para validar no momento em que a mensagem é enviada. Se um usuário não atender às validações de entrega definidas para uma etapa de mensagens, ele sairá do canva na etapa.

![A guia Configurações de entrega para as configurações do componente Mensagem. O Horário de silêncio está ativado, e a caixa de seleção Usar Intelligent Timing está marcada para entregar a mensagem em um horário ideal. 

## 

Todos os usuários que entrarem na etapa Mensagem avançarão para a próxima etapa quando qualquer uma das seguintes condições for atendida:

- Qualquer mensagem foi enviada
- Uma mensagem é limitada em termos de frequência e não é enviada
- Uma mensagem é cancelada
- Um usuário não pode ser acessado pelo canal, portanto, a mensagem não é enviada

{% raw %}
Se um Canva baseado em ação for disparado por uma mensagem SMS recebida, você poderá fazer referência às propriedades de SMS na primeira etapa (etapa de Mensagem) ou em uma etapa de Mensagem que esteja aninhada em uma etapa de Caminho de ação. Por exemplo, na etapa de envio de mensagens, você poderia usar `{{sms.${inbound_message_body}}}` ou `{{sms.${inbound_media_urls}}}`.
{% endraw %}

## 

 Essas propriedades também podem acessar as propriedades de cargas úteis de entrada em canvas disparados por API.  

  Os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% alert note %}

{% endalert %}

 Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

{% raw %}
Por exemplo, considere a seguinte solicitação: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Você poderia adicionar a palavra "sapatos" a uma mensagem com o Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

Também é possível aproveitar [as propriedades de entrada persistente]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) em qualquer etapa do Message para orientar os usuários por meio de etapas personalizadas em todo o fluxo de trabalho do Canva.

### Propriedades do evento

  

  

{% alert important %}

{% endalert %}

Na primeira etapa de mensagem após uma jornada de ação, você pode usar `event_properties` relacionado ao evento referenciado nessa jornada de ação. Você pode ter outras etapas (que não sejam outras jornadas de ação ou etapa de mensagem) entre essa etapa de jornadas de ação e a etapa de mensagem. Observe que você só terá acesso a `event_properties` se a etapa de mensagem puder ser rastreada até uma jornada que não seja "Restante do público" em uma etapa de jornada de ação.

{% alert important %}
 Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente antes da etapa de mensagem que inclui `event_properties`.
{% endalert %}



 

-  
- 
- 



## Análise de dados

Consulte a tabela a seguir para obter as definições das métricas do componente Mensagem: 

| Métrico | Descrição |
| --- | --- |
|  | O número de vezes que a etapa foi inserida. Se o seu canva tiver reelegibilidade e um usuário inserir uma etapa de mensagens duas vezes, duas entradas serão registradas. |
|  | O número de entradas que prosseguiram para a próxima etapa do canva. |
|  | O número total de mensagens que a etapa enviou. Se o seu canva for reelegível e um usuário entrar duas vezes na etapa de Mensagens, duas entradas serão registradas. |
|  | O número de usuários que receberam mensagens dessa etapa. |
|  | O número de vezes que um evento definido ocorreu após a interação ou a visualização de uma mensagem recebida de uma campanha do Braze. Você define esse evento ao criar a campanha. |
|  | A receita total em dólares dos destinatários da campanha dentro da janela de conversão primária definida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


