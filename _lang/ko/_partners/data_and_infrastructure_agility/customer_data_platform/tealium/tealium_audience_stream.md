---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "이 참조 문서에서는 모바일, 웹, 대체 데이터를 다른 서드파티 소스에 연결할 수 있는 유니버설 데이터 허브인 Tealium와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/)은 옴니채널 고객 세분화 및 실시간 실행 엔진입니다. AudienceStream은 EventStream으로 유입되는 데이터를 사용해 고객의 브랜드 참여에 대한 가장 중요한 속성을 나타내는 방문자 프로필을 생성합니다. 

Braze와 Tealium의 통합은 AudienceStream 방문자 프로필을 활용합니다. 공유된 행동은 이러한 프로필을 세분화하여 공통된 특성을 가진 방문자 집합, 즉 오디언스를 생성합니다. 이러한 오디언스는 커넥터를 통해 실시간으로 마케팅 기술 스택을 강화하는 데 도움이 될 수 있습니다. 

{% alert important %}
Tealium AudienceStreams 및 EventStreams는 배치 및 비배치 커넥터 작업을 모두 제공합니다. The non-batch connector should be used when real-time requests are important to the use case and there are no concerns about hitting the Braze API rate limit specifications. 궁금한 점이 있으면 Braze [지원팀]({{site.baseurl}}/braze_support/) 또는 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 전제 조건

| 이름 | 설명 |
| ---- | ----------- |
| Tealium 계정 | 서버 측 액세스 권한이 있는 [Tealium 계정이](https://my.tealiumiq.com/) 필요합니다. 이 파트너십을 활용하려면 클라이언트 측 통합 기능도 사용하는 것이 좋습니다. |
| REST API 키 | `users.track`, `users.delete`, `subscription.status.set` 권한이 있는 Braze REST API 키.<br><br>**Braze 대시보드 > 개발자 콘솔 > REST API 키 > 새 API 키 생성**에서 생성할 수 있습니다.|
| [Braze REST 엔드포인트][6] | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/#endpoints) 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 속성 및 배지 설정

#### 속성 이해

AudienceStream 사용의 첫 번째 단계는 속성을 만드는 것입니다. 속성을 사용하면 방문자의 습관, 선호도, 행동 및 브랜드에 대한 인게이지먼트를 나타내는 중요한 특성을 정의할 수 있습니다. 

**방문 속성**: 방문 속성은 사용자의 현재 방문(또는 세션)과 관련이 있습니다. 이러한 속성에 저장된 데이터는 방문 기간 동안 지속됩니다. 방문 속성의 몇 가지 예는 다음과 같습니다:
- 방문 기간(수)
- 현재 브라우저 (문자열)
- 현재 기기(문자열)
- 페이지 조회 수(숫자)

**방문자 속성**: 방문자 속성은 현재 사용자와 관련이 있습니다. 이러한 속성에 저장된 데이터는 사용자의 생애주기 동안 지속됩니다. 방문자 속성의 몇 가지 예는 다음과 같습니다: 
- 생애주기 주문 금액(숫자)
- 이름(문자열)
- 생년월일(날짜)
- 구매 브랜드(집계)

사용 가능한 데이터 유형 전체 목록을 보려면 [Tealium][1]을 방문하세요.

##### 속성 보강

원하는 속성을 식별한 후에는 속성 값을 업데이트할 시기와 방법을 결정하는 비즈니스 규칙인 [보강을](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) 사용하여 속성을 구성할 수 있습니다. 각 데이터 유형은 속성 값을 조작할 수 있는 고유한 보강 옵션을 제공합니다. 이는 'WHEN' 설정과 관련이 있습니다. 각 방문 및 방문자 속성에 대해 다음 옵션을 사용할 수 있습니다:

- 새 방문자: 방문자가 사이트를 처음 방문할 때 발생합니다.
- 새 방문: 방문자가 새로 방문했을 때 발생합니다.
- 모든 이벤트: 모든 이벤트에서 발생합니다.
- 방문 종료: 방문이 종료되면 발생합니다.

또한 규칙이라고 하는 커스텀 조건을 생성하여 보강 시점을 결정할 수도 있습니다.

#### 배지

배지는 중요한 행동 패턴을 나타내는 특별한 방문자 속성입니다. 배지는 보강 로직에 따라 방문자에게 할당되거나 제거됩니다. 이 로직은 일반적으로 여러 조건을 결합하여 방문자 세그먼트를 캡처하거나 특정 값에 도달하는 시점에 대한 임계치를 설정합니다.

#### 속성 및 배지 예제

{% tabs local %}
{% tab 속성 %}

완료된 모든 주문(구매 이벤트)에 대해 고객이 지출한 누적 금액(`order_total`)을 계산하는 방문자 속성 '생애주기 주문 금액'을 생성합니다. Tealium 계정에서 생애주기 주문 금액을 설정하려면 다음 지침을 따르세요.

1. **AudienceStream > 방문자/방문 속성**으로 이동하여 **속성 추가**를 클릭합니다.
2. 범위를 **방문자**로 선택하고 **계속**을 클릭합니다.
3. 데이터 유형 **숫자**를 선택하고 **계속**을 클릭합니다.
4. '생애주기 주문 금액' 속성의 이름을 입력합니다.
5. **보강 추가**를 클릭하고 **숫자 증분 또는 감소**를 선택합니다.
6. 증가시킬 값이 포함된 속성을 선택합니다(`order_total`).
7. 임의의 이벤트'로 설정된 '언제'를 '그대로 둔 다음, **새 규칙 생성**을 클릭합니다.
8. 구매 이벤트가 발생한 시점을 식별하는 규칙을 만듭니다.
9. **저장**을 클릭한 다음, **마침**을 클릭합니다.

이제 모든 고객에게 생애주기 주문 금액 속성이 연결됩니다.

{% endtab %}
{% tab 배지 %}

사용자가 공유하는 특정 속성을 기준으로 사용자를 분류하고 타겟팅하는 데 도움이 되는 배지를 만들 수 있습니다. 다음 예제에서는 '생애주기 주문 금액'이 $500이 넘는 사용자를 위한 VIP 배지를 생성합니다.

1. **AudienceStream > 방문자/방문 속성**으로 이동하여 **속성 추가**를 클릭합니다.
2. 범위를 **방문자**로 선택하고 **계속**을 클릭합니다.
3. 데이터 유형 **배지**를 선택하고 **계속**을 클릭합니다.
4. 배지 이름인 "VIP"를 입력합니다.
5. **보강 추가**를 클릭하고 **배지 할당**을 선택합니다.
6. '임의의 이벤트'로 설정된 '언제'를 그대로 둡니다.
7. **규칙 생성**을 선택하여 배지 할당 규칙을 생성합니다. 이 규칙에 제목을 할당하고 이전에 생성한 속성을 사용하여 '...생애주기 주문 금액이 500을 초과하는 속성'으로 규칙을 설정합니다.
8. **저장**을 클릭한 다음, **마침**을 클릭합니다.

{% endtab %}
{% endtabs %}

### 2단계: 오디언스 만들기

Tealium 홈 페이지의 사이드바 탐색에서 **AudienceStream** 아래에서 **오디언스를** 선택합니다. 여기에서 공통 속성을 가진 사용자 그룹을 만들 수 있습니다. 사용자가 이 오디언스에 들어오거나 나가면 다음 단계에서 설정된 커넥터 액션이 트리거가 되어 이 정보를 Braze의 사용자 프로필로 전달합니다. 

먼저 오디언스 이름을 지정한 다음, 생성하려는 오디언스의 유형에 어떤 속성을 적용할지 고려합니다. 예를 들어 VIP 사용자 대상 그룹을 만들려면 **VIP 배지가** 있는 방문자 대상 그룹을 만들 수 있습니다.

완료되면 오디언스를 **저장/게시하세요**.

### 3단계: 이벤트 커넥터 만들기

커넥터는 데이터를 전송하는 데 사용되는 Tealium과 다른 공급업체 간의 통합입니다. 이러한 커넥터에는 파트너가 지원하는 API를 나타내는 작업이 포함되어 있습니다. 

1. Tealium의 사이드바에서 **서버 측** 아래의 **AudienceStream > 오디언스 커넥터로** 이동합니다.
2. 파란색 **\+ 커넥터 추가** 버튼을 선택하여 커넥터 마켓플레이스를 살펴봅니다. 새 대화 상자가 나타나면 스포트라이트 검색을 사용하여 **Braze** 커넥터를 찾습니다.
3. 이 커넥터를 추가하려면 **브레이즈** 커넥터 타일을 클릭합니다. 클릭하면 연결 요약과 필수 정보 목록, 지원되는 작업 및 구성 지침을 볼 수 있습니다. 구성은 소스, 구성, 작업의 세 단계로 구성됩니다.

#### 소스

표시되는 **소스** 대화 상자에서 이전 단계에서 만든 대상과 상황에 적합하다고 생각되는 트리거를 선택합니다. 또한 빈도 상한을 토글하여 이 작업이 트리거되는 빈도를 제어할 수도 있습니다. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### 구성

다음으로 **구성** 대화 상자가 나타납니다. 페이지 하단에서 **커넥터 추가**를 선택합니다. 여기에서 커넥터의 이름을 지정하고 Braze API 엔드포인트와 Braze REST API 키를 제공합니다.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

이전에 커넥터를 만든 적이 있다면 사용 가능한 커넥터 목록에서 기존 커넥터를 선택적으로 사용하고 연필 아이콘을 사용하여 필요에 맞게 수정하거나 휴지통 아이콘을 사용하여 삭제할 수 있습니다. 

이 오디언스를 연결할 커넥터를 생성하거나 선택한 후 완료를 클릭하여 계속합니다.

#### 작업

그런 다음 커넥터 작업의 이름을 지정하고 구성한 매핑에 따라 데이터를 전송할 작업 유형을 선택합니다. 여기에서는 브레이즈 속성을 틸륨 속성 이름에 매핑합니다. 선택한 작업 유형에 따라 Tealium에서 요구하는 필드의 종류가 달라집니다. 다음은 이러한 필드에 대한 예시와 설명입니다.

{% alert important %}
제공되는 모든 필드가 필수 항목은 아닙니다.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab 사용자 추적 - 배치 및 비배치 %}

이 작업을 통해 사용자, 이벤트, 구매 속성을 모두 한 번에 추적할 수 있습니다. 사용자 추적 작업은 AudienceStream과 EventStream 모두에서 동일하지만, Tealium은 사용자 속성 매핑은 AudienceStream 작업으로, 이벤트 및 구매 매핑은 EventStream 작업으로 설정할 것을 권장합니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze의 해당하는 필드에 매핑합니다. 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선 순위에 따라 비어 있지 않은 첫 번째 값이 선택됩니다: 외부 아이디, Braze ID, 별칭 이름 및 별칭 라벨.<br><br>\- 푸시 토큰을 가져오는 경우 외부 ID와 Braze ID를 지정하지 않아야 합니다.<br>\- 사용자 별칭을 지정하는 경우 별칭 이름과 별칭 레이블을 설정해야 합니다. <br><br>자세한 내용은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 확인하세요. |
| 사용자 속성 | Use existing Braze user profile field names to update user profile values in the Braze dashboard or add your own custom [user attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object/) data to the user profiles.<br><br>\- 기본적으로 사용자가 없는 경우 새 사용자가 만들어집니다.<br>- **기존 사용자만 업데이트**를 `true`로 설정하면, 기존 사용자만 업데이트되고 새 사용자는 생성되지 않습니다.<br>\- Tealium 속성이 비어 있는 경우, null로 변환되어 Braze 고객 프로필에서 제거됩니다. 사용자 속성을 제거하기 위해 Braze에 null 값을 보내서는 안 되는 경우 보강을 사용해야 합니다. |
| 사용자 속성 수정 | 이 필드를 사용하여 특정 사용자 속성을 늘리거나 줄입니다.<br><br>\- 정수 속성은 양의 정수 또는 음의 정수로 증가될 수 있습니다.<br>\- 배열 속성은 기존 배열에서 값을 추가하거나 제거하여 수정할 수 있습니다. |
| 이벤트 | 이벤트는 특정 사용자가 특정 타임스탬프에 커스텀 이벤트가 한 번 발생한 것을 나타냅니다. 이 필드를 사용하여 Braze [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/)에서와 같이 이벤트 속성을 추적하고 매핑합니다. <br><br>\- 이벤트 속성 `Name`은 매핑된 모든 이벤트에서 필수입니다.<br>\- 이벤트 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 now로 설정됩니다. <br>\- 기본적으로 이벤트가 없는 경우 새 이벤트가 생성됩니다. `Update Existing Only` 을 `true` 으로 설정하면 기존 이벤트만 업데이트되고 새 이벤트는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 이벤트를 추가합니다. 배열 유형 속성은 길이가 같아야 합니다.<br>\- 단일 값 속성을 사용하여 각 이벤트에 적용할 수 있습니다. |
| 이벤트 템플릿 | 본문 데이터에서 참조할 이벤트 템플릿을 제공합니다. 템플릿을 사용하여 데이터를 Braze로 전송하기 전에 데이터를 변환할 수 있습니다. 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요. |
| 이벤트 템플릿 변수 | 이벤트 템플릿 변수를 데이터 입력으로 제공하세요. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
| 구매 | 이 필드를 사용하여 Braze [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/)에서와 같이 사용자 구매 속성을 추적하고 매핑합니다.<br><br>\- 매핑된 모든 구매에는 구매 속성 `Product ID`, `Currency`, `Price`가 필수입니다.<br>\- 구매 속성 `Time`은 명시적으로 매핑하지 않는 한 자동으로 now로 설정됩니다.<br>\- 기본적으로 구매가 없는 경우 새 구매가 생성됩니다. `Update Existing Only` 을 `true` 으로 설정하면 기존 구매만 업데이트되고 새 구매는 생성되지 않습니다.<br>\- 배열 유형 속성을 매핑하여 여러 구매 항목을 추가합니다. 배열 유형 속성은 길이가 같아야 합니다.<br>\- 단일 값 속성을 사용할 수 있으며 각 항목에 적용됩니다.|
| 구매 템플릿 | 템플릿은 데이터를 Braze로 전송하기 전에 데이터를 변환하는 데 사용할 수 있습니다.<br>\- 중첩된 개체 지원이 필요한 경우 구매 템플릿을 정의합니다.<br>\- 구매 템플릿이 정의되면 작업의 구매 섹션에 설정된 구성은 무시됩니다.<br>\- 자세한 내용은 Tealium의 [템플릿 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)를 참조하세요.|
| 구매 템플릿 변수 | 데이터 입력으로 제품 템플릿 변수를 제공합니다. 자세한 내용은 Tealium의 [템플릿 변수 가이드](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab 사용자 삭제 - 비일괄 %}

이 작업을 통해 Braze 대시보드에서 사용자를 삭제할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 사용자 ID | 이 필드를 사용하여 Tealium 사용자 ID 필드를 Braze에 해당하는 필드에 매핑할 수 있습니다.<br><br>\- 하나 이상의 사용자 ID 속성을 매핑합니다. 여러 ID가 지정된 경우 다음 우선 순위에 따라 비어 있지 않은 첫 번째 값이 선택됩니다: 외부 아이디, Braze ID, 별칭 이름 및 별칭 라벨.<br>\- 사용자 별칭을 지정할 때는 별칭 이름과 별칭 레이블을 모두 설정해야 합니다.<br><br>자세한 내용은 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab 사용자 구독 그룹 상태 업데이트 - 일괄 처리되지 않음 %}
이 작업을 통해 Braze SMS 또는 이메일 수신 그룹에서 사용자를 추가하거나 제거할 수 있습니다.

| 매개변수 | 설명 |
| ---------- | ----------- |
| 그룹 유형 | 이 필드를 사용하여 SMS인지 또는 이메일 구독 그룹인지 표시합니다. |
| 업데이트 유형 | 이 작업을 구독 취소 또는 구독 이벤트에 매핑합니다. 
| 속성 | \- 정기구독 그룹 ID(필수): 이전 필드에 매핑된 그룹 유형과 관련된 구독 그룹의 ID입니다.<br>\- 외부 ID: 사용자의 외부 ID입니다.<br><br>이메일 그룹별:<br>\- 이메일: 사용자의 이메일 주소입니다.<br>**외부 ID가 정의되지 않은 경우 이메일이 필요합니다.**<br><br>SMS 그룹별:<br>\- 전화: E.164 형식의 전화번호입니다. 예: +14155552671.<br>**외부 ID가 정의되어 있지 않으면 휴대폰이 필요합니다.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

**마침**을 선택합니다.

#### 요약

생성한 커넥터의 요약을 확인합니다. 선택한 옵션을 수정하려면 **뒤로**를 선택하거나 완료하려면 **마침**을 선택합니다.

이제 커넥터가 Tealium 홈 페이지의 커넥터 목록에 표시됩니다.

완료되면 커넥터를 저장하거나 게시하세요. 이제 트리거 연결이 충족되면 구성한 작업이 실행됩니다. 

### 4단계: Tealium 커넥터 테스트

커넥터를 시작 및 실행한 후에는 커넥터가 제대로 작동하는지 테스트해야 합니다. 이를 테스트하는 가장 간단한 방법은 Tealium **추적 툴**을 사용하는 것입니다. 추적 사용을 시작하려면 Tealium 툴 브라우저 확장을 추가했는지 확인합니다.

1. 새 추적을 시작하려면 사이드바의 **서버 측** 옵션 아래에서 **추적**을 선택합니다. **시작**을 클릭하고 추적 ID를 캡처합니다.
2. 브라우저 확장을 열고 AudienceStream 추적에 추적 ID를 입력합니다.
3. 실시간 로그를 살펴봅니다.
4. **트리거된 작업** 항목을 클릭하여 확장하고 유효성을 검사하려는 작업을 확인합니다.
5. 유효성을 검사하려는 작업을 찾아 로그 상태를 확인합니다. 

Tealium의 추적 툴 구현에 대한 자세한 지침은 Tealium의 [추적 설명서][21]를 참조하세요.

## 통합 데모

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 데이터 포인트 초과 가능성

Tealium을 통해 Braze를 통합할 때 실수로 데이터 초과량이 발생할 수 있는 주된 세 가지 경우가 있습니다.

#### 중복 데이터 전송 - Braze 델타의 속성만 전송합니다.
Tealium은 Braze의 사용자 속성 델타를 전송하지 않습니다. 예를 들어, 사용자의 이름, 이메일, 휴대폰 번호를 추적하는 EventStream 작업이 있는 경우, Tealium은 작업이 트리거될 때마다 세 가지 속성을 모두 Braze로 전송합니다. Tealium은 변경되거나 업데이트된 내용을 찾지 않고 해당 정보만 전송합니다.<br><br> 
**솔루션**: <br>백엔드를 확인하여 속성이 변경되었는지 여부를 평가하고, 변경된 경우 Tealium의 관련 메서드를 호출하여 사용자 프로필을 업데이트할 수 있습니다. **일반적으로 Braze를 직접 통합하는 사용자가 수행합니다.** <br>**OR**<br> 백엔드에 자체 버전의 고객 프로필을 저장하지 않고 속성이 변경되었는지 여부를 알 수 없는 경우 AudienceStream을 사용하고 값이 변경된 사용자 속성만 전송하도록 [보강을 생성](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)할 수 있습니다. 

#### 관련 없는 데이터를 전송하거나 불필요하게 데이터를 덮어쓰는 경우
동일한 이벤트 피드를 대상으로 하는 EventStreams가 여러 개 있는 경우, **해당 커넥터에 대해 활성화된 모든 작업**은 단일 작업이 트리거될 때마다 자동으로 실행되며, **이로 인해 Braze에서 데이터를 덮어쓸 수도 있습니다.**<br><br>
**솔루션**: <br>각 작업을 추적하기 위해 별도의 이벤트 사양 또는 피드를 설정하세요. <br>**OR**<br> 실행하지 않으려는 작업 또는 커넥터는 Tealium 대시보드의 토글을 사용하여 비활성화합니다.

#### 너무 일찍 Braze 초기화
Braze 웹 SDK 태그를 사용하여 Tealium과 통합하는 사용자는 MAU의 급격한 증가를 확인할 수도 있습니다. **페이지 로드 시 Braze가 초기화되면 웹 사용자가 웹사이트를 처음 탐색할 때마다 익명 프로필이 생성됩니다.** 사용자가 '로그인' 또는 '비디오 시청' 등의 특정 작업을 완료했을 때만 사용자 행동을 추적하여 MAU 수를 낮출 수도 있습니다. <br><br>
**솔루션**: <br>[로드 규칙](https://docs.tealium.com/iq-tag-management/load-rules/about/)을 설정하여 태그가 사이트에서 로드되는 시기와 위치를 정확하게 결정합니다.

[1]: https://docs.tealium.com/server-side/attributes/about/
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints
[21]:https://docs.tealium.com/server-side/connectors/trace/about/
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
