{% multi_lang_include developer_guide/prerequisites/cordova.md %} SDK를 통합한 후 기본 푸시 알림 기능이 기본값으로 활성화됩니다. [리치 푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) 및 [푸시 스토리]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova)를 사용하려면 개별적으로 설정해야 합니다. iOS 푸시 메시지를 사용하려면 유효한 푸시 인증서를 업로드해야 합니다.

{% alert warning %}
Cordova 플러그인을 추가, 제거 또는 업데이트할 때마다 Cordova는 iOS 앱의 Xcode 프로젝트에서 Podfile을 덮어씁니다. 이는 Cordova 플러그인을 수정할 때마다 이러한 기능을 다시 설정해야 함을 의미합니다.
{% endalert %}

## 푸시 딥링킹 활성화

기본적으로 Braze Cordova SDK는 푸시 알림에서 딥 링크를 자동으로 처리하지 않습니다. 푸시 딥링킹을 활성화하려면 [딥링킹]({{site.baseurl}}/developer_guide/cordova/deep_linking/)의 구성 단계를 따르세요.
이와 기타 푸시 구성 옵션에 대한 자세한 내용은 [선택적 구성]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)을 참조하세요.

## 기본 푸시 알림 비활성화(오직 iOS 전용)

iOS용 Braze Cordova SDK를 통합한 후 기본 푸시 알림 기능이 기본값으로 활성화됩니다. iOS 앱에서 이 기능을 비활성화하려면 `config.xml` 파일에 다음을 추가하세요. 자세한 내용은 [선택적 구성]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)을 참조하세요.

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
