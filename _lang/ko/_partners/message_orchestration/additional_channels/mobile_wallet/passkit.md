---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "이 참조 문서에서는 Braze와 Passkit 간의 파트너십을 간략히 설명합니다. 이 파트너십을 사용하여 Apple Wallet과 Google Pay 패스를 고객 경험에 통합함으로써 모바일 접근성을 확장할 수 있습니다."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit을 사용하여 Apple Wallet과 Google Pay 패스를 고객 경험에 통합함으로써 모바일 접근성을 확장할 수 있습니다. 또한 디지털 쿠폰과 고객 카드, 로열티 카드, 티겟 등 다양한 항목을 손쉽게 만들고 관리 및 배포하며 그 성과를 분석할 수 있습니다. 고객에게 필요한 다른 앱은 없습니다.

_This integration is maintained by Passkit._

## 통합 정보

Braze와 PassKit의 통합을 통해 커스텀 Apple Wallet 및 Google Pay 패스를 즉시 제공하여 온라인 캠페인의 인게이지먼트를 높이고 측정할 수 있습니다. 그런 다음 사용량을 분석하고 실시간으로 조정하여 위치 기반 메시지와 고객의 모바일 지갑에 대한 개인화된 동적 업데이트를 트리거하여 매장 내 트래픽을 늘릴 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| PassKit 계정 | PassKit 계정과 PassKit 계정 관리자가 있어야 합니다. |
| `userDefinedID` | 사용자 지정 이벤트 및 사용자 지정 속성을 PassKit과 Braze 간에 적절하게 업데이트하려면 Braze 외부 ID를 `userDefinedID` 로 설정해야 합니다. 이 `userDefinedID`는 PassKit 엔드포인트에 API 호출을 할 때 사용됩니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트  | 귀하의 REST 엔드포인트 URL. 사용자의 엔드포인트는 [인스턴스를 위한 Braze URL][6]에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

To further enrich your customers' mobile wallet experiences, from within your PassKit dashboard, you can opt to pass data into Braze through the Braze [`/users/track` endpoint][7]. 

PassKit에서 공유할 수 있는 데이터의 예는 다음과 같습니다.
- **패스 생성됨**: 고객이 패스 링크를 클릭하고 패스가 처음 표시되는 경우.
- **패스 설치됨**: 고객이 지갑 앱에 패스를 추가하고 저장하는 경우.
- **패스 업데이트**: 패스가 업데이트되는 경우.
- **패스 삭제**: 고객이 지갑 앱에서 패스를 삭제하는 경우.

데이터가 Braze로 전달되면, 오디언스를 구축하고, Liquid를 통해 콘텐츠를 개인화하며, 이러한 작업이 수행된 후 캠페인 또는 캔버스를 트리거할 수 있습니다.

## Braze에 Passkit 연결

PassKit에서 데이터를 전달하려면, Braze 외부 ID를 PassKit의 `externalId`로 설정했는지 확인합니다.

1. **설정** 내 PassKit 패스 프로젝트 또는 프로그램의 **통합**에서 **Braze** 탭 아래 **연결**을 클릭합니다.<br>![PassKit 플랫폼의 Braze 통합 타일입니다.][5]{: style="max-width:80%"}<br><br>
2. Braze API 키와 엔드포인트 URL을 입력하고 커넥터의 이름을 제공합니다.<br><br>
3. **통합 활성화** 및 Braze에서 메시지를 트리거하거나 개인화할 이벤트를 토글합니다.<br>![API 키, 엔드포인트 URL, 통합 이름, 활성화 설정, 멤버십 설정 및 패스 설정을 허용하도록 확장된 PassKit Braze 통합 타일.][4]{: style="max-width:70%"}

## SmartPass 링크를 사용하여 패스 생성

Braze 내에서 스마트패스 링크를 설정하여 고객이 Android 또는 iOS에서 패스를 설치할 수 있는 고유한 URL을 생성할 수 있습니다. 이렇게 하려면 Braze 콘텐츠 블록에서 호출할 수 있는 암호화된 SmartPass 데이터 페이로드를 정의해야 합니다. 이 [콘텐츠 블록][9]은 향후 패스 및 쿠폰에 재사용할 수 있습니다. 통합하는 동안 다음이 사용됩니다:

- **PassKit URL**: PassKit URL은 PassKit 프로그램에 대한 고유 URL입니다.<br>각 프로그램에는 고유한 URL이 있으며, PassKit 프로그램 또는 프로젝트의 **배포** 탭에서 찾을 수 있습니다. (예: https://pub1.pskt.io/c/ww0jir)<br><br>
- **PassKit 비밀**: URL과 함께 이 프로그램을 위한 PassKit 키가 준비되어 있어야 합니다.<br>PassKit URL과 같은 페이지에서 찾을 수 있습니다.<br><br>
- **프로그램(또는 프로젝트) ID**: SmartPass URL을 생성하려면 PassKit 프로그램 ID가 필요합니다. <br>프로젝트 또는 프로그램의 **설정** 탭에서 찾을 수 있습니다.

암호화된 SmartPass 링크 생성에 대한 자세한 내용은 이 [PassKit 문서][8]를 참조하세요.

### 1단계: 패스 데이터 페이로드 정의 {#passkit-integrations}

먼저 쿠폰 또는 회원 페이로드를 정의해야 합니다. 

페이로드에 포함할 수 있는 구성요소는 다양하지만, 여기서는 두 가지 중요한 구성요소에 주목합니다.

| 구성요소 | 필수 | 유형 | 설명 |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | 필수 | 문자열 | Braze 외부 ID로 설정하면 PassKit에서 Braze로의 콜백이 작동하여 Braze 사용자가 하나의 캠페인에서 여러 오퍼에 대한 쿠폰을 받을 수 있도록 하는 데 중요합니다. 고유한 것으로 적용되지 않습니다. |
| `members.member.externalId` | 선택 사항 | 문자열 | Braze 외부 ID로 설정하면 외부 ID를 사용하여 멤버십 패스를 업데이트할 수 있습니다. 이 필드를 설정하면 멤버십 프로그램 내에서 사용자를 고유하게 지정합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

사용 가능한 필드, 유형 및 유용한 설명의 전체 목록은 [PassKit GitHub 설명서][10] 을 참조하세요.

#### 페이로드 예시
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### 2단계: 정의되지 않은 페이로드 변수 생성 및 인코딩

Braze 대시보드 내에서 **템플릿** > **콘텐츠 블록으로** 이동하여 새 콘텐츠 블록을 만들고 이름을 지정합니다.

시작하려면 **콘텐츠 블록 생성**을 선택합니다.

다음으로, **콘텐츠 블록 Liquid 태그**를 정의해야 합니다. 이 콘텐츠 블록을 저장한 후에는 메시지를 작성할 때 이 Liquid 태그를 참조할 수 있습니다. 이 예제에서는 Liquid 태그를 {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}로 지정했습니다. 

이 콘텐츠 블록에서는 페이로드를 직접 포함하지 않고 {% raw %}`{{passData}}`{% endraw %} 변수에서 참조합니다. 콘텐츠 블록에 추가해야 하는 첫 번째 코드 스니펫은 {% raw %}`{{passData}}`{% endraw %} 변수의 Base64 인코딩을 캡처합니다.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### 3단계: SHA1 HMAC 해시를 사용하여 암호화 서명을 생성합니다.

다음으로, 프로젝트 URL과 페이로드의 [SHA1 HMAC][16] 해시를 사용하여 암호화 서명을 생성합니다. 

콘텐츠 블록에 추가해야 하는 두 번째 코드 스니펫은 해싱에 사용할 URL을 캡처합니다.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

다음으로 이 해시와 `Project Secret` 을 사용하여 서명을 생성해야 합니다. 세 번째 코드 스니펫을 포함하면 이 작업을 수행할 수 있습니다:
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

마지막으로, 다섯 번째 코드 스니펫을 사용하여 전체 URL에 서명을 추가합니다.
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### 4단계: URL 인쇄

마지막으로, 메시지 내에 SmartPass URL이 인쇄되도록 최종 URL을 호출해야 합니다.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

이 시점에서 다음과 같은 콘텐츠 블록을 만들었을 것입니다:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

이 예제에서는 이러한 설치의 소스를 Braze와 이 캠페인으로 추적하기 위해 UTM 매개변수가 추가되었습니다.

{% alert tip %}
페이지에서 나가기 전에 콘텐츠 블록을 저장해야 합니다.
{% endalert %}

### 5단계: 종합

이 콘텐츠 블록을 만든 후에는 나중에 다시 재사용할 수 있습니다. 

예제 콘텐츠 블록에 정의되지 않은 변수가 두 개 남아 있는 것을 볼 수 있습니다.<br> 
{% raw %}`{{passData}}`{% endraw %} - [1단계](#passkit-integrations)에서 정의한 JSON 패스 데이터 페이로드 <br>
{% raw %}`{{projectUrl}}`{% endraw %} - Passkit 프로젝트의 배포 탭에서 찾을 수 있는 프로젝트 또는 프로그램의 URL.

이 결정은 의도적인 것이며 콘텐츠 블록의 재사용성을 지원합니다. 이러한 변수는 콘텐츠 블록 내에서 생성되는 것이 아니라 참조될 뿐이므로 콘텐츠 블록을 다시 만들지 않고도 변수를 변경할 수 있습니다. 

예를 들어 로열티 프로그램에 더 많은 초기 포인트를 포함하도록 도입 오퍼를 변경하거나 보조 회원 카드 또는 쿠폰을 만들고 싶을 수 있습니다. 이러한 시나리오에는 다른 Passkit(`projectURLs`) 또는 다른 패스 페이로드가 필요하며, Braze에서 캠페인별로 정의할 수 있습니다.  

#### 메시지 본문 작성하기

메시지 본문에서 이 두 변수를 모두 캡처한 다음 콘텐츠 블록을 호출하려고 합니다.
[1단계](#passkit-integrations)에서 축소된 JSON 페이로드를 캡처합니다.

**프로젝트 URL 지정**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**JSON 캡처**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**방금 만든 콘텐츠 블록 참조**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

메시지 본문은 다음과 같이 표시되어야 합니다:
![캡처한 JSON 및 콘텐츠 블록 참조가 표시된 콘텐츠 블록 메시지 작성기의 이미지입니다.][1]{: style="max-width:70%"}

샘플의 출력 URL은 다음과 같습니다:
![무작위로 생성된 긴 문자 및 숫자 문자열이 포함된 출력 URL입니다.][2]{: style="max-width:70%"}

출력 URL이 길어집니다. 그 이유는 모든 패스 데이터가 포함되어 있고 동급 최고의 보안을 통합하여 데이터 무결성을 보장하고 URL 수정을 통한 조작이 없기 때문입니다. SMS를 사용하여 이 URL을 배포하는 경우 [bit.ly][3] 와 같은 링크 단축 프로세스를 통해 실행할 수 있습니다. 이는 bit.ly 엔드포인트에 대한 연결된 콘텐츠 호출을 통해 수행할 수 있습니다.

## PassKit 웹훅을 사용한 패스 업데이트

Braze 내에서 웹훅 캠페인 또는 캔버스 내 웹훅을 설정하여 사용자의 행동에 따라 기존 패스를 업데이트할 수 있습니다. 유용한 PassKit 엔드포인트에 대한 정보는 다음 링크를 확인하세요. 
- [회원 프로젝트][12]
- [쿠폰 프로젝트][13]
- [항공편 프로젝트][14]

### 페이로드 매개변수

시작하기 전에 PassKit에 대한 웹훅 생성 및 업데이트에 포함할 수 있는 일반적인 JSON 페이로드 매개변수는 다음과 같습니다.

| 데이터 | 유형 | 설명 |
| ---- | ---- | ----------- |
| `externalId` | 문자열 | 고유한 고객 식별자(예: 멤버십 번호)를 사용하여 기존 시스템과의 호환성을 제공하기 위해 패스 레코드에 고유 ID를 추가할 수 있습니다. 패스 ID 대신 `userDefinedId` 및 `campaignName`을 통해 이 엔드포인트를 사용하여 패스 데이터를 검색할 수 있습니다. 이 값은 캠페인 내에서 고유해야 하며, 이 값을 설정한 후에는 변경할 수 없습니다.<br><br>Braze 통합의 경우, Braze 외부 ID({% raw %}`{{${user_id}}}`{% endraw %})를 사용하는 것이 좋습니다. |
| `campaignId`(쿠폰) <br><br> `programId` (멤버십) | 문자열 | PassKit에서 생성한 캠페인 또는 프로그램 템플릿의 ID입니다. 이를 찾으려면 PassKit 패스 프로젝트의 **설정** 탭으로 이동하세요. |
| `expiryDate` | IO8601 날짜 시간 | 패스 만료일. 만료일이 지나면 패스는 자동으로 무효화됩니다(`isVoided` 참조). 이 값은 템플릿 및 캠페인 종료일 값보다 우선합니다. |
| `status` | 문자열 | 쿠폰의 현재 상태(예: `REDEEMED` 또는 `UNREDEEMED`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 1단계: Braze 웹훅 템플릿 만들기

향후 캠페인이나 캔버스에서 사용할 PassKit 웹훅 템플릿을 만들려면 Braze 대시보드의 **템플릿 및 미디어** 섹션으로 이동합니다. 일회성 PassKit 웹훅 캠페인을 만들거나 기존 템플릿을 사용하려면 새 캠페인을 만들 때 Braze에서 **웹훅을** 선택하세요.

PassKit 웹훅 템플릿을 선택하면 다음과 같은 내용이 표시됩니다:
- **웹훅 URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **요청 본문**: 원시 텍스트

#### 요청 헤더 및 메서드

PassKit는 base 64로 인코딩된 PassKit API 키가 포함된 인증용 `HTTP Header`를 요구합니다. 다음은 이미 템플릿에 키-값 쌍으로 포함되어 있지만 **설정** 탭에서 `<PASSKIT_LONG_LIVED_TOKEN>` 을 PassKit 토큰으로 바꿔야 합니다. 토큰을 검색하려면 PassKit 프로젝트/프로그램으로 이동하여 **설정 > 통합 > 장기 수명 토큰**으로 이동합니다.

{% raw %}
- **HTTP 메서드**: PUT
- **요청 헤더**:
  - **권한 부여**: Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

웹훅을 설정하려면 사용 사례에 필요한 페이로드 매개변수를 포함하여 요청 본문 내에 새 이벤트 세부 정보를 입력합니다.

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### 2단계: 요청 미리보기

원시 텍스트가 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다. 

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자, 기존 사용자를 선택하거나 직접 사용자 지정하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}

## 연결된 콘텐츠를 통해 패스 세부 정보 검색

In addition to creating and updating passes, you can also retrieve your users' pass metadata via Braze [Connected Content][15] to incorporate personalized pass details within your messaging campaigns.

**PassKit 커넥티드 콘텐츠 호출**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Liquid 예제 응답**

{% tabs local %}
{% tab 상환 전달 세부 정보 %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab 합격 상태 %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
[3]:https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]:https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]:https://github.com/PassKit/smart-pass-link-from-csv-generator
[12]:https://docs.passkit.io/protocols/member/
[13]:https://docs.passkit.io/protocols/coupon/
[14]:https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[16]:https://en.wikipedia.org/wiki/HMAC
