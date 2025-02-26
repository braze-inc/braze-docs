---
nav_title: 브레이즈 액션 딥링크
article_title: 브레이즈 액션 딥링크
page_order: 100
description: "이 참조 문서에서는 Braze 작업 딥링크를 사용하여 메시징 채널 버튼 내에서 SDK 작업을 수행하는 방법을 다룹니다."
hidden: true
---

# 브레이즈 액션 딥링크

> Braze 작업에서는 '딥링크'를 사용하여 기본 SDK 기능을 수행할 수 있습니다.<br><br>Braze 대시보드에는 인앱 메시지 및 콘텐츠 카드에서 사용할 수 있는 몇 가지 표준 클릭 시 작업(푸시 권한 요청, 커스텀 이벤트 기록, 커스텀 속성 기록)이 포함되어 있습니다.<br><br>다른 모든 작업에서 또는 여러 작업을 결합하려면 이 가이드를 사용하여 고유한 Braze 작업 딥링크를 구성하세요.

## SDK 지원

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

`brazeActions://` 딥링크 스키마는 인앱 메시지 및 콘텐츠 카드 내 딥링크 또는 리디렉션 옵션이 있는 모든 곳에서 사용할 수 있습니다.

HTML 인앱 메시지의 경우 대신 [`Javascript Bridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge)를 사용합니다. 딥링크는 HTML 메시지 유형에서 지원되지 않습니다.

## 스키마

`container` 작업 유형 내 여러 개의 작업 `steps`를 포함할 수 있습니다. `container` 없는 단일 단계도 유효합니다.

```json
{
    "type": "container",
    "steps": []
}
```

개별 `step`에는 작업 `type` 및 선택적 `args` 배열이 포함되어 있습니다.

```json
{
    "type": "logCustomEvent",
    "args": ["event name", {"event": ["properties"]}]
}
```

## URI 

Braze 작업 URI 스키마는 `brazeActions://v1/{base64encodedJsonString}`입니다.

다음 자바스크립트는 JSON 문자열을 인코딩하고 디코딩하는 방법을 보여줍니다:

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

## 지원되는 작업

|유형|인수|
|--|--|
|`container`|수행할 다른 작업의 배열|
|`logCustomEvent`|1. `event name`<br>2. `event properties JSON object` (선택 사항)|
|`setEmailNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setPushNotificationSubscriptionType`|`"opted_in" | "subscribed" | "unsubscribed"`|
|`setCustomUserAttribute`|1. `attribute_name`<br>2. `attribute_value`|
|`requestPushPermission`| N/A |
|`openLink`|1. `url`<br>2. `openInNewTab`(부울)|
|`openLinkInWebview`| `url`|
|`addToSubscriptionGroup`| `subscriptionGroupId`|
|`removeFromSubscriptionGroup`| `subscriptionGroupId`|
|`addToCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|
|`removeFromCustomAttributeArray`|1. `attribute_name`<br>2. `attribute_value`|

## JSON 인코더

JSON 문자열을 입력하여 결과 `brazeActions://` URI를 확인합니다. 또는 `brazeActions://` URI를 입력하여 해당 JSON을 디코딩합니다.

<div><h4>JSON 입력</h4></div>
<textarea id="braze-actions-input" rows="12"></textarea>
<div><h4>딥링크 출력</h4></div>
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
