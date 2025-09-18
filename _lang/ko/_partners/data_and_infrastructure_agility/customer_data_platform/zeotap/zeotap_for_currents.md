---
nav_title: 전류용 제오탭
article_title: 전류용 제오탭
description: "이 참조 문서에서는 신원 확인, 인사이트, 데이터 보강을 제공하여 모바일 잠재고객을 발견하고 이해하는 데 도움을 주는 차세대 고객 데이터 플랫폼인 브라즈 커런츠와 Zeotap의 파트너십에 대해 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner
---

# 전류용 제오탭

> [Zeotap](https://zeotap.com/)은(는) 차세대 고객 데이터 플랫폼으로, 신원 확인, 인사이트 및 데이터 강화 기능을 제공하여 모바일 오디언스를 발견하고 이해하는 데 도움을 줍니다.

Braze와 Zeotap의 통합을 통해 Zeotap 고객 세그먼트를 Braze 사용자 프로필에 동기화하여 캠페인의 규모와 도달 범위를 확장할 수 있습니다. [Currents를]({{site.baseurl}}/user_guide/data/braze_currents/) 사용하면 데이터를 Zeotap에 연결하여 전체 성장 스택에서 실행 가능한 데이터로 만들 수도 있습니다.

{% alert important %}
사용자 지정 HTTP 커넥터는 현재 베타 버전입니다. 이 통합을 설정하는 데 관심이 있으시면 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| --- | --- |
|Zeotap 계정 | 이 파트너십을 활용하려면 [Zeotap 계정](https://zeotap.com/)이 필요합니다. |
| 커런츠 | 데이터를 다시 제오탭으로 내보내려면 계정에 [Braze Currents를]({{site.baseurl}}/user_guide/data/braze_currents/) 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 구현

### 1단계: 커런츠 소스 만들기

1. Zeotap에서 **통합** 아래의 **소스로** 이동합니다.
2. **소스 생성을** 선택합니다.
3. 카테고리로 **고객 참여 채널을** 선택합니다.<br><br>!['고객 참여 채널'을 포함한 다양한 카테고리가 나열된 '소스 만들기' 창입니다.][1]{: style="max-width:70%;"}<br><br>
4. 데이터 소스로 **Braze를** 선택합니다.
5. 소스 이름을 입력합니다.
6. 지역을 선택하세요.<br><br>![지역 및 데이터 엔티티를 선택할 수 있는 옵션이 있는 창입니다.][6]{: style="max-width:70%;"}<br><br>
7. **소스 생성을** 선택합니다.
8. **구현 세부 정보** 탭으로 이동하여 **API URL과** **쓰기 키를** 메모합니다.<br><br>![API URL과 쓰기 키가 포함된 Braze Currents의 구현 세부 정보입니다.][2]

### 2단계: 커런츠에서 데이터 스트리밍 구성

1. Braze에서 **파트너 연동** > **데이터 내보내기로** 이동합니다.
2. **새 전류 만들기** 및 **사용자 지정 전류 내보내기를** 선택합니다.<br><br>!["사용자 지정 전류 내보내기"가 포함된 드롭다운이 있는 "새 전류 만들기" 버튼입니다.][3]{: style="max-width:60%;"}<br><br>
3. 연동 이름과 연동에서 오류가 발생할 경우 연락받을 이메일을 입력합니다.
4. **자격증명** 아래에 [1단계에서](#step-1-create-a-currents-source) 기록한 다음 정보를 입력합니다:
- **엔드포인트로서의** API URL
- **무기명 토큰으로서의** 쓰기 키<br><br>![통합 세부 정보 및 자격 증명을 입력하는 섹션입니다.][4]<br><br>
5. Select the message engagement events that you want to send to Zeotap.<br><br>![메시지 참여 이벤트를 선택할 수 있는 섹션이 있는 '일반 설정' 탭입니다.][5]
6. **현재 실행을** 선택하여 변경 사항을 저장하고 Zeotap에 이벤트 전송을 시작합니다.

{% alert important %}
커런츠 커넥터는 익명 사용자( `external_id`)는 지원하지 않습니다.
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}