---
nav_title: 세션 추적
article_title: 웹용 세션 추적
platform: Web
page_order: 0
description: "이 참조 문서에서는 웹용 세션을 추적하는 방법에 대해 설명합니다."

---

# 세션 추적

> Braze SDK는 사용자 참여도를 계산하는 데 사용되는 세션 데이터와 사용자를 이해하는 데 필수적인 기타 분석을 Braze 대시보드에 보고합니다. 저희 SDK는 다음 세션 시맨틱에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 "세션 시작" 및 "세션 종료" 데이터 포인트를 생성합니다.

## 세션 수명 주기

기본적으로 세션은 `braze.openSession()` 을 처음 호출할 때 시작되며 최소 30분 동안 활동이 없을 때까지 열려 있습니다. 즉, 사용자가 사이트를 떠났다가 30분 이내에 돌아오면 동일한 세션이 계속됩니다. 30분이 만료된 후 다시 돌아오면 이동한 시간에 대한 '세션 닫기' 데이터 포인트가 자동으로 생성되고 새 세션이 열립니다.

{% alert note %}
새 세션을 강제로 실행해야 하는 경우 사용자를 변경하여 실행할 수 있습니다.
{% endalert %}

## 세션 시간 초과 사용자 지정

세션 시간 제한을 사용자 지정하려면 \[`initialize`]\[session_tracking_5] 함수]에 `sessionTimeoutInSeconds` 옵션을 전달하세요. `sessionTimeoutInSeconds` 의 최소값은 1초입니다.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

세션 시간 제한을 설정한 경우 세션 시맨틱은 모두 해당 사용자 지정 시간 제한으로 확장됩니다.

## 테스트 세션 추적

사용자를 통한 세션을 감지하려면 대시보드에서 사용자를 찾아 사용자 프로필의 **앱 사용량으로** 이동합니다. 세션 지표가 예상한 시간에 증가하는지 확인하여 세션 추적이 작동하는지 확인할 수 있습니다.

![발생한 세션 수, 앱을 처음 사용한 시기, 마지막으로 사용한 시기를 보여주는 사용자 프로필 구성 요소입니다.]\[세션_추적_7]{: style="max-width:50%"}

\[세션_추적_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/#customizing-braze-on-startup
\[세션_추적_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
\[세션_추적_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
\[세션_추적_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
\[세션_추적_7]: {% image_buster /assets/img_archive/test_session.png %}
\[세션_추적_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
