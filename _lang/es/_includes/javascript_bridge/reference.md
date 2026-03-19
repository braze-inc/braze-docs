Los mensajes y banners HTML personalizados dentro de la aplicación admiten un «puente» JavaScript para interactuar con el SDK de Braze, lo que te permite desencadear acciones personalizadas de Braze cuando los usuarios realizan clics en elementos con enlaces o realizan alguna otra forma de interacción con tu contenido. Estos métodos existen con la variable global `brazeBridge` o `appboyBridge`.

{% alert important %}
Braze recomienda utilizar la variable global `brazeBridge`. La variable global `appboyBridge` está obsoleta pero seguirá funcionando para los usuarios existentes. Si estás utilizando `appboyBridge`, te sugerimos que migres a `brazeBridge`. <br><br> `appboyBridge` quedó obsoleto en las siguientes versiones del SDK:<br><br>
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Por ejemplo, para registrar un atributo personalizado y un evento personalizado, y luego cerrar el mensaje, puedes utilizar el siguiente JavaScript en tu HTML personalizado:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### Métodos puente de JavaScript {#bridge}

Los siguientes métodos JavaScript son compatibles con el HTML personalizado para mensajes dentro de la aplicación y banners:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
No puedes hacer referencia a Liquid para insertar <code>customAttributes</code> en métodos Bridge de JavaScript.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

### Seguimiento de clics en botones

Utiliza el`brazeBridge.logClick(button_id)`método para realizar el seguimiento de los clics en tu HTML personalizado.

{% alert note %}
**Banners:** Solo se admite`brazeBridge.logClick()`  (sin argumentos). Los ID de botones y el seguimiento de botones personalizados solo son compatibles con los mensajes dentro de la aplicación.
{% endalert %}

Para los mensajes dentro de la aplicación, puedes realizar el seguimiento mediante programación de «Botón 1», «Botón 2» y «Clics en el cuerpo» utilizando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')`, o `brazeBridge.logClick()`, respectivamente.

| Clics     | Método                       | Apoyado |
| ---------- | ---------------------------- | --------- |
| Clic en el cuerpo | `brazeBridge.logClick()`    | Mensajes y banners dentro de la aplicación |
| Botón 1   | `brazeBridge.logClick('0')` | Solo mensajes dentro de la aplicación |
| Botón 2   | `brazeBridge.logClick('1')` | Solo mensajes dentro de la aplicación |
| Seguimiento de botones personalizados |`brazeBridge.logClick('your custom name here')`| Solo mensajes dentro de la aplicación |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En el caso de los mensajes dentro de la aplicación, puedes realizar el seguimiento de varios eventos de clics en botones por impresión. Por ejemplo, para cerrar un mensaje y registrar un clic en el botón 2:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

También puede hacer un seguimiento de los nuevos nombres de botones personalizados (hasta 100 nombres únicos por campaña). Por ejemplo, `brazeBridge.logClick('blue button')` o `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Cuando utilices métodos JavaScript dentro de un`onclick`atributo, envuelve los valores de cadena entre comillas simples para evitar conflictos con el atributo HTML entre comillas dobles.
{% endalert %}

#### Limitaciones (solo mensajes dentro de la aplicación)

- Puedes tener hasta 100 ID de botón únicos por campaña.
- Los identificadores de los botones pueden tener hasta 255 caracteres cada uno.
- Los identificadores de botón sólo pueden incluir letras, números, espacios, guiones y guiones bajos.
