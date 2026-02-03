{% multi_lang_include developer_guide/prerequisites/swift.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 합니다.

{% alert note %}
이 구현 가이드는 Swift 구현을 중심으로 하지만 관심 있는 사람을 위해 Objective-C 스니펫도 제공됩니다.
{% endalert %}

## 알림 콘텐츠 앱 확장

![두 개의 푸시 메시지가 나란히 표시됩니다. 왼쪽의 메시지는 기본 UI에서 푸시가 어떻게 표시되는지 보여줍니다. 오른쪽의 메시지는 커스텀 푸시 UI를 구현하여 만든 커피 펀치 카드 푸시를 보여줍니다.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

알림 콘텐츠 앱 확장은 푸시 알림을 사용자 지정할 수 있는 뛰어난 옵션을 제공합니다. 알림 콘텐츠 앱 확장은 푸시 알림이 확장될 때 앱의 알림에 대한 커스텀 인터페이스를 표시합니다.

푸시 알림은 세 가지 방법으로 확장할 수 있습니다.
- 푸시 배너를 길게 누릅니다.
- 푸시 배너를 아래로 스와이프
- 배너를 왼쪽으로 스와이프하고 '보기'를 선택합니다.

이러한 사용자 지정 보기는 대화형 알림, 사용자 데이터로 채워진 알림, 전화번호 및 이메일과 같은 정보를 캡처할 수 있는 푸시 메시지 등 다양한 유형의 콘텐츠를 표시하여 고객의 참여를 유도하는 스마트한 방법을 제공합니다. Braze의 잘 알려진 기능 중 하나인 [푸시 스토리]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)는 푸시 알림 콘텐츠 앱 확장의 모습을 보여주는 대표적인 예입니다!

### 요구 사항

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- 앱에 성공적으로 통합된 [푸시 알림]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) 
- 코딩 언어에 따라 Xcode에서 생성되는 파일은 다음과 같습니다.

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## 대화형 푸시 알림

푸시 알림은 콘텐츠 앱 확장 내에서 사용자 작업에 응답할 수 있습니다. iOS 12 이상을 실행하는 사용자의 경우, 푸시 알림을 완전한 대화형 메시지로 전환할 수 있습니다! 이는 프로모션과 애플리케이션에 인터랙티브한 기능을 도입할 수 있는 흥미로운 옵션입니다. 예를 들어 푸시 알림에는 사용자가 플레이할 수 있는 게임, 할인 옵션을 제공하는 돌림판, 목록이나 노래를 저장하는 '좋아요' 버튼 등이 포함될 수 있습니다.

다음 예시는 사용자가 확장된 알림 내에서 매치 게임을 플레이할 수 있는 푸시 알림을 보여줍니다.

![대화형 푸시 알림의 단계가 어떤 모습일 수 있는지 보여주는 다이어그램입니다. 사용자가 대화형 매칭 게임을 표시하는 푸시 알림을 누르는 일련의 모습을 보여줍니다.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### 대시보드 구성

대화형 푸시 알림을 만들려면 대시보드에서 사용자 지정 보기를 설정해야 합니다. 

1. **캠페인** 페이지에서 **캠페인 생성**을 클릭하여 새 푸시 알림 캠페인을 시작합니다.
2. **작성** 탭에서 **알림 버튼**을 토글합니다. 
3. **iOS 알림 카테고리** 필드에 사용자 지정 iOS 카테고리를 입력합니다. 
4. 알림 콘텐츠 확장 대상의 `.plist` 에서 `UNNotificationExtensionCategory` 속성을 사용자 지정 iOS 카테고리로 설정합니다. 여기에 입력한 값은 **iOS 알림 카테고리** 아래의 Braze 대시보드에 설정된 값과 일치해야 합니다. 
5. `UNNotificationExtensionInteractionEnabled` 키를 `true` 으로 설정하여 푸시 알림에서 사용자 상호작용을 활성화합니다.

![푸시 메시지 작성기 설정에 있는 알림 버튼 옵션입니다.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## 개인화된 푸시 알림

![두 대의 iPhone이 나란히 표시됩니다. 첫 번째 iPhone은 푸시 메시지의 확장되지 않은 보기를 표시합니다. 두 번째 iPhone에는 코스의 '진행' 화면, 다음 세션 이름, 다음 세션의 만료 시점을 표시하는 확장된 버전의 푸시 메시지가 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

푸시 알림은 콘텐츠 확장 내에서 사용자별 정보를 표시할 수 있습니다. 이를 통해 여러 플랫폼에서 진행 상황을 공유하거나, 잠금 해제된 업적을 표시하거나, 온보딩 체크리스트를 표시하는 옵션을 추가하는 등 사용자 중심의 푸시 콘텐츠를 만들 수 있습니다. 이 예제에서는 사용자가 Braze 학습 과정에서 특정 작업을 완료한 후 사용자에게 표시되는 푸시 알림을 보여줍니다. 알림을 확장하면 사용자는 학습 경로를 통해 자신의 진행 상황을 확인할 수 있습니다. 여기에 제공된 정보는 사용자별로 다르며 세션이 완료되거나 특정 사용자 작업이 수행될 때 API 트리거를 활용하여 실행될 수 있습니다. 

### 대시보드 구성

개인화된 푸시 알림을 만들려면 대시보드에서 사용자 지정 보기를 설정해야 합니다. 

1. **캠페인** 페이지에서 **캠페인 생성**을 클릭하여 새 푸시 알림 캠페인을 시작합니다.
2. **작성** 탭에서 **알림 버튼**을 토글합니다. 
3. **iOS 알림 카테고리** 필드에 사용자 지정 iOS 카테고리를 입력합니다. 
4. **설정** 탭에서 표준 Liquid를 사용하여 키-값 쌍을 생성합니다. 메시지에 표시할 적절한 사용자 속성을 설정합니다. 이러한 보기는 특정 고객 프로필의 특정 사용자 속성을 기반으로 개인화될 수 있습니다.
5. 알림 콘텐츠 확장 대상의 `.plist` 에서 `UNNotificationExtensionCategory` 속성을 사용자 지정 iOS 카테고리로 설정합니다. 여기에 입력한 값은 **iOS 알림 카테고리** 아래의 Braze 대시보드에 설정된 값과 일치해야 합니다. 

![네 개의 키-값 페어 세트, "next_session_name" 및 "next_session_complete_date" 은 Liquid를 사용하여 API 트리거 속성으로 설정하고 "completed_session count" 및 "total_session_count" 은 Liquid를 사용하여 커스텀 사용자 속성으로 설정합니다.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### 키-값 쌍 처리하기

`didReceive` 메서드는 알림 콘텐츠 앱 확장이 알림을 받으면 호출됩니다. 이 방법은 `NotificationViewController` 에서 찾을 수 있습니다. 대시보드에 제공된 키-값 페어는 `userInfo` 사전을 사용하여 코드에 표시됩니다.

#### 푸시 알림에서 키-값 쌍 구문 분석하기

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## 정보 캡처 푸시 알림

푸시 알림은 콘텐츠 앱 확장 내에서 사용자 정보를 캡처할 수 있으므로 푸시로 가능한 작업의 한계를 뛰어넘을 수 있습니다. 푸시 알림을 통해 사용자 입력을 요청하면 이름이나 이메일과 같은 기본 정보를 요청할 수 있을 뿐만 아니라 사용자에게 피드백을 제출하거나 미완성된 사용자 프로필을 작성하라는 메시지를 표시할 수도 있습니다. 

{% alert tip %}
자세한 내용은 [푸시 알림 데이터 로깅하기를]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/) 참조하세요.
{% endalert %}

다음 흐름에서 사용자 지정 보기는 상태 변경에 응답할 수 있습니다. 이러한 상태 변경 구성요소가 각 이미지에 표시됩니다. 

1. 사용자가 푸시 알림을 받습니다.
2. 푸시가 열립니다. 확장 후 푸시는 사용자에게 정보를 입력하라는 메시지를 표시합니다. 이 예제에서는 사용자의 이메일 주소가 요청되었지만 모든 종류의 정보를 요청할 수 있습니다.
3. 정보가 제공되고 예상되는 형식인 경우 등록 버튼이 표시됩니다.
3. 확인 보기가 표시되고 푸시가 해제됩니다. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### 대시보드 구성

정보 캡처 푸시 알림을 만들려면 대시보드에서 사용자 지정 보기를 설정해야 합니다. 

1. **캠페인** 페이지에서 **캠페인 생성**을 클릭하여 새 푸시 알림 캠페인을 시작합니다.
2. **작성** 탭에서 **알림 버튼**을 토글합니다. 
3. **iOS 알림 카테고리** 필드에 사용자 지정 iOS 카테고리를 입력합니다. 
4. **설정** 탭에서 표준 Liquid를 사용하여 키-값 쌍을 생성합니다. 메시지에 표시할 적절한 사용자 속성을 설정합니다. 
5. 알림 콘텐츠 확장 대상의 `.plist` 에서 `UNNotificationExtensionCategory` 속성을 사용자 지정 iOS 카테고리로 설정합니다. 여기에 입력한 값은 **iOS 알림 카테고리** 아래의 Braze 대시보드에 설정된 값과 일치해야 합니다. 

예시에서 볼 수 있듯이 푸시 알림에 이미지를 포함할 수도 있습니다. 이렇게 하려면 [리치 알림]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)을 통합하고 캠페인에서 알림 스타일을 리치 알림으로 설정한 다음, 리치 푸시 이미지를 포함해야 합니다.

![세 세트의 키-값 쌍이 포함된 푸시 메시지입니다. 1. "Braze_id" 를 Liquid 호출로 설정하여 Braze ID를 검색합니다. 2. "cert_title" 을 "Braze 마케터 인증"으로 설정합니다. 3. "Cert_description" "인증된 Braze 마케터가 운전합니다..."로 설정.]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### 버튼 동작 처리하기

각 실행 버튼은 고유하게 식별됩니다. 이 코드는 응답 식별자가 `actionIndentifier`와 같은지 확인하고, 같다면 사용자가 실행 버튼을 클릭했음을 알 수 있습니다.

**푸시 알림 동작 버튼 응답 처리하기**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### 푸시 해제하기

푸시 알림은 실행 버튼을 누르면 자동으로 해제할 수 있습니다. 권장되는 세 가지 사전 빌드된 푸시 해제 옵션이 있습니다.

1. `completion(.dismiss)` - 알림을 해제합니다.
2. `completion(.doNotDismiss)` - 알림이 계속 열려 있습니다.
3. `completion(.dismissAndForward)` - 푸시가 해제되고 사용자가 애플리케이션으로 이동합니다.
