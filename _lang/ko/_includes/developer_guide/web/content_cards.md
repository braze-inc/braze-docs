{% multi_lang_include archive/web-v4-rename.md %}

## 필수 조건

콘텐츠 카드를 사용하려면 먼저 [Braze 웹 SDK를]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) 앱에 [통합해야]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) 합니다. 그러나 추가 설정은 필요하지 않습니다. 대신 고유한 UI를 구축하려면 [콘텐츠 카드 커스텀 가이드를]({{site.baseurl}}/developer_guide/content_cards/) 참조하세요.

## 표준 피드 UI

포함된 콘텐츠 카드 UI를 사용하려면 웹사이트에서 피드를 표시할 위치를 지정해야 합니다. 

이 예제에서는 콘텐츠 카드 피드를 `<div id="feed"></div>`에 배치하려고 합니다. 세 개의 버튼을 사용하여 피드를 숨기거나, 표시하거나, 토글(현재 상태에 따라 숨기거나 표시)합니다.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

`toggleContentCards(parentNode, filterFunction)` 및 `showContentCards(parentNode, filterFunction)` 메서드를 사용하는 경우 인수를 제공하지 않으면 모든 콘텐츠 카드가 페이지 오른쪽에 있는 고정 위치 사이드바에 표시됩니다. 그렇지 않으면 피드가 지정된 `parentNode` 옵션에 배치됩니다.

|매개변수 | Description |
|---|---|
|`parentNode` | 콘텐츠 카드를 렌더링할 HTML 노드입니다. 상위 노드에 이미 Braze 콘텐츠 카드 보기가 직계 하위로 존재하는 경우 기존 콘텐츠 카드가 대체됩니다. 예를 들어 `document.querySelector(".my-container")`를 전달해야 합니다.|
|`filterFunction` | 이 보기에 표시되는 카드의 필터 또는 정렬 기능입니다. `{pinned, date}` 기준으로 정렬된 `Card` 오브젝트 배열로 호출됩니다. 이 사용자에 대해 렌더링할 정렬된 `Card` 오브젝트 배열을 반환할 것으로 예상됩니다. 생략하면 모든 카드가 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

콘텐츠 카드 토글에 대한 자세한 내용은 [SDK 참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)를 참조하세요.

## 카드 유형 및 속성

콘텐츠 카드 데이터 모델은 웹 소프트웨어 개발 키트에서 사용할 수 있으며 다음과 같은 콘텐츠 카드 유형을 제공합니다: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html), [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). 각 유형은 기본 모델 [카드](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)에서 공통 속성정보를 상속받으며 다음과 같은 추가 속성정보가 있습니다.

{% alert tip %}
콘텐츠 카드 데이터를 로깅하려면 [분석 로깅을]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) 참조하세요.
{% endalert %}

### 기본 카드 모델

모든 콘텐츠 카드에는 이러한 공유 속성이 있습니다:

|등록정보|설명|
|---|---|
| `expiresAt` | 카드 만료 시간의 Unix 타임스탬프.|
| `extras`| (선택 사항) 값 문자열이 포함된 문자열 오브젝트로 형식이 지정된 키-값 페어 데이터. |
| `id` | (선택 사항) 카드의 ID입니다. 이는 분석 목적으로 이벤트와 함께 Braze에 다시 보고됩니다. |
| `pinned` | 이 속성정보는 대시보드에서 카드가 '고정됨'으로 설정되었는지 여부를 반영합니다.|
| `updated` | 이 카드가 마지막으로 수정된 시점의 UNIX 타임스탬프입니다. |
| `viewed` | 이 속성정보는 사용자가 카드를 조회했는지 여부를 반영합니다.|
| `isControl` | 이 속성정보는 카드가 A/B 테스트 내에서 '대조군'인 경우 `true`입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이미지만

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) 카드는 클릭 가능한 전체 크기 이미지입니다.

|등록정보|설명|
|---|---|
| `aspectRatio` | 카드 이미지의 가로 세로 비율이며 이미지 로딩이 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성이 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 순전히 커스텀 구현의 구성을 위해 제공되며, 대시보드 작성기에서 이러한 카테고리를 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 카드가 이 기기에서 클릭된 적이 있는지 여부를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `dismissed` | 이 속성은 이 카드가 기각되었는지 여부를 나타냅니다. |
| `dismissible` | 이 속성은 사용자가 카드를 해지하여 보기에서 제거할 수 있는지 여부를 반영합니다. |
| `imageUrl` | 카드 이미지의 URL입니다.|
| `linkText` | URL의 표시 텍스트입니다. |
| `url` | 카드를 클릭한 후 열릴 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 캡션 이미지

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) 카드는 클릭 가능한 전체 크기 이미지로, 설명 텍스트가 함께 제공됩니다.

|등록정보|설명|
|---|---|
| `aspectRatio` | 카드 이미지의 가로 세로 비율이며 이미지 로딩이 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성이 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 순전히 커스텀 구현의 구성을 위해 제공되며, 대시보드 작성기에서 이러한 카테고리를 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 카드가 이 기기에서 클릭된 적이 있는지 여부를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `dismissed` | 이 속성은 이 카드가 기각되었는지 여부를 나타냅니다. |
| `dismissible` | 이 속성은 사용자가 카드를 해지하여 보기에서 제거할 수 있는지 여부를 반영합니다. |
| `imageUrl` | 카드 이미지의 URL입니다.|
| `linkText` | URL의 표시 텍스트입니다. |
| `title` | 이 카드의 제목 텍스트입니다. |
| `url` | 카드를 클릭한 후 열릴 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 클래식

[클래식카드](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) 모델에는 텍스트가 없는 이미지 또는 텍스트가 있는 이미지가 포함될 수 있습니다.

|등록정보|설명|
|---|---|
| `aspectRatio` | 카드 이미지의 가로 세로 비율이며 이미지 로딩이 완료되기 전에 힌트 역할을 합니다. 특정 상황에서는 속성이 제공되지 않을 수 있습니다. |
| `categories` | 이 속성정보는 순전히 커스텀 구현의 구성을 위해 제공되며, 대시보드 작성기에서 이러한 카테고리를 설정할 수 있습니다. |
| `clicked` | 이 속성정보는 이 카드가 이 기기에서 클릭된 적이 있는지 여부를 나타냅니다. |
| `created` | Braze에서 카드가 생성된 시간의 UNIX 타임스탬프입니다. |
| `description` | 이 카드의 본문 텍스트입니다. |
| `dismissed` | 이 속성은 이 카드가 기각되었는지 여부를 나타냅니다. |
| `dismissible` | 이 속성은 사용자가 카드를 해지하여 보기에서 제거할 수 있는지 여부를 반영합니다. |
| `imageUrl` | 카드 이미지의 URL입니다.|
| `linkText` | URL의 표시 텍스트입니다. |
| `title` | 이 카드의 제목 텍스트입니다. |
| `url` | 카드를 클릭한 후 열릴 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 대조군

기본 콘텐츠 카드 피드를 사용하는 경우 노출 수와 클릭 수가 자동으로 추적됩니다.

콘텐츠 카드에 대한 커스텀 통합을 사용하는 경우 제어 카드가 표시되면 [노출 횟수를 기록]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/)해야 합니다. 이러한 노력의 일환으로, A/B 테스트에서 노출 횟수를 기록할 때 제어 카드를 처리해야 합니다. 이러한 카드는 비어 있으며 사용자에게 표시되지 않지만, 여전히 노출 횟수를 기록하여 제어 카드가 아닌 카드와 해당 성능을 비교해야 합니다.

콘텐츠 카드가 A/B 테스트의 대조군에 있는지 확인하려면 `card.isControl` 속성정보(Web SDK v4.5.0 이상)를 확인하거나 카드가 `ControlCard` 인스턴스(`card instanceof braze.ControlCard`)인지 확인합니다.

## 카드 방법

|방법 | 설명 |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| 지정된 카드 목록에 대한 노출 이벤트를 기록합니다. Braze UI가 아닌 사용자 지정 UI를 사용할 때 필요합니다.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| 지정된 카드에 대한 클릭 이벤트를 기록합니다. Braze UI가 아닌 사용자 지정 UI를 사용할 때 필요합니다.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| 사용자의 콘텐츠 카드를 표시합니다. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| 현재 표시된 Braze 콘텐츠 카드를 숨깁니다. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| 사용자의 콘텐츠 카드를 표시합니다. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|마지막 콘텐츠 카드 새로 고침에서 현재 사용 가능한 모든 카드를 가져옵니다.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| 콘텐츠 카드 업데이트에 가입합니다. <br> 구독자 콜백은 콘텐츠 카드가 업데이트될 때마다 호출됩니다. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|프로그래밍 방식으로 카드를 해제합니다(v2.4.1에서 사용 가능).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

자세한 내용은 [SDK 참조 설명서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)를 참조하세요.

## Google 태그 관리자 사용

Google 태그 매니저는 웹사이트 코드에 [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (웹 SDK 버전)을 직접 삽입하는 방식으로 작동하므로 콘텐츠 카드를 구현할 때를 제외하고는 Google 태그 매니저 없이 SDK를 통합한 것처럼 모든 SDK 방법을 사용할 수 있습니다.

### 콘텐츠 카드 설정하기

{% tabs local %}
{% tab Google 태그 관리자 %}
콘텐츠 카드 피드의 표준 통합을 위해 Google 태그 관리자에서 **사용자 정의 HTML** 태그를 사용할 수 있습니다. 표준 콘텐츠 카드 피드를 활성화하는 사용자 정의 HTML 태그에 다음을 추가합니다:

```html
<script>
   window.braze.showContentCards();
</script>
```

![콘텐츠 카드 피드를 표시하는 사용자 지정 HTML 태그의 Google 태그 관리자에서 태그 구성]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab 매뉴얼 %}
콘텐츠 카드의 모양과 피드를 보다 자유롭게 사용자 지정하려는 경우 콘텐츠 카드를 기본 웹사이트에 직접 통합할 수 있습니다. 표준 피드 UI를 사용하거나 커스텀 피드 UI를 생성하는 두 가지 접근 방식이 있습니다.

{% subtabs local %}
{% subtab standard feed %}
[표준 피드 UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui)를 구현할 때 Braze 메서드는 메서드 시작 부분에 `window.`를 추가해야 합니다. 예를 들어 `braze.showContentCards`는 `window.braze.showContentCards`가 되어야 합니다.
{% endsubtab %}

{% subtab custom feed %}
[커스텀 피드]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) 스타일의 경우, 단계는 GTM 없이 SDK를 통합한 경우와 동일합니다. 예를 들어 콘텐츠 카드 피드의 너비를 사용자 지정하려면 다음을 CSS 파일에 붙여넣으면 됩니다:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 템플릿 업그레이드 {#upgrading}

Braze 웹 SDK의 최신 버전으로 업그레이드하려면Google Tag Manager 대시보드에서 다음 세 단계를 수행합니다.

1. **태그 템플릿 업데이트**<br>워크스페이스 내의 **템플릿** 페이지로 이동합니다. 여기에 업데이트를 사용할 수 있음을 나타내는 아이콘이 표시됩니다.<br><br>![업데이트를 보여주는 템플릿 페이지]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>해당 아이콘을 클릭하고 변경 사항을 검토한 후 **업데이트 수락**을 클릭합니다.<br><br>!['업데이트 수락' 버튼이 있는 이전 태그 템플릿과 새 태그 템플릿을 비교하는 화면]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **업데이트 버전 번호**<br>태그 템플릿이 업데이트되면 Braze 초기화 태그를 편집하고 SDK 버전을 최신 `major.minor` 버전으로 업데이트합니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. SDK 버전 목록은 [변경 로그에서](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) 확인할 수 있습니다.<br><br>![SDK 버전 변경을 위한 입력 필드가 있는 Braze 초기화 템플릿]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA 및 게시**<br>태그 컨테이너에 업데이트를 게시하기 전에 Google 태그 관리자의 [디버깅 도구를](https://support.google.com/tagmanager/answer/6107056?hl=en) 사용하여 새 SDK 버전이 작동하는지 확인합니다.

### 문제 해결 {#troubleshooting}

#### 태그 디버깅 사용 {#debugging}

각 Braze 태그 템플릿에는 웹 페이지의 JavaScript 콘솔에 디버그 메시지를 기록하는 데 사용할 수 있는 **GTM 태그 디버깅** 체크박스(선택 사항)가 있습니다.

![Google 태그 관리자의 디버그 도구]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### 디버그 모드로 전환

Google 태그 관리자 연동 디버깅에 도움이 되는 또 다른 방법은 Google의 [미리보기 모드](https://support.google.com/tagmanager/answer/6107056) 기능을 사용하는 것입니다.

이렇게 하면 웹 페이지의 데이터 레이어에서 트리거된 각 Braze 태그로 전송되는 값을 식별하는 데 도움이 되며, 어떤 태그가 트리거되었는지 또는 트리거되지 않았는지도 설명할 수 있습니다.

![Braze 초기화 태그 요약 페이지에서는 트리거된 태그에 대한 정보를 포함하여 태그에 대한 개요를 확인할 수 있습니다.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### 상세 로깅 활성화

테스트하는 동안 Braze 기술 지원팀이 로그에 액세스할 수 있도록 하려면 Google Tag Manager 통합에서 상세 로깅을 활성화하면 됩니다. 이러한 로그는 브라우저 [개발자 도구의](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) **콘솔** 탭에 표시됩니다.

Google Tag Manager 통합에서 Braze 초기화 태그로 이동하고 **웹 SDK 로깅 활성화**를 선택합니다.

![웹 SDK 로깅 활성화 옵션이 켜져 있는 Braze 초기화 태그 요약 페이지.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
