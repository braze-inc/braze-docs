---
nav_title: Notificações por push silenciosas
article_title: Notificações por push silenciosas para Android
platform: Android
page_order: 3
description: "Este artigo aborda como implementar notificações por push silenciosas em seu aplicativo Android."
channel:
  - push

---

# Notificações por push silenciosas para Android

> As notificações silenciosas permitem que você notifique seu app em segundo plano quando ocorrerem eventos importantes. Talvez haja novas mensagens instantâneas a serem enviadas, novas edições de uma revista a serem publicadas, alertas de notícias de última hora a serem enviados ou o último episódio do programa de TV favorito do usuário pronto para ser baixado para visualização off-line. As notificações silenciosas também podem ser muito mais eficientes do que a busca em segundo plano, pois seu app só é iniciado quando necessário.

## Configurando notificações por push silenciosas

As notificações silenciosas estão disponíveis por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) do Braze. Para aproveitá-los, você precisa definir o sinalizador `send_to_sync` como `true` no [objeto Android push]({{site.baseurl}}/api/objects_filters/messaging/android_object/) e garantir que não haja campos `title` ou `alert` definidos, pois isso causará erros quando usado junto com `send_to_sync`- no entanto, você pode incluir dados `extras` no objeto.

{% alert tip %}
Ao [criar sua mensagem de notificação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message), você pode enviar uma notificação por push silenciosa para o Android enviando uma mensagem com apenas um espaço. Lembre-se de que esse **não** é o método recomendado para o envio de notificações por push, mas pode ser útil em alguns casos.
{% endalert %}

