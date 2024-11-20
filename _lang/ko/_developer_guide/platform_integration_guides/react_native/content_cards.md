---
nav_title: 콘텐츠 카드
article_title: React Native용 콘텐츠 카드
platform: React Native
page_order: 3
page_type: reference
description: "이 문서에서는 React Native 앱용 콘텐츠 카드 시작 방법을 다룹니다."
channel: content cards

---

# 콘텐츠 카드 통합

> 이 문서에서는 React Native용 콘텐츠 카드를 설정하는 방법을 다룹니다.

Braze SDK에는 콘텐츠 카드를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 카드 피드를 표시하려면 `Braze.launchContentCards()` 메서드를 사용할 수 있습니다. 기본 카드 피드는 Braze SDK에 포함되어 있으며 모든 분석 추적, 해제 및 사용자의 콘텐츠 카드 렌더링을 처리합니다.

## 맞춤화

자체 UI를 빌드하려면 사용 가능한 카드 목록을 가져오고 카드 업데이트를 수신 대기할 수 있습니다.

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
카드를 표시할 자체 UI를 빌드하려는 경우 해당 카드에 대한 분석을 수신하려면 `logContentCardImpression`을 호출해야 합니다. 여기에 `control` 카드가 포함되며, 사용자가 카드를 볼 수 없더라도 추적해야 합니다.
{% endalert %}

이러한 추가 메서드를 사용하여 앱 내에서 커스텀 콘텐츠 카드 피드를 빌드할 수 있습니다.

| 방법                                   | 설명                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | 콘텐츠 카드 UI 요소를 실행합니다.                                                                 |
| `requestContentCardsRefresh()`           | Braze SDK 서버에서 최신 콘텐츠 카드를 요청합니다. 결과 카드 목록은 이전에 등록된 각 [콘텐츠 카드 이벤트 리스너](#customization)로 전달됩니다. |
| `getContentCards()`                      | Braze SDK에서 콘텐츠 카드를 검색합니다. 이것은 서버에서 최신 카드 목록으로 해결되는 약속을 반환합니다. |
| `getCachedContentCards()`                | 캐시에서 가장 최근의 콘텐츠 카드 배열을 반환합니다.                                            |
| `logContentCardClicked(cardId)`          | 지정된 콘텐츠 카드 ID에 대한 클릭을 기록합니다. 이 방법은 분석에만 사용됩니다. 클릭 작업을 실행하려면 `processContentCardClickAction(cardId)`을(를) 추가로 호출하십시오.                                                        |
| `logContentCardImpression(cardId)`       | 지정된 콘텐츠 카드 ID에 대한 노출을 기록합니다.                                                      |
| `logContentCardDismissed(cardId)`        | 지정된 콘텐츠 카드 ID에 대한 해제를 기록합니다.                                                        |
| `processContentCardClickAction(cardId)`  | 특정 카드의 동작을 수행합니다.                                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 샘플 콘텐츠 카드를 표시하는 테스트

다음 단계를 따라 샘플 콘텐츠 카드를 테스트하세요.

1. [`Braze.changeUser('your-user-id')`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. **캠페인**으로 이동하여 [이 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create)를 따라 새 콘텐츠 카드 캠페인을 만드세요.
3. 테스트 콘텐츠 카드 캠페인을 작성하고 **테스트** 탭으로 이동하세요. 동일한 `user-id`을 테스트 사용자로 추가하고 **테스트 보내기**를 클릭하십시오. 곧 기기에서 콘텐츠 카드를 실행할 수 있습니다.

![자신의 사용자 ID를 테스트 수신자로 추가하여 콘텐츠 카드를 테스트할 수 있는 Braze 콘텐츠 카드 캠페인]({% image_buster /assets/img/react-native/content-card-test.png %} "콘텐츠 카드 캠페인 테스트")

더 많은 통합을 위해, 사용하는 플랫폼에 따라 [Android 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) 또는 [iOS 통합 지침](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui)을 따르세요.

이 샘플 구현은 [React Native SDK](https://github.com/braze-inc/braze-react-native-sdk) 내의 BrazeProject에서 찾을 수 있습니다.

## 콘텐츠 카드 데이터 모델

콘텐츠 카드 데이터 모델은 React Native SDK에서 사용할 수 있습니다. 콘텐츠 카드 데이터 모델에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard) 설명서를 참조하세요.

Braze React Native SDK는 기본 모델을 공유하는 세 가지 고유한 콘텐츠 카드 유형(**이미지 전용**, **자막 이미지**, **클래식**)을 지원합니다.

특정 카드에 대해 대조군에 속한 사용자에게 반환되는 특수 **제어** 카드 유형도 있습니다.

각 유형은 기본 모델에서 공통 속성을 상속하며 다음과 같은 추가 속성이 있습니다.

### 기본 콘텐츠 카드 모델 속성

기본 카드 모델은 모든 카드에 대한 기초적인 동작을 제공합니다.

|등록정보      | 설명                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
|`id`          | Braze에서 설정한 카드의 ID입니다.                                                                                            |
|`created`     | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다.                                                             |
|`expiresAt`   | 카드 만료 시간의 UNIX 타임스탬프입니다. 값이 0보다 작으면 카드가 만료되지 않는다는 의미입니다.      |
|`viewed`      | 사용자가 카드를 읽었는지 또는 읽지 않았는지 여부. 이는 분석을 기록하지 않습니다.                                           |
|`clicked`     | 사용자가 카드를 클릭했는지 여부.                                                                         |
|`pinned`      | 카드가 고정되어 있는지 여부.                                                                                            |
|`dismissed`   | 사용자가 이 카드를 해지했는지 여부입니다. 이미 기각된 카드를 기각된 것으로 표시하는 것은 불가능합니다. |
|`dismissible` | 사용자가 카드를 해지할 수 있는지 여부입니다.                                                                           |
|`url`         | (선택 사항) 카드 클릭 동작과 연결된 URL 문자열입니다.                                                       |
|`openURLInWebView` | 이 카드의 URL을 Braze의 WebView에서 열람할지 여부.                                            |
|`isControl`   | 이 카드가 제어 카드인지 여부. 제어 카드는 사용자에게 표시되지 않아야 합니다.                                |
|`extras`      | 이 카드의 키 값 추가 항목 맵.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

기본 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct) 설명서를 참조하세요.

### 이미지 전용 콘텐츠 카드 모델 속성

이미지 전용 카드는 클릭 가능한 전체 크기 이미지입니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | 콘텐츠 카드 유형, `IMAGE_ONLY`.                                                                              |
|`image`            | 카드 이미지의 URL입니다.                                                                                      |
|`imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이미지 전용 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) 설명서를 참조하세요.

### 캡션 이미지 콘텐츠 카드 모델 속성

캡션이 있는 이미지 카드는 클릭 가능한 전체 크기 이미지로, 설명 텍스트가 함께 제공됩니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | 콘텐츠 카드 유형, `CAPTIONED`.                                                                               |
|`image`            | 카드 이미지의 URL입니다.                                                                                      |
|`imageAspectRatio` | 카드 이미지의 종횡비입니다. 이미지 로드가 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성정보가 제공되지 않을 수 있습니다. |
|`title`            | 카드의 제목 텍스트입니다.                                                                                      |
|`cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
|`domain`           | (선택 사항) 속성 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

캡션이 있는 이미지 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct) 설명서를 참조하세요.

### 클래식 콘텐츠 카드 모델 속성

클래식 카드에는 텍스트 왼쪽에 제목, 설명, 이미지(선택 사항)가 있습니다.

|등록정보           | 설명                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
|`type`             | 콘텐츠 카드 유형, `CLASSIC`.                                                                                 |
|`image`            | (선택 사항) 카드 이미지의 URL입니다.                                                                           |
|`title`            | 카드의 제목 텍스트입니다.                                                                                      |
|`cardDescription`  | 카드의 설명 텍스트입니다.                                                                                |
|`domain`           | (선택 사항) 속성 URL의 링크 텍스트(예: `"braze.com/resources/"`). 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

클래식(텍스트 알림) 콘텐츠 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct) 설명서를 참조하세요. 클래식 이미지(짧은 뉴스) 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct) 문서를 참조하세요.

### 콘텐츠 카드 모델 속성 제어

제어 카드에는 몇 가지 중요한 차이점이 있는 모든 기본 속성이 포함됩니다. 특히 다음 사항이 중요합니다.

- `isControl` 속성은 `true`로 보장됩니다.
- `extras` 속성은 비어 있음을 보장합니다.

제어 카드에 대한 전체 참조는 [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) 및 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct) 설명서를 참조하세요.

## GIF 지원

{% multi_lang_include wrappers/gif_support/content_cards.md %}

