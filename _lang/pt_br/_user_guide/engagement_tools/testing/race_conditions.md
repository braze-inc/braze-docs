---
nav_title: Condições de corrida
article_title: Condições de corrida
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artigo aborda as práticas recomendadas para evitar que as condições de corrida afetem suas campanhas de mensagens."
toc_headers: h2
---

# Condições de corrida

> Uma condição de corrida ocorre quando um resultado depende da sequência ou do tempo de vários eventos. Por exemplo, se a sequência desejada de eventos for "Evento A" e depois "Evento B", mas às vezes o "Evento A" vem primeiro e outras vezes o "Evento B" vem primeiro, isso é conhecido como condição de corrida. Isso pode levar a resultados inesperados ou erros porque esses eventos competem para acessar recursos ou dados compartilhados.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

No Braze, as condições de corrida podem ocorrer quando várias ações são disparadas ao mesmo tempo com base em dados de usuários ou eventos. Por exemplo, se um usuário disparar várias campanhas (como inscrever-se em um boletim informativo ou fazer uma compra), ele poderá não receber as mensagens na ordem correta.

## Tipos de condições de corrida

Os tipos mais comuns de condições de corrida podem ocorrer quando você estiver fazendo o seguinte:

- Direcionamento a novos usuários
- Uso de vários endpoints de API
- Correspondência entre filtros de público e disparadores baseados em ação. 

Considere os seguintes cenários e implemente as práticas recomendadas para evitar essas condições de corrida.

## Cenário 1: Direcionamento a novos usuários

No Braze, uma das condições de corrida mais comuns ocorre com mensagens direcionadas a usuários recém-criados. A ordem esperada dos eventos é:

1. Um usuário é criado;
2. O mesmo usuário é imediatamente direcionado para uma mensagem, realiza um evento personalizado ou registra um atributo personalizado.

Entretanto, em alguns casos, o segundo evento será disparado primeiro. Isso significa que uma mensagem está tentando ser enviada para um usuário que ainda não existe. Como resultado, o usuário nunca a recebe. Isso também se aplica a eventos ou atribuições, em que o evento ou atributo tenta ser registrado de usuários de eventos em um perfil de usuário que ainda não foi criado.

### Melhores práticas

#### Introduzir postergações

Depois que um novo usuário é criado, é possível adicionar uma postergação antes de enviar qualquer campanha de direcionamento ou Canvas. Essa postergação permite que o perfil do usuário seja criado e que quaisquer atribuições relevantes sejam atualizadas, o que pode determinar sua elegibilidade para receber a mensagem.

Por exemplo, depois que um usuário se registra no seu app, você pode enviar uma oferta promocional após 24 horas. Ou, se estiver criando um usuário ou registrando um atributo personalizado, poderá adicionar uma postergação de um minuto antes de prosseguir com o processo para evitar essa condição de corrida.

Também é possível adicionar essa postergação no [SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration) para o evento personalizado específico que dispara a entrada de um novo usuário em um Canva. 

## Cenário 2: Uso de vários endpoints de API

Há alguns cenários em que vários endpoints da API também podem resultar nessa condição de corrida, como quando:

- Usar endpoints de API separados para criar usuários e disparar Canvas ou campanhas
- Fazer várias chamadas separadas para o endpoint `/users/track` para atualizar atributos, eventos ou compras personalizados

Quando as informações do usuário são enviadas para o Braze usando o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), elas podem ocasionalmente levar alguns segundos para serem processadas. Isso significa que quando as solicitações são feitas simultaneamente aos endpoints `/users/track` e de envio de mensagens, como `/campaign/trigger/send`, não há garantia de que as informações do usuário serão atualizadas antes do envio de uma mensagem.

{% alert note %}
Se as atribuições e os eventos do usuário forem enviados na mesma solicitação (de `/users/track` ou do SDK), o Braze processará os atributos antes dos eventos ou da tentativa de enviar qualquer mensagem.
{% endalert %}

### Melhores práticas

#### Ao usar vários endpoints, envie suas solicitações uma de cada vez

Se estiver usando vários endpoints, tente escalonar as solicitações para que cada uma seja concluída antes do início da próxima. Isso pode reduzir a chance de uma condição de corrida. Por exemplo, se for necessário atualizar as atribuições do usuário e enviar uma mensagem, primeiro espere que o perfil do usuário seja completamente atualizado antes de enviar uma mensagem usando um endpoint.

Se estiver enviando uma solicitação de API de mensagem programada, essas solicitações deverão ser separadas e um usuário deverá ser criado antes de enviar a solicitação de API programada.

#### Incluir dados-chave com o disparador

Em vez de usar vários pontos de extremidade, é possível incluir as [atribuições do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) e as [propriedades do gatilho]({{site.baseurl}}/api/objects_filters/trigger_properties_object) em uma única chamada de API usando o [endpoint `campaign/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

Quando esses objetos forem incluídos no disparador, as atribuições serão processadas primeiro, antes que a mensagem seja disparada, eliminando possíveis condições de corrida. Note que as propriedades do disparador não atualizam o perfil do usuário, mas são usadas apenas no contexto da mensagem.

#### Use o POST: Ponto de extremidade de rastreamento de usuários (sincronização)

Use o [endpoint `/users/track/sync/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) para registrar eventos e compras personalizados e atualizar os atributos do perfil do usuário de forma síncrona. O uso desse endpoint para atualizar os perfis de usuário ao mesmo tempo e em uma única chamada pode ajudar a evitar possíveis condições de corrida.

{% alert important %}
Esse ponto de extremidade está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar da versão beta.
{% endalert %}

## Cenário 3: Correspondência de disparadores baseados em ação e filtros de público

Outra condição de corrida comum pode ocorrer se você configurar uma campanha baseada em ação ou o Canvas com o mesmo disparo que o filtro de público (como um atributo alterado ou a realização de um evento personalizado). O usuário pode não estar no público no momento em que realizar o evento de gatilho, o que significa que ele não receberá a campanha nem entrará no Canva.

### Melhores práticas

#### Verifique seu público após uma postergação

Para evitar o uso de filtros de público que contenham os critérios de disparo, recomendamos verificar seu público antes da entrega. Por exemplo, você pode [usar as validações de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) nas etapas do Canva Message como uma verificação adicional para confirmar que seu público atende aos critérios de entrega no envio da mensagem. Você também pode aproveitar os critérios de saída do Canva para sair de qualquer usuário em qualquer ponto da jornada do usuário, se ele atender aos seus critérios.

Para campanhas, é possível usar eventos de saída para permitir que as campanhas com um evento de gatilho abortem o envio de mensagens aos usuários que realizarem o evento de saída durante a postergação.

#### Use filtros exclusivos com o evento de gatilho

Ao configurar seus filtros, talvez você queira adicionar um filtro redundante "por precaução". No entanto, essa redundância pode levar a mais problemas. Em vez disso, evite usar qualquer filtro que contenha o disparador quando possível. Esse é o caminho mais seguro para evitar uma condição de corrida.

Por exemplo, se o disparo de sua campanha for "Fez uma compra" e o filtro do público for "Fez qualquer compra", essa redundância poderá causar uma condição de corrida. 

#### Evite filtros de público que presumam que o evento de gatilho foi atualizado

Essa prática recomendada é semelhante a evitar filtros redundantes com o evento de gatilho. Normalmente, um filtro que presume que o evento de gatilho é atualizado no perfil do usuário falhará.

#### Use Liquid aborts (somente atribuições)

Nas campanhas e etapas do Canva, use o Liquid aborts para evitar o uso de filtros de público que contenham os atributos de disparo na programação de entrada. Por exemplo, digamos que você tenha um atributo de matriz "cores favoritas" e queira direcionar qualquer usuário que atualize a matriz de atributos com qualquer valor e que também tenha a cor "azul" na matriz após a conclusão da atualização. Se você usar os filtros de público neste exemplo, encontrará uma condição de corrida e perderá os usuários que adicionarem "blue" na matriz pela primeira vez.

Nesse caso, é possível implementar uma postergação de disparo em uma campanha ou usar uma etapa do canva para permitir que o perfil do usuário seja atualizado por um período de tempo e, em seguida, usar a seguinte lógica de abortamento do Liquid:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}


