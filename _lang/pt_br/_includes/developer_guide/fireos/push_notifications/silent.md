{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configurando notificações por push silenciosas

As notificações silenciosas estão disponíveis por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) do Braze. Para aproveitá-las, você precisa definir o sinalizador `send_to_sync` como `true` no [objeto push do Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) e garantir que não haja campos `title` ou `alert` definidos, pois isso causará erros quando usado junto com `send_to_sync`. No entanto, você pode incluir dados `extras` dentro do objeto.

As notificações silenciosas também estão disponíveis no dashboard. Para enviar uma notificação silenciosa, certifique-se de que os campos de título e corpo da notificação estejam em branco, conforme mostrado na figura:

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android")
