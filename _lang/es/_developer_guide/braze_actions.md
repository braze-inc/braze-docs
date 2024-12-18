---
nav_title: Vínculos profundos con Acciones Braze
article_title: Vínculos profundos con Acciones Braze
page_order: 100
description: "Este artículo de referencia explica cómo utilizar los enlaces profundos de acción Braze para realizar acciones del SDK dentro de los botones del canal de mensajería."
hidden: true
---

# Vínculos profundos con Acciones Braze

> Las Acciones Braze te permiten utilizar "vínculos profundos" para realizar funciones nativas del SDK.<br><br>El panel de Braze incluye varias acciones estándar al hacer clic (Solicitar permiso push, Registrar evento personalizado y Registrar atributo personalizado) que pueden utilizarse en mensajes dentro de la aplicación y en tarjetas de contenido.<br><br>Para todas las demás acciones, o para combinar varias acciones, utiliza esta guía para construir tu propio enlace profundo de Acción Braze.

## Soporte SDK

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

El esquema de enlace profundo `brazeActions://` puede utilizarse siempre que exista una opción de enlace profundo o de redireccionamiento dentro de los mensajes dentro de la aplicación y de las tarjetas de contenido.

Para los mensajes HTML dentro de la aplicación, utiliza el botón [`Javascript Bridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) ya que los enlaces profundos no son compatibles con los tipos de mensajes HTML.

## Esquema

Puedes incluir varias acciones `steps` dentro de un tipo de acción `container`. También es válido un solo paso sin `container`.

```json
{
    "type": "container",
    "steps": []
}
```

Un `step` individual contiene un `type` de acción y una matriz opcional `args`:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

El esquema URI de las acciones Braze es `brazeActions://v1/{base64encodedJsonString}`.

El siguiente JavaScript muestra cómo codificar y descodificar la cadena JSON:

```javascript
function decode(encoded) {
    const binary = window.atob(encoded.replace(/-/g, '+').replace(/_/g, '/'));
    let bits8 = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bits8[i] = binary.charCodeAt(i);
    }
    const bits16 = new Uint16Array(bits8.buffer);
    return String.fromCharCode(...bits16);
}

/**
 * Returns a url-safe base64 encoded string of the input.
 * Unicode inputs are accepted.
 * Converts a UTF-16 string to UTF-8 to comply with base64 encoding limitations.
 */
function encode(input) {
    // Split the original 16-bit char code into two 8-bit char codes then 
    // reconstitute a new string (of double length) using those 8-bit codes
    // into a UTF-8 string.
    const codeUnits = new Uint16Array(input.length);
    for (let i = 0; i < codeUnits.length; i++) {
        codeUnits[i] = input.charCodeAt(i);
    }
    const charCodes = new Uint8Array(codeUnits.buffer);
    let utf8String = "";
    for (let i = 0; i < charCodes.byteLength; i++) {
        utf8String += String.fromCharCode(charCodes[i]);
    }
    return btoa(utf8String).replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
}
```

## Acciones apoyadas

|Tipo|Args|
|--|--|
|`container`|Una serie de otras acciones a realizar|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (opcional)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| N/A |
|`openLink`|1. `url`<br>2. `openInNewTab` (booleano)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## Codificador JSON

Introduce una cadena JSON para ver la URI resultante `brazeActions://`. O introduce una URI de `brazeActions://` para descodificar su JSON.

<div><h4>Entrada JSON</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Respuesta de vínculos profundos</h4></div>
<textarea id="braze-actions-output" rows="6"></textarea>
<style>
    #braze-actions-input, #braze-actions-output {
        width: 90%;
        border: solid 1px #1f1f1f !important;
        margin-top: 10px;
        border-radius: 4px;
        font-family: courier;
        font-size: 14px;
        padding: 4px;
    }
</style>
<script>
(function(){
    const input = document.getElementById('braze-actions-input');
    const output = document.getElementById('braze-actions-output');
    var debouncer;
    input.oninput = function(event){
        clearTimeout(debouncer);
        debouncer = setTimeout(function(){
            try {
                const jsonString = event.target.value.replace(/^\s+|\s+$/g, '');
                output.value = `brazeActions://v1/${encode(jsonString)}`
            } catch(e){
                output.value = `Invalid JSON`;
            }
        }, 100);
    }
    output.oninput = function(event){
        clearTimeout(debouncer);
        debouncer = setTimeout(function(){
            try {
                const base64 = event.target.value.replace(/^brazeActions:\/\/v\d+\//, '').replace(/\s/g, '');
                const json = JSON.parse(decode(base64));
                input.value = JSON.stringify(json, null, 4);
            } catch(e){
                input.value = `Invalid brazeActions:// link`;
            }
        }, 100);
    }

    input.value = JSON.stringify({
        "type": "container",
        "steps": [{
            "type": "addToSubscriptionGroup",
            "args": ["your-subscription-group-ID-here"]
        }]
    }, null, 2);
    input.dispatchEvent(new Event("input"));

    function decode(encoded) {
        const binary = window.atob(encoded.replace(/-/g, '+').replace(/_/g, '/'));
        let bits8 = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i++) {
        bits8[i] = binary.charCodeAt(i);
        }
        const bits16 = new Uint16Array(bits8.buffer);
        return String.fromCharCode(...bits16);
    }


    function encode(input) {
        const codeUnits = new Uint16Array(input.length);
        for (let i = 0; i < codeUnits.length; i++) {
            codeUnits[i] = input.charCodeAt(i);
        }
        const charCodes = new Uint8Array(codeUnits.buffer);
        let utf8String = "";
        for (let i = 0; i < charCodes.byteLength; i++) {
            utf8String += String.fromCharCode(charCodes[i]);
        }
        return btoa(utf8String).replace(/\+/g, "-").replace(/\//g, "_").replace(/=/g, "");
    }
})();
</script>
