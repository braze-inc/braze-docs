{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## 카드 피드

Braze SDK에는 기본 카드 피드가 포함되어 있습니다. 기본 카드 피드를 표시하려면 `launchContentCards()` 방법을 사용할 수 있습니다. 이 메서드는 사용자의 콘텐츠 카드에 대한 모든 분석 추적, 해제 및 렌더링을 처리합니다.

## 콘텐츠 카드

이러한 추가 메서드를 사용하여 앱 내에서 커스텀 콘텐츠 카드 피드를 빌드할 수 있습니다.

|방법 | 설명 |
|---|---|
|`requestContentCardsRefresh()`|Braze SDK 서버에서 최신 콘텐츠 카드를 요청하는 백그라운드 요청을 보냅니다.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Braze SDK에서 콘텐츠 카드를 검색합니다. 이렇게 하면 서버에서 최신 콘텐츠 카드를 요청하고 완료되면 카드 목록을 반환합니다.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Braze SDK에서 콘텐츠 카드를 검색합니다. 이렇게 하면 마지막 새로 고침 시 업데이트된 로컬 캐시에서 최신 카드 목록이 반환됩니다.|
|`logContentCardClicked(cardId)`|지정된 콘텐츠 카드 ID에 대한 클릭을 기록합니다.|
|`logContentCardImpression(cardId)`|지정된 콘텐츠 카드 ID에 대한 노출을 기록합니다.|
|`logContentCardDismissed(cardId)`|지정된 콘텐츠 카드 ID에 대한 해제를 기록합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
