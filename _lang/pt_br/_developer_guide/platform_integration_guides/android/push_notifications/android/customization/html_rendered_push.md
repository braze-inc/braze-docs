---
nav_title: Notificações por push em HTML
article_title: Notificações por push em HTML para Android
platform: Android
page_order: 6
description: "Este artigo de referência aborda como implementar notificações por push em HTML em seu aplicativo Android."
channel:
  - push

---

# Notificações por push em HTML

> Este artigo de referência aborda como implementar notificações por push em HTML em seu aplicativo Android.

Na versão 3.1.1 do SDK da Braze, o HTML pode ser enviado a um dispositivo para renderizar o texto multiplicador nas notificações por push.

![Uma mensagem push do Android "Multicolor Push test message" em que as letras são de cores diferentes, em itálico e com uma cor de fundo.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Esse exemplo é renderizado com o seguinte HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

O sistema operacional Android limita quais elementos/tags HTML são válidos nas notificações por push. Por exemplo, `marquee` não é permitido.

{% alert important %}
Observe que a renderização de texto multicolorido é específica do dispositivo e pode não ser exibida com base no dispositivo ou na versão do Android.
{% endalert %}

## Implementação

Para renderizar texto multicolorido em uma notificação por push:

Adicione o seguinte em `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**OU** 

Adicione o seguinte em seu [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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

