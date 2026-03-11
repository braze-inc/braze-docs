---
nav_title: Código personalizado y puente JavaScript
article_title: Código personalizado y puente JavaScript para banners
page_order: 2
page_type: reference
description: "Aprende a utilizar HTML personalizado en banners y el puente JavaScript para registrar clics y desencadenar acciones de Braze."
channel:
  - banners
---

# Código personalizado y puente JavaScript para banners

> Cuando utilices el bloque de editor **de código personalizado** en el compositor de banners, debes llamar`brazeBridge.logClick()`a  desde tu HTML personalizado para registrar los clics. Los banners utilizan el mismo puente JavaScript que los mensajes dentro de la aplicación, por lo que se aplican los mismos métodos y patrones.

Si utilizas HTML personalizado en tu diseño de banner, el SDK de Braze no puede adjuntar automáticamente detectores de clics a los elementos dentro de tu código personalizado. Debes llamar explícitamente a`brazeBridge.logClick()`  para cualquier elemento en el que se pueda hacer clic (enlaces, botones y similares) que desees seguir en los análisis de la campaña.

Por ejemplo, para registrar un clic cuando un usuario pulsa un botón en tu HTML personalizado:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para obtener la referencia completa del puente JavaScript, incluidos todos los métodos disponibles y las opciones de seguimiento de clics, consulta la sección siguiente.

## Puente JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}
