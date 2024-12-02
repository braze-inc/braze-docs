---
nav_title: Deep links de ação da Braze
article_title: Deep links de ação da Braze
page_order: 100
description: "Este artigo de referência aborda como usar os deep links de ação da Braze para executar ações do SDK nos botões do canal de envio de mensagens."
hidden: true
---

# Deep links de ação da Braze

> As ações da Braze permitem que você use deep links para executar a funcionalidade nativa do SDK.<br><br>O dashboard da Braze inclui várias ações padrão ao clicar (Solicitar permissão para push, Registrar evento personalizado e Registrar atributo personalizado) que podem ser usadas em mensagens no app e cartões de conteúdo.<br><br>Para todas as outras ações, ou para combinar várias ações, use este guia para construir seu próprio deeplink Braze Action.

## Suporte a SDK

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

O esquema de deep link `brazeActions://` pode ser usado sempre que houver uma opção de deep link ou redirecionamento nas mensagens no app e nos cartões de conteúdo.

Para mensagens no app em HTML, use o [`Javascript Bridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) em vez disso, pois os deep links não são compatíveis com tipos de mensagens HTML.

## Esquema

Você pode incluir várias ações `steps` em um tipo de ação `container`. Uma única etapa sem um `container` também é válida.

```json
{
    "type": "container",
    "steps": []
}
```

Um `step` individual contém uma ação `type` e um vetor `args` opcional:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

O esquema de URI do Braze Actions é `brazeActions://v1/{base64encodedJsonString}`.

O JavaScript a seguir mostra como codificar e decodificar a string JSON:

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

## Ações apoiadas

|Tipo|Args|
|--|--|
|`container`|Uma matriz de outras ações a serem executadas|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (opcional)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| N/D |
|`openLink`|1. `url`<br>2. `openInNewTab` (booleano)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## Codificador JSON

Insira uma string JSON para ver o URI `brazeActions://` resultante. Ou digite um URI `brazeActions://` para decodificar seu JSON.

<div><h4>Entrada JSON</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Saída do deep link</h4></div>
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
