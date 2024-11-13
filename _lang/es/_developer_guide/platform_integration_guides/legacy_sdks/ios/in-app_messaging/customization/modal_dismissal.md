---
nav_title: Descarte de modal
article_title: Desconexión modal de mensajes dentro de la aplicación para iOS
platform: iOS
page_order: 29
description: "Este artículo de referencia trata sobre el cierre modal de la mensajería dentro de la aplicación para tu aplicación de iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Descartar modal por toque externo

El valor predeterminado es `NO`. Determina si el mensaje modal dentro de la aplicación se descartará cuando el usuario pulse fuera del mensaje dentro de la aplicación.

Para habilitar los descartes por toque externo, añade un diccionario llamado `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada booleana `DismissModalOnOutsideTap` y establece el valor `YES`, como se muestra en el siguiente fragmento de código. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

```
<key>Braze</key>
<dict>
  <key>DismissModalOnOutsideTap</key>
  <boolean>YES</boolean>
</dict>
```

También puedes habilitar la característica en tiempo de ejecución configurando `ABKEnableDismissModalOnOutsideTapKey` en `YES` en `appboyOptions`.

| `DismissModalOnOutsideTap` | Descripción |
|----------|-------------|
| `YES`       | Los mensajes modales dentro de la aplicación se descartarán al tocar fuera.     |
| `NO`        | Predeterminado, los mensajes modales dentro de la aplicación no se descartarán al tocar fuera. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }