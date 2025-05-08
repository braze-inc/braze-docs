---
nav_title: Conversación push
article_title: Conversación Push para Android
platform: Android
page_order: 5.92
description: "Esta aplicación explica cómo implementar el push de conversaciones de Android en tu aplicación Android."
channel:
  - push

---

# Conversación push

> Esta aplicación explica cómo implementar el push de conversaciones de Android en tu aplicación Android.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

La [iniciativa de personas y conversaciones](https://developer.android.com/guide/topics/ui/conversations) es una iniciativa plurianual de Android que pretende elevar las personas y las conversaciones en las superficies del sistema del teléfono. Esta prioridad se basa en el hecho de que la comunicación y la interacción con otras personas sigue siendo el área funcional más valorada e importante para la mayoría de los usuarios de Android de todos los grupos demográficos.

No se requiere ninguna integración adicional ni cambios en el SDK para utilizar esta característica. Los dispositivos o SDK que no cumplan los requisitos mínimos de versión mostrarán en su lugar una notificación push estándar.

## Requisitos de uso

- Este tipo de notificación requiere la versión 15.0.0 en adelante del SDK de Braze para Android y dispositivos Android a partir de la versión 11. 
- Los dispositivos o SDK no compatibles recibirán como alternativa una notificación push estándar.

Esta característica sólo está disponible a través de la API REST de Braze. Consulta el [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object) para más información.

