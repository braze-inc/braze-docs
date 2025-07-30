---
nav_title: 이메일 환경설정
article_title: 이메일 환경설정
page_type: reference
page_order: 14
description: "이 참조 문서는 Braze 대시보드에서 이메일 환경 설정을 다루며, 발송 구성, 열람 추적 픽셀, 구독 페이지 및 바닥글 등을 포함합니다."
tool: Dashboard
channel: email

---

# 이메일 환경설정

> 이메일 환경설정은 커스텀 바닥글, 커스텀 옵트인 및 옵트아웃 페이지 등 특정 발신 이메일 설정을 할 수 있는 곳입니다. 아웃바운드 이메일에 이러한 옵션을 포함하면 사용자에게 유연하고 일관된 경험을 제공할 수 있습니다.

**이메일 환경설정**은 대시보드의 **설정**에서 찾을 수 있습니다.

## 구성 보내기

**보내기 구성** 섹션의 이메일 설정은 이메일 캠페인에 포함되는 세부 정보를 결정합니다. 특히 이러한 설정은 사용자가 Braze로부터 이메일을 받을 때 보는 것과 주로 관련이 있습니다.

### 아웃바운드 이메일 설정

이메일 설정을 구성할 때, 발신 이메일 설정은 Braze가 사용자에게 이메일을 보낼 때 사용되는 이름과 이메일 주소를 식별합니다.

{% tabs 로컬 %}
{% tab 표시 이름 주소 %}

이 섹션에서는 Braze가 사용자에게 이메일을 보낼 때 사용할 수 있는 이름과 이메일 주소를 추가할 수 있습니다. 표시 이름과 이메일 주소는 이메일 캠페인을 작성할 때 **보내기 정보 편집** 옵션에서 사용할 수 있습니다. 업데이트가 아웃바운드 이메일 설정에 적용되더라도 기존 발송에는 소급 적용되지 않습니다. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab 받는 사람 주소 %}

이 섹션에 이메일 주소를 추가하면 이메일 캠페인의 회신 주소로 선택할 수 있습니다. 이메일 주소를 기본값으로 설정하려면 **기본값으로 설정**을 선택하세요. 이 이메일 주소는 이메일 캠페인을 작성할 때 **편집 발송 정보** 옵션에서 사용할 수 있습니다.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCC 주소 %}

이 섹션에서는 Braze에서 발송된 아웃바운드 이메일 메시지에 추가할 수 있는 BCC 주소를 추가하고 관리할 수 있습니다. 이메일 메시지에 BCC 주소를 추가하면 사용자가 받는 메시지와 동일한 메시지 사본이 BCC 받은편지함으로 전송됩니다. 이것은 준수 요구 사항 또는 고객 지원 문제에 대해 사용자가 보낸 메시지의 사본을 보관하는 데 유용한 도구입니다. BCC 이메일은 이메일 보고 및 분석에 포함되지 않습니다.

{% alert important %}
캠페인이나 캔버스에 BCC 주소를 추가하면 Braze가 사용자에게 한 개의 메시지를 보내고 BCC 주소로 한 개의 메시지를 보내므로 캠페인 또는 캔버스 구성 요소에 대한 청구 가능한 이메일이 두 배로 늘어납니다.
{% endalert %}

![BCC 주소 섹션의 이메일 설정 탭.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

주소를 추가하면 캠페인 또는 캔버스 단계에서 이메일을 작성할 때 선택할 수 있도록 주소가 제공됩니다. 주소 옆의 **기본값으로 설정**을 선택하여 새 이메일 캠페인 또는 캔버스 구성 요소를 시작할 때 이 주소가 기본적으로 선택되도록 설정합니다. 메시지 수준에서 이를 재정의하려면 메시지를 설정할 때 **BCC 없음**을 선택할 수 있습니다.

Braze에서 보내는 모든 이메일 메시지에 BCC 주소가 포함되도록 하려면 **모든 이메일 캠페인에 BCC 주소 필요** 토글을 선택할 수 있습니다. 이 작업을 수행하려면 새 이메일 캠페인 또는 캔버스 단계에서 자동으로 선택되는 기본 주소를 선택해야 합니다. 기본값 주소는 또한 당사의 REST API를 통해 트리거된 모든 메시지에 자동으로 추가됩니다. 기존 API 요청에 주소를 포함할 필요가 없습니다.

{% endtab %}
{% endtabs %}

## 추적 픽셀 열기

[![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

이메일 오프닝 추적 픽셀은 이메일 HTML에 자동으로 삽입되는 보이지 않는 1 x 1 픽셀 이미지입니다. 이 픽셀은 Braze가 최종 사용자가 이메일을 열었는지 여부를 감지하는 데 도움이 됩니다. 이메일 오픈 정보는 매우 유용할 수 있으며, 사용자가 해당 오픈율을 이해함으로써 효과적인 마케팅 전략을 결정하는 데 도움을 줍니다.

### 추적 픽셀 배치

Braze의 기본 동작은 추적 픽셀을 이메일 하단에 추가하는 것입니다. 대부분의 사용자에게 이것은 픽셀을 놓기에 이상적인 장소입니다. 픽셀은 이미 가능한 한 적은 시각적 변화를 일으키도록 스타일링되어 있지만, 의도하지 않은 시각적 변화는 이메일 하단에서 가장 덜 눈에 띌 것입니다. 이것은 또한 SendGrid 및 SparkPost와 같은 이메일 제공자에 대한 기본값입니다.

### 추적 픽셀의 위치 변경

Braze는 현재 이메일의 `<body>`의 마지막 태그에서 `<body>`의 첫 번째 태그로 ESP의 기본값 열람 추적 픽셀 위치를 재정의하는 것을 지원합니다.
  
![][13]{: style="max-width:80%;" }

위치를 변경하려면:

1. Braze에서 **설정** > **이메일 환경설정**으로 이동합니다.
2. **커스텀 열람 추적 픽셀 설정** 아래의 체크박스를 클릭하세요. 
3. **저장**을 누르세요.

저장되면 Braze는 모든 HTML 이메일 상단에 열람 추적 픽셀을 배치하기 위해 ESP에 특별 지침을 보냅니다.
  
{% alert important %}
SSL 인에이블먼트는 추적 픽셀의 URL을 HTTP 대신 HTTPS로 감쌀 것입니다. SSL이 잘못 구성된 경우 추적 픽셀의 효율성에 영향을 미칠 수 있습니다.
{% endalert %}

## List-unsubscribe 헤더 {#list-unsubscribe}

{% alert note %}
2024년 2월 15일부터 새로운 회사는 기본적으로 list-unsubscribe 헤더(한 번의 클릭으로 구독 취소)가 활성화됩니다.
{% endalert %}

list-unsubscribe 헤더를 사용하면 수신자가 메일함 UI 내에 **탈퇴** 버튼을 표시하여 마케팅 이메일에서 쉽게 탈퇴할 수 있으며, 메시지 본문에는 표시되지 않습니다.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

수신자가 **구독 취소**를 클릭하면 받은편지함 제공자는 이메일 헤더에 정의된 대상에게 구독 취소 요청을 보냅니다.

List-unsubscribe 활성화하는 것은 전달 가능성 모범 사례이며 일부 주요 받은편지함 공급자의 요구 사항입니다. 최종사용자가 이메일 클라이언트에서 스팸 버튼을 누르는 것보다 원치 않는 메시지에서 안전하게 제거하도록 권장합니다. 후자는 발신 평판과 이메일 전달 가능성에 해롭습니다.

### 받은편지함 공급자 지원

다음 표는 "mailto:" 헤더, 목록 구독 취소 URL 및 원클릭 구독 취소([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대한 받은편지함 공급자 지원을 요약한 것입니다.

| List-unsubscribe 헤더 | Mailto: 헤더 | List-unsubscribe URL | 원클릭 탈퇴 (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | 지원됨* | 지원됨 | 지원됨 |
| Gmail 모바일 | 지원되지 않음 | 지원되지 않음 | 지원되지 않음 |
| Apple Mail | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Outlook.com | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| 야후! 메일 | 지원됨* | 지원되지 않음 | 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo와 Gmail은 결국 "mailto:" 헤더를 사용하지 않게 되고, 한 번의 클릭만 지원하게 될 것입니다._

헤더 표시 여부는 궁극적으로 메일박스 제공자가 결정합니다. Gmail에서 수신자의 원시(텍스트) 이메일에 list-unsubscribe 헤더가 포함되어 있는지 확인하려면 다음을 수행하세요.

1. 이메일에서 **원본 보기**를 선택하세요. 이것은 이메일의 원본 버전과 헤더가 있는 새 탭을 엽니다.
2. "list-unsubscribe"를 검색합니다.

헤더가 이메일의 원시 버전에 있지만 표시되지 않는 경우, 받은편지함 제공자가 구독 취소 옵션을 표시하지 않기로 결정한 것이며, 받은편지함 제공자가 헤더를 표시하지 않는 이유에 대해 더 이상의 인사이트가 없음을 의미합니다. list-unsubscribe 헤더를 보는 것은 궁극적으로 평판 기반입니다. 대부분의 경우, 받은편지함에서 발송자 평판이 좋을수록 list-unsubscribe 헤더가 나타날 가능성이 적습니다.

### 워크스페이스의 이메일 구독 취소 헤더

![]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

이메일 구독 취소 헤더 기능이 켜지면 이 설정은 회사 수준이 아닌 전체 워크스페이스에 적용됩니다. 캠페인 및 캔버스에 추가되어 구독하거나 옵트인한 사용자 또는 캠페인 및 캔버스 빌더의 **오디언스** 단계에서 옵트인한 사용자에게 전송됩니다.

'워크스페이스 기본값'을 사용하는 경우, Braze는 '구독을 취소한 사용자를 포함한 모든 사용자에게 보내기'로 구성된 트랜잭션으로 간주되는 캠페인에 대해 원클릭 구독 취소 헤더를 추가하지 않습니다. 이를 재정의하고 수신 거부한 사용자에게 보낼 때 원클릭 수신 거부 헤더를 추가하려면 메시지 수준 원클릭 목록 수신 거부 설정에서 **모든 이메일에서 전역적으로 수신 거부하기를** 선택하면 됩니다.

### 기본값 list-unsubscribe 헤더

{% alert important %}
Gmail은 발신자가 2024년 6월 1일부터 모든 발신 상업적, 홍보 메시지에 대해 원클릭 구독 취소를 구현하도록 의도하고 있습니다. 자세한 내용은 [Gmail의 발신자 지침](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) 및 [Gmail의 이메일 발신자 지침 FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)을 참조하세요. 야후는 업데이트 요구 사항에 대한 2024년 초 일정을 발표했습니다. 자세한 내용은 [더 안전하고 적은 스팸을 참조하세요. 더 나은 경험을 위한 이메일 표준 시행](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Braze 구독 취소 기능을 사용하여 구독 취소를 직접 처리하려면, **구독 또는 옵트인한 사용자에게 발송된 이메일에 대해 원클릭 list-unsubscribe (mailto 및 HTTP) 이메일 헤더 포함**을 선택하고 표준 Braze URL 및 mail-to로 **Braze 기본값**을 선택하세요. 

![구독 또는 옵트인한 사용자에게 발송된 이메일에 대해 list-unsubscribe 헤더를 자동으로 포함하는 옵션.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:80%;"}

Braze는 다음 버전의 list-unsubscribe 헤더를 지원합니다.

| list-unsubscribe 버전 | 설명 | 
| ----- | --- |
| 원-클릭 (RFC 8058) | 수신자가 단일 클릭으로 이메일 수신을 거부할 수 있는 간단한 방법을 제공합니다. 이것은 대량 발송자를 위한 Yahoo 및 Gmail의 요구 사항입니다. |
| 리스트-탈퇴 URL 또는 HTTPS | 수신자에게 수신자를 웹 페이지로 안내하는 링크를 제공하여 구독 취소할 수 있습니다. |
| Mailto | 수신자가 브랜드로부터 구독 취소 요청 메시지를 보낼 대상 이메일 주소를 지정합니다. <br><br> _메일 수신 거부 요청을 처리하려면, 해당 수신 거부 요청에 구독 취소하는 최종사용자의 Braze에 저장된 이메일 주소가 포함되어야 합니다. 이는 최종 사용자가 구독을 취소하는 이메일의 "발신 주소"에서 제공될 수 있으며, 최종사용자가 구독을 취소하는 이메일에서 받은 인코딩된 제목 또는 인코딩된 본문에서 제공될 수 있습니다. 매우 제한된 경우에 일부 받은편지함 제공자는 [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) 프로토콜을 준수하지 않아 이메일 주소가 제대로 전달되지 않는 경우가 있습니다. 이로 인해 Braze에서 구독 취소 요청을 처리할 수 없게 될 수 있습니다._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze가 위의 방법 중 하나를 통해 사용자의 목록 구독 취소 요청을 받으면, 해당 사용자의 글로벌 이메일 구독 상태가 구독 취소로 설정됩니다. 일치하는 항목이 없으면, Braze는 이 요청을 처리하지 않습니다.

### 원클릭 구독 취소

list-unsubscribe 헤더([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대해 원클릭 구독 취소를 사용하면 수신자가 이메일 수신을 거부하는 쉬운 방법을 제공하는 데 중점을 둡니다.

### 메시지 수준 원클릭 목록 구독 취소

메시지 수준 원클릭 목록 구독 취소 설정은 워크스페이스에 설정된 이메일 구독 취소 헤더 기능을 무시합니다. 다음 용도에 대해 캠페인 또는 캔버스 단계별로 원클릭 구독 취소 동작을 적용하세요.

- 특정 구독 그룹에 대해 Braze 원클릭 구독 취소를 추가하여 하나의 워크스페이스 내에서 여러 브랜드/목록을 지원합니다
- 기본 Braze 구독 취소 또는 커스텀 URL 사이에서 토글
- 귀하의 커스텀 원클릭 구독 취소 URL을 추가하세요
- 이 메시지에서 원클릭 탈퇴를 생략하세요

{% alert note %}
메시지 수준 원클릭 목록 구독 취소 설정은 업데이트된 HTML 편집기를 사용할 때만 사용할 수 있습니다. 이전 HTML 편집기를 사용 중인 경우 업데이트된 HTML 편집기로 전환하여 이 기능을 사용하십시오.
{% endalert %}

이메일 편집기에서 **보내기 설정** > **보내기 정보**로 이동합니다. 다음 옵션 중에서 선택하십시오:

- **워크스페이스 기본값 사용**: **이메일 탈퇴 헤더** 설정은 **이메일 환경 설정**에서 설정됩니다. 이 설정을 변경하면 모든 메시지에 변경 사항이 적용됩니다.
- **모든 이메일에서 전역으로 탈퇴**: Braze 기본 원클릭 구독취소 헤더를 사용합니다. 클릭 버튼을 탈퇴하는 사용자는 전역 이메일 구독 상태가 "구독 취소됨"으로 설정됩니다.
- **특정 구독 그룹에서 탈퇴**: 지정된 구독 그룹을 사용합니다. 구독 취소 버튼을 클릭하는 사용자는 선택한 구독 그룹에서 구독 취소됩니다.
    - 구독 그룹을 선택할 때 **구독 그룹** 필터를 **대상 청중**에 추가하여 이 특정 그룹에 가입한 사용자만 타겟팅합니다. 원클릭 탈퇴를 위해 선택한 구독 그룹은 타겟팅하는 구독 그룹과 일치해야 합니다. 구독 그룹에 불일치가 있는 경우, 이미 구독 취소된 구독 그룹에서 구독 취소를 시도하는 사용자에게 보낼 위험이 있습니다.
- **커스텀:** 구독취소를 직접 처리할 수 있도록 커스텀 원클릭 구독취소 URL을 추가합니다.
- **탈퇴 제외**

{% alert important %}
클릭 한 번으로 탈퇴하거나 탈퇴 메커니즘을 제외하는 것은 비밀번호 재설정, 영수증 및 확인 이메일과 같은 거래 메시징에만 해당되어야 합니다.
{% endalert %}

이 설정을 조정하면 이 이메일에서 원클릭 목록 탈퇴에 대한 기본값 동작이 재정의됩니다.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 요구 사항

자신만의 커스텀 탈퇴 기능을 사용하여 이메일을 보내는 경우, 설정한 원클릭 구독 취소 URL이 RFC 8058에 부합하도록 하기 위해 다음 요구 사항을 충족해야 합니다.

* URL은 구독 취소 POST 요청을 처리할 수 있어야 합니다.
* URL은 `https://`로 시작해야 합니다.
* URL은 HTTPS 리디렉션이나 본문을 반환해서는 안 됩니다. 원클릭 탈퇴 링크가 랜딩 페이지 또는 다른 유형의 웹 페이지로 이동하는 경우 RFC 8058을 준수하지 않습니다.
* POST 요청은 쿠키를 설정해서는 안 됩니다.

**커스텀 list-unsubscribe 헤더**를 선택하여 사용자가 구성한 원클릭 구독 취소 엔드포인트 및 선택적 "mailto:"를 추가합니다. Braze는 Yahoo 및 Gmail의 대량 발송자에게 요구되는 원클릭 탈퇴 HTTP를 지원하기 위해 URL 입력이 필요합니다. 커스텀 list-unsubscribe 헤더를 지원하기 위해 URL 입력이 필요합니다.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## 이메일 제목 줄 추가

토글을 사용하여 테스트 및 시드 이메일 제목란에 "[TEST]" 및 "[SEED]"를 포함하세요. 이것은 테스트로 발송된 이메일 캠페인을 식별하는 데 도움이 될 수 있습니다.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 기본값으로 새 이메일의 인라인 CSS

CSS는 이메일과 새 이메일에 대한 CSS 스타일을 자동으로 인라인하는 기술입니다. 일부 이메일 클라이언트의 경우, 이를 통해 이메일이 렌더링되는 방식을 개선할 수 있습니다.

이 설정을 변경하더라도 기존 이메일 메시지 또는 템플릿에 전혀 영향을 미치지 않습니다. 메시지 또는 템플릿을 작성하는 동안 언제든지 이 기본값을 재정의할 수 있습니다. 자세한 내용은 [CSS][10]를 참조하세요.

## 사용자의 이메일이 변경될 때 다시 구독시키기

사용자가 이메일 주소를 변경할 때 자동으로 다시 구독할 수 있습니다. 예를 들어, 이전에 구독 취소한 워크스페이스 사용자가 이메일 주소를 Braze의 구독 취소 목록에 없는 주소로 변경하면 자동으로 다시 구독됩니다.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 구독 페이지 및 바닥글

{% tabs 로컬 %}
{% tab 커스텀 Footer %}

상업용 이메일의 경우 [CAN-SPAM 법](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)은 모든 상업용 이메일에 탈퇴 옵션을 포함하도록 요구합니다. 커스텀 바닥글 설정을 사용하면 이메일 옵트아웃 바닥글을 커스터마이징하면서 CAN-SPAM 규정을 준수할 수 있습니다. 준수를 유지하려면 이 워크스페이스의 캠페인의 일부로 전송되는 모든 이메일에 커스텀 바닥글을 추가해야 합니다.

이메일 메시징을 위한 커스텀 바닥글을 만들 때 다음 요구 사항을 참고하세요.
- 구독 취소 URL 및 실제 우편 주소를 포함해야 합니다.
- 100KB 미만이어야 합니다.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

커스텀 바닥글 Liquid 템플릿에 대해 자세히 알아보려면 [커스텀 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 설명서를 확인하세요.

{% endtab %}
{% tab 커스텀 구독 취소 페이지 %}

Braze를 사용하면 자체 HTML로 **커스텀 탈퇴 페이지**를 설정할 수 있습니다. 이 페이지는 사용자가 이메일 하단에서 구독 취소를 선택한 후에 나타납니다. 이 페이지는 750KB 미만이어야 합니다. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

[이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 이메일 목록 관리에 대한 모범 사례에 대해 자세히 알아보세요.

{% endtab %}
{% tab 커스텀 옵트인 페이지 %}

귀하의 HTML을 사용하여 커스텀 옵트인 페이지를 만들 수 있습니다. 이메일에 이를 포함하는 것은 사용자 라이프사이클 전반에 걸쳐 브랜드와 메시지를 일관되게 유지하고자 할 때 특히 유익할 수 있습니다. 이 페이지는 750KB 미만이어야 합니다. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

[이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 이메일 목록 관리에 대한 모범 사례에 대해 자세히 알아보세요.

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 원클릭 구독 취소

{% details list-unsubscribe를 통한 원클릭 구독 취소 URL이 선호 설정 센터로 연결될 수 있습니까? %}
아니요, 그것은 RFC 8058을 준수하지 않으므로 Yahoo와 Gmail의 원클릭 구독 취소 요구 사항을 준수하지 않습니다.
{% enddetails %}

{% details 왜 내 환경 설정 센터를 작성할 때 오류 메시지 "이메일 본문에 구독 취소 링크가 포함되어 있지 않습니다"가 표시되나요? %}
환경 설정 센터는 구독 취소 링크로 간주되지 않습니다. 이메일 수신자는 CAN-SPAM 준수를 유지하기 위해 모든 상업적 이메일에서 구독 취소할 수 있는 옵션이 있어야 합니다.
{% enddetails %}


{% details 제가 이전 이메일 캠페인과 캔버스를 편집하여 원클릭 구독 취소 설정을 적용해야 하나요? %}
메시지 수준의 원클릭 목록 탈퇴 설정에 대한 사용 사례가 없는 경우, **이메일 환경 설정**에서 설정이 켜져 있는 한 필요한 조치는 없습니다. Braze는 모든 발신 마케팅 및 프로모션 메시지에 원클릭 구독 취소 헤더를 자동으로 추가합니다. 그러나 메시지 수준별로 원클릭 구독 취소 동작을 구성해야 하는 경우, 이전 캠페인 및 캔버스 단계를 이메일에 따라 업데이트해야 합니다.
{% enddetails %}

{% details 원본 메시지 또는 원시 데이터에서 list-unsubscribe 및 원클릭 구독 취소 헤더를 볼 수 있지만, 왜 Gmail 또는 Yahoo에서 구독 취소 버튼이 보이지 않나요? %}
Gmail과 Yahoo는 궁극적으로 목록 구독 취소 또는 원클릭 구독 취소 헤더를 표시할지 여부를 결정합니다. 새로운 발신자 또는 발송자 평판이 낮은 발신자의 경우, 이는 때때로 구독 취소 버튼이 표시되지 않게 할 수 있습니다.
{% enddetails %}

{% details 커스텀 원-클릭 탈퇴 헤더가 Liquid를 지원하나요? %}
네, Liquid 및 조건 로직이 지원되어 헤더에 동적 원클릭 구독 취소 URL을 허용합니다.
{% enddetails %}

{% alert tip %}
조건 로직을 추가하는 경우 Braze는 이러한 공백을 제거하지 않으므로 URL에 공백을 추가하는 출력 값을 피하십시오.
{% endalert %}

### 메시지 수준 원클릭 목록 구독 취소

{% details 이메일 헤더를 수동으로 추가하고 이메일 구독 취소 헤더가 켜져 있으면 예상되는 동작은 무엇입니까? %}
이메일 헤더는 한 번의 클릭으로 list-unsubscribe를 위해 추가되며, 이 캠페인의 모든 향후 발송에 적용됩니다.
{% enddetails %}

{% details 구독 그룹이 메시지 배리언트 간에 일치해야 시작할 수 있는 이유는 무엇입니까? %}
캠페인에 A/B 테스트를 사용하는 경우, Braze는 사용자에게 변형 중 하나를 무작위로 보냅니다. 동일한 캠페인에 두 개의 다른 구독 그룹이 설정된 경우(배리언트 A가 구독 그룹 A에 설정되고, 배리언트 B가 구독 그룹 B에 설정된 경우), 구독 그룹 B에만 가입한 사용자가 배리언트 B를 받을 것이라고 보장할 수 없습니다. 사용자가 이미 선택 해제된 구독 그룹에서 구독을 취소하는 시나리오가 있을 수 있습니다.
{% enddetails %}

{% details 이메일 구독 취소 헤더 설정이 이메일 환경설정에서 꺼져 있지만, 내 캠페인의 발송 정보에서는 원클릭 list-unsubscribe 설정이 "워크스페이스 기본값 사용"으로 설정되어 있습니다. 이것은 버그인가요? %}
아니요. 워크스페이스 설정이 꺼져 있고 메시지 설정이 **워크스페이스 기본값 사용**으로 설정된 경우, Braze는 **이메일 환경설정**에 구성된 내용을 따릅니다. 이는 캠페인에 대해 원클릭 구독 취소 헤더를 추가하지 않음을 의미합니다.
{% enddetails %}

{% details 구독 그룹이 보관되면 어떻게 되나요? 이것이 이메일에서 보내는 원클릭 구독 취소를 깨뜨릴까요? %}
**발송 정보**에서 원클릭에 참조된 구독 그룹이 보관된 경우에도 Braze는 원클릭에서 구독 취소를 계속 처리합니다. 구독 그룹은 더 이상 대시보드(세그먼트 필터, 고객 프로필 및 유사한 영역)에 표시되지 않습니다.
{% enddetails %}

{% details 이메일 템플릿에 원클릭 구독 취소 설정이 가능합니까? %}
아니요, 현재 이메일 템플릿에 대해 이를 추가할 계획은 없습니다. 이러한 템플릿은 발송 도메인에 할당되지 않습니다. 이 이메일 템플릿 기능에 관심이 있다면, [제품 피드백]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)을 제출하세요.
{% enddetails %}

{% details 이 기능은 클릭 한 번으로 구독 취소할 수 있는 URL이 커스텀 옵션에 추가되었는지 확인합니까? %}
아니요, 우리는 Braze 대시보드에서 링크를 확인하거나 검증하지 않습니다. 출시 전에 URL을 제대로 테스트하십시오.
{% enddetails %}


[0]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[6]:https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[13]: {% image_buster /assets/img/open_pixel.png %}
