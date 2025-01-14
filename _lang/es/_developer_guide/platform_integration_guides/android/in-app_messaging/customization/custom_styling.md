---
nav_title: Estilo personalizado
article_title: Estilo personalizado de mensajes dentro de la aplicación para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Este artículo de referencia trata del estilo personalizado de la mensajería dentro de la aplicación para tu aplicación Android o FireOS."
channel:
  - in-app messages

---

# Estilo personalizado

> Los elementos de la interfaz de usuario de Braze vienen con un aspecto predeterminado que se ajusta a las directrices de la interfaz de usuario estándar de Android y proporciona una experiencia sin fisuras. Este artículo de referencia trata del estilo personalizado de la mensajería dentro de la aplicación para tu aplicación Android o FireOS.

Puedes ver los estilos predeterminados en el archivo del SDK de Braze [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml):

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

Si lo prefieres, puedes anular estos estilos para crear un aspecto que se adapte mejor a tu aplicación.

Para anular un estilo, cópialo en su totalidad en el archivo `styles.xml` de tu proyecto y haz modificaciones. Debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados. Ten en cuenta que estos estilos personalizados son para cambios en elementos individuales de la interfaz de usuario, no para cambios generales en los diseños. Los cambios a nivel de diseño deben gestionarse con vistas personalizadas.

{% alert note %}
Puedes personalizar algunos colores directamente en tu campaña Braze sin modificar el XML. Ten en cuenta que los colores establecidos en el panel de Braze anularán los colores que establezcas en cualquier otro lugar.
{% endalert %}

## Fuente personalizada

Braze permite configurar una fuente personalizada utilizando la [guía de familias de fuentes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Para utilizarlo, anula el estilo para el texto del mensaje, los encabezados y el texto del botón y utiliza el atributo `fontFamily` para indicar a Braze que utilice tu familia de fuentes personalizada.

Por ejemplo, para actualizar la fuente del texto de tu botón de mensajes dentro de la aplicación, anula el estilo `Braze.InAppMessage.Button` y haz referencia a tu familia de fuentes personalizada. El valor del atributo debe apuntar a una familia de fuentes de tu directorio `res/font`.

Aquí tienes un ejemplo truncado con una familia de fuentes personalizada, `my_custom_font_family`, a la que se hace referencia en la última línea:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Aparte del estilo `Braze.InAppMessage.Button` para el texto de los botones, el estilo para el texto de los mensajes es `Braze.InAppMessage.Message` y el estilo para las cabeceras de los mensajes es `Braze.InAppMessage.Header`. Si quieres utilizar tu familia de fuentes personalizada en todo el texto posible de los mensajes dentro de la aplicación, puedes establecer tu familia de fuentes en el estilo `Braze.InAppMessage`, que es el estilo padre de todos los mensajes dentro de la aplicación.

{% alert important %}
Al igual que con otros estilos personalizados, debes copiar todo el estilo en tu archivo local `styles.xml` para que todos los atributos estén correctamente configurados.
{% endalert %}

## Establecer una orientación fija

Para establecer una orientación fija para un mensaje dentro [de la aplicación, establece primero una escucha personalizada del administrador de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/). A continuación, llama a `setOrientation()` sobre el objeto `IInAppMessage` en el método delegado `beforeInAppMessageDisplayed()`:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Para dispositivos de tableta, los mensajes dentro de la aplicación aparecerán en el estilo de orientación preferido por el usuario, independientemente de la orientación real de la pantalla.

