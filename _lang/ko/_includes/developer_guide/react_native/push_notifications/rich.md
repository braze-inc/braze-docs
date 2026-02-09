{% multi_lang_include developer_guide/prerequisites/react_native.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native) 합니다.

## 엑스포를 사용하여 리치 푸시 알림 인에이블먼트하기

React Native 소프트웨어 개발 키트의 경우 **기본값으로 Android에 리치 푸시 알림을 사용할 수 있습니다**.

Expo를 사용하여 iOS에서 리치 푸시 알림을 활성화하려면 `app.json`의 `expo.plugins` 오브젝트에서 `enableBrazeIosRichPush` 속성정보를 `true`로 구성합니다.

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

마지막으로, 프로젝트의 자격 증명 구성에 이 앱 확장에 대한 번들 식별자를 추가합니다. `<your-app-bundle-id>.BrazeExpoRichPush`. 이 프로세스에 대한 자세한 내용은 [Expo 애플리케이션 서비스에서 앱 확장 사용]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions)을 참조하세요.
