---
nav_title: 워크스페이스 간 복사
article_title: 워크스페이스 간 복사
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "이 문서에서는 캠페인을 여러 워크스페이스에 복사하는 방법에 대한 개요를 제공합니다."
tool: Campaigns
---

# 워크스페이스 간 복사

> 워크스페이스 간에 캠페인을 복사하면 다른 워크스페이스에 있는 캠페인의 복사본으로 시작하여 메시지 구성을 바로 시작할 수 있습니다. 이 사본은 편집하고 시작할 때까지 초안으로 유지되므로 성공적인 메시징 전략을 유지하고 발전시키는 데 도움이 됩니다.<br><br>이 페이지에서는 캠페인을 다른 워크스페이스로 복사하는 방법과 복사할 수 있는 항목과 복사하지 않는 항목을 나열합니다.

{% alert important %}
일반적으로 다음과 같은 지원되는 채널에서 워크스페이스 간에 캠페인을 복사할 수 있습니다. 바로 SMS, 인앱 메시지, 이메일, 이메일 템플릿 및 콘텐츠 블록입니다. 다른 채널 지원(예: 푸시 및 콘텐츠 카드)은 아직 제공되지 않습니다.
{% endalert %}

## 캠페인을 다른 워크스페이스로 복사하는 방법

![Menu with "Copy to workspace" option.][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Select the <i class="fas fa-cog"></i> gear icon next to the selected campaign, and select **Copy to workspace**. 복사한 후에는 캠페인을 검토하고 테스트하여 모든 필드가 제대로 작동하는지 확인하는 것이 좋습니다.

워크스페이스 간에 캠페인을 복사하면 캠페인 이름 및 설명, 배리언트, 전달 일정 유형 및 전환 행동과 같은 필드가 복사됩니다. 이메일 캠페인의 경우 이메일 본문, 제목, 프리헤더와 같은 필드도 대상 워크스페이스로 복사됩니다. 

지원되지 않는 채널이 있는 멀티채널 캠페인은 다른 워크스페이스로 복사할 수 없습니다.

### 워크스페이스 간에 복사되는 항목

다음은 워크스페이스 전체에 복사되는 항목과 생략되는 항목의 전체 목록이 아닙니다. 모범 사례로 캠페인 세부 정보를 확인하고 테스트하여 캠페인이 예상대로 작동하는지 확인합니다.

{% tabs %}
{% tab 캠페인 %}

| 복사됨 | 생략 |
|---|---|
| 설명 | 지역 | 
| 유형 | 태그 | 
| 작업(중첩) | 세그먼트 | 
| 전환 행동(중첩) | 승인 | 
| 조용한 시간 구성 | 트리거 일정 | 
| 주파수 제한 구성 | 캠페인 요약 | 
| 수신자 구독 상태 |  | 
| 반복 일정 |  | 
| 트랜잭션 |  | 

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 전환 행동 %}

| 복사됨 | 생략 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| 캠페인 상호 작용 |  캠페인 ID | 
| 사용자 지정 이벤트 이름 |  | 
| 제품 이름 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 작업 %}

| 복사됨 | 생략 |
|---|---|
| 작업 유형 | 전송 횟수 |
| 메시지 변형 |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 메시지 변형 %}

| 복사됨 | 생략 |
|---|---|
| 전송 비율 | API ID |
| 유형 |  시드 그룹 ID | 
|  |  링크 템플릿 ID | 
|  |  내부 사용자 그룹 ID | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 이메일 메시지 변형 %}

| 복사됨 | 생략 |
|---|---|
| [이메일 본문]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | 주소에서 |
| 메시지 추가 정보 |  댓글 | 
| 제목 |  BCC | 
| 제목 |  링크 템플릿 | 
|  |  링크 별칭 지정 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 이메일 본문 %}

| 복사됨 | 생략 |
|---|---|
| 일반 텍스트 | 링크 별칭 지정 |
| HTML 및 드래그 앤 드롭 콘텐츠 |  | 
| 프리헤더 |  | 
| 인라인 CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 이메일 템플릿 %}

| 복사됨 | 생략 |
|---|---|
| [이메일 본문]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | API ID |
| 설명 | 이미지 ID | 
| 제목 | 지역 | 
| 헤더 | 태그 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 콘텐츠 블록 %}

| 복사됨 | 생략 |
|---|---|
| 이름 | 링크 별칭 지정 |
| 설명 | API 키 | 
| 콘텐츠 | 지역 | 
| HTML 및 드래그 앤 드롭 콘텐츠 | 태그 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SMS 메시지 변형 %}

| 복사됨 | 생략 |
|---|---|
| 본문 | 메시징 서비스 |
| 링크 단축 | VCF 미디어 항목 | 
| 클릭 추적 |  | 
| 미디어 항목 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Liquid가 포함된 캠페인 복사하기

Liquid 참조가 포함된 메시지 본문의 경우 참조가 대상 워크스페이스로 복사되지만 예상대로 작동하지 않을 수 있습니다. 즉, 워크스페이스 A의 캠페인이 워크스페이스 B로 복사되는 경우 워크스페이스 B는 Liquid 참조를 포함하여 워크스페이스 A의 세부 정보를 참조할 수 없습니다. 예를 들어 트리거 동작 및 오디언스 필터와 같은 필드는 복사되지 않습니다.

워크스페이스 간에 캠페인을 복사할 때 종속성이 있는 다음 Liquid 참조에 유의하세요.

- 카탈로그 항목 태그
- 연결된 콘텐츠 태그
- 콘텐츠 블록
- 사용자 지정 속성
- 환경설정 센터
- 제품 추천
- 구독 상태 태그
- 바우처 및 프로모션 태그

워크스페이스 간에 캠페인을 복사하는 경우 콘텐츠 블록은 복사되지 않습니다. 그러나 같은 이름의 블록이 있는 경우 대상 워크스페이스에서 콘텐츠 블록을 참조할 수 있습니다. 또는 대상 워크스페이스에서 콘텐츠 블록(또는 이러한 Liquid 참조)을 생성하여 캠페인을 시작할 때 오류를 방지할 수 있습니다.

### Copying campaigns with feature flags

To copy a feature flag campaign between workspaces, make sure the destination workspace has a [feature flag experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments) configured with an ID that matches the feature flag referenced in the original campaign. If you copy a campaign but a matching feature flag ID doesn't exist in the destination workspace, the feature flag selection in the campaign will be blank when copied, and you'll have to select a different one.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

