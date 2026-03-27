{% multi_lang_include developer_guide/prerequisites/react_native.md %} 푸시 알림을 [설정해야 합니다.]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native)

## React Native에서 푸시 사용자 정의

Braze React Native SDK는 JavaScript API를 통해 푸시 알림 사용자 정의(실행 버튼, 카테고리, 커스텀 알림 팩토리)를 노출하지 않습니다. 이 기능은 iOS 및 Android 프로젝트에서 네이티브 구성이 필요합니다.

다음 표는 어떤 기능이 네이티브 구성을 요구하는지 보여줍니다:

| Feature | iOS | Android |
| --- | --- | --- |
| 실행 버튼 | 네이티브 Swift/Objective-C에서 구성 | 네이티브 Java/Kotlin에서 구성 |
| 푸시 카테고리 | 네이티브 Swift/Objective-C에서 구성 | 네이티브 Java/Kotlin에서 구성 |
| 커스텀 알림 팩토리 | N/A | 네이티브 Java/Kotlin에서 구성 |
| 배지 사용자 정의 | 네이티브 Swift/Objective-C에서 구성 | N/A |
| 사용자 지정 사운드 | 네이티브 Swift/Objective-C에서 구성 | 네이티브 Java/Kotlin에서 구성 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### iOS 사용자 정의

iOS에서 푸시 실행 버튼, 카테고리, 배지 또는 커스텀 사운드를 추가하려면 `AppDelegate` (Swift 또는 Objective-C)에서 네이티브 구성을 구현하십시오. 단계별 지침은 [푸시 알림 사용자 정의 – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift)를 참조하십시오.

### Android 사용자 정의

Android에서 푸시 실행 버튼, 카테고리 또는 커스텀 알림 팩토리를 추가하려면 Android 프로젝트에서 네이티브 구성을 구현하십시오. 단계별 지침은 [푸시 알림 사용자 정의 – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android)를 참조하십시오.
