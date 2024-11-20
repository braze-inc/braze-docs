---
nav_title: Notificaciones push HTML
article_title: Notificaciones push HTML para Android
platform: Android
page_order: 6
description: "Este artículo de referencia explica cómo implementar notificaciones push HTML en tu aplicación Android."
channel:
  - push

---

# Notificaciones push HTML

> Este artículo de referencia explica cómo implementar notificaciones push HTML en tu aplicación Android.

En la versión 3.1.1 del SDK de Braze, se puede enviar HTML a un dispositivo para mostrar texto multiplicador en las notificaciones push.

![Un mensaje push de Android "Mensaje de prueba push multicolor" en el que las letras son de distintos colores, están en cursiva y tienen un color de fondo.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Este ejemplo se muestra con el siguiente HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

El sistema operativo Android limita qué elementos/etiquetas HTML son válidos en las notificaciones push. Por ejemplo, `marquee` no está permitido.

{% alert important %}
Ten en cuenta que la representación del texto multicolor es específica del dispositivo y puede que no se muestre según el dispositivo o la versión de Android.
{% endalert %}

## Aplicación

Para mostrar texto multicolor en la notificación push:

Añade lo siguiente en tu `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**O** 

Añade lo siguiente en tu [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

