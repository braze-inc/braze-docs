---
nav_title: 작업 공간 간 복사
article_title: 작업 공간 간 복사
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "이 참고 문서에서는 캠페인과 캔버스를 다른 작업 공간으로 복사하는 방법에 대한 개요를 제공합니다."
tool:
    - Campaigns
    - Canvas
---

# 여러 워크스페이스에서 캠페인 및 캔버스 복사하기

> 워크스페이스 간에 캠페인을 복사하면 다른 워크스페이스에 있는 캠페인의 복사본으로 시작하여 메시지 구성을 바로 시작할 수 있습니다. 이 페이지에서는 캠페인을 다른 워크스페이스로 복사하는 방법과 복사할 수 있는 항목과 복사하지 않는 항목을 나열합니다.

캠페인이나 캔버스를 다른 작업 공간으로 복사하면 편집하고 실행할 때까지 복사본이 초안으로 유지되므로 성공적인 메시징 전략을 유지하고 구축하는 데 도움이 됩니다.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
일반적으로 워크스페이스 간에 캠페인을 복사할 수 있습니다. 현재 콘텐츠 카드에 대한 채널 지원은 제공되지 않습니다.
{% endalert %}

이러한 지원되는 채널에 대해 워크스페이스 간에 캠페인을 복사할 수 있습니다: SMS, 인앱 메시지, 푸시 알림, 이메일, 웹훅. 이메일 템플릿, 기능 플래그 및 콘텐츠 블록 간에 복사할 수도 있습니다. 지원되지 않는 채널이 있는 멀티채널 캠페인은 다른 워크스페이스로 복사할 수 없다는 점에 유의하세요.

캠페인을 다른 워크스페이스로 복사하려면 다음과 같이 하세요:

1. 선택한 캠페인 옆의 <i class="fas fa-cog"></i> 톱니바퀴 아이콘을 선택합니다.
2. **작업 공간에 복사를** 선택합니다. 
3. 복사한 후 캠페인을 검토하고 테스트하여 모든 필드가 제대로 작동하는지 확인합니다.

{% endtab %}
{% tab canvas %}

{% alert important %}
일반적으로 작업 공간 간에 캔버스를 복사할 수 있습니다. 현재 지원되지 않는 채널은 다음과 같습니다: LINE, 콘텐츠 카드, WhatsApp.
{% endalert %}

이메일, 인앱 메시지, 푸시, 웹훅, SMS 등 지원되는 채널에 대해 워크스페이스 간에 캔버스를 복사할 수 있습니다.

캔버스를 다른 작업 공간으로 복사하려면:

1. 선택한 캔버스 옆의 <i class="fa-solid fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **작업 공간에 복사를** 선택합니다. 
3. 복사한 후 캔버스를 검토하고 테스트하여 모든 필드가 제대로 작동하는지 확인합니다.

오디언스 동기화 단계가 있는 캔버스를 복사할 때 설정은 대상 워크스페이스로 복사되지 않지만 여정의 단계는 복사됩니다.

{% endtab %}
{% endtabs %}

## 작업 공간 간에 복사되는 항목

다음은 작업 공간 전체에 복사되는 항목과 생략되는 항목의 전체 목록이 아닙니다. 캠페인 및 캔버스 세부 정보를 확인하고 메시지가 예상대로 작동하는지 테스트하는 것이 가장 좋습니다.

### 세부 정보

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 설명 | 지역 | 
| 유형 | 태그 | 
| 작업(중첩) | 세그먼트 | 
| 전환 동작(중첩) | 승인 | 
| 조용한 시간 구성 | 트리거 일정 | 
| 최대 게재빈도 설정 구성 | 캠페인 요약 | 
| 수신자 구독 상태 |  | 
| 반복 일정 |  | 
| 트랜잭션 여부 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 설명 | 지역 | 
| 유형 | 태그 | 
| 작업(중첩) | 세그먼트 | 
| 전환 동작(중첩) | 승인 | 
| 조용한 시간 구성 | 트리거 일정 | 
| 최대 게재빈도 설정 구성 | 캔버스 요약 | 
| 수신자 구독 상태 |  | 
| 반복 일정 |  | 
| 트랜잭션 여부 |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 전환 행동

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| 캠페인 상호 작용 |  캠페인 ID | 
| 커스텀 이벤트 이름 |  | 
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| 캔버스 상호 작용 |  캔버스 ID | 
| 커스텀 이벤트 이름 |  | 
| 제품 이름 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 작업

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| 캠페인 상호 작용 |  캠페인 ID | 
| 커스텀 이벤트 이름 |  | 
| 제품 이름 |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 유형 동작 | 워크스페이스 ID |
| 캔버스 상호 작용 |  캔버스 ID | 
| 커스텀 이벤트 이름 |  | 
| 제품 이름 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 메시지 변형

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 전송 비율 | API ID |
| 유형 |  시드 그룹 ID | 
|  |  링크 템플릿 ID | 
|  |  내부 사용자 그룹 ID | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 전송 비율 | API ID |
| 유형 |  시드 그룹 ID | 
|  |  링크 템플릿 ID | 
|  |  내부 사용자 그룹 ID | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### 이메일 메시지 변형

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 이메일 본문 | 주소에서 |
| 메시지 추가 정보 |  댓글 | 
| 제목 |  BCC | 
| 제목 |  링크 템플릿 | 
|  |  링크 별칭 지정 |
|  | 번역 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 이메일 본문 | 주소에서 |
| 메시지 추가 정보 |  댓글 | 
| 제목 |  BCC | 
| 제목 |  링크 템플릿 | 
|  |  링크 별칭 지정 |
|  | 번역 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 이메일 본문

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 일반 텍스트 | 링크 별칭 지정 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 번역 | 
| 프리헤더 |  | 
| 인라인 CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 일반 텍스트 | 링크 별칭 지정 |
| HTML 및 드래그 앤 드롭 콘텐츠 | 번역 | 
| 프리헤더 |  | 
| 인라인 CSS |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 이메일 템플릿

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 이메일 본문 | API IDs |
| 설명 | 이미지 ID | 
| 제목 | 지역 | 
| 헤더 | 태그 | 
| | 번역 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 이메일 본문 | API IDs |
| 설명 | 이미지 ID | 
| 제목 | 지역 | 
| 헤더 | 태그 | 
| | 번역 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 콘텐츠 블록

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 이름 | 링크 별칭 지정 |
| 설명 | API 키 | 
| 콘텐츠 | 지역 | 
| HTML 및 드래그 앤 드롭 콘텐츠 | 태그 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 이름 | 링크 별칭 지정 |
| 설명 | API 키 | 
| 콘텐츠 | 지역 | 
| HTML 및 드래그 앤 드롭 콘텐츠 | 태그 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### SMS 메시지 변형

{% tabs local %}
{% tab campaigns %}

| 복사됨 | 생략 |
|---|---|
| 본문 | 메시징 서비스 |
| 링크 단축 | VCF 미디어 항목 | 
| 클릭 추적 |  | 
| 미디어 항목 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| 복사됨 | 생략 |
|---|---|
| 본문 | 메시징 서비스 |
| 링크 단축 | VCF 미디어 항목 | 
| 클릭 추적 |  | 
| 미디어 항목 |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Liquid가 포함된 메시지 복사하기

메시지 본문 내의 Liquid 참조가 대상 워크스페이스로 복사되지만 참조가 예상대로 작동하지 않을 수 있습니다. 즉, 워크스페이스 A의 캔버스를 워크스페이스 B로 복사하면 워크스페이스 B는 Liquid 참조를 포함하여 워크스페이스 A의 세부 정보를 참조할 수 없습니다. 예를 들어 트리거 동작 및 오디언스 필터와 같은 필드는 복사되지 않습니다.

워크스페이스 간에 캠페인과 캔버스를 복사할 때 종속성이 있는 다음 Liquid 참조를 추적하세요:

- 카탈로그 항목 태그
- 연결된 콘텐츠 태그
- 콘텐츠 블록
- 커스텀 속성
- 환경 설정 센터
- 제품 추천
- 구독 상태 태그
- 바우처 및 프로모션 태그

## 기능 플래그가 있는 메시지 복사하기

워크스페이스 간에 기능 플래그 캠페인과 기능 플래그 단계가 있는 캔버스를 복사하려면 대상 워크스페이스에 원래 캠페인에서 참조한 기능 플래그 또는 원래 캔버스에서 참조한 기능 플래그 단계와 일치하는 ID로 구성된 [기능 플래그 실험이]({{site.baseurl}}/developer_guide/feature_flags/experiments) 있는지 확인합니다.

대상 워크스페이스에 존재하지 않는 기능 플래그 ID를 가진 기능 플래그 단계가 있는 캠페인 또는 캔버스를 복사하는 경우 기능 플래그 단계는 복사되지만 해당 콘텐츠는 복사되지 않습니다.

## 콘텐츠 블록으로 메시지 복사하기

워크스페이스 간에 캠페인을 복사하는 경우 콘텐츠 블록은 복사되지 않습니다. 그러나 같은 이름의 블록이 있는 경우 대상 워크스페이스에서 콘텐츠 블록을 참조할 수 있습니다. 또는 대상 워크스페이스에 콘텐츠 블록(또는 이러한 Liquid 참조)을 생성하여 캠페인을 시작할 때 오류를 방지할 수 있습니다.

콘텐츠 블록을 참조하는 캔버스의 경우 먼저 콘텐츠 블록을 대상 워크스페이스에 복사해야 합니다.
