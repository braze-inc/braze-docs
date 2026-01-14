---
nav_title: 이메일 기본 설정
article_title: 이메일 기본 설정
page_type: reference
page_order: 14
description: "이 참조 문서에서는 Braze 대시보드의 이메일 기본 설정, 발송 구성, 열기 추적 픽셀, 구독 페이지 및 바닥글 등을 다룹니다."
tool: Dashboard
channel: email

---

# 이메일 기본 설정

> 이메일 기본 설정에서는 사용자 정의 바닥글, 사용자 정의 수신 및 수신 거부 페이지 등과 같은 특정 발신 이메일 설정을 설정할 수 있습니다. 이러한 옵션을 발신 이메일에 포함하면 사용자에게 유연하고 일관된 경험을 제공합니다.

**이메일 기본 설정**은 대시보드의 **설정** 아래에서 찾을 수 있습니다.

## 발송 구성

**발송 구성** 섹션 아래의 이메일 설정은 이메일 캠페인에 포함되는 세부 정보를 결정합니다. 특히, 이러한 설정은 사용자가 Braze로부터 이메일을 받을 때 보는 내용과 관련이 있습니다.

### 발신 이메일 설정

이메일 설정을 구성할 때, 발신 이메일 설정은 Braze가 사용자에게 이메일을 보낼 때 사용되는 이름과 이메일 주소를 식별합니다.

{% tabs local %}
{% tab Display Name Address %}

이 섹션에서는 Braze가 사용자에게 이메일을 보낼 때 사용할 수 있는 이름과 이메일 주소를 추가할 수 있습니다. 표시 이름과 이메일 주소는 이메일 캠페인을 작성할 때 **발송 정보 편집** 옵션에서 사용할 수 있습니다. 발신 이메일 설정에 대한 업데이트는 기존 발송에 소급하여 영향을 미치지 않습니다.

\!["발신 이메일 설정" 섹션에는 다양한 표시 이름과 도메인에 대한 필드가 있습니다.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Liquid로 개인화하기

또한 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)을 **보내는 표시 이름** 및 **로컬 부분** 필드에서 사용하여 사용자 정의 속성을 기반으로 발송 이메일을 동적으로 템플릿화할 수 있습니다. 예를 들어, 서로 다른 브랜드나 지역에서 발송하기 위해 조건부 논리를 사용할 수 있습니다:

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

이 섹션에 이메일 주소를 추가하면 이메일 캠페인의 회신 주소로 선택할 수 있습니다. 이메일 주소를 기본 주소로 만들려면 **기본 설정**을 선택할 수 있습니다. 이 이메일 주소는 이메일 캠페인을 작성할 때 **발송 정보 편집** 옵션에서 사용할 수 있습니다.

\!["회신 주소" 섹션으로 여러 회신 주소를 입력할 수 있는 필드가 있습니다.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Liquid로 개인화하기

또한 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)을 사용하여 **회신 주소** 필드에서 사용자 정의 속성에 따라 동적으로 회신 주소를 템플릿화할 수 있습니다. 예를 들어, 조건 논리를 사용하여 다른 지역이나 부서로 회신을 보낼 수 있습니다:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
us-support@company.com
{% elsif {{custom_attribute.${region}}} == 'EU' %}
eu-support@company.com
{% else %}
global-support@company.com
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

이 섹션에서는 Braze에서 발송된 아웃바운드 이메일 메시지에 추가할 수 있는 BCC 주소를 추가하고 관리할 수 있습니다. BCC 주소는 SendGrid 및 SparkPost에서만 사용할 수 있습니다. BCC 주소의 대안으로, 사용자에게 보낸 메시지의 사본을 보관하거나 준수 목적으로 [메시징 아카이빙]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/)을 사용하는 것을 권장합니다.

이메일 메시지에 BCC 주소를 추가하면 사용자가 받는 메시지의 동일한 사본이 BCC 수신함으로 전송됩니다. 이는 준수 요구 사항이나 고객 지원 문제를 위해 사용자에게 보낸 메시지의 사본을 보관하는 유용한 도구입니다. BCC 이메일은 이메일 보고서 및 분석에 포함되지 않습니다.

{% alert important %}
캠페인이나 캔버스에 BCC 주소를 추가하면 Braze가 사용자에게 하나의 메시지를 보내고 BCC 주소로 하나의 메시지를 보내기 때문에 청구 가능한 이메일이 두 배로 증가합니다.
{% endalert %}

\![이메일 설정 탭의 BCC 주소 섹션.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

주소를 추가한 후, 캠페인 또는 캔버스 단계에서 이메일을 작성할 때 선택할 수 있도록 주소가 제공됩니다. 새 이메일 캠페인이나 캔버스 구성 요소를 시작할 때 기본적으로 선택되도록 하려면 주소 옆의 **기본 설정**을 선택하십시오. 메시지 수준에서 이를 무시하려면 메시지를 설정할 때 **BCC 없음**을 선택할 수 있습니다.

Braze에서 발송되는 모든 이메일 메시지에 BCC 주소가 포함되도록 하려면 **모든 이메일 캠페인에 BCC 주소 필요** 토글을 선택할 수 있습니다. 이렇게 하면 기본 주소를 선택해야 하며, 이는 새로운 이메일 캠페인이나 캔버스 단계에서 자동으로 선택됩니다. 기본 주소는 또한 REST API를 통해 트리거된 모든 메시지에 자동으로 추가됩니다. 기존 API 요청에 주소를 포함하도록 변경할 필요가 없습니다.

{% endtab %}
{% endtabs %}

## 추적 픽셀 열기

[![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

이메일 열기 추적 픽셀은 이메일 HTML에 자동으로 삽입되는 보이지 않는 1 x 1 px 이미지입니다. 이 픽셀은 Braze가 최종 사용자가 이메일을 열었는지 감지하는 데 도움을 줍니다. 이메일 열기 정보는 매우 유용할 수 있으며, 사용자가 해당 열기 비율을 이해하여 효과적인 마케팅 전략을 결정하는 데 도움을 줍니다.

### 추적 픽셀 배치

Braze의 기본 동작은 추적 픽셀을 이메일 하단에 추가하는 것입니다. 대부분의 사용자에게 이것은 픽셀을 배치하기에 이상적인 장소입니다. 픽셀이 가능한 한 시각적 변화를 최소화하도록 스타일이 지정되어 있지만, 의도하지 않은 시각적 변화는 이메일 하단에서 가장 덜 눈에 띄게 됩니다. 이것은 SendGrid 및 SparkPost와 같은 이메일 제공자의 기본값이기도 합니다.

### 추적 픽셀 위치 변경

Braze는 현재 ESP의 기본 열기 추적 픽셀 위치(이메일의 `<body>` 마지막 태그)를 재정의하여 `<body>` 첫 번째 태그로 이동하는 것을 지원합니다.
  
\!["Open Tracking Pixel" 섹션에서 SendGrid, SparkPost 또는 Amazon SES로 이동할 옵션.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

위치를 변경하려면:

1. Braze에서 **Settings** > **Email Preferences**로 이동합니다.
2. 다음 옵션 중에서 선택하십시오: **SendGrid로 이동**, **SparkPost로 이동**, 또는 **Amazon SES로 이동**
3. **저장**을 선택하십시오.

저장되면 Braze는 모든 HTML 이메일의 상단에 열기 추적 픽셀을 배치하기 위해 ESP에 특별 지침을 보냅니다.
  
{% alert important %}
SSL 활성화는 추적 픽셀의 URL을 HTTP 대신 HTTPS로 감쌉니다. SSL이 잘못 구성된 경우 추적 픽셀의 효율성에 영향을 미칠 수 있습니다.
{% endalert %}

## 리스트-구독 해지 헤더 {#list-unsubscribe}

{% alert note %}
2024년 2월 15일부터 새로운 회사는 기본적으로 리스트-구독 해지 헤더(원클릭 구독 해지 포함)가 활성화됩니다.
{% endalert %}

리스트-구독 해지 헤더를 사용하면 수신자가 메일박스 UI 내에서 **구독 해지** 버튼을 표시하여 마케팅 이메일에서 쉽게 구독을 해지할 수 있습니다.

\![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

수신자가 **구독 해지**를 클릭하면 메일박스 제공자가 이메일 헤더에 정의된 목적지로 구독 해지 요청을 보냅니다.

리스트-구독 해지 활성화는 배달 가능성의 모범 사례이며 일부 주요 메일박스 제공자의 요구 사항입니다. 이는 최종 사용자가 이메일 클라이언트에서 스팸 버튼을 누르는 대신 원하지 않는 메시지에서 안전하게 자신을 제거하도록 장려합니다. 후자는 발송 평판과 이메일 배달 가능성에 해롭습니다.

### 메일박스 제공자 지원

다음 표는 "mailto:" 헤더, 리스트-구독 해지 URL 및 원클릭 구독 해지([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대한 메일박스 제공자 지원을 요약합니다.

| 리스트-구독 해지 헤더 | 메일투: 헤더 | 리스트-구독 해지 URL | 원클릭 구독 해지 (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | 지원됨* | 지원됨 | 지원됨 |
| Gmail 모바일 | 지원되지 않음 | 지원되지 않음 | 지원되지 않음 |
| 애플 메일 | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| Outlook.com | 지원됨 | 지원되지 않음 | 지원되지 않음 |
| 야후! 메일 | 지원됨* | 지원되지 않음 | 지원됨 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*야후와 지메일은 결국 "mailto:" 헤더를 사용 중단하고 원클릭만 지원할 것입니다._

헤더 표시 여부는 궁극적으로 메일박스 제공업체에 의해 결정됩니다. 지메일에서 수신자의 원본(텍스트) 이메일에 list-unsubscribe 헤더가 포함되어 있는지 확인하려면 다음을 수행하십시오:

1. 이메일에서 **원본 보기**를 선택하십시오. 이것은 이메일의 원본 버전과 그 헤더가 있는 새 탭을 엽니다.
2. "List-Unsubscribe"를 검색하십시오.

헤더가 이메일의 원본 버전에 있지만 표시되지 않는 경우, 메일박스 제공업체가 구독 취소 옵션을 표시하지 않기로 결정한 것이며, 이는 메일박스 제공업체가 헤더를 표시하지 않는 이유에 대한 추가 통찰력이 없음을 의미합니다. list-unsubscribe 헤더를 보는 것은 궁극적으로 평판 기반입니다. 대부분의 경우, 메일박스 제공업체와의 발신자 평판이 좋을수록 list-unsubscribe 헤더가 나타날 가능성이 높습니다.

### 작업 공간의 이메일 구독 취소 헤더

\![어떤 사용자에게 보낼지에 대한 "구독 중이거나 선택한 사용자"를 선택합니다.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

이메일 구독 취소 헤더 기능이 켜지면 이 설정은 회사 수준이 아닌 전체 작업 공간에 적용됩니다. 이것은 구독 중이거나 선택한 사용자 또는 캠페인 및 캔버스 빌더의 **대상 청중** 단계에서 선택한 사용자에게 보내도록 설정된 캠페인 및 캔버스에 추가됩니다.

"작업 공간 기본값"을 사용할 때, Braze는 "구독 취소된 사용자를 포함하여 모든 사용자에게 보내기"로 구성된 거래로 간주되는 캠페인에 대해 원클릭 구독 취소 헤더를 추가하지 않습니다. 구독 취소된 사용자에게 보낼 때 원클릭 구독 취소 헤더를 추가하려면 메시지 수준의 원클릭 구독 취소 설정에서 **모든 이메일에서 전역적으로 구독 취소**를 선택할 수 있습니다.

### 기본 list-unsubscribe 헤더

{% alert important %}
지메일은 발신자가 2024년 6월 1일부터 모든 발신 상업적, 홍보 메시지에 대해 원클릭 구독 취소를 구현할 것을 의도하고 있습니다. 자세한 내용은 [Gmail의 발신자 가이드라인](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) 및 [Gmail의 이메일 발신자 가이드라인 FAQ](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages)를 참조하십시오. Yahoo는 2024년 초 업데이트 요구 사항에 대한 일정을 발표했습니다. 자세한 내용은 [더 안전하고, 스팸은 적게: 더 나은 경험을 위한 이메일 표준 시행](https://blog.postmaster.yahooinc.com/)입니다.
{% endalert %}

Braze의 구독 취소 기능을 사용하여 구독 취소를 직접 처리하려면, **구독된 사용자 또는 선택된 사용자에게 발송되는 이메일에 대해 원클릭 목록-구독 취소(메일투 및 HTTP) 이메일 헤더 포함**를 선택하고, **Braze 기본값**을 표준 Braze URL 및 메일투로 선택하십시오. 

\![구독된 사용자 또는 선택된 사용자에게 발송되는 이메일에 대한 목록-구독 취소 헤더를 자동으로 포함하는 옵션.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze는 다음 목록-구독 취소 헤더 버전을 지원합니다:

| 목록-구독 취소 버전 | 설명 | 
| ----- | --- |
| 원클릭 (RFC 8058) | 수신자가 단일 클릭으로 이메일에서 선택 해제할 수 있는 간단한 방법을 제공합니다. 이는 대량 발신자에 대한 Yahoo 및 Gmail의 요구 사항입니다. |
| 목록-구독 취소 URL 또는 HTTPS | 수신자에게 수신자가 구독 취소할 수 있는 웹 페이지로 안내하는 링크를 제공합니다. |
| 메일투 | 수신자가 브랜드에 구독 취소 요청 메시지를 보낼 이메일 주소를 지정합니다. <br><br> _메일투 목록-구독 취소 요청을 처리하려면, 이러한 구독 취소 요청에는 구독 취소하는 최종 사용자에 대해 Braze에 저장된 이메일 주소가 포함되어야 합니다. 이는 최종 사용자가 구독 취소하는 이메일의 "보낸 주소", 인코딩된 제목 또는 최종 사용자가 구독 취소하는 이메일에서 받은 인코딩된 본문에 의해 제공될 수 있습니다. 매우 제한된 경우에 일부 수신함 제공자는 [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) 프로토콜을 준수하지 않아 이메일 주소가 제대로 전달되지 않을 수 있습니다. 이로 인해 Braze에서 구독 취소 요청을 처리할 수 없게 될 수 있습니다._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze가 위의 방법 중 하나를 통해 사용자로부터 목록-구독 취소 요청을 받으면, 이 사용자의 전역 이메일 구독 상태가 구독 취소로 설정됩니다. 일치하는 항목이 없으면 Braze는 이 요청을 처리하지 않습니다.

### 원클릭 구독 취소

목록-구독 취소 헤더([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))에 대한 원클릭 구독 취소를 사용하면 수신자가 이메일을 쉽게 선택 해제할 수 있는 방법을 제공합니다.

### 메시지 수준 원클릭 목록-구독 취소

메시지 수준 원클릭 목록-구독 취소 설정은 작업 공간에 대해 설정된 이메일 구독 취소 헤더 기능을 무시합니다. 다음 용도에 대해 캠페인 또는 캔버스 단계별로 원클릭 구독 취소 동작을 적용하십시오:

- 하나의 작업 공간 내에서 여러 브랜드/목록을 지원하기 위해 특정 구독 그룹에 Braze 원클릭 구독 취소를 추가하십시오.
- 기본 Braze 구독 취소 또는 사용자 지정 URL 간 전환
- 사용자 지정 원클릭 구독 취소 URL을 추가하십시오.
- 이 메시지에서 원클릭 구독 취소 생략

{% alert note %}
메시지 수준 원클릭 목록-구독 취소 설정은 드래그 앤 드롭 편집기와 업데이트된 HTML 편집기를 사용할 때만 사용할 수 있습니다. 이전 HTML 편집기를 사용 중이라면, 이 기능을 사용하기 위해 업데이트된 HTML 편집기로 전환하십시오.
{% endalert %}

이메일 편집기에서 **전송 설정** > **전송 정보**로 이동하십시오. 다음 옵션 중에서 선택하십시오:

- **작업 공간 기본값 사용**: **이메일 기본 설정**에서 설정된 **이메일 구독 취소 헤더** 설정을 사용합니다. 이 설정에 대한 모든 변경 사항은 모든 메시지에 적용됩니다.
- **모든 이메일에서 전역적으로 구독 취소**: Braze 기본 원클릭 구독 취소 헤더를 사용합니다. 구독 취소 버튼을 클릭한 사용자는 전 세계 이메일 구독 상태가 "구독 취소됨"으로 설정됩니다.
- **특정 구독 그룹에서 구독 취소**: 지정된 구독 그룹을 사용합니다. 구독 취소 버튼을 클릭한 사용자는 선택한 구독 그룹에서 구독 취소됩니다.
    - 구독 그룹을 선택할 때, 이 특정 그룹에 구독된 사용자만 타겟팅하기 위해 **구독 그룹** 필터를 **대상 청중**에 추가하세요. 원클릭 구독 취소를 위해 선택된 구독 그룹은 타겟팅하는 구독 그룹과 일치해야 합니다. 구독 그룹에 불일치가 있을 경우, 이미 구독 취소된 구독 그룹에서 구독 취소하려는 사용자에게 발송할 위험이 있습니다.

{% alert important %}
**특정 구독 그룹에서 구독 취소** 설정은 원클릭 목록-구독 취소 헤더에만 적용됩니다. 이 옵션을 선택할 때 mailto 목록-구독 취소 헤더는 영향을 받지 않습니다. 이는 이 방법으로 구독 취소하는 수신자가 특정 구독 그룹에서 구독 취소하는 것이 아니라 전 세계적으로 구독 취소를 기록한다는 것을 의미합니다. 전 세계적으로 구독 취소하는 사용자에게서 mailto 목록-구독 취소 헤더를 제외하려면 이 설정을 선택할 때 [지원]({{site.baseurl}}/support_contact/)에 문의하세요.
{% endalert %}

- **사용자 정의:** 구독 취소를 직접 처리할 수 있도록 사용자 정의 원클릭 구독 취소 URL을 추가합니다.
- **구독 취소 제외**

{% alert important %}
원클릭 구독 취소 또는 기타 구독 취소 메커니즘을 제외하는 것은 비즈니스 메시지, 예를 들어 비밀번호 재설정, 영수증 및 확인 이메일에 대해서만 수행해야 합니다.
{% endalert %}

이 설정을 조정하면 이 이메일의 원클릭 목록 구독 취소에 대한 기본 동작이 무시됩니다.

\![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### 요구 사항

자신의 사용자 정의 구독 취소 기능을 사용하여 이메일을 보내는 경우, 설정한 원클릭 구독 취소 URL이 RFC 8058에 따라 적합한지 확인하기 위해 다음 요구 사항을 충족해야 합니다:

* URL은 구독 취소 POST 요청을 처리할 수 있어야 합니다.
* URL은 `https://`로 시작해야 합니다.
* URL은 HTTPS 리디렉션이나 본문을 반환하지 않아야 합니다. 랜딩 페이지나 다른 유형의 웹 페이지로 가는 원클릭 구독 취소 링크는 RFC 8058을 준수하지 않습니다.
* POST 요청은 쿠키를 설정해서는 안 됩니다.

자신이 구성한 원클릭 구독 취소 엔드포인트와 선택적 "mailto:"를 추가하려면 **사용자 정의 목록-구독 취소 헤더**를 선택하십시오. Braze는 원클릭 구독 취소 HTTP가 대량 발송자에 대한 Yahoo 및 Gmail의 요구 사항이기 때문에 사용자 정의 목록-구독 취소 헤더를 지원하기 위해 URL 입력이 필요합니다.

\![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## 이메일 제목 줄 추가

토글을 사용하여 테스트 및 시드 이메일 제목 줄에 "[TEST]" 및 "[SEED]"를 포함하십시오. 이것은 테스트로 발송된 이메일 캠페인을 식별하는 데 도움이 될 수 있습니다.

\![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## 기본적으로 새 이메일에 인라인 CSS

CSS 인라인화는 이메일 및 새 이메일에 대한 CSS 스타일을 자동으로 인라인화하는 기술입니다. 일부 이메일 클라이언트의 경우, 이는 이메일 렌더링 방식을 개선할 수 있습니다.

이 설정을 변경해도 기존 이메일 메시지나 템플릿에는 영향을 미치지 않습니다. 메시지나 템플릿을 작성하는 동안 언제든지 이 기본값을 재정의할 수 있습니다. 자세한 내용은 [CSS 인라인화]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)를 참조하십시오.

## 사용자의 이메일이 변경될 때 재구독

사용자가 이메일 주소를 변경할 때 자동으로 재구독할 수 있습니다. 예를 들어, 이전에 구독 취소된 작업 공간 사용자가 Braze의 구독 취소 목록에 없는 이메일 주소로 변경하면 자동으로 재구독됩니다.

\![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## 구독 페이지 및 바닥글

{% tabs local %}
{% tab Custom Footer %}

상업용 이메일의 경우, [CAN-SPAM 법](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003)은 모든 상업용 이메일에 구독 취소 옵션을 포함할 것을 요구합니다. 사용자 정의 바닥글 설정을 통해 CAN-SPAM 규정을 준수하면서 이메일 옵트아웃 바닥글을 사용자 정의할 수 있습니다. 규정을 준수하려면 이 작업 공간의 캠페인에 발송되는 모든 이메일에 사용자 정의 바닥글을 추가해야 합니다.

이메일 메시징을 위한 사용자 정의 바닥글을 만들 때 다음 요구 사항을 유의하십시오:
- 구독 취소 URL과 실제 우편 주소를 포함해야 합니다.
- 100 KB 미만이어야 합니다.

\![]({% image_buster /assets/img/email_settings/custom_footer.png %})

사용자 정의 바닥글 Liquid 템플릿에 대해 더 알아보려면 [사용자 정의 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions)에 대한 문서를 확인하세요.

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze를 사용하면 자신의 HTML로 **사용자 정의 구독 취소 페이지**를 설정할 수 있습니다. 이 페이지는 사용자가 이메일 하단에서 구독 취소를 선택한 후에 나타납니다. 이 페이지는 750 KB 미만이어야 합니다. 

\![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

이메일 목록 관리에 대한 모범 사례에 대해 [이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 더 알아보세요.

{% endtab %}
{% tab Custom Opt-In Page %}

자신의 HTML을 사용하여 사용자 정의 옵트인 페이지를 만들 수 있습니다. 이것을 이메일에 포함하면 사용자 생애 주기 전반에 걸쳐 브랜드와 메시지가 일관되게 유지되도록 하는 데 특히 유용할 수 있습니다. 이 페이지는 750 KB 미만이어야 합니다. 

\![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

이메일 목록 관리에 대한 모범 사례에 대해 [이메일 구독 관리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses)에서 더 알아보세요.

{% endtab %}
{% endtabs %}

## 자주 묻는 질문

### 원클릭 구독 취소

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
아니요, 이는 RFC 8058을 준수하지 않으며, 따라서 Yahoo 및 Gmail의 원클릭 구독 취소 요구 사항을 준수하지 않습니다.
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
선호 센터는 구독 취소 링크로 간주되지 않습니다. 이메일 수신자는 CAN-SPAM 규정을 준수하기 위해 모든 상업적 이메일에서 구독 취소 옵션을 가져야 합니다.
{% enddetails %}

{% details Will I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
메시지 수준의 원클릭 목록 구독 취소 설정에 대한 사용 사례가 없다면, **이메일 기본 설정**에서 설정이 켜져 있는 한 필수 조치는 없습니다. Braze는 모든 발송되는 마케팅 및 프로모션 메시지에 원클릭 구독 취소 헤더를 자동으로 추가합니다. 그러나 메시지 수준에서 원클릭 구독 취소 동작을 구성해야 하는 경우, 이전 캠페인 및 캔버스 단계를 이메일에 맞게 업데이트해야 합니다.
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
Gmail과 Yahoo는 궁극적으로 목록 구독 취소 또는 원클릭 구독 취소 헤더를 표시할지 여부를 결정합니다. 새 발신자 또는 발신자 평판이 낮은 경우, 때때로 구독 취소 버튼이 표시되지 않을 수 있습니다.
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
예, Liquid 및 조건부 로직이 지원되어 헤더에 대한 동적 원클릭 구독 취소 URL을 허용합니다.
{% enddetails %}

{% alert tip %}
조건부 로직을 추가하는 경우, Braze가 이러한 공백을 제거하지 않으므로 URL에 공백을 추가하는 출력 값을 피하십시오.
{% endalert %}

### 메시지 수준 원클릭 목록-구독 취소

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
원클릭 목록 구독 취소를 위해 추가된 이메일 헤더는 이 캠페인의 모든 향후 발송에 적용됩니다.
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
A/B 테스트가 있는 캠페인의 경우, Braze는 사용자에게 무작위로 변형 중 하나를 보냅니다. 같은 캠페인에 대해 두 개의 서로 다른 구독 그룹이 설정되어 있는 경우(변형 A는 구독 그룹 A에 설정되고, 변형 B는 구독 그룹 B에 설정됨), 구독 그룹 B에만 가입된 사용자가 변형 B를 받을 것이라고 보장할 수 없습니다. 사용자가 이미 선택 해제한 구독 그룹에서 구독 취소를 하는 시나리오가 있을 수 있습니다.
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
아니요. 작업 공간 설정이 꺼져 있고 메시지 설정이 **작업 공간 기본값 사용**로 설정된 경우, Braze는 **이메일 기본 설정**에 구성된 내용을 따릅니다. 이는 캠페인에 대해 원클릭 구독 취소 헤더를 추가하지 않음을 의미합니다.
{% enddetails %}

{% details What happens if a subscription group is archived? Will this break the one-click unsubscribe on emails sent? %}
원클릭을 위한 **발송 정보**에서 참조된 구독 그룹이 보관된 경우, Braze는 여전히 원클릭에서 구독 취소를 처리합니다. 구독 그룹은 대시보드(세그먼트 필터, 사용자 프로필 및 유사한 영역)에서 더 이상 표시되지 않습니다.
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
아니요, 현재 이메일 템플릿에 대해 이를 추가할 계획이 없습니다. 이러한 템플릿은 발송 도메인에 할당되지 않기 때문입니다. 이메일 템플릿에 대한 이 기능에 관심이 있으시면 [제품 피드백]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)을 제출하십시오.
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
아니요, 우리는 Braze 대시보드에서 링크를 확인하거나 검증하지 않습니다. 출시 전에 URL을 제대로 테스트해야 합니다.
{% enddetails %}


