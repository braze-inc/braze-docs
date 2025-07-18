---
nav_title: WhatsApp 메시지 생성
article_title: WhatsApp 메시지 생성
page_order: 4
description: "이 참조 문서에서는 WhatsApp 메시지를 작성하고 만드는 데 필요한 단계를 다룹니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# 메시지 만들기

> WhatsApp 캠페인은 고객에게 직접 도달하고 프로그래밍 방식으로 대화하는 데 매우 유용합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인적인 경험을 만들고 브랜드에 대한 사용자 경험을 방해하지 않는 환경을 조성하고 향상시킬 수 있습니다. 

## 전제 조건

WhatsApp 메시지를 생성하기 전에 [WhatsApp 개요]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)를 검토하고 완료해야 합니다:
  - 정책, 한도 및 콘텐츠 규칙을 인정하십시오
  - WhatsApp 연결 설정
  - 메타에서 메시지에 사용할 초기 템플릿을 구축합니다

## 메시지 생성

### 1단계: 메시지를 작성할 위치 선택

{% alert note %}
WhatsApp은 각 언어에 대해 다른 [메시지 템플릿](#template-messages)을 생성합니다. 각 언어에 대한 캠페인을 생성하여 사용자에게 올바른 템플릿을 제공하기 위해 세분화를 사용하거나, 캔버스를 사용하세요.
{% endalert %}

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab 캠페인 %}

**단계:**

1. **캠페인** 페이지로 이동하여 <i class="fas fa-plus"></i> **캠페인 생성**을 클릭하십시오.
2. **WhatsApp**을 선택하거나, 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널 캠페인**을 선택하세요.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) as needed.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), you can filter by particular tags.
5. 캠페인에 필요한 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.

{% alert tip %}
캠페인에 있는 모든 메시지가 비슷하거나 동일한 내용을 가지고 있다면, 추가적인 변형을 추가하기 전에 메시지를 작성하십시오. 그런 다음 ** 배리언트 **추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab 캔버스 %}

**단계:**

1. 캔버스 작성기를 사용하여 [캔버스를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 스케줄]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)을 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 메시지가 전송된 후 지연 시간이 지나면 오디언스 옵션이 확인됩니다.
5. [진행 동작]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)을 선택하세요.
6. 연결할 메시징 채널을 선택하세요.

{% alert tip %}
인바운드 WhatsApp 메시지에 의해 액션 기반 캔버스가 트리거되면, 다음 행동 경로까지 모든 캔버스 단계에서 WhatsApp 속성을 참조할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2단계: WhatsApp 메시지를 작성하세요

WhatsApp [템플릿 메시지](#template-messages) 또는 응답 메시지를 생성할지 선택하세요, 사용 사례에 따라 다릅니다. 모든 비즈니스 시작 대화는 승인된 템플릿에서 시작해야 하며, 응답 메시지는 사용자로부터 24시간 이내에 수신된 메시지에 대한 응답으로 사용할 수 있습니다.

![메시지 변형 섹션에서는 구독 그룹과 두 가지 메시지 유형 중 하나를 선택할 수 있습니다: WhatsApp 템플릿 메시지 및 응답 메시지.][5]{: style="max-width:80%;"}

#### 템플릿 메시지

[승인된 WhatsApp 템플릿 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
)를 사용하여 WhatsApp에서 사용자와 대화를 시작할 수 있습니다. 이 메시지는 콘텐츠 승인을 위해 사전에 WhatsApp에 제출되며, 승인은 최대 24시간이 소요될 수 있습니다. 복사본에 대한 모든 편집은 편집하여 WhatsApp에 다시 제출해야 합니다.

비활성화된 텍스트 필드(회색으로 강조 표시됨)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집하고 다시 승인받아야 합니다.

##### 언어

각 템플릿에는 할당된 언어가 있으므로 사용자 매칭을 올바르게 설정하려면 각 언어에 대해 캠페인 또는 캔버스 단계를 생성해야 합니다. 예를 들어, 인도네시아어와 영어로 지정된 템플릿을 사용하는 캔버스를 만드는 경우, 인도네시아어 템플릿을 위한 캔버스 단계를 만들고 영어 템플릿을 위한 캔버스 단계를 만들어야 합니다.

![템플릿 목록에는 메시지 미리보기, 할당된 언어 및 승인 상태가 포함됩니다.][8]{: style="max-width:80%;"}

If you're adding copy in a language that is written right-to-left, note that the final appearance of right-to-left messages depends largely on how service providers render them. For best practices on crafting right-to-left messages that display as accurately as possible, refer to [Creating right-to-left messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

##### 변수

Meta Business 관리자에서 WhatsApp 템플릿을 만들 때 변수를 추가한 경우, 해당 변수는 메시지 작성기에 빈 공간으로 표시됩니다. 이 빈칸을 Liquid 또는 일반 텍스트로 바꾸세요. 일반 텍스트를 사용하려면, 이중 중괄호로 둘러싸인 "여기에 텍스트" 형식을 사용하세요. 템플릿을 만들 때 이미지를 포함하기로 선택한 경우, 미디어 라이브러리에서 이미지를 업로드하거나 추가하거나 이미지 URL을 참조하여 이미지를 추가할 수 있습니다.

비활성화된 텍스트 필드(회색 강조 표시)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집하고 다시 승인받아야 합니다.

{% alert tip %}
{% raw %}
Liquid을 사용하려는 경우 선택한 개인화를 위한 기본값을 포함해야 하므로 수신자의 고객 프로필이 불완전한 경우 메시지를 받지 않게 됩니다. 누락된 Liquid 변수가 있는 메시지는 WhatsApp에 의해 전송되지 않습니다.
{% endraw %}
{% endalert %}

![개인화 추가 도구는 속성 "first_name"과 기본값 "you"를 사용합니다.][2]{: style="max-width:80%;"}

#### 동적 링크 

클릭 유도 URL에는 변수가 포함될 수 있지만, Meta는 URL의 끝에 `{% raw %}https://example.com/{{variable}}{% endraw %}`와 같이 변수가 있어야 한다고 요구합니다. 그런 다음 변수는 Braze에서 Liquid로 대체될 수 있습니다. 링크는 템플릿의 일부로 본문 텍스트로도 포함될 수 있습니다. 이 시점에서는 이 링크들 중 어느 것도 단축할 수 없습니다. 

#### 응답 메시지

사용자에게서 들어오는 메시지에 응답 메시지를 사용할 수 있습니다. 이 메시지는 작성 경험 중에 Braze에서 앱 내에서 작성되며 언제든지 편집할 수 있습니다. Liquid을 사용하여 응답 메시지 언어를 적절한 사용자에게 맞출 수 있습니다.

사용할 수 있는 세 가지 응답 메시지 레이아웃이 있습니다:
- 빠른 회신
- 메시지 입력
- 미디어 메시지

![새 사용자에게 할인 코드를 제공하는 환영 메시지에 대한 응답 메시지 작성기.][6]{: style="max-width:80%;"}

### 3단계: 메시지 미리보기 및 테스트

Braze는 메시지를 보내기 전에 항상 미리보기 및 테스트를 권장합니다. **테스트** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트 WhatsApp 메시지를 보내거나 Braze에서 사용자로 메시지를 직접 미리보기 합니다.

![기존 사용자 Suzanne에게 보낼 미리보기 메시지입니다.][3]{: style="max-width:80%;"}

{% alert note %}
응답 메시지(테스트 메시지 포함)를 보내려면 대화 창이 필요합니다. 대화 창을 시작하려면, 이 메시지에 사용 중인 구독 그룹과 연결된 전화번호로 WhatsApp 메시지를 보내세요. 연관된 전화번호는 **테스트** 탭의 경고에 나열되어 있습니다.
{% endalert %}

![경고: "테스트하려면 먼저 WhatsApp 메시지를 +1 631-202-0907로 보내 대화 창을 여세요." 그런 다음, 테스트 사용자에게 응답 메시지를 보내십시오."][7]{: style="max-width:80%;"}

### 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab 캠페인 %}

다음으로, 나머지 캠페인을 구축하십시오. WhatsApp 메시지를 구축하기 위해 도구를 가장 효과적으로 사용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 전달 일정 또는 트리거를 선택하십시오

WhatsApp 메시지는 예약된 시간, 작업 또는 API 트리거를 기반으로 전달될 수 있습니다. 자세한 내용은 [캠페인 일정 잡기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)을 참조하세요.

액션 기반 전달의 경우 캠페인의 기간과 [조용한 시간을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 받을 수 있도록 [다시 자격]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)을 얻을 수 있도록 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수 있습니다.

#### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 [사용자를 타겟팅하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) 오디언스의 범위를 좁혀야 합니다. 이미 구독 그룹을 선택했어야 하는데, 이 그룹은 사용자와 소통하고자 하는 수준이나 카테고리에 따라 사용자 범위를 좁혀줍니다. 이 단계에서는 세그먼트에서 더 큰 오디언스를 선택하고 필터를 사용하여 해당 세그먼트를 더 좁힙니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 것을 기억하십시오.

#### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 행동, [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용할 수 있습니다.

특정 사용 사례에 따라 사용자 지정 전환 이벤트를 설정할 수도 있습니다. 창의력을 발휘하여 이 캠페인의 성공을 어떻게 측정하고 싶은지 진지하게 생각해 보세요.

{% endtab %}

{% tab 캔버스 %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 자세한 내용은 캔버스의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대해 설명서의 [캔버스 구축]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) 단계를 참조하세요.

대화 창은 수신 메시지당 24시간만 지속될 수 있으므로, Braze는 수신 메시지와 응답 메시지 사이에 24시간을 초과하는 지연이 없는지 확인합니다. 

{% endtab %}
{% endtabs %}

### 5단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 제작을 완료한 후에는 세부 정보를 검토하고 테스트한 다음 전송하세요!

다음으로 [WhatsApp 보고]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/)를 확인하여 WhatsApp 캠페인 결과에 액세스하는 방법을 알아보세요.

## 지원되는 WhatsApp 기능

### 발신 메시지

Braze를 통해 전송하는 아웃바운드 WhatsApp 메시지에 대해 지원되는 기능은 다음과 같습니다:

| Feature | 세부 정보 | 최대 크기 | 지원되는 형식 |
| ------- | ------- | ------------- | ---------------------- |
| 헤더 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | —
| 본문 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | — |
| 바닥글 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | — |
| CTA 링크 | 다양한 클릭 유도 문안(CTA) 유형이 지원됩니다. 자세한 내용은 [클릭 유도 문안 유형](#ctas)을 참조하십시오. | — | — |
| 이미지 | 이미지는 본문 텍스트 내에 삽입할 수 있습니다. 이미지는 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| 문서* | 문서는 본문 텍스트 내에 삽입할 수 있습니다. 파일은 URL을 통해 호스팅되어야 합니다. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| 비디오* | 비디오는 본문 텍스트 내에 삽입될 수 있습니다. 파일은 URL 또는 [Braze 미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)에 호스팅되어야 합니다. | < 16 MB | `.3gp`, `.mp4` |
| 오디오* | 오디오는 응답 메시징을 통해서만 지원됩니다. 파일은 URL을 통해 호스팅되어야 합니다. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

<sup>_\*현재 초기 액세스 중입니다. 참여에 관심이 있으시면 Braze 계정 매니저에게 문의하십시오._</sup>

### 수신 메시지

Braze를 통해 수신하는 인바운드 WhatsApp 메시지에 대해 지원되는 기능은 다음과 같습니다:

| Feature | 세부 정보 | 지원되는 형식 |
| ------- | ------- | ------------------ |
| 본문 텍스트 | 표준 문자열만 지원됩니다. | — |
| 이미지 | 이미지는 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. 파일은 5 MB 미만이어야 합니다. | `.jpg`, `.png` |
| 오디오 | Opus 코덱으로 인코딩된 Ogg 파일만 지원됩니다. 다른 Ogg 형식은 지원되지 않습니다. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| 문서 | 문서는 메시지 첨부를 통해 지원됩니다. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| 동영상 | 오직 H.264 비디오 코덱과 AAC 오디오 코덱만 지원됩니다. 비디오는 단일 오디오 스트림이 있거나 오디오 스트림이 없어야 합니다. | `.mp4`, `.3gp` |
| CTA 링크 | 다양한 클릭 유도 문안(CTA) 유형이 지원됩니다. 자세한 내용은 [클릭 유도 문안 유형](#ctas)을 참조하십시오. | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 행동 유도 유형 {#ctas}

Braze를 통해 전송하는 WhatsApp 메시지에 대해 지원되는 행동 유도 유형은 다음과 같습니다:

| CTA 유형    | 세부 정보 |
| ----------- |---------------- | 
| 웹사이트 방문 | 버튼 하나 최대(변수 매개변수 포함). |
| 전화번호로 전화하기 | 메시지 템플릿에서만 사용 가능합니다. <br>버튼 하나 최대. |
| 커스텀 빠른 응답 버튼 | 최대 세 개의 버튼. |
| 마케팅 옵트아웃 버튼 | 기본적으로 구독 상태는 자동으로 업데이트되지 않습니다. 전체 안내는 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection)을 참조하세요. |
| 쿠폰 코드 메시지 템플릿 | 메시지 템플릿에서만 사용 가능합니다. <br>이들은 다른 메시지 템플릿처럼 열고 편집할 수 있으며, Liquid 및 Braze 프로모션 코드와 호환됩니다. |
| CTA 응답 메시지  | 응답 메시지를 생성하여 실행 버튼을 포함합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
