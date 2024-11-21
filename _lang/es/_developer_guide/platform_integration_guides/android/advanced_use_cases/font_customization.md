---
nav_title: Personalización de fuentes
article_title: Personalización de fuentes para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 7
description: "Este artículo de referencia cubre las opciones de personalización de fuentes, como la definición de una familia de fuentes, y muestra cómo hacer referencia a ella en toda tu aplicación Android o FireOS."

---

# Personalización de fuentes

> Este artículo de referencia cubre las opciones de personalización de fuentes, como la definición de una familia de fuentes, y muestra cómo hacer referencia a ella en toda tu aplicación Android o FireOS.

Las fuentes del SDK de Braze pueden configurarse mediante XML utilizando las bibliotecas de AndroidX según [Fuente en XML](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html). Para utilizar tu fuente personalizada con el SDK de Braze, primero tendrás que crear una familia de fuentes.

## Crear una familia tipográfica

A continuación se muestra un ejemplo de definición de familia de fuentes personalizada utilizando la [guía de familias de fuentes](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family). Para este ejemplo, utilizamos la [fuente Bungee Shade](https://fonts.google.com/specimen/Bungee+Shade).

```XML
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

Después de almacenar la definición de la familia tipográfica en `/res/font/bungee_font_family.xml`, podemos referirnos a ella en XML como `@font/bungee_font_family`.

## Hacer referencia a tu familia tipográfica

Ahora que la familia de fuentes está creada, puedes anular los predeterminados de estilo Braze en tu `styles.xml` para incluir referencias a la familia de fuentes.

Por ejemplo, la siguiente sustitución de estilos utilizaría la familia de fuentes `bungee` para todos los mensajes dentro de la aplicación Braze.

```
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
Ambos atributos de estilo `android:fontFamily` y `fontFamily` deben estar configurados para mantener la compatibilidad en todas las versiones del SDK.
{% endalert %}

