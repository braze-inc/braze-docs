{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## 푸시 프로토콜

웹 푸시 알림은 대부분의 주요 브라우저에서 지원하는 [W3C 푸시 표준](http://www.w3.org/TR/push-api/)을 사용하여 구현됩니다. 특정 푸시 프로토콜 표준 및 브라우저 지원에 대한 자세한 내용은 [Apple](https://developer.apple.com/notifications/safari-push-notifications/) [Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) 및 [Microsoft의](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/) 리소스를 참조하세요.

## 푸시 알림 설정하기

### 1단계: 서비스 종사자 구성하기

프로젝트의 `service-worker.js` 파일에 다음 스니펫을 추가하고 초기화 옵션을 [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 초기화 옵션을 `true` 로 설정합니다.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
웹 서버는 서비스 종사자 파일을 제공할 때 `Content-Type: application/javascript`를 반환해야 합니다. 또한 서비스 종사자 파일 이름이 `service-worker.js` 가 아닌 경우 `serviceWorkerLocation` [초기화 옵션을](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) 사용해야 합니다.
{% endalert %}

### 2단계: 브라우저 등록

브라우저에서 푸시 알림을 받을 수 있도록 사용자에게 푸시 권한을 즉시 요청하려면 `braze.requestPushPermission()` 으로 전화하세요. 먼저 브라우저에서 푸시가 지원되는지 테스트하려면 `braze.isPushSupported()` 으로 문의하세요.

푸시 권한을 요청하기 전에 사용자에게 [소프트 푸시 프롬프트를 보내]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web) 푸시 관련 UI를 직접 표시할 수도 있습니다.

{% alert important %}
MacOS의 경우 권한이 부여된 경우에도 푸시 알림을 표시하려면 **시스템 설정 > 알림에서** 최종 사용자가 **Google 크롬과** **Google 크롬 도우미(알림)를** 모두 인에이블먼트해야 합니다.
{% endalert %}

### 3단계: `skipWaiting` 사용 안 함(선택 사항)

Braze 서비스 종사자 파일은 설치 시 자동으로 `skipWaiting` 으로 호출됩니다. 이 기능을 비활성화하려면 Braze를 가져온 후 서비스 종사자 파일에 다음 코드를 추가하세요:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## 사용자 탈퇴하기

사용자를 탈퇴하려면 `braze.unregisterPush()` 으로 문의하세요.

{% alert important %}
최신 버전의 Safari 및 Firefox에서는 버튼 클릭 핸들러 또는 소프트 푸시 프롬프트와 같이 수명이 짧은 이벤트 핸들러에서 이 메서드를 호출해야 합니다. 이는 푸시 등록에 대한 [Chrome의 사용자 환경 모범 사례](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)와 일관됩니다.
{% endalert %}

## 대체 도메인

웹 푸시를 통합하려면 도메인이 [보안](https://w3c.github.io/webappsec-secure-contexts/)되어야 합니다. 일반적으로 `https`, `localhost` 및 [W3C 푸시 표준](https://www.w3.org/TR/service-workers/#security-considerations)에 정의된 기타 예외를 의미합니다. 또한 도메인 루트에 서비스 종사자를 등록할 수 있거나 최소한 해당 파일의 HTTP 헤더를 제어할 수 있어야 합니다. 이 문서에서는 대체 도메인에서 Braze 웹 푸시를 통합하는 방법을 다룹니다.

### 사용 사례

[W3C 푸시 표준에](https://www.w3.org/TR/service-workers/#security-considerations) 설명된 모든 기준을 충족할 수 없는 경우 이 방법을 사용하여 대신 웹사이트에 푸시 프롬프트 대화 상자를 추가할 수 있습니다. 이는 사용자가 `http` 웹사이트나 브라우저 확장 프로그램 팝업에서 옵트인하도록 하여 푸시 안내 메시지가 표시되지 않도록 하려는 경우에 유용할 수 있습니다.

### 고려 사항

웹 브라우저는 다른 많은 해결 방법과 마찬가지로 계속 발전하고 있으며, 이 방법은 향후에는 실행되지 않을 수도 있습니다. 계속하기 전에 다음 사항을 확인하세요:

- 별도의 보안 도메인(`https://`)을 소유하고 있으며 해당 도메인에 서비스 종사자를 등록할 수 있는 권한이 있습니다.
- 사용자가 웹사이트에 로그인하면 푸시 토큰이 올바른 프로필과 일치하는지 확인합니다.

{% alert important %}
이 방법을 사용하여 Shopify에 대한 푸시 알림을 구현할 수 없습니다. Shopify는 푸시 전송에 필요한 헤더를 자동으로 제거합니다.
{% endalert %}

### 대체 푸시 도메인 설정하기

다음 예제를 명확히 살펴보기 위해 방문자가 `http://insecure.com` 에서 푸시를 등록하는 것을 목표로 `http://insecure.com` 및 `https://secure.com`을 두 개의 도메인으로 사용합니다. 이 예제는 브라우저 확장의 팝업 페이지에 대한 `chrome-extension://` 스키마에도 적용할 수 있습니다.

#### 1단계: 프롬프트 흐름 시작

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

#### 2단계: 푸시 등록하기

이때 `secure.com`에서 동일한 사용자 ID에 대해 Braze 웹 SDK를 초기화하고 웹 푸시에 대한 사용자의 권한을 요청할 수 있는 팝업 창이 열립니다.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### 3단계: 도메인 간 통신(선택 사항)

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

## 자주 묻는 질문(FAQ)

### 서비스 작업자

#### 루트 디렉터리에 서비스 워커를 등록할 수 없으면 어떻게 하나요?

기본적으로 서비스 종사자는 등록된 동일한 디렉토리 내에서만 사용할 수 있습니다. 예를 들어 서비스 종사자 파일이 `/assets/service-worker.js`에 있는 경우 `example.com/assets/*` 또는 `assets` 폴더의 하위 디렉토리에만 등록할 수 있으며 홈 페이지(`example.com/`)에는 등록할 수 없습니다. 따라서 서비스 종사자를 루트 디렉토리(예: `https://example.com/service-worker.js`)에 호스팅하고 등록하는 것이 좋습니다.

루트 도메인에 서비스 종사자를 등록할 수 없는 경우 다른 방법은 서비스 종사자 파일을 제공할 때 [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) HTTP 헤더를 사용하는 것입니다. 서비스 워커에 대한 응답으로 `Service-Worker-Allowed: /` 을 반환하도록 서버를 구성하면 브라우저가 범위를 넓혀 다른 디렉토리 내에서 사용할 수 있도록 지시합니다.

#### Tag Manager를 사용하여 서비스 종사자를 생성할 수 있나요?

아니요, 서비스 워커는 웹사이트의 서버에서 호스팅되어야 하며 태그 관리자를 통해 로드할 수 없습니다.

### 사이트 보안

#### HTTPS가 필수인가요?

예. 웹 표준에서는 푸시 알림 권한을 요청하는 도메인의 보안을 요구합니다.

#### 언제 사이트가 "안전한" 것으로 간주되나요?

사이트가 다음 보안 출처 패턴 중 하나와 일치하면 안전한 것으로 간주됩니다. Braze 웹 푸시 알림은 이러한 개방형 표준을 기반으로 구축되었으므로 중간자 공격을 방지할 수 있습니다.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### 보안 사이트를 사용할 수 없는 경우 어떻게 하나요?

업계 모범 사례는 전체 사이트를 보안하는 것이지만, 사이트 도메인을 보안할 수 없는 고객은 보안 Modal을 사용하여 요구 사항을 해결할 수 있습니다. [대체 푸시 도메인]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) 사용 관련 가이드 또는 [작업 데모](http://appboyj.com/modal-test.html)를 참조하세요.
