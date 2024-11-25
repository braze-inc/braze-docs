---
nav_title: Envío de mensajes
article_title: Eliminación de mensajes dentro de la aplicación para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 5
description: "Este artículo de referencia cubre la eliminación de mensajes dentro de la aplicación para tu aplicación Android o FireOS."
channel:
  - in-app messages

---

# Descarte de mensajes

> Este artículo de referencia cubre la eliminación de mensajes dentro de la aplicación para tu aplicación Android o FireOS.

## Desactivar el botón de retroceso

De manera predeterminada, el botón de retroceso del hardware descarta los mensajes dentro de la aplicación de Braze. Este comportamiento puede desactivarse por mensaje mediante [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

En el siguiente ejemplo, `disable_back_button` es un par clave-valor personalizado establecido en el mensaje dentro de la aplicación que indica si el mensaje debe permitir el botón de retroceso para descartar el mensaje:

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Ten en cuenta que si esta función está desactivada, se utilizará en su lugar el comportamiento predeterminado del botón de retroceso del hardware de la actividad anfitriona. Esto puede hacer que el botón Atrás cierre la aplicación en lugar del mensaje dentro de la aplicación que se muestra.
{% endalert %}

## Descartar modal en grifo exterior

El valor predeterminado e histórico es `false`, lo que significa que los clics fuera del modal no lo cerrarán. Si estableces este valor en `true`, el mensaje modal dentro de la aplicación se cancelará cuando el usuario pulse fuera del mensaje dentro de la aplicación. Este comportamiento se puede alternar llamando a:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

