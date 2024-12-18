---
nav_title: 대체 웹 푸시 도메인
article_title: 대체 웹 푸시 도메인
platform: Web
page_order: 20
page_type: reference
description: "이 문서에서는 대체 도메인에서 Braze 웹 푸시를 통합하는 방법을 다룹니다."
channel: push

---

# 대체 웹 푸시 도메인

> 웹 푸시를 통합하려면 도메인이 [보안](https://w3c.github.io/webappsec-secure-contexts/)되어야 합니다. 일반적으로 `https`, `localhost` 및 [W3C 푸시 표준](https://www.w3.org/TR/service-workers/#security-considerations)에 정의된 기타 예외를 의미합니다. 또한 도메인 루트에 서비스 종사자를 등록할 수 있거나 최소한 해당 파일의 HTTP 헤더를 제어할 수 있어야 합니다. 이 문서에서는 대체 도메인에서 Braze 웹 푸시를 통합하는 방법을 다룹니다.

_이러한 기준을 모두 충족할 수 없는 경우_ 이 가이드를 사용하여 웹사이트에 푸시 프롬프트 대화 상자를 추가할 수 있는 해결 방법을 설정하세요. 예를 들어, 사용자가 `http`(비보안) 웹사이트 또는 푸시 프롬프트의 표시를 차단하는 브라우저 확장 팝업에서 옵트인하도록 하려는 경우 이 문서가 도움이 될 수 있습니다.

## 주의 사항
웹의 많은 해결 방법과 마찬가지로 브라우저도 계속 발전하고 있으며, 향후 해결 방법이 의도한 대로 작동하지 않을 수도 있습니다.

- 이를 위해서는 다음이 필요합니다:
  - 별도의 보안 도메인(`https://`)을 소유하고 있으며 해당 도메인에 서비스 종사자를 등록할 수 있는 액세스 권한이 있습니다.
  - 푸시 토큰이 동일한 프로필에 연결되도록 웹사이트에 로그인한 사용자가 필요합니다.

{% alert note %}
이러한 방식으로는 Shopify에 대한 푸시를 구현할 수 없습니다. Shopify는 푸시 전송에 필요한 헤더를 제거하는 단계를 수행합니다.
{% endalert %}

## 통합

다음 예제를 명확히 살펴보기 위해 방문자가 `http://insecure.com` 에서 푸시를 등록하는 것을 목표로 `http://insecure.com` 및 `https://secure.com`을 두 개의 도메인으로 사용합니다. 이 예제는 브라우저 확장의 팝업 페이지에 대한 `chrome-extension://` 스키마에도 적용할 수 있습니다.

### 1단계: 프롬프트 흐름 시작

`insecure.com` 에서 URL 매개변수를 사용하여 보안 도메인의 새 창을 열어 현재 로그인한 사용자의 Braze 외부 ID를 전달합니다.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

### 2단계: 푸시 등록하기

이때 `secure.com`에서 동일한 사용자 ID에 대해 Braze 웹 SDK를 초기화하고 웹 푸시에 대한 사용자의 권한을 요청할 수 있는 팝업 창이 열립니다.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### 3단계: 도메인 간 통신(선택 사항)

사용자가 `insecure.com`에서 시작된 이 워크플로우에서 옵트인할 수 있으므로 사용자가 이미 옵트인했는지 여부에 따라 사이트를 수정할 수 있습니다. 이미 푸시 등록을 한 사용자에게 푸시 등록을 요청하는 것은 의미가 없습니다.

아이프레임과 [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API를 사용하여 두 도메인 간에 통신할 수 있습니다. 

**insecure.com**

`insecure.com` 도메인에서 보안 도메인(푸시가 _실제로_ 등록된 곳)에 현재 사용자의 푸시 등록에 대한 정보를 요청합니다.

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

