---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "이 참조 문서에서는 모바일, 웹, 대체 데이터를 다른 서드파티 소스에 연결할 수 있는 유니버설 데이터 허브인 Tealium와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/)은 모바일, 웹, 타사 소스의 대체 데이터를 연결할 수 있는 EventStream, AudienceStream, iQ 태그 관리로 구성된 유니버설 데이터 허브이자 고객 데이터 플랫폼입니다. Braze에 Tealium을 연결하면 커스텀 이벤트, 사용자 속성, 구매 데이터의 데이터 흐름을 통해 실시간으로 데이터에 기반한 조치를 취할 수 있습니다.

![다양한 Tealium 제품과 Braze 플랫폼이 어떻게 크로스채널 캠페인을 실시간으로 활성화하는지를 보여주는 Tealium 개요 그래픽.][22]{: style="border:0;"}

Braze와 Tealium의 통합을 통해 사용자를 추적하고 다양한 사용자 분석 제공업체로 데이터를 라우팅할 수 있습니다. Tealium을 통해 다음이 가능합니다.
- Braze 캠페인과 캔버스를 개인화하거나 세그먼트를 구축하는 데 사용할 수 있도록 Tealium 오디언스를 [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/)에서 Braze에 동기화합니다.
- [여러 플랫폼에서 데이터를 가져옵니다](#choose-your-integration-type). Braze는 Android, iOS, 웹 애플리케이션을 위한 [나란히](#side-by-side-sdk-integration) 배치된 SDK 통합과 이벤트 데이터를 보고할 수 있는 모든 플랫폼 내에서 사용할 수 있는 [서버 간](#server-to-server-integration) 통합을 모두 제공합니다.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream은 데이터의 중심에 존재하는 데이터 수집 및 API 허브입니다. EventStream은 설정 및 설치부터 수신되는 사용자 데이터의 식별, 유효성 검사, 개선에 이르기까지 전체 데이터 공급망을 처리합니다. EventStream은 이벤트 피드와 커넥터를 통해 실시간으로 작업을 수행합니다. [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/)을 구성하는 기능은 다음과 같습니다.
- 데이터 소스(설치 및 데이터 수집)
- 라이브 이벤트(실시간 데이터 검사)
- 이벤트 사양 및 속성(데이터 계층 요구 사항 및 유효성 검사)
- 이벤트 피드(필터링된 이벤트 유형)
- 이벤트 커넥터(API 허브 작업)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream은 옴니채널 고객 세분화 및 실시간 실행 엔진입니다. AudienceStream은 EventStream으로 유입되는 데이터를 사용해 고객의 브랜드 참여에 대한 가장 중요한 속성을 나타내는 방문자 프로필을 생성합니다. 설정 단계는 [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) 문서를 참조하세요.

{% endtab %}
{% tab iQ 태그 관리 %}
Tealium iQ는 Tealium iQ 태그 관리 UI에서 태그를 사용하여 앱에서 코드를 트리거할 수 있습니다. 이 태그는 모바일 및 웹 플랫폼에서 이벤트 데이터를 수집, 제어 및 전달하므로 앱에 Braze 관련 코드를 추가하지 않고도 기본 Braze 구현을 구성할 수 있습니다. 사용자는 iQ 태그 관리 또는 JSON 구성 파일을 통해 모바일 원격 명령을 통합하도록 선택할 수 있습니다(권장되는 Tealium 접근 방식). Braze 웹 SDK를 사용하는 사용자는 웹 iQ 태그를 통해 통합해야 합니다.

각 방법의 장단점에 대해 자세히 알아보려면 다음 [Tealium iQ 태그 관리자](#mobile-remote-commands) 섹션을 참조하세요.
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium은 배치 및 비배치 커넥터 작업을 모두 제공합니다. 비배치 커넥터는 실시간 요청이 사용 사례에 중요하고 Braze API 속도 제한 사양에 도달할 염려가 없는 경우에 사용해야 합니다. 궁금한 점이 있으면 Braze 지원팀 또는 고객 성공 관리자에게 문의하세요.<br><br>

배치 커넥터의 경우 다음 임계값 중 하나가 충족될 때까지 요청이 대기줄에서 대기합니다.<br><br>
- 최대 요청 수: 75
- 가장 오래된 요청 이후 최대 시간. 10분
- 최대 요청 크기: 1MB

Tealium은 기본적으로 동의 이벤트(가입 환경설정) 또는 사용자 삭제 이벤트를 배치 처리하지 않습니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tealium 계정 | 이 파트너십을 활용하려면 서버 및/또는 클라이언트 측 액세스 권한이 있는 [Tealium 계정](https://my.tealiumiq.com/)이 필요합니다. | 
| 설치된 소스 및 Tealium 소스 [라이브러리](https://docs.tealium.com/platforms/) | 모바일 앱, 웹사이트 또는 백엔드 서버 등 Tealium으로 전송된 모든 데이터의 출처입니다.<br><br>앱, 사이트 또는 서버에 라이브러리를 설치해야만 Tealium 커넥터를 성공적으로 설정할 수 있습니다. |
| Braze REST 및 SDK 엔드포인트 | REST 또는 SDK 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/#endpoints) 따라 달라집니다. |
| Braze 앱 식별자 키(나란히만 사용 가능) | 앱 식별자 키. <br><br>**Braze 대시보드 > 설정 관리 > API 키**에서 찾을 수 있습니다. |
| 코드 버전(병렬 전용) | SDK 버전에 해당하며 major.minor 형식이어야 합니다(예: 3.0.1이 아닌 3.2). 코드 버전은 3.0 이상이어야 합니다. |
| REST API 키(서버 간에만 해당) | `users.track` 및 `users.delete` 권한이 있는 Braze REST API 키. <br><br>**Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 생성할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 유형 선택

| 통합 | 세부 정보 |
| ----------- | ------- |
| [병렬](#side-by-side-sdk-integration) | Tealium의 SDK를 사용하여 이벤트를 Braze 네이티브 호출로 변환하여 서버 간 통합보다 더 심층적인 기능에 액세스하고 더 포괄적으로 Braze를 사용할 수 있습니다.<br><br>Braze 원격 명령을 사용하려는 경우, Tealium이 모든 Braze 메서드(예: 콘텐츠 카드)를 지원하지는 않는다는 점에 유의하세요. 해당 원격 명령을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 기본 Braze 코드를 추가하여 메서드를 호출해야 합니다.|
| [서버 간](#server-to-server-integration) | Tealium에서 Braze REST API 엔드포인트로 데이터를 전달합니다.<br><br>인앱 메시징, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 메서드를 통해 사용할 수 없는 기기 수준 필드와 같이 자동으로 캡처된 데이터도 존재합니다.<br><br>이 기능을 사용하려면 병렬 통합을 고려합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK 병렬 통합

### 원격 명령

원격 명령은 Tealium iOS 및 Android 라이브러리의 기능으로, Tealium SDK에서 Braze 서버를 통해 Braze로 호출할 수 있습니다. Braze 원격 명령 모듈은 필요한 Braze 라이브러리를 자동으로 설치 및 빌드하고 모든 메시지 렌더링 및 분석 추적을 처리합니다. Braze 모바일 원격 명령을 사용하려면 앱에 Tealium 라이브러리가 설치되어 있어야 합니다.

Tealium은 모바일 원격 명령을 통합하는 두 가지 방법을 제공하며, 통합 유형 간에 기능 손실이 없고 기본 네이티브 코드가 동일합니다.

| 모바일 원격 명령 방법 | 장점 | 단점 |
| --- | --- | --- |
| **원격 명령 태그** | Tealium iQ UI를 사용하여 원격 명령으로 전송되는 매핑과 데이터를 쉽게 수정할 수 있습니다.<br><br>이를 통해 클라이언트가 앱을 업데이트할 필요 없이 앱을 이미 App Store에 등록한 후 추가 데이터나 이벤트를 서드파티 SDK로 전송할 수 있습니다. | 앱의 태그 관리 모듈은 숨겨진 웹뷰를 사용하여 JavaScript를 처리합니다. |
| **JSON 구성 파일**<br>[(권장](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | JSON 메서드를 사용하면 앱에 숨겨진 웹뷰가 필요하지 않으며 메모리 사용량을 크게 줄일 수 있습니다.<br><br>JSON 파일은 원격으로 호스팅하거나 고객 앱 내에서 로컬로 호스팅할 수 있습니다. | 현재로서는 이를 관리할 수 있는 UI가 없기 때문에 약간의 추가 노력이 필요합니다.<br><br>참고: Tealium은 이 문제를 해결하고 iQ Tag 관리 버전과 동일한 수준의 유연성을 JSON 원격 명령에 제공할 수 있는 관리 UI를 추가하기 위해 노력하고 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze 모바일 원격 명령 데이터 매핑을 사용하여 기본 사용자 속성 및 사용자 지정 속성을 설정하고 구매 및 사용자 지정 이벤트를 추적할 수 있습니다. 해당 Braze 메서드는 다음 차트를 참조하세요.

| 원격 명령 | 브레이징 방법 |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| 이메일 알림 | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| 초기화 | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| 로그 구매 | logPurchase() |
| 푸시 알림 | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| 사용자 식별자 | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze 모바일 원격 명령 설정 방법과 지원되는 메서드의 개요에 대한 자세한 내용은 Tealium 개발자 설명서에서 확인할 수 있습니다.
- [원격 명령](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [원격 명령 태그](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Braze 모바일 원격 명령은 일부 Braze 메서드와 메시징 채널(예: 콘텐츠 카드)을 지원하지 않습니다. 해당 원격 명령을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 기본 Braze 코드를 추가하여 직접 메서드를 호출해야 합니다.
{% endalert%}

### Braze 웹 SDK 태그

브레이즈 웹 SDK 태그를 사용하여 웹사이트에 브레이즈 웹 SDK를 배포하세요. [Tealium iQ 태그 관리](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)를 통해 고객은 방문자 활동을 추적하기 위해 Tealium 대시보드 내에 Braze를 태그로 추가할 수 있습니다. 태그는 일반적으로 마케팅 담당자가 온라인 광고, 이메일 마케팅 및 사이트 개인화의 효과를 파악하는 데 사용합니다.

1. Tealium에서 **iQ > 태그 > + 태그 추가 > Braze 웹 SDK**로 이동합니다.
2. 태그 구성 대화 상자에서 API 키(Braze 앱 식별자 키), 기본 URL(Braze SDK 엔드포인트), [Braze 웹 SDK 코드 버전을](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) 입력합니다. 디버깅 목적으로 웹 콘솔에 정보를 기록하도록 로깅을 활성화할 수도 있습니다.
3. [로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/) 대화 상자에서 '모든 페이지에 로드'를 선택하거나 **규칙 생성**을 선택하여 사이트에서 이 태그의 인스턴스를 로드할 시기와 위치를 결정합니다.
4. 에서 **[데이터 매핑](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** 대화 상자에서 **매핑 생성을** 선택하여 Tealium 데이터를 Braze에 매핑합니다. Braze 웹 SDK 태그의 대상 변수는 태그의 **데이터 매핑** 탭에 내장되어 있습니다. [다음 표](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)에서는 사용 가능한 대상 카테고리를 나열하며 각 대상 이름을 설명합니다.
5. **마침**을 선택합니다.

### 병렬 통합 리소스

- iOS 원격 명령: [Tealium 문서](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub 리포지토리](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android 원격 명령: [Tealium 문서](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub 리포지토리](https://github.com/Tealium/tealium-android-braze-remote-command)
- 웹 SDK 태그: [Tealium 문서](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## 서버 간 통합

이 통합은 Tealium에서 Braze REST API로 데이터를 전달합니다.

서버 간 통합은 인앱 메시징, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 메서드를 통해 사용할 수 없는 기기 수준 필드와 같이 자동으로 캡처된 데이터도 존재합니다.

이 데이터와 이러한 기능을 사용하려면 SDK [병렬]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration) 통합을 사용하는 것이 좋습니다.

### 1단계: 소스 설정

Tealium에서는 먼저 커넥터에서 가져올 유효한 데이터 소스를 설정해야 합니다.
1. Tealium의 사이드바에서 **서버 측** 아래의 **소스 > 데이터 소스 > + 데이터 소스 추가**로 이동합니다.
2. 사용 가능한 카테고리에서 원하는 플랫폼을 찾고 소스 이름을 입력합니다(필수 필드).<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. **이벤트 사양** 옵션에서 포함할 [이벤트 사양](https://docs.tealium.com/server-side/event-specifications/about/)을 선택합니다. 이벤트 사양은 설치에서 추적할 이벤트 이름과 필수 속성을 식별하는 데 도움이 됩니다. 이러한 사양은 수신 이벤트에 적용됩니다.<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>어떤 데이터가 가장 가치가 있는지, 어떤 사양이 사용 사례에 가장 적합한지 생각해 보세요. [커스텀 이벤트 사양][19]도 사용할 수 있습니다. <br>
4. 다음 대화 상자는 **코드 가져오기** 단계로 진행됩니다. 여기에 제공된 기본 코드와 이벤트 추적 코드는 설치 가이드 역할을 합니다. 이 지침을 팀과 공유하려면 제공된 PDF를 다운로드하세요. 완료되면 **저장 후 계속**을 선택합니다.<br>
5. 이제 저장된 소스를 확인하고 이벤트 사양을 추가하거나 제거할 수 있습니다. <br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>세부 데이터 소스 보기에서 다음 작업을 수행할 수 있습니다.
- 데이터 소스 키 보기 및 복사
- 설치 지침 보기
- **코드 받기** 페이지로 돌아가기
- 이벤트 사양 추가 또는 제거
- 이벤트 사양과 관련된 실시간 이벤트를 보기 위해 탐색
- 기타...<br>
6. 마지막으로, 페이지 상단에 있는 **저장/게시**를 선택합니다. 소스를 게시하지 않으면 Braze 커넥터를 구성할 때 소스를 찾을 수 없습니다.

데이터 소스 설정 및 편집에 대한 자세한 지침은 [데이터 소스](https://docs.tealium.com/server-side/data-sources/about-data-sources/)를 참조하세요.

### 2단계: 이벤트 커넥터 만들기

커넥터는 데이터를 전송하는 데 사용되는 Tealium과 다른 공급업체 간의 통합입니다. 이러한 커넥터에는 파트너가 지원하는 API를 나타내는 작업이 포함되어 있습니다. 

1. Tealium의 사이드바에서 **서버 측** 아래의 **EventStream > 이벤트 커넥터**로 이동합니다.
2. 파란색 **\+ 커넥터 추가** 버튼을 선택하여 커넥터 마켓플레이스를 살펴봅니다. 새 대화 상자가 나타나면 스포트라이트 검색을 사용하여 **Braze** 커넥터를 찾습니다.
3. 이 커넥터를 추가하려면 **브레이즈** 커넥터 타일을 클릭합니다. 클릭하면 연결 요약과 필수 정보 목록, 지원되는 작업 및 구성 지침을 볼 수 있습니다. 구성은 소스, 구성, 작업의 세 단계로 구성됩니다.

#### 소스

소스를 구성한 후 **이벤트스트림** > **이벤트 커넥터** > **\+ 커넥터 추가** > **브레이즈** 아래의 브레이즈 커넥터 페이지로 돌아갑니다. 

그런 다음 방금 구축한 데이터 소스를 선택하고 **이벤트 피드에서** **모든 이벤트** 또는 특정 이벤트 사양(변경된 값만 Braze로 전송하도록 권장되는 경로)을 선택합니다. **계속**을 선택합니다.

#### 구성

그런 다음, 페이지 하단에서 **커넥터 추가**를 선택합니다. 여기에서 커넥터의 이름을 지정하고 Braze API 엔드포인트와 Braze REST API 키를 제공합니다.

![][15]{: style="max-width:70%;"}

이전에 커넥터를 만든 적이 있다면 사용 가능한 커넥터 목록에서 기존 커넥터를 선택적으로 사용하고 연필 아이콘을 사용하여 필요에 맞게 수정하거나 휴지통 아이콘을 사용하여 삭제할 수 있습니다. 

#### 작업

그런 다음 커넥터 작업의 이름을 지정하고 구성한 매핑에 따라 데이터를 전송할 작업 유형을 선택합니다. 여기에서 Braze 속성, 이벤트 및 구매를 Tealium 속성, 이벤트 및 구매 이름에 매핑합니다.

{% alert important %}
제공되는 모든 필드가 필수 항목은 아닙니다.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab 사용자 추적 - 배치 및 비배치 %}

이 작업을 통해 사용자, 이벤트, 구매 속성을 모두 한 번에 추적할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze의 해당하는 필드에 매핑합니다. 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선 순위에 따라 비어 있지 않은 첫 번째 값이 선택됩니다: 외부 아이디, Braze ID, 별칭 이름 및 별칭 라벨.<br><br>\- 푸시 토큰을 가져오는 경우 외부 ID와 Braze ID를 지정하지 않아야 합니다.<br>\- 사용자 별칭을 지정하는 경우 별칭 이름과 별칭 레이블을 설정해야 합니다. <br><br>자세한 내용은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 확인하세요. |
| 사용자 속성 | 기존 Braze 사용자 프로필 필드 이름을 사용하여 Braze 대시보드에서 사용자 프로필 값을 업데이트하거나 사용자 프로필에 사용자 지정 [사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 데이터를 추가할 수 있습니다.<br><br>\- 기본적으로 사용자가 없는 경우 새 사용자가 만들어집니다.<br>- **기존 사용자만 업데이트**를 `true`로 설정하면, 기존 사용자만 업데이트되고 새 사용자는 생성되지 않습니다.<br>\- Tealium 속성이 비어 있는 경우, null로 변환되어 Braze 고객 프로필에서 제거됩니다. 사용자 속성을 제거하기 위해 Braze에 null 값을 보내서는 안 되는 경우 보강을 사용해야 합니다. |
| 사용자 속성 수정 | 이 필드를 사용하여 특정 사용자 속성을 늘리거나 줄입니다.<br><br>\- 정수 속성은 양의 정수 또는 음의 정수로 증가될 수 있습니다.<br>\- 배열 속성은 기존 배열에서 값을 추가하거나 제거하여 수정할 수 있습니다. |
| 이벤트 | 이벤트는 특정 사용자가 특정 타임스탬프에 커스텀 이벤트가 한 번 발생한 것을 나타냅니다. 이 필드를 사용하여 Braze [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/)에서와 같이 이벤트 속성을 추적하고 매핑합니다. <br><br>\- 이벤트 속성 `Name`은 매핑된 모든 이벤트에서 필수입니다.<br>\- 이벤트 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 now로 설정됩니다. <br>\- 기본적으로 이벤트가 없는 경우 새 이벤트가 생성됩니다. `Update Existing Only` 을 `true` 으로 설정하면 기존 이벤트만 업데이트되고 새 이벤트는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 이벤트를 추가합니다. 배열 유형 속성은 길이가 같아야 합니다.<br>\- 단일 값 속성을 사용하여 각 이벤트에 적용할 수 있습니다. |
| 이벤트 템플릿 | 본문 데이터에서 참조할 이벤트 템플릿을 제공합니다. 템플릿을 사용하여 데이터를 Braze로 전송하기 전에 데이터를 변환할 수 있습니다. 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요. |
| 이벤트 템플릿 변수 | 이벤트 템플릿 변수를 데이터 입력으로 제공하세요. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
| 구매 | 이 필드를 사용하여 Braze [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)에서와 같이 사용자 구매 속성을 추적하고 매핑합니다.<br><br>\- 매핑된 모든 구매에는 구매 속성 `Product ID`, `Currency`, `Price`가 필수입니다.<br>\- 구매 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 now로 설정됩니다.<br>\- 기본적으로 구매가 없는 경우 새 구매가 생성됩니다. `Update Existing Only` 을 `true` 으로 설정하면 기존 구매만 업데이트되고 새 구매는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 구매 항목을 추가합니다. 배열 유형 속성은 길이가 같아야 합니다.<br>\- 단일 값 속성을 사용할 수 있으며 각 항목에 적용됩니다.|
| 구매 템플릿 | 템플릿은 데이터를 Braze로 전송하기 전에 데이터를 변환하는 데 사용할 수 있습니다.<br>\- 중첩된 개체 지원이 필요한 경우 구매 템플릿을 정의합니다.<br>\- 구매 템플릿이 정의되면 작업의 구매 섹션에 설정된 구성은 무시됩니다.<br>\- 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요.|
| 구매 템플릿 변수 | 데이터 입력으로 제품 템플릿 변수를 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab 사용자 삭제 - 비일괄 %}

이 작업을 통해 Braze 대시보드에서 사용자를 삭제할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze에 해당하는 필드에 매핑합니다. <br><br>\- 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선 순위에 따라 비어 있지 않은 첫 번째 값이 선택됩니다: 외부 아이디, Braze ID, 별칭 이름 및 별칭 라벨.<br>\- 사용자 별칭을 지정할 때는 별칭 이름과 별칭 레이블을 모두 설정해야 합니다.<br><br>자세한 내용은 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

선택한 옵션을 수정하려면 **뒤로**를 선택하거나 완료하려면 **마침**을 선택합니다.

{% endtab %}
{% endtabs %}

**계속**을 선택합니다.

이제 커넥터가 Tealium 홈 페이지의 커넥터 목록에 표시됩니다. <br>![][13]{: style="max-width:80%;"}

완료되면 커넥터에 대해 **저장/게시하기를** 선택해야 합니다. 이제 트리거 연결이 충족되면 구성한 작업이 실행됩니다. 

### 3단계: Tealium 커넥터 테스트

커넥터를 시작 및 실행한 후에는 커넥터가 제대로 작동하는지 테스트해야 합니다. 이를 테스트하는 가장 간단한 방법은 Tealium **추적 툴**을 사용하는 것입니다. 추적 사용을 시작하려면 Tealium 툴 브라우저 확장을 추가했는지 확인합니다.

1. 새 추적을 시작하려면 사이드바의 **서버 측** 옵션 아래에서 **추적**을 선택합니다. **시작을** 선택하고 추적 ID를 캡처합니다.
2. 브라우저 확장을 열고 AudienceStream 추적에 추적 ID를 입력합니다.
3. 실시간 로그를 살펴봅니다.
4. 확장할 **작업 트리거** 항목을 선택하여 유효성을 검사하려는 작업을 확인합니다.
5. 유효성을 검사하려는 작업을 찾아 로그 상태를 확인합니다. 

Tealium의 추적 툴 구현에 대한 자세한 지침은 Tealium의 [추적 설명서][21]를 참조하세요.

## 통합 데모

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 데이터 포인트 초과 가능성

Tealium을 통해 Braze를 통합할 때 실수로 데이터 초과량이 발생할 수 있는 주된 세 가지 경우가 있습니다.

#### 중복 데이터 전송 - Braze 델타의 속성만 전송합니다.

Tealium은 사용자 속성의 Braze 델타를 전송하지 않습니다. 예를 들어, 사용자의 이름, 이메일, 휴대폰 번호를 추적하는 EventStream 작업이 있는 경우, Tealium은 작업이 트리거될 때마다 세 가지 속성을 모두 Braze로 전송합니다. Tealium은 변경되거나 업데이트된 내용을 찾지 않고 해당 정보만 전송합니다.

**솔루션**: <br>백엔드를 확인하여 속성이 변경되었는지 여부를 평가하고, 변경된 경우 Tealium의 관련 메서드를 호출하여 사용자 프로필을 업데이트할 수 있습니다. **일반적으로 Braze를 직접 통합하는 사용자가 수행합니다.** <br>**OR**<br> 백엔드에 자체 버전의 고객 프로필을 저장하지 않고 속성이 변경되었는지 여부를 알 수 없는 경우 AudienceStream을 사용할 수 있습니다.
값이 변경된 경우에만 사용자 속성을 전송하도록 [보강 기능을 생성합니다](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/). [보강 규칙](https://docs.tealium.com/server-side-connectors/braze-connector/)은 Tealium 설명서를 참조하세요.

#### 관련 없는 데이터를 전송하거나 불필요하게 데이터를 덮어쓰는 경우

동일한 이벤트 피드를 대상으로 하는 이벤트스트림이 여러 개 있는 경우, **해당 커넥터에 대해 활성화된 모든 액션** 은 단일 액션이 트리거될 때마다 자동으로 실행되며, \*\*이 경우 Braze에서 데이터를 덮어쓰고 불필요한 데이터 포인트를 소비할 수도 있습니다.

**솔루션**: <br>각 작업을 추적하기 위해 별도의 이벤트 사양 또는 피드를 설정하세요. <br>**OR**<br> 실행하지 않으려는 작업 또는 커넥터는 Tealium 대시보드의 토글을 사용하여 비활성화합니다.

#### 너무 일찍 Braze 초기화

Braze 웹 SDK 태그를 사용하여 Tealium과 통합하는 사용자는 MAU의 급격한 증가를 확인할 수도 있습니다. **페이지 로드 시 Braze가 초기화되면 웹 사용자가 웹사이트를 처음 탐색할 때마다 익명 프로필이 생성됩니다.** 사용자가 '로그인' 또는 '비디오 시청' 등의 특정 작업을 완료했을 때만 사용자 행동을 추적하여 MAU 수를 낮출 수도 있습니다.

**솔루션**: <br>[로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/)을 설정하여 태그가 사이트에서 로드되는 시기와 위치를 정확하게 결정합니다. 

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]:https://docs.tealium.com/iq-tag-management/events/about/
[21]:https://docs.tealium.com/server-side/connectors/trace/about/
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}
