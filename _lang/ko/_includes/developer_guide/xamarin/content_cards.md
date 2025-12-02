## .NET MAUI 콘텐츠 카드 정보

브레이즈 .NET MAUI SDK에는 콘텐츠 카드를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 기본 카드 피드는 Braze SDK에 포함되어 있으며 모든 분석 추적, 해제 및 사용자의 콘텐츠 카드 렌더링을 처리합니다.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## 카드 유형 및 속성

브레이즈 .NET MAUI SDK에는 기본 모델을 공유하는 세 가지 고유한 콘텐츠 카드 유형이 있습니다: [배너](#xamarin_banner), [캡션 이미지](#xamarin_captioned-image) 및 [클래식](#xamarin_classic). 각 유형은 기본 모델에서 공통 속성을 상속하며 다음과 같은 추가 속성이 있습니다.

### 기본 카드 모델

|등록정보           | 설명                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
|`idString`         | Braze에서 설정한 카드의 ID입니다.                                                                                            |
|`created`          | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다.                                                             |
|`expiresAt`        | 카드 만료 시간의 UNIX 타임스탬프입니다. 값이 0보다 작으면 카드가 만료되지 않는다는 의미입니다.      |
|`viewed`           | 사용자가 카드를 읽었는지 또는 읽지 않았는지 여부. 이는 분석을 기록하지 않습니다.                                           |
|`clicked`          | 사용자가 카드를 클릭했는지 여부.                                                                         |
|`pinned`           | 카드가 고정되어 있는지 여부.                                                                                            |
|`dismissed`        | 사용자가 이 카드를 해지했는지 여부입니다. 이미 기각된 카드를 기각된 것으로 표시하는 것은 불가능합니다. |
|`dismissible`      | 사용자가 카드를 해지할 수 있는지 여부입니다.                                                                           |
|`urlString`        | (선택 사항) 카드 클릭 동작과 연결된 URL 문자열입니다.                                                       |
|`openUrlInWebView` | 이 카드의 URL을 Braze WebView에서 열어야 하는지 여부입니다.                                                 |
|`isControlCard`    | 이 카드가 제어 카드인지 여부. 제어 카드는 사용자에게 표시되지 않아야 합니다.                                |
|`extras`           | 이 카드의 키 값 추가 항목 맵.                                                                             |
|`isTest`           | 이 카드가 테스트 카드인지 여부.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기본 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) 설명서를 참조하세요.

### 배너

배너 카드는 클릭 가능한 전체 크기 이미지입니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | 카드 이미지의 URL입니다.                                                                                      |
|`imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

배너 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) 문서(현재 이미지 전용으로 이름이 변경됨)를 참조하세요.

### 캡션 이미지

캡션이 있는 이미지 카드는 클릭 가능한 전체 크기 이미지로, 설명 텍스트가 함께 제공됩니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | 카드 이미지의 URL입니다.                                                                                      |
|`imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
|`title`            | 카드의 제목 텍스트입니다.                                                                                      |
|`cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
|`domain`           | (선택 사항) 속성 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

캡션이 있는 이미지 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) 설명서를 참조하세요.

### 클래식

클래식 카드에는 텍스트 왼쪽에 제목, 설명, 이미지(선택 사항)가 있습니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`image`            | (선택 사항) 카드 이미지의 URL입니다.                                                                           |
|`title`            | 카드의 제목 텍스트입니다.                                                                                      |
|`cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
|`domain`           | (선택 사항) 속성 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

클래식(텍스트 알림) 콘텐츠 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) 설명서를 참조하세요. 클래식 이미지(짧은 뉴스) 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) 문서를 참조하세요.

## 카드 방법

이러한 추가 메서드를 사용하여 앱 내에서 커스텀 콘텐츠 카드 피드를 빌드할 수 있습니다.

| 방법                                   | 설명                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()`           | Braze SDK 서버에서 최신 콘텐츠 카드를 요청합니다.                                           |
| `getContentCards()`                      | Braze SDK에서 콘텐츠 카드를 검색합니다. 그러면 서버에서 최신 카드 목록이 반환됩니다. |
| `logContentCardClicked(cardId)`          | 지정된 콘텐츠 카드 ID에 대한 클릭을 기록합니다. 이 방법은 분석에만 사용됩니다.                    |
| `logContentCardImpression(cardId)`       | 지정된 콘텐츠 카드 ID에 대한 노출을 기록합니다.                                                      |
| `logContentCardDismissed(cardId)`        | 지정된 콘텐츠 카드 ID에 대한 해제를 기록합니다.                                                        |
