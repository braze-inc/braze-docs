## Google 태그 관리자 사용 {#initialization-tag}

### 1단계: 푸시 설정(선택 사항)

선택적으로 Google Tag Manager를 통해 푸시를 보낼 수 있도록 하려면 먼저 [푸시 통합]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) 지침에 따라 다음을 수행합니다.
1. 사이트의 서비스 종사자를 사이트의 루트 디토리에 배치하여 구성
2. 브라우저 등록 설정 - 서비스 종사자가 구성된 후에는 해당 앱에서 기본적으로 또는 커스텀 HTML 태그를 통해(GTM 대시보드 사용) `braze.requestPushPermission()` 메서드를 설정해야 합니다. 또한 SDK가 초기화된 후 태그가 실행되는지 확인해야 합니다.

### 2단계: 초기화 태그 선택

커뮤니티 템플릿 갤러리에서 Braze를 검색하고 **Braze 초기화 태그**를 선택합니다.

![Braze 초기화 태그 구성 설정을 보여주는 대화 상자. 포함된 설정은 "태그 유형", "API 키", "API 엔드포인트", "SDK 버전", "외부 사용자 ID" 및 "Safari 웹 푸시 ID"입니다.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### 3단계: 설정 구성

대시보드의 **설정 관리** 페이지에서 찾을 수 있는 Braze API 앱 식별자 키와 SDK 엔드포인트를 입력합니다. 웹 SDK의 최신 버전( `major.minor` )을 입력합니다. 예를 들어 최신 버전이 `4.1.2`인 경우 `4.1`을 입력합니다. SDK 버전 목록은 [변경 로그에서](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) 확인할 수 있습니다.

### 4단계: 초기화 옵션 선택

초기 설정]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) 가이드)에 설명된 추가 초기화 옵션 중에서 선택합니다.

### 5단계: 검증 및 QA

이 태그를 배포한 후에는 두 가지 방법으로 제대로 통합되었는지 확인할 수 있습니다.

1. Google 태그 관리자의 [디버깅 도구를](https://support.google.com/tagmanager/answer/6107056?hl=en) 사용하면 구성된 페이지 또는 이벤트에서 Braze 초기화 태그가 트리거된 것을 확인할 수 있습니다.
2. 이제 Braze에 대한 네트워크 요청이 표시되어야 하며, 글로벌 `window.braze` 라이브러리가 웹 페이지에 정의되어 있어야 합니다.
