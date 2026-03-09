{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## 푸시 딥링킹 활성화

기본적으로 Braze Cordova SDK는 알림에서 푸시 딥링킹을 자동으로 처리하지 않습니다. 푸시 딥링킹을 활성화하려면, 프로젝트의 `config.xml` 파일의 `platform` 요소에 다음 기본 설정을 추가하세요.

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_forward_universal_links" value="YES" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
</platform>
```

딥 링크가 따라질 때 백 스택 동작을 사용자 정의하려면, 이러한 선택적 기본 설정도 추가할 수 있습니다:

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

사용 가능한 푸시 구성 옵션의 전체 목록은 [선택적 구성]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)을 참조하세요.
