---
nav_title: Condições de corrida
article_title: Condições de corrida
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artigo aborda as práticas recomendadas para evitar que as condições de corrida afetem suas campanhas de mensagens."

---

# Condições de corrida

> Uma condição de corrida é um conceito em que um resultado depende da sequência ou do tempo de outros eventos. 

Por exemplo, se a sequência desejada de eventos for "Evento A" e depois "Evento B", mas às vezes o "Evento A" vem primeiro e outras vezes o "Evento B" vem primeiro, isso é conhecido como condição de corrida.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

## Direcionamento a novos usuários

No Braze, uma das condições de corrida mais comuns ocorre com mensagens direcionadas a usuários recém-criados. Aqui, a ordem esperada dos eventos é:

1. Um usuário é criado;
2. O mesmo usuário é imediatamente direcionado para uma mensagem, realiza um evento personalizado ou registra um atributo personalizado.

Entretanto, em alguns casos, o segundo evento será disparado primeiro. Isso significa que uma mensagem está tentando ser enviada a um usuário que ainda não foi criado e, como resultado, o usuário nunca a recebe. O mesmo se aplica a eventos ou atribuições, em que o evento ou atributo está tentando ser registrado de usuários de eventos que ainda não existem.

## Uso de vários endpoints de API

Há alguns cenários em que vários endpoints da API também podem resultar nessa condição de corrida, como quando:

- Usar endpoints de API separados para criar usuários e disparar Canvas ou campanhas
- Fazer várias chamadas separadas para o endpoint `/users/track` para atualizar atributos, eventos ou compras personalizados

Quando as informações do usuário são enviadas para a Braze por meio do endpoint `/users/track`, elas podem levar alguns segundos para serem processadas. Como resultado, quando são feitas solicitações aos endpoints `/users/track` e [de envio de mensagens][4] ao mesmo tempo, atualmente não há garantia de que as informações do usuário serão atualizadas antes do envio de uma mensagem.

Em ambos os cenários anteriores, se essas solicitações forem feitas na mesma solicitação de API, não haverá problema.

{% alert note %}
Se as atribuições e os eventos do usuário forem enviados na mesma solicitação (de `/users/track` ou do SDK), o Braze processará os atributos antes dos eventos ou da tentativa de enviar qualquer mensagem.
{% endalert %}

Note que, se estiver enviando uma solicitação de API de mensagem programada, essas solicitações deverão ser separadas e um usuário deverá ser criado antes de enviar a solicitação de API programada.

### Evitando a condição de corrida

Uma maneira de evitar essa condição de corrida é adicionar uma postergação - cerca de um minuto - entre a criação de um usuário e o direcionamento desse usuário pelo seu Canva ou campanha, ou a tentativa de registro de usuários de eventos para esse perfil de usuário.

Da mesma forma, você pode usar o objeto [`Attributes`][1] para adicionar, criar ou atualizar um usuário e, em seguida, direcioná-lo usando o [endpoint`/canvas/trigger/send` ][2] ou [`/campaign/trigger/send`.][3] Essa solicitação da API processará o objeto `attributes` antes de direcionar os usuários.

As atribuições incluídas nesse objeto serão processadas antes que o Braze comece a enviar a campanha. Se o sinalizador `send_to_existing_only` estiver definido como false e não existir um `external_user_id` no banco de dados do Braze, criaremos um perfil de usuário para o `external_user_id` e processaremos as atribuições associadas ao perfil de usuário antes que o Braze comece a enviar a campanha. Observe também que, se o sinalizador `send_to_existing_only` estiver definido como false, o objeto de atribuição deverá ser incluído para criar o usuário. O sinalizador `send_to_existing_only` não pode ser usado com aliases de usuário.

## Correspondência de disparadores baseados em ação e filtros de público

Outra condição de corrida comum pode ocorrer se você configurar uma campanha baseada em ação ou o Canvas com o mesmo disparo que o filtro de público (como um atributo alterado ou a realização de um evento personalizado). O usuário pode não estar no público no momento em que realizar o evento de gatilho, o que significa que ele não receberá a campanha nem entrará no Canva. Nesse caso, a Braze recomenda que você evite configurar seu disparador para corresponder ao filtro de público. 

### Evitando a condição de corrida

Uma maneira de evitar essa condição de corrida pode ser adicionar uma postergação de mais de um minuto para permitir que os usuários tenham tempo suficiente para entrar no Canva.

[1]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[3]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[4]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
