{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## 데이터 모델

인앱 메시지 모델은 React Native SDK에서 사용할 수 있습니다. Braze에는 동일한 데이터 모델을 공유하는 네 가지 인앱 메시지 유형( **슬라이드업**, **모달**, **전체** 및 **HTML 전체**)이 있습니다.

### Messages

인앱 메시지 모델은 모든 인앱 메시지의 기본을 제공합니다.

|등록정보          | 설명                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | 메시지 JSON 표현입니다.                                                                                |
|`message`         | 메시지 텍스트입니다.                                                                                                      |
|`header`          | 메시지 헤더입니다.                                                                                                    |
|`uri`             | 버튼 클릭 액션과 연결된 URI입니다.                                                                       |
|`imageUrl`        | 메시지 이미지 URL입니다.                                                                                                 |
|`zippedAssetsUrl` | HTML 콘텐츠를 표시하도록 준비된 압축된 에셋입니다.                                                                    |
|`useWebView`      | 버튼 클릭 동작이 웹 보기를 사용하여 리디렉션할지 여부를 나타냅니다.                                            |
|`duration`        | 메시지 표시 기간입니다.                                                                                          |
|`clickAction`     | 버튼 클릭 액션 유형입니다. 유형은 `URI` 및 `NONE` 입니다.                                     |
|`dismissType`     | 메시지 닫기 유형. 두 가지 유형(`SWIPE` 및 `AUTO_DISMISS`)이 있습니다.                                                 |
|`messageType`     | SDK에서 지원하는 인앱 메시지 유형입니다. 네 가지 유형(`SLIDEUP`, `MODAL`, `FULL`, `HTML_FULL`)이 있습니다.          |
|`extras`          | 메시지 추가 항목 사전. 기본값: `[:]`.                                                                   |
|`buttons`         | 인앱 메시지의 버튼 목록입니다.                                                                             |
|`toString()`      | 문자열 표현으로서의 메시지입니다.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

인앱 메시지 모델에 대한 전체 참조는 [안드로이드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) 설명서를 참조하십시오.

### 버튼

인앱 메시지에 버튼을 추가하여 작업 및 로그 분석을 수행할 수 있습니다. 버튼 모델은 모든 인앱 메시지 버튼의 기본을 제공합니다.

|등록정보          | 설명                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | 버튼의 텍스트입니다.                                                                                                     |
|`uri`             | 버튼 클릭 액션과 연결된 URI입니다.                                                                            |
|`useWebView`      | 버튼 클릭 동작이 웹 보기를 사용하여 리디렉션할지 여부를 나타냅니다.                                                 |
|`clickAction`     | 사용자가 버튼을 클릭할 때 처리되는 클릭 동작 유형입니다. 유형은 `URI` 및 `NONE` 입니다. |
|`id`              | 메시지의 버튼 ID.                                                                                               |
|`toString()`      | 문자열 표현으로서의 버튼입니다.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

버튼 모델에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button) 설명서를 참조하십시오.
