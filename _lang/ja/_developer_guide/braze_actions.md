---
nav_title: Braze Actions ディープリンク
article_title: Braze Actions ディープリンク
page_order: 100
description: "このリファレンス記事では、Braze Actions ディープリンクを使用して、メッセージングチャネルボタン内でSDKアクションを実行する方法について説明する。"
hidden: true
---

# Braze Actions ディープリンク

> Braze Actionsを使えば、「ディープリンク」を使ってネイティブSDKの機能を実行できる。<br><br>Braze ダッシュボードには、いくつかの標準的なクリック時アクション (プッシュ通知の権限を要求、カスタムイベントをログに記録、カスタム属性をログに記録) が含まれており、アプリ内メッセージやコンテンツカードで使用することができます。<br><br>その他のすべてのアクション、または複数のアクションを組み合わせる場合は、このガイドを使用して独自のBraze Actionディープリンクを構築する。

## SDKサポート

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

`brazeActions://` ディープリンク・スキームは、アプリ内メッセージやコンテンツ・カード内にディープリンクやリダイレクト・オプションがあれば、どこでも使用できる。

HTML アプリ内メッセージの場合、HTML メッセージタイプではディープリンクはサポートされていないため、代わりに [`Javascript Bridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) を使用してください。

## スキーマ

複数のアクションの `steps` を `container` アクションタイプに含めることができます。`container` を含まない単一のステップも有効です。

```json
{
    "type": "container",
    "steps": []
}
```

個々の `step` には、アクションの `type` とオプションの `args` 配列が含まれています。

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

Braze ActionsのURIスキームは`brazeActions://v1/{base64encodedJsonString}` 。

次のJavaScriptは、JSON文字列のエンコードとデコードの方法を示している：

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

## 対応アクション

|タイプ|引数|
|--|--|
|`container`|実行する他のアクションの配列|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (オプション)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| 該当なし |
|`openLink`|1. `url`<br>2\.`openInNewTab` (boolean)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## JSONエンコーダー

JSON文字列を入力すると、結果の`brazeActions://` URIが表示される。または、`brazeActions://` URIを入力してJSONをデコードする。

<div><h4>JSON入力</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>ディープリンク出力</h4></div>
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
