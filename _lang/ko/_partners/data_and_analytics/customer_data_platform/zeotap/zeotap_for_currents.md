---
nav_title: Zeotap for Currents
article_title: Zeotap for Currents
description: "This reference article outlines the partnership between Braze Currents and Zeotap, a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap for Currents

> [Zeotap](https://zeotap.com/) is a next-generation customer data platform that helps you discover and understand your mobile audience by providing identity resolution, insights, and data enrichment.

The Braze and Zeotap integration empowers you to extend the scale and reach of your campaigns by syncing Zeotap customer segments to Braze user profiles. With [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), you can also connect data to Zeotap to make it actionable across the entire growth stack.

{% alert important %}
The custom HTTP connector is currently in beta. 이 통합을 설정하는 데 관심이 있는 경우에는 고객 성공 매니저에게 문의하세요.
{% endalert %}

## Prerequisites

| Requirement | Description |
| --- | --- |
|Zeotap account | A [Zeotap account](https://zeotap.com/) is required to take advantage of this partnership. |
| Currents | To export data back into Zeotap, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Implementation

### Step 1: Create a Currents source

1. In Zeotap, go to **Sources** under **Integrate**.
2. Select **Create Source**.
3. 카테고리로 **고객 참여 채널을** 선택합니다.<br><br>!['고객 참여 채널'을 포함한 다양한 카테고리가 나열된 '소스 만들기' 창입니다.]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. 데이터 소스로 **Braze를** 선택합니다.
5. Enter a source name.
6. 지역을 선택하세요.<br><br>![지역 및 데이터 엔티티를 선택할 수 있는 옵션이 있는 창입니다.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. **소스 생성을** 선택합니다.
8. **구현 세부 정보** 탭으로 이동하여 **API URL과** **쓰기 키를** 메모합니다.<br><br>![API URL과 쓰기 키가 포함된 Braze Currents의 구현 세부 정보입니다.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### 2단계: Configure data streaming in Currents

1. In Braze, go to **Partner Integrations** > **Data Export**.
2. **새 전류 만들기** 및 **사용자 지정 전류 내보내기를** 선택합니다.<br><br>!["사용자 지정 전류 내보내기"가 포함된 드롭다운이 있는 "새 전류 만들기" 버튼입니다.]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. 연동 이름과 연동에서 오류가 발생할 경우 연락받을 이메일을 입력합니다.
4. Under **Credentials**, enter the following information you noted from [Step 1](#step-1-create-a-currents-source):
- The API URL as the **Endpoint**
- **무기명 토큰으로서의** 쓰기 키<br><br>![통합 세부 정보 및 자격 증명을 입력하는 섹션입니다.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Select the message engagement events that you want to send to Zeotap.<br><br>![메시지 참여 이벤트를 선택할 수 있는 섹션이 있는 '일반 설정' 탭입니다.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. **현재 실행을** 선택하여 변경 사항을 저장하고 Zeotap에 이벤트 전송을 시작합니다.

{% alert important %}
The Currents connector doesn't support anonymous users (users without an `external_id`).
{% endalert %}

