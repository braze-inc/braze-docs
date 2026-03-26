### 필수 조건

이 통합 방법을 사용하기 전에 Google Tag Manager에 대한 계정과 컨테이너를 [생성해야 합니다](https://support.google.com/tagmanager/answer/14842164).

### 1단계: 태그 템플릿 갤러리를 엽니다

[Google Tag Manager](https://tagmanager.google.com/)에서 작업 공간을 선택한 다음 **템플릿**을 선택합니다. **태그 템플릿** 창에서 **갤러리 검색**을 선택합니다.

![Google Tag Manager의 예제 작업 공간에 대한 템플릿 페이지입니다.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### 2단계: 초기화 태그 템플릿을 추가합니다

템플릿 갤러리에서 `braze-inc`을 검색한 다음 **Braze 초기화 태그**를 선택합니다.

![다양한 'braze-inc' 템플릿을 보여주는 템플릿 갤러리입니다.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**작업 공간에 추가** > **추가**를 선택합니다.

![Google Tag Manager의 'Braze 초기화 태그' 페이지입니다.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### 3단계: 태그를 구성합니다

**템플릿** 섹션에서 새로 추가한 템플릿을 선택합니다.

![Braze 초기화 태그 템플릿을 보여주는 Google Tag Manager의 "템플릿" 페이지입니다.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

연필 아이콘을 선택하여 **태그 구성** 드롭다운을 엽니다.

![연필 아이콘이 표시된 태그 구성 타일입니다.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

필수 최소 정보를 입력하세요:

| 필드         | 설명 |
| ------------- | ----------- |
| **API 키**   | Braze 대시보드의 [Braze API 키]({{site.baseurl}}/api/basics/#about-rest-api-keys)에서 찾을 수 있는 정보입니다. **설정** > **앱 설정** 아래에 있습니다. |
| **API 엔드포인트** | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
| **SDK 버전**  | `MAJOR.MINOR`웹 Braze SDK의 가장 최근 버전이 [체인지로그]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)에 나열되어 있습니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. 자세한 내용은 [SDK 버전 관리에 대한 정보]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

추가 초기화 설정을 위해 **Braze 초기화 옵션**을 선택하고 필요한 옵션을 선택하십시오.

![태그 구성 아래의 Braze 초기화 옵션 목록입니다.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### 4단계: 초기화 옵션 선택

Braze 초기화 태그는 다음 옵션을 노출합니다. 이들 대부분은 [웹 SDK `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)에 직접 매핑되며, 일부는 초기화 중 태그가 호출할 웹 SDK 메서드에 해당합니다. 통합 요구 사항에 맞는 옵션을 선택하십시오:

| GTM 옵션 | 웹 SDK 구성 또는 메서드 | 설명 |
| --- | --- | --- |
| **HTML 인앱 메시지 허용** | `allowUserSuppliedJavascript` | HTML 인앱 메시지, 배너 및 사용자 제공 JavaScript 클릭 작업을 활성화합니다. 사용자 정의 HTML을 사용하는 [HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) 및 [배너]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web)에 필요합니다. HTML 및 JavaScript 콘텐츠를 신뢰할 때만 이 기능을 활성화하십시오. 사용자 제공 JavaScript 실행을 허용합니다. |
| **앱 버전 번호** | `appVersion`, `appVersionNumber` | 세분화를 위한 앱 버전(예: `1.2.3.4`). |
| **새 세션 자동 열기** | `braze.openSession()` | SDK가 초기화된 후 이 메서드를 호출하여 새 세션을 엽니다. |
| **새 인앱 메시지 자동 표시** | `braze.automaticallyShowInAppMessages()` | 초기화 후 이 메서드를 호출하여 서버에서 도착한 새 인앱 메시지를 자동으로 표시합니다. |
| **자동 푸시 토큰 유지 관리 비활성화** | `disablePushTokenMaintenance` | 새 세션에서 Braze 백엔드와 푸시 토큰을 동기화하지 않도록 SDK를 중지합니다. |
| **자동 서비스 종사자 등록 비활성화** | `manageServiceWorkerExternally` | 서비스 종사자를 직접 등록하고 제어하는 경우 사용하십시오. |
| **쿠키 비활성화** | `noCookies` | 사용자/세션 데이터에 쿠키 대신 localStorage를 사용합니다. 교차 서브도메인 인식을 방지합니다. |
| **폰트 어썸 비활성화** | `doNotLoadFontAwesome` | SDK가 CDN에서 Font Awesome을 로드하지 않도록 방지합니다. 사이트에 자체 Font Awesome이 있는 경우 사용하십시오. |
| **SDK 인증 활성화** | `enableSdkAuthentication` | [SDK 인증]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)을 활성화합니다. |
| **웹 SDK 로깅 활성화** | `enableLogging` | 디버깅을 위한 콘솔 로깅을 활성화합니다. 프로덕션 전에 제거하십시오. |
| **트리거된 메시지 간 최소 간격** | `minimumIntervalBetweenTriggerActionsInSeconds` | 트리거 작업 간 최소 초(기본값: 30). |
| **새 탭에서 카드 열기** | `openCardsInNewTab` | 기본 피드 UI를 사용할 때 콘텐츠 카드 링크를 새 탭에서 엽니다. |
| **서비스 종사자 위치** | `serviceWorkerLocation` | 서비스 종사자 파일의 사용자 지정 경로(기본값: `/service-worker.js`). |
| **세션 타임아웃 (초)** | `sessionTimeoutInSeconds` | 세션 타임아웃(초) (기본값: 1800). |

{% alert note %}
Google Tag Manager Braze 초기화 태그를 사용할 때 [커스텀 HTML 인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/)를 활성화하려면 **Braze 초기화 옵션**에서 **HTML 인앱 메시지 허용**을 선택하세요. 이 체크박스는 `braze.initialize()`의 `allowUserSuppliedJavascript` 초기화 옵션에 매핑되며 `true`로 설정됩니다. Google Tag Manager Braze 초기화 태그는 옵션 이름 대신 이 레이블을 사용합니다.
{% endalert %}

GTM 템플릿에서 노출되지 않은 옵션(예: `contentSecurityNonce`, `localization` 또는 `devicePropertyAllowlist`)의 경우 [런타임 초기화]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)를 대신 사용하세요.

### 5단계: 모든 페이지에서 트리거로 설정

초기화 태그는 사이트의 모든 페이지에서 실행되어야 합니다. 이것은 Braze SDK 메서드를 사용하고 웹 푸시 분석을 기록할 수 있게 해줍니다.

### Step 6: 통합을 확인하세요

다음 옵션 중 하나를 사용하여 통합을 확인할 수 있습니다:

- **Option 1:** Google Tag Manager의 [디버깅 툴](https://support.google.com/tagmanager/answer/6107056?hl=en)를 사용하여 Braze 초기화 태그가 구성된 페이지나 이벤트에서 올바르게 트리거되는지 확인할 수 있습니다.
- **Option 2:** 웹 페이지에서 Braze로 전송된 네트워크 요청을 확인하세요. 추가로, 전역 `window.braze` 라이브러리가 이제 정의되어야 합니다.
