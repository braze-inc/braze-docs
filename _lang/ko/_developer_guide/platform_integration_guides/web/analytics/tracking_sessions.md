---
nav_title: 세션 추적
article_title: 웹용 세션 추적
platform: Web
page_order: 0
description: "이 참조 문서에서는 웹용 세션을 추적하는 방법에 대해 설명합니다."

---

# 세션 추적

> Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. 저희 SDK는 다음 세션 시맨틱에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 "세션 시작" 및 "세션 종료" 데이터 포인트를 생성합니다.

## 세션 수명 주기

기본적으로 세션은 `braze.openSession()`을 처음 호출할 때 시작되며 최소 30분 동안 활동이 없을 때까지 열려 있습니다. 즉, 사용자가 사이트에서 자리를 비웠다가 30분 이내에 돌아오면 동일한 세션이 계속됩니다. 30분이 만료된 후 다시 돌아오는 경우 자리를 비운 시점에 '세션 닫기' 데이터 포인트가 자동으로 생성되고 새 세션이 열립니다.

{% alert note %}
새 세션을 강제로 시작해야 하는 경우 사용자를 변경하면 됩니다.
{% endalert %}

## 세션 시간 초과 사용자 지정

세션 시간 초과를 사용자 지정하려면 `sessionTimeoutInSeconds` 옵션을 [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 함수에 전달하세요. `sessionTimeoutInSeconds` 의 최소값은 1초입니다.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

세션 시간 제한을 설정한 경우 세션 시맨틱은 모두 해당 사용자 지정 시간 제한으로 확장됩니다.

## 테스트 세션 추적

사용자를 통해 세션을 감지하려면 대시보드에서 사용자를 찾고 고객 프로필에서 **앱 사용**으로 이동합니다. 세션 추적이 예상대로 작동하는지 확인하려면 세션 메트릭이 예상대로 증가하는지 확인하십시오.

![발생한 세션 수, 앱을 처음 사용한 시기, 마지막으로 사용한 시기를 보여주는 사용자 프로필 구성 요소입니다.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

