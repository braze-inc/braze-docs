---
nav_title: Actions deeplink de Braze
article_title: Actions deeplink de Braze
page_order: 100
description: "Cet article de référence explique comment utiliser les liens profonds d’action Braze pour effectuer des actions SDK dans les boutons du canal de communication."
hidden: true
---

# Actions deeplink de Braze

> Les actions de Braze vous permettent d’utiliser des « deeplinks » pour exécuter la fonctionnalité de SDK natif.<br><br>Le tableau de bord de Braze comprend plusieurs actions lors du clic standard (demande de permission pour les notifications push, enregistre l’événement personnalisé et enregistre l’attribut personnalisé) qui peuvent être utilisées dans les messages in-app et les cartes de contenu.<br><br>Pour toutes les autres actions, ou pour combiner plusieurs actions, utilisez ce Guide pour créer votre propre action deeplink de Braze.

## Support SDK

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Le schéma deeplink `brazeActions://` peut être utilisé partout où un deeplink ou une option de redirection existe dans les messages in-app et les cartes de contenu.

Pour les messages in-app au format HTML, utilisez plutôt l'icône [`Javascript Bridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) car les liens profonds ne sont pas pris en charge dans les types de messages HTML.

## Schéma

Vous pouvez inclure plusieurs actions `steps` dans un type d’action `container`. Une seule étape sans `container` est également valide.

```json
{
    "type": "container",
    "steps": []
}
```

Une `step` individuelle correspond à une action `type` et un tableau `args` facultatif :

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

Le schéma URI des actions Braze est `brazeActions://v1/{base64encodedJsonString}`.

Le JavaScript suivant montre comment encoder et décoder la chaîne de caractères JSON :

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

## Actions prises en charge

|Type|Args|
|--|--|
|`container`|Éventail d’autres actions à réaliser|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (facultatif)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| S.O. |
|`openLink`|1. `url`<br>2. `openInNewTab` (booléen)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## Encodeur JSON

Saisissez une chaîne de caractères JSON pour voir les résultats `brazeActions://` URI. Ou saisissez un `brazeActions://` URI pour décoder son JSON.

<div><h4>Entrée JSON</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>Sortie Deeplink</h4></div>
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
})() ;
</script>
