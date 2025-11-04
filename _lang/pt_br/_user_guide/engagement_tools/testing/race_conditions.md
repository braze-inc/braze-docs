---
nav_title: Condições da corrida
article_title: Condições da corrida
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artigo aborda as práticas recomendadas para evitar que as condições de corrida afetem suas campanhas de mensagens."
toc_headers: h2
---

# Condições da corrida

> Uma condição de corrida ocorre quando um resultado depende da sequência ou do tempo de vários eventos. Por exemplo, se a sequência desejada de eventos for "Evento A" e, em seguida, "Evento B", mas às vezes o "Evento A" vem primeiro e outras vezes o "Evento B" vem primeiro, isso é conhecido como condição de corrida. Isso pode levar a resultados inesperados ou erros porque esses eventos competem para acessar recursos ou dados compartilhados.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

No Braze, as condições de corrida podem ocorrer quando várias ações são acionadas ao mesmo tempo com base em dados ou eventos do usuário. Por exemplo, se um usuário acionar várias campanhas (como se inscrever em um boletim informativo ou fazer uma compra), ele poderá não receber as mensagens na ordem correta.

## Tipos de condições de corrida

Os tipos mais comuns de condições de corrida podem ocorrer quando você estiver fazendo o seguinte:

- Direcionamento para novos usuários
- Uso de vários pontos de extremidade de API
- Combinação de filtros de público e acionadores baseados em ações. 

Considere os cenários a seguir e implemente as práticas recomendadas para evitar essas condições de corrida.

## Cenário 1: Direcionamento para novos usuários

No Braze, uma das condições de corrida mais comuns ocorre com mensagens que visam usuários recém-criados. A ordem esperada dos eventos é:

1. Um usuário é criado;
2. O mesmo usuário é imediatamente direcionado para uma mensagem, realiza um evento personalizado ou registra um atributo personalizado.

No entanto, em alguns casos, o segundo evento será acionado primeiro. Isso significa que uma mensagem está tentando ser enviada a um usuário que ainda não existe. Como resultado, o usuário nunca a recebe. Isso também se aplica a eventos ou atributos, em que o evento ou atributo tenta ser registrado em um perfil de usuário que ainda não foi criado.

### Práticas recomendadas

#### Introduzir atrasos

Depois que um novo usuário é criado, você pode adicionar um atraso antes de enviar qualquer campanha direcionada ou Canvases. Esse atraso permite que o perfil do usuário seja criado e que quaisquer atributos relevantes sejam atualizados, o que pode determinar sua elegibilidade para receber a mensagem.

Por exemplo, depois que um usuário se registra no seu aplicativo, você pode enviar uma oferta promocional após 24 horas. Ou, se você estiver criando um usuário ou registrando um atributo personalizado, poderá adicionar um atraso de um minuto antes de prosseguir com o processo para evitar essa condição de corrida.

Você também pode adicionar esse atraso no [SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration) para o evento personalizado específico que aciona um novo usuário para entrar em um Canvas. 

## Cenário 2: Uso de vários pontos de extremidade de API

{% alert important %}
Usamos o processamento assíncrono para maximizar a velocidade e a flexibilidade. Isso significa que quando as chamadas de API são enviadas para nós separadamente, não podemos garantir que elas serão processadas na ordem em que foram enviadas.
{% endalert %}

Há alguns cenários em que vários endpoints de API também podem resultar nessa condição de corrida, como quando:

- Usar endpoints de API separados para criar usuários e acionar Canvases ou campanhas
- Fazer várias chamadas separadas para o ponto de extremidade `/users/track` para atualizar atributos, eventos ou compras personalizados

Quando as informações do usuário são enviadas para a Braze por meio do [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), elas podem levar alguns segundos para serem processadas. Isso significa que quando as solicitações são feitas simultaneamente aos endpoints `/users/track` e Messaging, como `/campaign/trigger/send`, não há garantia de que as informações do usuário serão atualizadas antes do envio de uma mensagem.

{% alert note %}
Se os atributos do usuário e os eventos forem enviados na mesma solicitação (de `/users/track` ou do SDK), o Braze processará os atributos antes dos eventos ou da tentativa de enviar qualquer mensagem.
{% endalert %}

### Práticas recomendadas

#### Ao usar vários endpoints, envie suas solicitações uma de cada vez

Se estiver usando vários endpoints, tente escalonar as solicitações para que cada uma seja concluída antes do início da próxima. Isso pode reduzir a chance de uma condição de corrida. Por exemplo, se você precisar atualizar os atributos do usuário e enviar uma mensagem, primeiro espere que o perfil do usuário seja completamente atualizado antes de enviar uma mensagem usando um endpoint.

Se você estiver enviando uma solicitação de API de mensagem agendada, essas solicitações deverão ser separadas e um usuário deverá ser criado antes de enviar a solicitação de API agendada.

#### Incluir dados importantes com o acionador

Em vez de usar vários pontos de extremidade, é possível incluir os [atributos do usuário]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) e [as propriedades do acionador]({{site.baseurl}}/api/objects_filters/trigger_properties_object) em uma única chamada de API usando o [ponto de extremidade`campaign/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

Quando esses objetos forem incluídos no acionador, os atributos serão processados primeiro, antes que a mensagem seja acionada, eliminando possíveis condições de corrida. Observe que as propriedades do acionador não atualizam o perfil do usuário, mas são usadas apenas no contexto da mensagem.

#### Use o POST: Ponto de extremidade de rastreamento de usuários (sincronização)

Use o [endpoint`/users/track/sync/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) para registrar eventos e compras personalizados e atualizar os atributos do perfil do usuário de forma síncrona. Usar esse endpoint para atualizar os perfis de usuário ao mesmo tempo e em uma única chamada pode ajudar a evitar possíveis condições de corrida.

{% alert important %}
Esse endpoint está atualmente na versão beta. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar da versão beta.
{% endalert %}

## Cenário 3: Correspondência de acionadores baseados em ações e filtros de público-alvo

Outra condição de corrida comum pode ocorrer se você configurar uma campanha baseada em ação ou o Canvas com o mesmo acionador que o filtro de público-alvo (como um atributo alterado ou um evento personalizado realizado). O usuário pode não estar no público no momento em que executar o evento de acionamento, o que significa que ele não receberá a campanha nem entrará no Canvas.

### Práticas recomendadas

#### Verifique seu público após um atraso

Para evitar o uso de filtros de público-alvo que contenham os critérios de acionamento, recomendamos verificar seu público-alvo antes da entrega. Por exemplo, você pode [usar validações de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) nas etapas do Canvas Message como uma verificação adicional para confirmar que seu público-alvo atende aos critérios de entrega no envio da mensagem. Você também pode aproveitar os critérios de saída do Canvas para sair de qualquer usuário em qualquer ponto durante a jornada do usuário, se ele atender aos seus critérios.

Para campanhas, você pode usar eventos de saída para permitir que as campanhas com um evento de acionamento abortem mensagens para usuários que executam o evento de saída enquanto estão no atraso.

#### Use filtros exclusivos com o evento de acionamento

Ao configurar seus filtros, talvez você queira adicionar um filtro redundante "por precaução". No entanto, essa redundância pode levar a mais problemas. Em vez disso, evite usar qualquer filtro que contenha o acionador quando possível. Esse é o caminho mais seguro para evitar uma condição de corrida.

Por exemplo, se o acionador da campanha for "Has made a purchase" (Fez uma compra) e o filtro de público-alvo for "Has made any purchase" (Fez qualquer compra), essa redundância poderá causar uma condição de corrida. 

#### Evite filtros de público que presumam que o evento de acionamento foi atualizado

Essa prática recomendada é semelhante a evitar filtros redundantes com o evento de acionamento. Normalmente, um filtro que presume que o evento de acionamento é atualizado para o perfil do usuário falhará.

#### Use Liquid aborts (somente atributos)

Em campanhas e etapas do Canvas, use o Liquid aborts para evitar o uso de filtros de público-alvo que contenham os atributos de acionamento na programação de entrada. Por exemplo, digamos que você tenha um atributo de matriz "cores favoritas" e queira segmentar qualquer usuário que atualize a matriz de atributos com qualquer valor e que também tenha a cor "azul" na matriz após a conclusão da atualização. Se você usar os filtros de público neste exemplo, encontrará uma condição de corrida e perderá os usuários que adicionarem "blue" na matriz pela primeira vez.

Nesse caso, você pode implementar um atraso de acionador em uma campanha ou usar uma etapa de Atraso no Canvas para permitir que o perfil do usuário seja atualizado por um período de tempo e, em seguida, usar a seguinte lógica de abortamento do Liquid:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirme como os dados do usuário estão sendo gerenciados

Se houver uma condição de corrida durante a avaliação da entrada do Canvas, os usuários poderão entrar em um Canvas que não deveriam ter entrado. Por exemplo, o perfil do usuário pode ser definido para ser incluído no público e posteriormente atualizado depois que o Canvas enfileirar os usuários para que não sejam mais elegíveis no público. 

Recomendamos confirmar como os dados do usuário são gerenciados e atualizados, especificamente quando e como atributos específicos são atualizados, como por SDK, API, API em lote e outros métodos. Isso pode ajudar a identificar e esclarecer por que um usuário entrou em uma campanha ou Canvas em comparação com quando o perfil de um usuário foi atualizado.
