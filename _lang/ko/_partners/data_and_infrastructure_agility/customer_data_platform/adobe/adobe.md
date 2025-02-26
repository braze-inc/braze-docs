---
nav_title: Adobe
article_title: Adobe
description: "이 페이지에서는 브랜드가 Adobe 데이터(사용자 지정 속성 및 세그먼트)를 실시간으로 Braze에 연결하고 매핑할 수 있는 고객 데이터 플랫폼인 Braze와 Adobe 간의 파트너십에 대해 간략하게 설명합니다. 그런 다음, 브랜드는 이 데이터를 기반으로 조치를 취하여 해당 사용자에게 개인화된 타겟팅 경험을 제공할 수 있습니다."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Adobe Experience Platform을 기반으로 구축된 Adobe의 실시간 고객 데이터 플랫폼은 여러 기업 소스의 알려진 데이터와 익명의 데이터를 통합하여 고객 프로필을 생성합니다. 그런 다음, 이러한 프로필을 사용하여 모든 채널과 기기에서 실시간으로 개인화된 경험을 제공할 수 있습니다.

Braze와 Adobe CDP 통합은 브랜드의 Adobe 데이터(사용자 지정 속성 및 세그먼트)를 실시간으로 Braze에 연결하고 매핑합니다. 그런 다음 이 데이터를 기반으로 조치를 취하여 사용자에게 개인화된 타겟팅 경험을 제공할 수 있습니다. Adobe를 사용하면 직관적으로 통합할 수 있습니다. Adobe [ID](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en)를 가져와서 Braze 외부 ID에 매핑한 다음, Braze 플랫폼으로 전송하기만 하면 됩니다. 전송된 모든 데이터는 새로운 `AdobeExperiencePlatformSegments` 기여를 통해 Braze에서 액세스할 수 있습니다.

{% alert important %}
Adobe Experience Platform 통합은 현재 동적 대상 멤버십을 지원하지 않습니다. 즉, 사용자 프로필에 값을 추가할 수만 있고 제거할 수는 없습니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Adobe 계정 | 이 파트너십을 활용하려면 [Adobe 계정이](https://account.adobe.com/) 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 브레이즈 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저로부터 가져오거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에]({{site.baseurl}}/api/basics/#endpoints) 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
추가 사용자 지정 속성을 전송하면 데이터 포인트 사용량이 증가합니다. 고객 성공 관리자와 상담하여 이러한 잠재적인 데이터 포인트 증가에 대해 더 잘 이해하는 것이 좋습니다.
{% endalert %}

## 통합

### 1단계: Braze 대상 구성

Adobe **설정** 페이지의 **모음** 아래에서 **대상**을 선택합니다. 거기에서 **Braze** 타일을 찾아 **구성을** 선택합니다. 

![][1]

{% alert note %}
이미 Braze와의 연결이 있는 경우 대상 카드에 **활성화** 버튼이 표시됩니다. 활성화와 구성 간 차이점에 대한 자세한 내용은 Adobe 대상 워크스페이스 [설명서](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog)의 카탈로그 섹션을 참조하세요.
{% endalert %}

### 2단계: Braze 토큰 제공

**계정** 단계에서 Braze API 키를 입력하고 **대상에 연결을** 선택합니다.

![][3]{: style="max-width:60%"}

### 3단계: 인증

다음으로 **인증** 단계에서 Braze 연결 정보를 입력합니다:
- **이름**: 향후 이 목적지를 인식할 수 있는 이름을 입력하세요.
- **대상**: 이 대상을 식별하는 데 도움이 되는 설명을 입력합니다.
- **엔드포인트 인스턴스**: Braze 엔드포인트 인스턴스를 입력합니다.
- **마케팅 사용 사례**: 마케팅 사용 사례는 데이터를 대상에 내보낼 의도를 나타냅니다. Adobe에서 정의한 마케팅 사용 사례 중에서 선택하거나 고유한 마케팅 사용 사례를 생성할 수 있습니다. Adobe 마케팅 사용 사례에 대한 자세한 내용은 [Adobe Experience Platform의 데이터 거버넌스](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations)를 참조하세요.

![][4]{: style="max-width:60%;"}

### 4단계: 목적지 만들기
**대상 생성을** 선택합니다. 목적지가 생성되었습니다. **저장 후 종료를** 선택하여 나중에 세그먼트를 활성화하거나 **다음을** 선택하여 워크플로를 계속하고 활성화할 세그먼트를 선택할 수 있습니다. 

### 5단계: 세그먼트 활성화
세그먼트를 Braze 대상에 매핑하여 Adobe 실시간 CDP에 있는 데이터를 활성화합니다.

다음 목록에는 세그먼트를 활성화하는 데 필요한 일반적인 단계가 나와 있습니다. Adobe 세그먼트 및 세그먼트 활성화 워크플로에 대한 자세한 지침을 보려면 [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites)를 방문하세요.

1. Braze 대상을 선택하고 활성화합니다.
2. 해당 세그먼트를 선택합니다.
4. 내보내는 각 세그먼트에 대한 예약 및 파일 이름을 구성합니다.
5. Braze로 전송할 속성을 선택합니다.
6. 활성화를 검토하고 확인합니다.

### 6단계: 필드 매핑

Adobe Experience Platform에서 Braze로 오디언스 데이터를 올바르게 전송하려면 필드 매핑 단계를 완료해야 합니다. 매핑하면 Adobe Experience 데이터 모델 필드와 해당 Braze 플랫폼 필드 간에 링크가 생성됩니다.

1. 매핑 단계에서 **새 매핑 추가를** 선택합니다.<br>![][5]{: style="max-width:50%;"}<br><br>
2. 소스 필드 섹션에서 빈 필드 옆의 화살표 버튼을 선택하여 소스 필드 선택 창을 엽니다.<br>![][6]<br><br>
3. 창에서 Braze 속성에 매핑할 Adobe 속성을 선택합니다. <br>![][7]{: style="max-width:70%;"}<br><br>다음으로 ID 네임스페이스를 선택합니다. 이 옵션은 플랫폼 아이덴티티 네임스페이스를 Braze 네임스페이스에 매핑하는 데 사용됩니다.<br>![][8]{: style="max-width:80%;"}<br> 소스 필드를 선택한 다음 **선택을 선택합니다**.<br><br>
4. 대상 필드 섹션에서 필드 옆의 매핑 아이콘을 선택합니다.<br>![][9]{: style="max-width:90%;"} <br><br>
5. 대상 필드 선택 창에서 세 가지 카테고리의 대상 필드 중에서 선택할 수 있습니다.<br><br>- **ID 네임스페이스 선택**: 이 옵션을 사용하여 플랫폼 ID 네임스페이스를 Braze ID 네임스페이스에 매핑합니다.<br>- **커스텀 속성 선택**: 이 옵션을 사용하여 Braze 계정에서 정의한 커스텀 Braze 속성에 Adobe XDM 속성을 매핑합니다. <br><br>![][10]{: style="max-width:60%;"}<br><br>**이 옵션을 사용하여 기존 XDM 속성의 이름을 Braze로 변경할 수도 있습니다.** 예를 들어, `lastname` XDM 속성을 Braze의 커스텀 `Last_Name` 속성에 매핑하면, 아직 존재하지 않는 경우 Braze에 `Last_Name` 속성이 생성되고 `lastname` XDM 속성이 여기에 매핑됩니다. <br><br> 대상 필드를 선택한 다음 **선택을 선택합니다**.<br><br>
6. 필드 매핑이 목록에 표시되어야 합니다.<br>![][11]<br><br>
7. 매핑을 더 추가하려면 필요에 따라 1~6단계를 반복합니다. 

## 사용 사례

XDM 프로필 스키마와 Braze 인스턴스에 다음과 같은 속성과 ID가 포함되어 있다고 가정합니다.

|     | XDM 프로필 스키마 | 브레이즈 인스턴스 |
| --- | ------------------ | -------------- |
| 속성 | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| ID | - `Email`<br>\- Google 광고 ID (`GAID`)<br>\- 광고주용 Apple ID (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

올바른 매핑은 다음과 같습니다:

![대상 매핑: IdentityMap:IDFA는 IdentityMap:external_id에, IdentityMap:GAID는 IdentityMap:external_id에, IdentityMap:Email은 IdentityMap:external_id에, xdm:mobilePhone.number는 CustomAttribute:PhoneNumber에, xdm:person.name.lastName은 CustomAtrribute:LastName에, xdm:person.name.firstName은 CustomAttribute:FirstName에 매핑됨][12]

## 내보낸 데이터
데이터가 Braze로 성공적으로 내보내졌는지 확인하려면 Braze 계정을 확인하세요. Adobe Experience Platform 세그먼트는 `AdobeExperiencePlatformSegments` 속성을 사용하여 Braze로 내보냅니다.

## 데이터 사용량 및 거버넌스
모든 Adobe Experience Platform 대상은 데이터를 처리할 때 데이터 사용 정책을 준수합니다. Adobe Experience Platform에서 데이터 거버넌스를 적용하는 방법에 대한 자세한 내용은 [실시간 CDP의 데이터 거버넌스](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en)를 참조하세요. 

[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %}
[3]: {% image_buster /assets/img/adobe/braze-destination-account.png %}
[4]: {% image_buster /assets/img/adobe/braze-destination-authentication.png %}
[5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %}
[6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source.png %}
[7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}
[8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}
[9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}
[10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}
[11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %}
[12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 