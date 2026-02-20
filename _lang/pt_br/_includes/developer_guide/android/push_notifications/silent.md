{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configurando notificações por push silenciosas

As notificações silenciosas estão disponíveis por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/) do Braze. Para aproveitá-los, você precisa definir o sinalizador `send_to_sync` como `true` no [objeto Android push]({{site.baseurl}}/api/objects_filters/messaging/android_object/) e garantir que não haja campos `title` ou `alert` definidos, pois isso causará erros quando usado junto com `send_to_sync`- no entanto, você pode incluir dados `extras` no objeto.
