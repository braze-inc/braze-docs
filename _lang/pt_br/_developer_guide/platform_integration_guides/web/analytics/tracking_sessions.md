---
nav_title: Sessões de rastreamento
article_title: Sessões de rastreamento para a Web
platform: Web
page_order: 0
description: "Este artigo de referência aborda como rastrear sessões para a Web."

---

# Sessões de rastreamento

> O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que levam em conta a duração da sessão e a contagem de sessões visualizáveis no dashboard do Braze com base na seguinte semântica de sessão.

## Ciclo de vida da sessão

Por padrão, as sessões começam quando `braze.openSession()` é chamado pela primeira vez e permanecem abertas até pelo menos 30 minutos de inatividade. Isso significa que, se o usuário sair do site e retornar menos de 30 minutos depois, a mesma sessão continuará. Se eles retornarem após os 30 minutos terem expirado, um ponto de dados de "fechar sessão" será gerado automaticamente para o tempo em que eles não navegaram, e uma nova sessão será aberta.

{% alert note %}
Se precisar forçar uma nova sessão, basta mudar de usuário.
{% endalert %}

## Personalização do tempo limite da sessão

Para personalizar o tempo limite da sessão, passe a opção `sessionTimeoutInSeconds` para sua função [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize). O valor mínimo para `sessionTimeoutInSeconds` é 1 segundo.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

Se você tiver definido um tempo limite da sessão, a semântica da sessão se estenderá até esse tempo limite personalizado.

## Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até **App Usage (Uso do aplicativo** ) no perfil do usuário. Você pode confirmar que o rastreamento de sessão está funcionando verificando se a métrica da sessão aumenta quando você espera que isso aconteça.

![Um componente de perfil de usuário que mostra quantas sessões ocorreram, quando o app foi usado pela primeira vez e quando foi usado pela última vez.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

