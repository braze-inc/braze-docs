---
nav_title: WhatsApp 메시지 만들기
article_title: WhatsApp 메시지 만들기
page_order: 0
description: "이 참조 문서에서는 WhatsApp 메시지를 구축하고 생성하는 단계에 대해 설명합니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp 메시지 만들기

> WhatsApp 캠페인은 고객에게 직접 다가가 프로그래밍 방식으로 대화하는 데 적합합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인화된 경험을 만들고 브랜드에 대한 사용자 경험을 촉진하고 향상시키는 환경을 조성할 수 있습니다. 

## 전제 조건

WhatsApp 메시지를 만들려면 먼저 [WhatsApp 개요에서]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) 다음 사항을 검토하고 완료해야 합니다:
  - 정책, 제한 및 콘텐츠 규칙 확인
  - WhatsApp 연결 설정
  - 메시징에 사용할 초기 템플릿을 메타에서 구축하세요.

## 메시지 작성하기

### 1단계: 메시지 구축 위치 선택하기

{% alert note %}
WhatsApp은 각 언어별로 서로 다른 [메시지 템플릿을](#template-messages) 생성합니다. 사용자에게 올바른 템플릿을 제공하기 위해 세그먼트를 세분화하여 언어별로 캠페인을 만들거나 캔버스를 사용하세요.
{% endalert %}

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **캠페인** 페이지로 이동하여 <i class="fas fa-plus"></i> **캠페인 만들기를** 클릭합니다.
2. **WhatsApp을** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널 캠페인을** 선택합니다.
3. 캠페인 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) 및 [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 구축할 수 있습니다. 예를 들어 [보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 특정 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사를** 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

1. 캔버스 작성기를 사용하여 캔버스를 [만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 일정을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 오디언스 옵션은 메시징이 전송되는 시점에 지연이 발생한 후에 확인됩니다.
5. [진행 방식을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% alert tip %}
작업 기반 캔버스가 인바운드 WhatsApp 메시지에 의해 트리거된 경우, 다음 작업 경로까지 모든 캔버스 단계에서 WhatsApp 속성을 참조할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2단계: WhatsApp 메시지 작성하기

사용 사례에 따라 WhatsApp [템플릿 메시지](#template-messages) 또는 응답 메시지를 만들 것인지 선택합니다. 비즈니스에서 시작된 모든 대화는 승인된 템플릿에서 시작해야 하며, 응답 메시지는 24시간 이내에 사용자가 보낸 인바운드 메시징에 대한 응답에 사용할 수 있습니다.

메시지 배리언트 섹션에서는 구독 그룹과 두 가지 메시지 유형 중 하나를 선택할 수 있습니다: WhatsApp 템플릿 메시지 및 응답 메시지.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Template messages %}

[승인된 WhatsApp 템플릿 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) 사용하여 WhatsApp에서 사용자와 대화를 시작할 수 있습니다. 이러한 메시지는 콘텐츠 승인을 위해 사전에 WhatsApp에 제출되며, 승인까지 최대 24시간이 소요될 수 있습니다. 복사한 내용을 편집한 후 WhatsApp에 다시 제출해야 합니다.

비활성화된 텍스트 필드(회색으로 강조 표시됨)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집하고 다시 승인을 받아야 합니다.

#### 언어

각 템플릿에는 언어가 할당되어 있으므로 각 언어에 대한 캠페인 또는 캔버스 단계를 만들어야 사용자 매칭을 올바르게 설정할 수 있습니다. 예를 들어 인도네시아어와 영어로 할당된 템플릿을 사용하는 캔버스를 구축하는 경우 인도네시아어 템플릿을 위한 캔버스 단계와 영어 템플릿을 위한 캔버스 단계를 만들어야 합니다.

메시지 미리보기, 할당된 언어 및 승인 상태를 포함한 템플릿 목록.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

오른쪽에서 왼쪽으로 쓰이는 언어로 문구를 추가하는 경우, 오른쪽에서 왼쪽으로 쓰이는 메시징의 최종 모양은 서비스 제공업체의 렌더링 방식에 따라 크게 달라질 수 있습니다. 최대한 정확하게 오른쪽에서 왼쪽으로 표시되는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 메시지 만들기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

#### 변수

메타 비즈니스 매니저에서 WhatsApp 템플릿을 만들 때 변수를 추가한 경우 해당 변수는 메시지 작성기에 빈 공간으로 표시됩니다. 이러한 빈칸을 Liquid 또는 일반 텍스트로 대체합니다. 일반 텍스트를 사용하려면 이중 중괄호로 묶은 '여기에 텍스트' 형식을 사용합니다. 템플릿을 구축할 때 이미지를 포함하도록 옵트인한 경우 미디어 라이브러리에서 이미지를 업로드하거나 추가하거나 이미지 URL을 참조하여 이미지를 추가할 수 있습니다.

비활성화된 텍스트 필드(회색으로 강조 표시됨)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없다는 점에 유의하세요. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집한 후 다시 승인을 받아야 합니다.

{% alert tip %}
{% raw %}
Liquid를 사용하려는 경우 선택한 개인화에 대한 기본값을 포함해야 수신자의 고객 프로필이 불완전한 경우 메시지를 받지 못합니다. 누락된 Liquid 변수가 있는 메시지는 WhatsApp에서 전송되지 않습니다.
{% endraw %}
{% endalert %}

속성이 "first_name", 기본값이 "you"인 개인화 추가 도구.]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### 동적 링크 

콜투액션 URL에는 변수가 포함될 수 있지만, 메타에서는 `{% raw %}https://example.com/{{variable}}{% endraw %}` 과 같이 URL 끝에 변수가 있어야 하며, 이 경우 변수는 Braze에서 Liquid로 대체할 수 있습니다. 링크는 템플릿의 일부로 본문 텍스트로 포함할 수도 있습니다. 이 두 링크는 [클릭 추적을]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) 사용하여 단축하고 추적할 수 있습니다.

{% endtab %}
{% tab Response messages %}

응답 메시지를 사용하여 사용자의 인바운드 메시징에 회신할 수 있습니다. 이러한 메시지는 작곡 경험을 하는 동안 Braze에 인앱으로 구축되며 언제든지 편집할 수 있습니다. Liquid를 사용하여 응답 메시지 언어를 적절한 사용자에게 일치시킬 수 있습니다.

사용할 수 있는 응답 메시지 레이아웃은 5가지입니다:
- 빠른 댓글
- 문자 메시지
- 미디어 메시지
- 콜투액션 버튼
- 목록 메시지

할인 코드가 있는 신규 사용자를 환영하는 답장 메시지용 응답 메시지 작성기입니다.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### 3단계: 메시지 미리보기 및 테스트하기

Braze는 항상 메시지를 보내기 전에 미리 보고 테스트할 것을 권장합니다. **테스트** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) 또는 개별 사용자에게 테스트 WhatsApp 메시지를 보내거나 Braze에서 직접 사용자로 메시지를 미리 볼 수 있습니다.

Max라는 커스텀 사용자에 대한 미리 보기 메시지입니다.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
테스트 메시지를 포함한 응답 메시지를 보내려면 대화 창이 필요합니다. 대화 창을 시작하려면 이 메시지에 사용 중인 구독 그룹과 연결된 휴대폰 번호로 WhatsApp 메시지를 보내세요. 연결된 전화번호는 **테스트** 탭의 알림에 나열됩니다.
{% endalert %}

"테스트하려면 먼저 +1 217-582-9414로 WhatsApp 메시지를 보내 대화 창을 엽니다."라는 알림이 표시됩니다. 그런 다음 테스트 사용자에게 응답 메시지를 보냅니다."]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

### 4단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}

그런 다음 나머지 캠페인을 구축합니다. 다음 섹션에서 도구를 사용하여 WhatsApp 메시지를 구축하는 방법에 대한 자세한 내용을 참조하세요.

#### 전달 일정 또는 트리거를 선택하세요.

WhatsApp 메시지는 예약된 시간, 동작 또는 API 트리거에 따라 전달될 수 있습니다. 자세한 내용은 [캠페인 예약하기를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 참조하세요.

실행 기반 전달의 경우 캠페인 기간과 조용한 시간을 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 [다시]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 수신할 수 있도록 허용하거나 [최대 게재빈도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 설정 규칙을 인에이블하는 등 전달 제어를 지정할 수도 있습니다.

#### 타겟팅할 사용자 선택하기

다음으로 세그먼트 또는 필터를 선택하여 오디언스 범위를 좁혀 [사용자를 타겟팅해야]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) 합니다. 사용자와 소통하고자 하는 수준이나 카테고리에 따라 사용자를 좁혀주는 구독 그룹을 이미 선택하셨을 것입니다. 이 단계에서는 세그먼트에서 더 큰 오디언스를 선택하고 필터를 사용하여 해당 세그먼트를 더 좁힙니다. 현재 대략적인 세그먼트 인구가 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지 전송 직전에 계산된다는 점을 기억하세요.

{% multi_lang_include target_audiences.md %}

#### 전환 이벤트 선택하기

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 액션, [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환이 카운트되는 기간을 최대 30일까지 허용할 수 있습니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의력을 발휘하여 이 캠페인의 성공을 진정으로 측정할 수 있는 방법을 생각해 보세요.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 구성 요소의 나머지 섹션을 완료하세요. 나머지 캔버스를 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 캔버스 [구축]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) 단계를 참조하세요.

대화 창은 인바운드 메시지당 24시간 동안만 지속될 수 있으므로 Braze는 인바운드 메시지와 응답 메시지 사이에 24시간을 초과하는 지연이 없는지 확인합니다. 

{% endtab %}
{% endtabs %}

### 5단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 구축을 완료한 후에는 세부 사항을 검토하고 테스트한 다음 전송하세요!

다음으로, WhatsApp 캠페인 결과에 액세스하는 방법을 알아보려면 [WhatsApp 리포팅을]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) 확인하세요.

## 지원되는 WhatsApp 기능

### 아웃바운드 메시지

Braze를 통해 보내는 아웃바운드 WhatsApp 메시징에는 다음 기능이 지원됩니다:

| 기능 | 세부 정보 | 최대 크기 | 지원되는 형식 |
| ------- | ------- | ------------- | ---------------------- |
| 헤더 텍스트 | 문자열 및 가변 매개변수가 지원됩니다. | - | -
| 본문 텍스트 | 문자열 및 가변 매개변수가 지원됩니다. | - | - |
| 바닥글 텍스트 | 문자열 및 가변 매개변수가 지원됩니다. | - | - |
| CTA 링크 | 다양한 클릭 유도 문안(CTA) 유형이 지원됩니다. 자세한 내용은 [콜투액션 유형을](#ctas) 참조하세요. | - | - |
| 이미지 | 본문 텍스트에 이미지를 삽입할 수 있습니다. 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. | < 5MB | `.png`, `.jpg`, `.jpeg` |
| 설명서 | 설명서를 본문 텍스트에 포함할 수 있습니다. 파일은 URL을 통해 호스팅해야 합니다. | < 100MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| 동영상 | 동영상은 본문 텍스트 내에 삽입할 수 있습니다. 파일은 URL 또는 [Braze 미디어 라이브러리를]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) 통해 호스팅해야 합니다. | < 16MB | `.3gp`, `.mp4` |
| 오디오 | 오디오는 응답 메시징을 통해서만 지원됩니다. 파일은 URL을 통해 호스팅해야 합니다. | < 16MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 인바운드 메시지

Braze를 통해 수신하는 인바운드 WhatsApp 메시징에는 다음 기능이 지원됩니다:

| 기능 | 세부 정보 | 지원되는 형식 |
| ------- | ------- | ------------------ |
| 본문 텍스트 | 표준 문자열만 지원됩니다. | - |
| 이미지 | 이미지는 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. 파일 용량은 5MB 미만이어야 합니다. | `.jpg`, `.png` |
| 오디오 | Opus 코덱으로 인코딩된 Ogg 파일만 지원됩니다. 다른 Ogg 형식은 그렇지 않습니다. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| 설명서 | 설명서는 메시지 첨부 기능을 통해 지원됩니다. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| 비디오 | H.264 비디오 코덱과 AAC 오디오 코덱만 지원됩니다. 동영상에는 단일 오디오 스트림이 있거나 오디오 스트림이 없어야 합니다. | `.mp4`, `.3gp` |
| CTA 링크 | 다양한 클릭 유도 문안(CTA) 유형이 지원됩니다. 자세한 내용은 [콜투액션 유형을](#ctas) 참조하세요. | - |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 클릭 유도 문안 유형 {#ctas}

Braze를 통해 보내는 WhatsApp 메시징에는 다음과 같은 콜투액션 유형이 지원됩니다:

| CTA 유형    | 세부 정보 |
| ----------- |---------------- | 
| 웹사이트 방문 | 버튼은 최대 1개(가변 매개변수 포함)입니다. |
| 전화 번호 | 메시지 템플릿에만 사용할 수 있습니다. <br>버튼은 최대 1개입니다. |
| 커스텀 빠른 답장 버튼 | 버튼은 최대 3개입니다. |
| 마케팅 옵트아웃 버튼 | 기본적으로 구독 상태는 자동으로 업데이트되지 않습니다. 전체 안내는 [옵트인 & 옵트아웃을]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection) 참조하세요. |
| 쿠폰 코드 메시지 템플릿 | 메시지 템플릿에만 사용할 수 있습니다. <br>다른 메시지 템플릿과 마찬가지로 열고 편집할 수 있으며 Liquid 및 Braze 프로모션 코드와 호환됩니다. |
| CTA 응답 메시지  | 클릭 유도 문안 실행 버튼이 포함된 응답 메시지를 작성합니다. |
| [응답 메시지 나열하기]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#list-messages) | 사용자가 선택할 수 있는 최대 10개의 옵션 목록이 포함된 응답 메시지를 작성합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

