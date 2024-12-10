---
nav_title: Guia de atualização do Android 13
article_title: Guia de atualização do Android 13
page_order: 9
platform: 
  - Android
  - FireOS
description: "Este artigo aborda o Android 13, as atualizações do SDK, as alterações na permissão push, a compatibilidade do SDK e muito mais."
---
<br>

# Guia para fazer upgrade do Android 13

> Este guia descreve as alterações relevantes introduzidas no Android 13 (2022) e as etapas de upgrade necessárias para a integração de seu SDK da Braze para Android.

Consulte a [documentação do desenvolvedor do Android 13](https://developer.android.com/about/versions/13) para obter um guia de migração completo.

## Android 13 Braze SDK

Para se preparar para o Android 13, faça o upgrade do SDK da Braze para a [versão mais recente (v21.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300). Ao fazer isso, você terá acesso ao nosso novo [ recurso de push primer "sem código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

## Alterações no Android 13

### Permissão de push {#push-permission}

O Android 13 introduz uma [grande mudança](https://developer.android.com/about/versions/13/changes/notification-permission) na forma como os usuários gerenciam os apps que enviam notificações por push. No Android 13, os apps precisam obter permissão antes que as notificações por push possam ser exibidas. 

![Uma mensagem push do Android perguntando "Allow Kitchenerie to send you notifications?" (Permitir que o Kitchenerie envie notificações para você) com dois botões "Allow" (Permitir) e "Don't allow" (Não permitir) na parte inferior da mensagem.]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

Essa nova permissão segue um padrão semelhante ao do iOS e do Web push, em que você só tem uma tentativa de obter permissão. Se um usuário escolher `Don't Allow` ou ignorar o prompt, seu app não poderá solicitar permissão novamente.

Note que os apps recebem uma [isenção](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility) para os usuários que já tinham as notificações por push ativadas antes da atualização para o Android 13. Esses usuários [continuarão elegíveis](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps) para receber push quando atualizarem para o Android 13, sem precisar solicitar permissão.

#### Tempo de solicitação de permissão {#push-permission-timing}

**Direcionamento para o Android 13**

Os apps direcionados ao Android 13 podem controlar quando solicitar permissão e mostrar o prompt push nativo. 

Se o seu usuário fizer upgrade do Android 12 para o 13, seu aplicativo estiver instalado anteriormente e você já estiver enviando notificações por push, o sistema automaticamente concederá previamente a nova permissão de notificação a todos os aplicativos elegíveis. Em outras palavras, esses apps podem continuar a enviar notificações aos usuários, e os usuários não veem uma solicitação de permissão em tempo de execução.

Para obter mais detalhes sobre isso, consulte a Documentação do desenvolvedor do Android para obter [efeitos sobre atualizações de apps existentes](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps).

**Direcionamento para o Android 12 ou anterior**

Se o seu aplicativo ainda não estiver direcionado ao Android 13 e um novo usuário no Android 13 instalar o seu aplicativo, ele verá automaticamente um prompt de permissão por push quando o aplicativo criar o primeiro canal de notificação (via `notificationManager.createNotificationChannel`). Os usuários que já têm o seu app instalado e fazem upgrade para o Android 13 nunca recebem uma solicitação e recebem automaticamente a permissão push.

{% alert note %}
O SDK da Braze v23.0.0 cria automaticamente um canal de notificação padrão se ainda não existir um quando uma notificação por push for recebida. Se você não estiver direcionando o Android 13, isso fará com que o prompt de permissão por push seja exibido, o que é necessário para mostrar a notificação.
{% endalert %}

## Preparação para o Android 13 {#next-steps}

É altamente recomendável que o seu app tenha como alvo o Android 13 para controlar quando a permissão push é solicitada aos usuários.

Isso permitirá que você otimize suas [taxas de aceitação push](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps) solicitando aos usuários em momentos mais apropriados e levará a uma melhor experiência do usuário em como e quando seu app pede permissão push.

Para começar a usar nosso novo [ recurso de push primer "sem código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/), faça upgrade do SDK do Android para a [versão mais recente (v23.0.0+)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300).

