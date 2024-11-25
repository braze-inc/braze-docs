---
nav_title: Notificações por push silenciosas
article_title: Notificações por push silenciosas para o FireOS
platform: FireOS
page_order: 3

page_type: reference
description: "Este artigo de referência descreve como enviar notificações por push silenciosas do FireOS e os possíveis casos de uso em que as notificações por push silenciosas podem ser preferíveis."
channel: push

---

# Notificações por push silenciosas

> As notificações silenciosas permitem que você notifique seu app em segundo plano quando ocorrerem eventos importantes. Talvez haja novas mensagens instantâneas a serem enviadas, novas edições de uma revista a serem publicadas, alertas de notícias de última hora a serem enviados ou o último episódio do programa de TV favorito do usuário pronto para ser baixado para visualização off-line. As notificações silenciosas também podem ser muito mais eficientes do que a busca em segundo plano, pois seu app só é iniciado quando necessário.

As notificações silenciosas estão disponíveis por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) do Braze. Para aproveitá-las, você precisa definir o sinalizador `send_to_sync` como `true` no [objeto push do Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) e garantir que não haja campos `title` ou `alert` definidos, pois isso causará erros quando usado junto com `send_to_sync`. No entanto, você pode incluir dados `extras` dentro do objeto.

As notificações silenciosas também estão disponíveis no dashboard. Para enviar uma notificação silenciosa, certifique-se de que os campos de título e corpo da notificação estejam em branco, conforme mostrado na figura:

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Exemplo de notificação por push silenciosa -- Android")

