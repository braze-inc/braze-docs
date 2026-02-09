---
nav_title: Wyng
article_title: Wyng
description: "이 참고 문서에서는 마이크로 경험, 고객 선호도 포털 및 API 플랫폼을 통해 고객 선호도와 속성을 수집, 사용 및 통합하는 데 사용되는 제로파티 데이터 플랫폼인 Braze와 Wyng의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng은](https://wyng.com/) 중요한 순간에 소비자의 참여를 유도하고, 선호도 및 기타 제로파티 데이터를 수집하며, 실시간으로 개인화된 대화형 디지털 경험(퀴즈, 선호도 센터, 프로모션)을 구축할 수 있는 툴을 제공합니다.

_This integration is maintained by Wyng._

## About the integration

The Braze and Wyng integration allows you to leverage zero-party data earned via Wyng experiences to personalize interactions in Braze Campaigns and Braze Canvas. Wyng can also power a preference center, so consumers can control the data and preferences (including communication preferences) they share with your brand.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Wyng account | A Wyng account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect the Braze integration

In Wyng, go to [**Integrations**](https://wyng.com/dashboard/integrations/) and select the **Add** tab. 다음으로, **Braze** 위로 마우스를 가져가서 통합을 위해 **Connect**를 클릭합니다.

![Wyng 플랫폼의 Braze 파트너 타일.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### 2단계: Configure the Braze connector

1. 열리는 구성 창에서 Braze REST API 키를 입력하세요.
![자격 증명 프롬프트 모습을 보여주는 이미지.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. 다음으로, 드롭다운을 사용하여 Braze와 공유할 Wyng 캠페인을 선택합니다.![Braze와 공유할 Braze 커넥터를 선택하라는 프롬프트를 보여주는 기존 Wyng 캠페인 이미지.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로, 가입, 속성 및 이벤트 오브젝트, 커스텀 이벤트를 설정해야 합니다.<br><br>
- **Subscriptions setup (required)**<br>
To subscribe users to subscription groups, click **Add Subscription** and add your subscription group name and ID. 여러 그룹 이름과 ID를 추가하려면 **구독 추가** 버튼을 다시 클릭하십시오.<br>![구독 그룹 이름과 ID를 묻는 이미지입니다.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **사용자 추적 설정**<br>
Click **Add custom property** to add attribute and event object pairs to send to the `/users/track` endpoint. Use this to add hard-coded attribute values for each data transaction sent for the integration. 여러 속성을 추가하려면 **커스텀 속성** 버튼을 다시 클릭하십시오.<br>![속성 커스텀 속성을 추가하라는 메시지가 표시된 이미지입니다.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **커스텀 이벤트 전송**<br>
Optionally, you can enable **Sending custom event**. 활성화된 경우 이벤트 이름과 해당 앱 ID를 포함해야 합니다.<br>![필요한 경우 커스텀 이벤트를 보내도록 요청하는 이미지입니다.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. 마지막으로, 사용 사례에 따라 Wyng 필드를 Braze API 필드에 매핑해야 합니다. Click **Select a field** to choose fields to map, and afterwards, **Save** your integration. 저장되면 이러한 매핑된 필드는 **Integrations > Manage** 아래에서 찾을 수 있습니다.
![다양한 Wyng 필드를 특정 Braze 필드에 매핑할 수 있는 예]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![사용 가능한 동기화 필드 목록입니다.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### 3단계: Test your integration

In Wyng, test submitting the form in your Wyng campaign. You can also submit it in the preview campaign if you do not want to add a record to the main production campaign. You should see a successful transaction in the **Integration** dashboard.

## Using this integration

Once the data connector is in place, any fields created in Wyng and added to Braze can be used just like any other data field to trigger campaigns, segment audiences, or feed personalized content.

Applications are broad, and specific questions can be addressed to [contact@wyng.com](mailto:contact@wyng.com) or your specific account manager.

## Troubleshooting

### Failed submission

제출 실패의 경우, Braze에 데이터를 보낼 때, 실패한 제출 및 관련 오류 메시지를 검토하려면 **로그 보기** 링크를 클릭하십시오.

!['로그 보기' 링크는 작업 헤더 아래에 있습니다.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

로그 페이지에는 실패한 제출, 재시도 횟수, 제출의 데이터, 오류 및 제출을 다시 푸시하는 링크가 표시됩니다.

![실패한 제출물이 표시되는 예시입니다.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

**오류 보기** 섹션은 오류 코드와 오류의 원인에 대한 추가 정보를 표시합니다. 그런 다음 오류 코드를 Braze와 대조하여 원인을 확인할 수 있습니다.

![Wyng 플랫폼에 표시된 예제 오류 로그입니다.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

추가 질문이 있는 경우 Wyng 지원팀[(support@wyng.com](mailto:contact@wyng.com))에 문의하여 도움을 받으세요.


