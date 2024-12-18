---
nav_title: Descarte de modal
article_title: Desconexión modal de mensajes dentro de la aplicación para iOS
platform: Swift
page_order: 7
description: "Este artículo de referencia cubre el descarte de modal de mensajería dentro de la aplicación para el SDK Swift."
channel:
  - in-app messages
---

# Descarte de modal

> Para habilitar los descartes por toque externo, puedes modificar la propiedad `dismissOnBackgroundTap` en la estructura `Attributes` del tipo de mensaje dentro de la aplicación que desees personalizar. 

Por ejemplo, si deseas habilitar esta característica para los mensajes dentro de la aplicación con imágenes modales, puedes configurar lo siguiente:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJETIVO-C %}

La personalización a través de `Attributes` no está disponible en Objective-C.

{% endtab %}
{% endtabs %}

El valor predeterminado es `false`. Determina si el mensaje modal dentro de la aplicación se descartará cuando el usuario pulse fuera del mensaje dentro de la aplicación.

| `DismissModalOnOutsideTap` | Descripción |
|----------|-------------|
| `true`         | Los mensajes modales dentro de la aplicación se descartarán al tocar fuera.     |
| `false`        | Predeterminado, los mensajes modales dentro de la aplicación no se descartarán al tocar fuera. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para más detalles sobre la personalización de mensajes dentro de la aplicación, consulta este [artículo](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).