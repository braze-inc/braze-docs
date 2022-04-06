---
nav_title: Braze Actions Deeplinks
article_title: Braze Actions Deeplink
page_order: 100
description: "Use the `brazeActions://` deeplinks to perform SDK actions within messaging channel buttons"
hidden: true
---

# Braze Actions

Braze Actions let you use "deeplinks" to perform native SDK functionality.

The Braze dashboard includes a few out-of-the-box actions (Request Push Permission, Log Custom Event, and Log Custom Attribute) which can be used in In-App Messages and Content Cards.

For all other actions, or to combine multiple actions, use this guide to construct your own Braze Action deeplink.

## SDK Support

{% sdk_min_versions ios:5.1.0 android:19.1.0 web:4.0.0 %}

The `brazeActions://` deeplink scheme can be used wherever a deeplink/redirect option exists within In-App Messages and Content Cards.

For HTML In-App Messages, use the [`Javascript Bridge`](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) instead as deeplinks are not supported in HTML message types.

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

/**
 * Returns an url-safe base64 encoded string of the input.
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

## Supported Actions

|Type|Args|
|--|--|
|`container`|1. An array of other actions to perform|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (optional)|
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

<div>JSON Input:</div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div>Deeplink Output:</div>
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

    input.value = JSON.stringify({
        "type": "container",
        "steps": [{
            "type": "addToSubscriptionGroup",
            "args": ["your-subscription-group-ID-here"]
        }]
    }, null, 2);
    input.dispatchEvent(new Event("input"));

    function decode(encoded) {
        const binary = atob(encoded)
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < bytes.length; i++) {
            bytes[i] = binary.charCodeAt(i);
        }
        return String.fromCharCode(...new Uint16Array(bytes.buffer));
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
