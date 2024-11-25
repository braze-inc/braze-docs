---
nav_title: Safari 모바일 웹 푸시
article_title: Safari 모바일 웹 푸시
platform: Web
channel: push
page_order: 5
page_type: reference
description: "이 참조 문서에서는 iOS 및 iPad Safari 브라우저에서 웹 푸시를 통합하는 방법을 다룹니다."
search_rank: 3
---

# Safari 모바일 웹 푸시(iOS 및 iPadOS)

> [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)는 모바일 웹 푸시를 지원하므로 이제 iOS 및 iPadOS에서 푸시 알림을 통해 모바일 사용자의 참여를 다시 유도할 수 있습니다.<br><br>이 문서에서는 Safari용 모바일 푸시를 설정하는 데 필요한 단계를 안내합니다.

## 통합 단계

먼저 표준 [웹 푸시 통합 가이드]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)를 읽고 따릅니다 다음 단계는 iOS 및 iPadOS 지원을 위해 Safari에서 웹 푸시를 지원하는 경우에만 필요합니다.

### 1단계: 매니페스트 파일 만들기 {#manifest}

[웹 애플리케이션 매니페스트](https://developer.mozilla.org/en-US/docs/Web/Manifest)는 웹사이트가 사용자의 홈 화면에 설치될 때 표시되는 방식을 제어하는 JSON 파일입니다.

예를 들어 [앱 스위처에서](https://support.apple.com/en-us/HT202070) 사용하는 배경 테마 색상과 아이콘, 기본 앱과 비슷하게 전체 화면으로 렌더링할지, 앱을 가로 또는 세로 모드로 열지 여부를 설정할 수 있습니다.

웹사이트의 루트 디렉터리에 다음과 같은 필수 필드를 사용하여 `manifest.json` 파일을 새로 만듭니다. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

지원되는 전체 필드 목록은 [여기에서](https://developer.mozilla.org/en-US/docs/Web/Manifest) 확인할 수 있습니다.

### 2단계: 매니페스트 파일 링크 {#manifest-link}

웹사이트의 `<head>` 요소에 매니페스트 파일이 호스팅되는 위치를 가리키는 다음 `<link>` 태그를 추가합니다.

```html
<link rel="manifest" href="/manifest.json" />
```

### 3단계: 서비스 종사자 추가 {#service-worker}

[웹 푸시 통합 가이드에]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker) 설명된 대로 웹사이트에 Braze 서비스 워커 라이브러리를 가져오는 서비스 워커 파일이 있어야 합니다.

### 4단계: 홈 화면에 추가 {#add-to-homescreen}

Chrome 및 Firefox와 같은 주요 브라우저와 달리 Safari iOS/iPadOS에서는 웹사이트가 사용자의 홈 화면에 추가되지 않은 경우 푸시 권한을 요청할 수 없습니다. 

[홈 화면에 추가](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) 기능을 사용하면 사용자가 웹사이트를 북마크에 추가하여 귀사의 아이콘을 소중한 홈 화면 공간에 추가할 수 있습니다.

![웹사이트를 북마크하고 홈 화면에 저장하는 옵션을 보여주는 iPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### 5단계: 기본 푸시 프롬프트 표시 {#push-prompt}
앱이 홈 화면에 추가되면 이제 사용자가 버튼을 클릭하는 등의 작업을 수행할 때 푸시 권한을 요청할 수 있습니다. [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) 메서드를 사용하거나 [노코드 푸시 프라이머 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)를 사용하여 수행할 수 있습니다.

{% alert note %}
메시지를 수락하거나 거부하면 해당 웹사이트를 삭제한 후 홈 화면에 다시 설치해야 프롬프트가 다시 표시될 수 있습니다.
{% endalert %}

![알림을 '허용' 또는 '허용하지 않음'으로 설정할지 묻는 푸시 메시지]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

예를 들어, 다음과 같습니다.

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```


## 다음 단계

그런 다음 [테스트 메시지를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) 보내 통합을 검증합니다. 통합이 완료되면 [코드가 없는 푸시 프라이머 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) 사용하여 푸시 옵트인율을 최적화할 수 있습니다.

