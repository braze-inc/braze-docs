---
nav_title: Pares clave-valor
article_title: Pares clave-valor de mensajes dentro de la aplicación para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "Este artículo de referencia trata de los pares clave-valor de la mensajería dentro de la aplicación para tu aplicación Android o FireOS."
channel:
  - in-app messages

---

# Pares clave-valor

> Este artículo de referencia trata de los pares clave-valor de la mensajería dentro de la aplicación para tu aplicación Android o FireOS.

Los objetos de mensaje dentro de la aplicación pueden llevar pares clave-valor como `extras`. Se especifican en el panel, en **Configuración**, al crear una campaña de mensajes dentro de la aplicación. Se pueden utilizar para enviar datos con un mensaje dentro de la aplicación para que la aplicación los gestione posteriormente.

Llama a lo siguiente cuando obtengas un objeto de mensaje dentro de la aplicación para recuperar sus extras:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

Consulta este [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) para más información.

