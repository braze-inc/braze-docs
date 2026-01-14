## Prerequisites

콘텐츠 카드를 사용하려면 먼저 [Braze Swift SDK를]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) 앱에 통합해야 합니다. 그런 다음 tvOS 앱 설정 단계를 완료해야 합니다.

{% alert important %}
콘텐츠 카드는 tvOS용 기본 UI나 보기가 포함되지 않은 Swift SDK를 사용하는 헤드리스 UI를 통해 지원되므로 자체 커스텀 UI를 구현해야 합니다.
{% endalert %}

## tvOS 앱 설정하기

### 1단계: 새 iOS 앱 만들기

Braze에서 **설정** > **앱 설정**을 선택한 다음, **앱 추가**를 선택합니다. tvOS 앱 이름을 입력하고 _tvOS가 아닌_ **iOS**를 선택한 다음, **앱 추가**를 선택합니다.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS** 확인란을 선택하면 tvOS용 콘텐츠 카드를 사용자 지정할 수 없습니다.
{% endalert %}

### 2단계: 앱의 API 키 가져오기

앱 설정에서 새 tvOS 앱을 선택한 다음, 앱의 API 키를 기록합니다. 이 키를 사용하여 Xcode에서 앱을 구성할 수 있습니다.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### 3단계: BrazeKit 통합

앱의 API 키를 사용하여 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk)를 Xcode의 tvOS 프로젝트에 통합합니다. Braze Swift SDK에서 BrazeKit를 통합하기만 하면 됩니다.

### 4단계: 사용자 지정 UI 만들기

Braze는 tvOS에서 콘텐츠 카드에 대한 기본 UI를 제공하지 않으므로 직접 사용자 지정해야 합니다. 전체 안내는 단계별 튜토리얼을 참조하세요. [tvOS용 콘텐츠 카드 사용자 지정](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). 샘플 프로젝트는 [Braze Swift SDK 샘플](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui)을 참조하세요.
