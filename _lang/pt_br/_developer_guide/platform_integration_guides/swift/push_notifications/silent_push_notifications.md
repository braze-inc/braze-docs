---
nav_title: Notificações por push silenciosas
article_title: Notificações por push silenciosas para iOS
platform: Swift
page_order: 4
description: "Este artigo aborda como implementar notificações por push silenciosas do iOS para o SDK SWIFT."
channel:
  - push

---

# Notificações por push silenciosas para iOS

> Notificações por push permitem que você envie notificações do seu app quando eventos importantes ocorrerem. 

Você pode enviar uma notificação por push quando tiver um alerta importante para um usuário. Notificações por push podem também ser silenciosas, não contendo mensagem de alerta ou som, sendo usadas apenas para atualizar a interface do seu app ou disparar trabalho em segundo plano. Notificações por push silenciosas podem acordar seu app de um estado "Suspenso" ou "Não está em execução" para atualizar conteúdo ou executar certas tarefas sem notificar seus usuários.

Braze possui vários recursos que dependem de notificações por push silenciosas:

|Recurso|Experiência do Usuário|
|---|---|
|[Uninstall Tracking]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/uninstall_tracking/) | O usuário recebe um push de rastreamento de desinstalação silenciosa, noturna.|
|[Geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences) | Sincronização silenciosa de geofences do servidor para o dispositivo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configurando notificações por push silenciosas

Para usar notificações por push silenciosas para disparar trabalho em segundo plano, você deve configurar seu app para receber notificações mesmo quando estiver em segundo plano. Para fazer isso, adicione a capacidade de Modos de Fundo usando o painel **Assinatura e Capacidades** ao alvo principal do app no Xcode. Selecione a caixa de seleção **Notificações remotas**.

![O Xcode mostra a caixa de seleção do modo "notificações remotas" em "capacitações".]({% image_buster /assets/img_archive/background_mode.png %} "background mode enabled")

Mesmo com o modo de fundo de notificações remotas ativado, o sistema não iniciará seu app em segundo plano se o usuário tiver forçado o encerramento do aplicativo. O usuário deve iniciar explicitamente o aplicativo ou reiniciar o dispositivo antes que o app possa ser lançado automaticamente em segundo plano pelo sistema.

Para saber mais, consulte as [atualizações de fundo do push](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) e a [documentação](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplicationDelegate_Protocol/index.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:didReceiveRemoteNotification:fetchCompletionHandler:) do site `application:didReceiveRemoteNotification:fetchCompletionHandler:`.

## Enviando notificações por push silenciosas

Para enviar uma notificação por push silenciosa, defina a `content-available` bandeira para `1` em uma carga útil de notificação por push. 

{% alert note %}
O que a Apple chama de notificação remota é apenas uma notificação por push normal com a sinalização `content-available` definida.
{% endalert %}

A `content-available` flag pode ser definida no dashboard da Braze, assim como dentro do nosso [objeto de push da Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) na [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/).

{% alert warning %}
Anexar tanto um título quanto um corpo de texto com `content-available=1` não é recomendado porque pode levar a um comportamento indefinido. Para garantir que uma notificação seja realmente silenciosa, exclua o título e o corpo ao definir o sinalizador `content-available` como `1.`. Para obter mais detalhes, consulte a [documentação oficial da Apple sobre atualizações em segundo plano](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app).
{% endalert %}

![O painel do Braze mostra a caixa de seleção "content-available" (conteúdo disponível) encontrada na guia "settings" (configurações) do criador do push.]({% image_buster /assets/img_archive/remote_notification.png %} "content available" (conteúdo disponível))

Ao enviar uma notificação por push silenciosa, você também pode querer incluir alguns dados na carga útil da notificação, para que seu aplicativo possa referenciar o evento. Isso pode economizar algumas solicitações de rede e aumentar a capacidade de resposta do seu app.

## limitações de notificações silenciosas do iOS

O sistema operacional iOS pode bloquear notificações para alguns recursos. Nota que se você estiver enfrentando dificuldades com esses recursos, o portão de notificações silenciosas do iOS pode ser a causa.

Consulte a documentação sobre o [método de instância](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) e as [notificações não recebidas](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG23) da Apple para obter mais detalhes.

