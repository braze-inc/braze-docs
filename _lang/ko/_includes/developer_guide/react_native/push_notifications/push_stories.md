{% multi_lang_include developer_guide/prerequisites/react_native.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native) 합니다.

## 푸시 스토리 인에이블먼트

React Native 소프트웨어 개발 키트의 경우 **푸시 스토리는 기본값으로 Android에 사용할 수 있습니다**.

Expo를 사용하여 iOS에서 푸시 스토리를 활성화하려면 애플리케이션에 대한 앱 그룹이 정의되어 있는지 확인합니다. 자세한 내용은 [앱 그룹 추가하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group) 참조하세요.

그런 다음, `enableBrazeIosPushStories` 속성정보를 `true`로 구성하고 `app.json`에 있는 `expo.plugins` 오브젝트의 `iosPushStoryAppGroup`에 앱 그룹 ID를 할당합니다.

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

마지막으로, 프로젝트의 자격 증명 구성에 이 앱 확장에 대한 번들 식별자를 추가합니다. `<your-app-bundle-id>.BrazeExpoPushStories`. 이 프로세스에 대한 자세한 내용은 [Expo 애플리케이션 서비스에서 앱 확장 사용]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions)을 참조하세요.

{% alert warning %}
Expo 애플리케이션 서비스와 함께 푸시 스토리를 사용하는 경우 `eas build`를 실행할 때 `EXPO_NO_CAPABILITY_SYNC=1` 플래그를 사용해야 합니다. 확장의 프로비저닝 프로필에서 앱 그룹 기능이 제거되는 것은 명령줄의 알려진 문제입니다.
{% endalert %}
