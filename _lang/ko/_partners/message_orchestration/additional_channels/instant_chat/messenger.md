---
nav_title: 메신저
article_title: Facebook 메신저
alias: /partners/messenger/
description: "이 참조 문서에서는 세계에서 가장 인기 있는 인스턴트 메시징 플랫폼 중 하나인 Facebook Messenger와 Braze의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Facebook 메신저

> [Facebook Messenger](https://developers.facebook.com/docs/messenger-platform/)는 10억 명에 가까운 월간 활성 사용자가 사용하는 세계에서 가장 인기 있는 인스턴트 메시징 플랫폼 중 하나입니다. 이 플랫폼을 통해 브랜드는 고객과 지능적이고 자동으로 상호 작용하는 매력적인 챗봇을 만들 수 있습니다.

Braze와 Facebook 통합은 Braze 웹훅, 세분화, 개인화 및 트리거 기능을 활용하여 메신저 플랫폼 API를 통해 Facebook Messenger에서 사용자에게 메시지를 보낼 수 있습니다. 사용자 지정 Facebook Messenger 웹훅 템플릿은 플랫폼의 **템플릿** > **웹훅 템플릿에** 포함되어 있습니다.

Facebook Messenger 플랫폼은 "기존 거래를 촉진하거나 기타 고객 지원 조치를 제공하거나 개인이 요청한 콘텐츠를 전달하는 비홍보성 메시지"를 위한 것입니다. 자세한 내용은 [Facebook의 플랫폼 가이드라인](https://developers.facebook.com/docs/messenger-platform) 및 [허용되는 사용 사례 예제](https://developers.facebook.com/docs/messenger-platform/app-review#examples_acceptable)를 참조하세요.

## 전제 조건

통합을 진행하기 전에 다음 사항을 확인하시기 바랍니다:
- Facebook은 메신저 플랫폼을 사용하여 마케팅 메시지를 보내는 것을 허용하지 않습니다. 
- 페이지의 메시지에 대한 사용자의 명시적인 권한이 필요합니다. 
- Facebook 앱의 테스트 사용자가 아닌 사용자에게 메시지를 보내려면 앱이 Facebook의 [앱 검토를](https://developers.facebook.com/docs/messenger-platform/app-review) 통과해야 합니다.<br><br>

| 요구 사항| Origin| 접근| 설명|
| ---| ---| ---|
| Facebook Messenger 페이지| Facebook| [https://www.facebook.com/pages/create](https://www.facebook.com/pages/create) | Facebook 페이지가 봇의 ID로 사용됩니다. 앱에서 채팅할 때 페이지 이름과 프로필 사진이 표시됩니다.|
| Facebook 메신저 앱| Facebook| [https://developers.facebook.com/apps](https://developers.facebook.com/apps) | Facebook 앱에는 액세스 토큰을 포함한 메신저 봇에 대한 설정이 포함되어 있습니다.
| 앱 봇 검토 및 승인 | Facebook | [https://developers.facebook.com/docs/messenger-platform/app-review](https://developers.facebook.com/docs/messenger-platform/app-review) | 봇을 대중에게 공개할 준비가 되면 검토 및 승인을 위해 Facebook에 봇을 제출해야 합니다. 이 검토 프로세스를 통해 메신저의 모든 사용자가 사용할 수 있도록 먼저 메신저 봇이 정책을 준수하며 예상대로 작동하는지 확인할 수 있습니다. |
| 페이지 범위 ID(PSID) | Facebook | [https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) | Facebook Messenger에서 메시지를 보내려면 사용자 PSID가 있어야 합니다. 사용자가 메신저를 통해 앱과 상호 작용하면 Facebook에서 PSID를 생성합니다. 이 PSID는 문자열 사용자 지정 속성으로 Braze에 전송할 수 있습니다.
| 페이지 액세스 토큰 | Facebook | [https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup#page_access_token) | 이러한 액세스 토큰은 Facebook 페이지에 속한 데이터를 읽거나 쓰거나 수정하는 API에 권한을 제공한다는 점을 제외하면 사용자 액세스 토큰과 유사합니다. 페이지 액세스 토큰을 얻으려면 사용자 액세스 토큰을 얻은 후 `manage_pagespermission`을 요청해야 합니다. 사용자 액세스 토큰이 있으면 그래프 API를 통해 페이지 액세스 토큰을 가져옵니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

다음에서는 Braze Facebook 메신저 웹훅을 설정하는 방법을 보여줍니다.
봇을 설정하는 데 추가적인 도움이 필요하다면 전체 메신저 봇 튜토리얼과 예제 코드를 [Braze GitHub 리포지토리](https://github.com/Appboy/appboy-fb-messenger-bot)에서 확인하실 수 있습니다!

### 1단계: PSID 수집

Facebook Messenger에서 메시지를 보내려면 사용자를 식별하고 지속적으로 소통할 수 있도록 사용자의 페이지별 ID(PSID)를 수집해야 합니다. PSID는 사용자의 Facebook ID와 동일하지 않습니다. Facebook은 회원님이 고객에게 메시지를 보낼 때마다 또는 고객이 회원님에게 메시지를 보낼 때마다 이 식별자를 생성합니다.

PSID는 Facebook에서 제공하는 다양한 [진입점](https://developers.facebook.com/docs/messenger-platform/discovery) 중 하나를 사용하여 찾을 수 있습니다. 사용자가 앱에 메시지를 보내거나 대화에서 버튼을 탭하거나 메시지를 보내는 등의 작업을 수행하면 해당 사용자의 PSID가 웹훅 이벤트의 `sender.id` 속성에 포함되므로 봇이 작업을 수행한 사용자를 식별할 수 있습니다.

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "<DEVELOPER_DEFINED_PAYLOAD>"
    }
  }
}
```

메시지를 보낼 때마다 메시지를 받아야 하는 사람을 식별하기 위해 요청의 `recipient.id` 속성에 해당 사용자의 PSID가 포함됩니다.

### 2단계: 사용자 지정 속성으로 Braze에 보내기

PSID를 받고 있다는 확신이 들면, 개발자와 조율하고 이를 공유하여 PSID를 [사용자 지정 속성으로]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#custom-attributes) Braze에 전송하세요. PSID는 [API 호출을](https://developers.facebook.com/docs/messenger-platform/reference/send-api) 통해 액세스할 수 있는 문자열입니다.

### 3단계: 웹훅 템플릿 설정

**템플릿 및 미디어**에서 **웹훅 템플릿**으로 이동하여 **Facebook 메신저 웹훅 템플릿**을 선택합니다.

1. 템플릿 이름을 입력하고 필요에 따라 팀과 태그를 추가합니다.
2. 메시지를 직접 입력하거나 [Facebook에서 제공하는](https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messages) 메시지 템플릿 중에서 선택하세요. 메시지 [유형이나](https://developers.facebook.com/docs/messenger-platform/send-messages#message_types) [태그를](https://developers.facebook.com/docs/messenger-platform/send-messages/message-tags) 선택할 수도 있습니다.
3. PSID를 사용자 지정 속성으로 포함합니다. **요청 본문** 상자 모서리에 있는 파란색과 흰색 **+** 버튼을 사용하여 이 작업을 수행할 수 있습니다.
3. `FACEBOOK_PAGE_ACCESS_TOKEN`을 사용자 토큰으로 바꿔 웹훅 URL에 페이지 액세스 토큰을 추가합니다.

#### 웹훅 미리보기 및 테스트

메시지를 보내기 전에 웹훅을 테스트하세요. 메신저 ID가 Braze에 저장되어 있는지 확인하고(또는 찾아서 사용자 지정된 사용자로 테스트) 미리보기를 사용하여 테스트 메시지를 전송합니다.

![테스트 탭에서 기존 사용자에게 메시지를 전송하여 미리 볼 수 있음을 보여주는 Facebook Messenger 웹훅 템플릿입니다.][60]

메시지를 성공적으로 수신했다면 메시지 전달 설정을 구성할 수 있습니다.

## 이 통합 사용

설정이 완료되면 이 연동 기능을 사용하여 Facebook Messenger 사용자를 타겟팅하세요. 사용자의 전화번호를 사용하여 메시지를 보내지 않고 반복적으로 메신저 메시지를 보낼 계획이라면 커스텀 속성으로 메신저 ID가 존재하는 모든 사용자에 대해 [세그먼트를 생성][62]하고 [분석 추적][61] 을 켜서 시간에 따른 메신저 가입 비율을 추적해야 합니다. 

![세그먼트 필터 "messenger_id"를 "비어 있지 않음"으로 설정합니다.][63]

메신저 가입자를 위한 특정 세그먼트를 생성하지 않으려는 경우 오류를 방지하기 위해 존재하는 메신저 ID에 대한 필터를 포함해야 합니다.

다른 세분화를 사용하여 메신저 캠페인을 타겟팅할 수도 있으며, 다른 캠페인과 마찬가지로 캠페인 생성 프로세스의 나머지 부분을 사용할 수 있습니다.

[60]: {% image_buster /assets/img_archive/fbm-test.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}