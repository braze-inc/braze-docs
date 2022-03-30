---
nav_title: Braze Actions Deeplinks
article_title: Braze Actions Deeplink
page_order: 100
description: "Use the `brazeActions://` deeplinks to perform SDK actions within messaging channel buttons"
hidden: true
---

# Braze Actions

Braze Actions allow you to set up In-App Message or Content Card buttons to perform native SDK functionality.

For example, you may want a button to request push permission, log a custom event or attribute, or add/remove a user from a specific subscription group.

## Schema

Multiple action `steps` can be included within a `container` action type. A single step without a `container` is also valid.

```json
{
    "type": "container",
    "steps": []
}
```

An individual `step` contains an an action `type`, and optional `args` array:

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

The Braze Actions URI scheme is `brazeActions://v1/{base64encodedJsonString}`

The following javascript shows how to encode/decode the JSON string:

```javascript
 function decode(encoded) {
    const binary = atob(encoded)
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < bytes.length; i++) {
        bytes[i] = binary.charCodeAt(i);
    }
    return String.fromCharCode(...new Uint16Array(bytes.buffer));
}


function encode(string) {
    const codeUnits = new Uint16Array(string.length);
    for (let i = 0; i < codeUnits.length; i++) {
        codeUnits[i] = string.charCodeAt(i);
    }
    return btoa(String.fromCharCode(...new Uint8Array(codeUnits.buffer))).replace(/=/g, '');
}
```

## Supported Actions

|Type|Args|
|--|--|
|`container`|1. An array of other actions to perform|
|`logCustomEvent`|1. `event name`<br>2. `event properties` (optional)|
|`setEmailNotificationSubscriptionType`|1.  `"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|1. `"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`|n/a|
|`openLink`|1. `url`<br>2. openInNewTab (`boolean`)|
|`openLinkInWebview`|1. `url`|
|`addToSubscriptionGroup`|1. `subscriptionGroupId`|
|`removeFromSubscriptionGroup`|1. `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## JSON Encoder

Enter a JSON string to see the resulting `brazeActions://` URI. Or, enter a `brazeActions://` URI to decode its JSON.

<div>Input:</div>
<textarea id="braze-actions-input"></textarea>
<div>Output:</div>
<textarea id="braze-actions-output"></textarea>
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
                const jsonString = event.target.value.replace(/\s/g, '');
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

    function decode(encoded) {
        const binary = atob(encoded)
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < bytes.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }
        return String.fromCharCode(...new Uint16Array(bytes.buffer));
    }


    function encode(string) {
        const codeUnits = new Uint16Array(string.length);
        for (let i = 0; i < codeUnits.length; i++) {
            codeUnits[i] = string.charCodeAt(i);
        }
        return btoa(String.fromCharCode(...new Uint8Array(codeUnits.buffer))).replace(/=/g, '');
    }
})();
</script>
