{% multi_lang_include developer_guide/prerequisites/cordova.md %} SDK를 통합하면 기본 푸시 알림 기능이 기본값으로 인에이블먼트됩니다. [리치 푸시 알림과]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) [푸시 스토리를]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova) 사용하려면 개별적으로 설정해야 합니다. iOS 푸시 메시지를 사용하려면 유효한 푸시 인증서도 업로드해야 합니다.

{% alert warning %}
Cordova 플러그인을 추가, 제거 또는 업데이트할 때마다 Cordova는 iOS 앱의 Xcode 프로젝트에 있는 Podfile을 덮어씁니다. 즉, Cordova 플러그인을 수정할 때마다 이러한 기능을 다시 설정해야 합니다.
{% endalert %}

## 기본 푸시 알림 비활성화하기(iOS만 해당)

iOS용 Braze Cordova SDK를 통합하면 기본 푸시 알림 기능이 기본값으로 인에이블먼트됩니다. iOS 앱에서 이 기능을 비활성화하려면 `config.xml` 파일에 다음을 추가하세요. 자세한 내용은 [선택적 구성을]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional) 참조하세요.

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
