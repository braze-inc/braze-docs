## 분석 보기

캠페인을 시작한 후, 해당 캠페인의 세부 정보 페이지로 돌아가 주요 측정기준을 확인할 수 있습니다. **캠페인** 페이지로 이동하여 캠페인을 선택하여 세부정보 페이지를 엽니다.{% if include.channel != "banner" %} {% if include.channel == "Content Card" %}콘텐츠 카드 {% elsif include.channel == "banner" %}배너 {% elsif include.channel == "email" %}이메일 {% elsif include.channel == "in-app message" %}인앱 메시지 {% elsif include.channel == "push" %}푸시 메시지 {% elsif include.channel == "SMS" %}SMS 메시지 {% elsif include.channel == "whatsapp" %}WhatsApp 메시지 {% elsif include.channel == "webhook" %}웹훅 {% endif %}캔버스에서 전송된 경우, [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)를 참조하십시오.{% endif %}

{% alert tip %}
보고서에 나열된 용어와 측정기준에 대한 정의를 찾고 계십니까? 참고:
  {% if include.channel == "email" %}[이메일 분석 용어집]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 배너로 필터링합니다.
  {% elsif include.channel == "Content Card" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 콘텐츠 카드로 필터링합니다.
  {% elsif include.channel == "in-app message" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 인앱 메시지로 필터링합니다.
  {% elsif include.channel == "push" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 푸시로 필터링합니다.
  {% elsif include.channel == "SMS" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 SMS/MMS 및 RCS로 필터링합니다.
  {% elsif include.channel == "whatsapp" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 WhatsApp으로 필터링합니다.
  {% elsif include.channel == "webhook" %}[보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/) 및 웹훅으로 필터링합니다.{% endif %}
{% endalert %}

**캠페인 분석** 탭에서, 일련의 패널에서 보고서를 볼 수 있습니다. 아래 섹션에 나열된 것보다 더 많거나 적은 항목을 볼 수 있지만, 각각 유용한 목적이 있습니다.

### 시간 범위

기본값으로 **캠페인 분석의** 시간 범위는 현재 시간으로부터 최근 90일을 표시합니다. 즉, 캠페인이 90일 이상 전에 시작된 경우 해당 기간 동안 분석 결과가 "0"으로 표시됩니다. 이전 캠페인에 대한 모든 분석을 보려면 보고 시간 범위를 조정하세요.

### 캠페인 세부 정보

**캠페인 세부정보** 패널은 전체 성능에 대한 고급 개요를 보여줍니다.
  {% if include.channel == "banner" %}배너.
  {% elsif include.channel == "Content Card" %}콘텐츠 카드.
  {% elsif include.channel == "email" %}이메일.
  {% elsif include.channel == "in-app message" %}인앱 메시지.
  {% elsif include.channel == "push" %}푸시 메시지.
  {% elsif include.channel == "SMS" %}SMS, MMS 및 RCS.
  {% elsif include.channel == "whatsapp" %}WhatApp 메시지.
  {% elsif include.channel == "webhook" %}웹훅.
  {% endif %}

이 패널을 검토하여 수신자 수에 전송된 메시지 수, 주요 전환율 및 이 메시지로 인해 발생한 총 매출 등의 전반적인 측정기준을 확인할 수 있습니다. 이 페이지에서 전달, 오디언스 및 전환 설정을 검토할 수도 있습니다.

{% if include.channel == "whatsapp" %}
{% alert note %}
WhatsApp 채널에는 읽기 비율이 포함됩니다. 이 측정기준은 읽음 확인이 켜진 사용자에게만 제공되며, 이는 다를 수 있습니다.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/campaign_details_iam.png %})

캔버스에서, 생성한 캔버스에 매핑된 인앱 메시지 성능을 볼 수 있습니다. 페이지 상단의 제어판을 사용하여 다른 메시징 유형(채널)을 지우고 캔버스에서 인앱 메시지만 볼 수 있습니다.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![캠페인 세부정보 패널은 캠페인 성능을 결정하는 데 사용되는 측정기준의 개요를 제공합니다.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### 대조군 {#cc-control-group}

개별 콘텐츠 카드의 영향을 측정하기 위해 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부정보** 패널에는 대조군 배리언트의 측정기준이 포함되어 있지 않습니다.

{% elsif include.channel == "SMS" %}

#### 대조군 {#sms-control-group}

개별 SMS, MMS 또는 RCS 메시지의 영향을 측정하려면 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부정보** 패널에는 대조군 배리언트의 측정기준이 포함되어 있지 않습니다.

{% elsif include.channel == "whatsapp" %}

#### 대조군 {#whatsapp-control-group}

개별 WhatsApp 메시지의 영향을 측정하기 위해 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부정보** 패널에는 대조군 배리언트의 측정기준이 포함되어 있지 않습니다.

{% elsif include.channel == "webhook" %}

#### 대조군 {#webhook-control-group}

개별 웹훅 메시지의 영향을 측정하기 위해 A/B 테스트에 [대조군]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants)을 추가할 수 있습니다. 최상위 **캠페인 세부정보** 패널에는 대조군 배리언트의 측정기준이 포함되어 있지 않습니다.

{% endif %}

#### 마지막 확인 이후 변경 사항

캠페인에 대한 팀의 다른 구성원들의 업데이트 수는 캠페인 개요 페이지의 *변경 사항 마지막으로 본 이후* 메트릭에 의해 추적됩니다. **변경 사항**을 선택하여 캠페인의 이름, 일정, 태그, 메시지, 오디언스, 승인 상태 또는 팀 접근 구성에 대한 체인지로그를 확인하세요. 각 업데이트마다 누가 업데이트를 수행했는지와 언제 수행했는지 확인할 수 있습니다. 이 체인지로그를 사용하여 캠페인에 대한 변경 사항을 감사할 수 있습니다.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### 콘텐츠 카드 성능

**콘텐츠 카드 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![콘텐츠 카드 메시지 성능 분석]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### 이메일 성과

**이메일 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![이메일 메시지 성능 분석]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### 인앱 메시지 성능/성과

**인앱 메시지 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![인앱 메시지 성능 분석]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### 푸시 성과

**푸시 성능** 패널에는 다양한 측면에서 메시지의 성과가 얼마나 잘 나타났는지 요약되어 있습니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![푸시 메시지 성능 분석]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS 성과

**SMS/MMS/RCS 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![SMS/MMS/RCS 대조군, 배리언트 1 및 배리언트 2에 대한 측정기준 표가 포함된 성능 패널입니다.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### 배너 성능

**배너 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 측정기준은 메시징 채널에 따라 다르며 다변량 테스트를 실행 중인지 여부에 따라 달라집니다.

![SMS/MMS 성능 패널에는 대조군, 배리언트 1 및 배리언트 2에 대한 측정기준 표가 포함되어 있습니다.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "webhook" %}
### 웹훅 성과

**웹훅 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![웹훅 성능 패널에는 대조군과 배리언트 1에 대한 측정기준 표가 포함되어 있습니다.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp 성과

**WhatsApp 성능** 패널은 메시지가 다양한 차원에서 얼마나 잘 수행되었는지를 설명합니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![WhatsApp 성능 패널에는 배리언트 1에 대한 측정기준 표가 포함되어 있습니다.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

보기를 간소화하려면 <i class="fas fa-plus"></i> **열 추가/제거**를 클릭하고 원하는 대로 측정기준을 지우세요. 기본적으로 모든 메트릭이 표시됩니다.

{% if include.channel == "email" %}

#### 히트맵

히트맵을 사용하여 단일 이메일 캠페인에서 다양한 링크가 얼마나 성공적인지 확인할 수 있습니다. **메시지 분석** 섹션에서 **이메일 성능** 패널로 이동하세요. **미리보기 및 히트맵**을 선택하여 이메일 캠페인의 미리보기와 히트맵을 확인하세요. 대안적으로, 배리언트 이름의 하이퍼링크를 선택하여 히트맵을 볼 수 있습니다.

이 보기에서는 **Show Heatmap** 토글을 사용하여 캠페인의 수명 동안 클릭의 전반적인 빈도와 위치를 보여주는 이메일의 시각적 보기를 가져올 수 있습니다. **링크 테이블 총 클릭 수** 패널에서 이메일 캠페인의 모든 링크를 보고 총 클릭 수로 정렬할 수 있습니다. 이것은 사용자가 어디로 이동하는지에 대한 추가 인사이트를 제공할 수 있습니다. 참고용으로 히트맵의 복사본을 저장하려면 다운로드 버튼을 선택하세요.

![미리보기 및 히트맵 페이지의 예로, 이메일 캠페인과 총 클릭 수가 포함된 링크 별칭 예시 패널이 포함되어 있습니다.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### 이미지

이미지 URL에 대한 CORS를 활성화하여 히트맵 미리보기 및 내보내기에서 이미지가 깨지는 것을 방지하는 것을 권장합니다.

{% endif %}

{% if include.channel == "Content Card" %}

#### 콘텐츠 카드 측정기준

여기 메시지 성능을 검토하는 동안 볼 수 있는 몇 가지 주요 측정기준에 대한 분석이 있습니다. 모든 콘텐츠 카드 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하고 콘텐츠 카드로 필터링하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">메시지 발송됨</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Messages Sent' %} <br><br>
                이것은 사용자가 선택한 것에 따라 다르게 계산됩니다. 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">카드 생성</a>:<br><br>
                <ul>
                    <li><b>출시 또는 단계 진입 시:</b> 생성된 카드의 수와 볼 수 있는 카드의 수. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.</li>
                    <li><b>첫인상:</b> 사용자에게 표시되는 카드 수.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} 이는 동일한 사용자에 대해 여러 번 증가할 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">이 카운트</span>는 사용자가 콘텐츠 카드를 두 번째로 볼 때 증가하지 않습니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> 콘텐츠 카드의 경우 각 콘텐츠 카드는 한 번만 수신될 수 있으므로, 같은 콘텐츠 카드를 두 번째로 보는 것은 날짜에 관계없이 이 카운트를 증가시키지 않습니다. 시청자는 매일 고유한 수신자가 될 수 있으므로, <i>고유 노출 수</i>보다 더 높을 것으로 예상해야 합니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 여기에는 Braze에서 제공하는 탈퇴 링크에 대한 클릭이 포함됩니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">고유 무시 수</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
인상 기록 방식에 관해서는 웹, Android, iOS 간에 몇 가지 뉘앙스가 있습니다. 일반적으로 말하자면, Braze는 사용자가 피드에서 특정 콘텐츠 카드를 스크롤할 때 카드를 볼 때 노출 횟수를 기록합니다.
{% endalert %}

#### 고유 수신자 대 고유 노출

메시지 가시성을 다루는 몇 가지 측정기준이 있습니다. 여기에는 _고유 수신자_ 및 _고유 노출 횟수가_ 포함됩니다. 이 메트릭을 더 잘 이해하기 위해 몇 가지 예시 시나리오를 사용해 보겠습니다.

오늘 콘텐츠 카드를 보고, 내일 같은 캠페인에서 새로운 카드를 받고, 모레 다시 보게 된다면, _고유 수신자_으로 세 번 카운트됩니다. 그러나 단지 하나의 _고유 노출 횟수_로만 계산됩니다. 당신은 또한 _전송된 메시지 수_에 포함될 것이며, 카드가 당신의 기기에서 사용 가능했기 때문입니다.

또 다른 예로, 콘텐츠 카드 캠페인에서 150,000 _메시지 전송됨_을 보여주는 다섯 _고유 노출_을 보았다고 가정해 보세요. 이것은 카드가 150,000명의 오디언스에게(백엔드에서) 제공되었음을 의미하지만, 그 전송이 발생한 후 오직 다섯 사용자의 기기만이 다음 모든 단계를 수행했습니다.

1. 세션을 시작했거나 앱이 명시적으로 콘텐츠 카드 동기화를 요청했습니다(또는 둘 다).
2. 콘텐츠 카드 보기로 이동했습니다.
3. 소프트웨어 개발 키트가 노출 횟수를 기록하고 이를 서버에 기록했습니다.

_보낸 메시지_는 볼 수 있는 콘텐츠 카드와 관련이 있으며, _고유 수신자_는 실제로 본 콘텐츠 카드를 나타냅니다.

{% elsif include.channel == "banner" %}

### 배너 측정기준

이들은 배너 캠페인 성과를 검토하는 동안 추적해야 할 주요 측정기준입니다. 배너의 클릭 수와 노출 수는 SDK를 통해 자동으로 추적됩니다. 

모든 배너 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하고 배너로 필터링하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">각 사용자는 한 번만 계산됩니다.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">총 클릭 수</a></td>
            <td class="no-split"><i>총 클릭</i> 수는 동일한 사용자가 여러 번 클릭했는지 여부와 관계없이 전달된 메시지 내에서 클릭한 사용자의 총 수(및 백분율)입니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 각 사용자는 한 번만 계산됩니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">주요 전환</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Unique Recipients</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} <br><br> 시청자는 매일 고유한 수신자가 될 수 있으므로, <i>고유 노출 수</i>보다 더 높을 것으로 예상해야 합니다.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Revenue</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">신뢰도</a></td>
            <td>{% multi_lang_include analytics/metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### 배너 측정기준 계산 예시

메시지 가시성을 다루는 몇 가지 측정기준이 있습니다. 여기에는 _고유 수신자_ 및 _고유 노출 횟수가_ 포함됩니다. 이러한 측정기준을 더 잘 이해하기 위해 몇 가지 예시 시나리오를 사용해 보겠습니다.

오늘 배너를 보고 내일도 같은 배너를 보고 모레도 같은 배너를 본다고 가정하면, _고유 수신자로_ 세 번 계산됩니다. 그러나 단지 하나의 _고유 노출 횟수_로만 계산됩니다.

다른 예로, 배너 캠페인에 5개의 _고유 노출 횟수가_ 있다고 가정해 보겠습니다. 즉, 다음 단계를 모두 수행한 사용자의 기기는 5대에 불과했습니다:

1. 세션을 시작했거나 앱이 명시적으로 배너 동기화를 요청했습니다 (또는 둘 다)
2. 배너 보기로 이동했습니다.
3. 소프트웨어 개발 키트가 노출 횟수를 기록하고 이를 서버에 기록했습니다.

_고유 수신자란_ 실제로 표시된 배너를 의미합니다.

{% elsif include.channel == "email" %}

#### 이메일 측정기준

여기 다른 채널에서는 볼 수 없는 몇 가지 주요 이메일 전용 측정기준이 있습니다. Braze에서 사용되는 모든 이메일 측정기준의 전체 정의를 보려면 [Email Analytics Glossary]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)를 참조하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">고유 클릭 수</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} 이는 이메일에 대해 7일 동안 추적되며 <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>로 측정됩니다. 여기에는 Braze에서 제공한 탈퇴 링크를 클릭하는 것이 포함됩니다. 이 숫자는 5–10% 사이여야 합니다. 10%보다 큰 것은 예외적입니다!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">고유 열람</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Unique Opens' %} 이메일의 경우, 이는 7일 동안 추적됩니다. 이 숫자는 30–40% 사이여야 합니다. 40%보다 큰 것은 예외적입니다!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">클릭 후 열람률</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">스팸율</a></td>
            <td class="no-split">
                {% multi_lang_include analytics/metrics.md metric='Spam' %}이 측정기준이 0.08보다 크면, 이는 메시지 내용이 너무 판매적이거나, 이메일 주소 수집 방법을 재고해야 할 수 있음을 나타낼 수 있습니다(서신에 관심이 있는 사람들에게 메시징하고 있는지 확인하기 위해).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">구독 취소 또는 구독 취소</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">기타 열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">추정된 실제 열람</a></td>
            <td class="no-split"> {% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} 자세한 내용은 다음 섹션을 참조하세요.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">기계 열람</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">반송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">하드바운스</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">소프트바운스</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">연기</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### 연기

지연 또는 연기는 이메일이 즉시 전달되지 않았을 때를 의미하지만, Braze는 이 임시 전달 실패 후 최대 72시간 동안 이메일을 재전송하여 특정 캠페인에 대한 시도가 중단되기 전에 성공적인 전달 가능성을 극대화합니다. 전형적인 연기 사유에는 받은편지함 제공자의 평판 기반 이메일 볼륨 속도 제한, 일시적인 연결 문제 또는 DNS 오류가 포함됩니다.

_연기(Deferrals)_는 _소프트 반송(Soft Bounces)_과 다릅니다. 이 재시도 기간 동안 성공적으로 전달된 이메일이 없으면, Braze는 시도된 캠페인당 하나의 소프트 바운스 이벤트를 보낼 것입니다. 2025년 2월 25일 이전에, 이러한 재시도는 1개의 캠페인 발송에 대해 여러 번의 소프트 반송으로 계산되었습니다.

_Deferrals_는 현재 Currents 또는 Braze Snowflake 기능(예: Query Builder, SQL Segment, Snowflake Data Sharing)을 사용하여만 사용할 수 있습니다. 캠페인 또는 캔버스 분석에 포함하고 싶으시다면, [제품 피드백]({{site.baseurl}}/user_guide/administrative/access_braze/portal)을 제출해 주시기 바랍니다.

##### 추정된 실제 열람율 {#estimated-real-open-rate}

이 통계는 Braze에서 개발한 독점 분석 모델을 사용하여 기계 열람이 존재하지 않는 것처럼 캠페인의 고유한 열람율 추정치를 재구성합니다. 이메일 발신자로부터 일부 열람 이벤트에 대해 *머신 열람이라는* 라벨을 받지만(위 참조), 이러한 라벨은 종종 실제 열람을 머신 열람으로 표시할 수 있습니다. 다시 말해, *Other Opens*는 실제 사용자에 의한 실제 오픈 수를 과소 추정할 가능성이 높습니다. 대신, Braze는 각 캠페인의 클릭 데이터를 사용하여 실제 사용자가 메시지를 열어본 비율을 추론합니다. 이는 Apple의 MPP를 비롯한 다양한 기기 개방 메커니즘을 보완합니다.

_예상 실제 열람율_은 이메일 발송이 시작된 후 36시간이 지나면 계산되며, 그 이후 매 24시간마다 재계산됩니다. 캠페인이 반복되면, 다른 발송이 발생한 후 36시간 후에 추정치가 재계산됩니다.

일반적으로 통계가 성공적으로 계산되기 위해서는 약 10,000개의 배달된 이메일이 필요하지만, 그 숫자는 클릭률에 따라 달라질 수 있습니다. 통계가 계산될 수 없으면 열에 "--"가 표시됩니다.

###### 제한 사항

예상 실제 열람율은 캠페인에서만 사용할 수 있으며, 현재 이벤트에서는 보고되지 않습니다. 이 지표는 2023년 11월 14일 이전에 시작된 활성 캠페인에 대해서만 소급하여 계산됩니다.

##### 클릭률 증가 처리

오픈율은 이메일 캠페인에서 추적할 수 있는 통찰력 있는 지표가 될 수 있습니다. 하지만 이러한 오픈율이 반드시 이메일 캠페인에 대한 사람들의 참여를 정확하게 나타내는 지표는 아닙니다. 열람 이벤트는 사용자가 이메일을 열었을 때 발생하며, 이는 투명한 열람 추적 픽셀이 성공적으로 다운로드되었음을 의미합니다. 

또한 보안 스캐닝 도구를 사용하면 오픈율이 부풀려질 수 있습니다. 이러한 도구 중 일부는 수신되는 이메일에서 악성 콘텐츠를 스캔하여 링크를 클릭하여 합법성을 확인함으로써 사용자를 보호합니다. 이러한 클릭을 흔히 "봇 클릭" 또는 "비인간 상호작용(NHI)"이라고 합니다. 

궁극적으로 이메일이 서버를 떠난 후에는 다음에 어떤 일이 발생하는지 파악하기 어렵지만, 결과에 영향을 미치는 NHI 관리를 위한 권장 사항은 다음과 같습니다:

1. 이는 발신자와 거의 모든 수신자에게 발생할 수 있다는 점에 유의하세요. 열기와 같은 클릭은 메시지와 사람의 상호 작용을 완전히 신뢰할 수 있는 지표가 아니므로 NHI를 방지할 수 없습니다.
2. 긍정적인 참여도가 높을수록 NHI가 낮아지는 경향이 있으므로 이메일 메시징 [모범 사례를]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) 따르는 것이 중요합니다. 여기에는 사용자로부터 이메일 전송에 대한 명시적인 권한을 받고 참여하지 않는 구독자를 정기적으로 일몰시키는 것이 포함됩니다. 
3. 가능하면 이메일에 HTTPS 링크를 사용하세요. NHI는 보안 링크를 사용하는 발신자에게는 덜 일반적입니다.
4. 원클릭 탈퇴 프로세스를 사용하는 경우에는 사용자를 알림 환경설정을 편집하고 관리할 수 있는 페이지로 안내하는 [환경설정 센터를]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview) 만드는 것도 고려해 보세요. 이는 NHI가 실수로 사용자의 구독을 취소할 수 있기 때문에 유용할 수 있습니다.
5. 전환, 앱 세션 또는 사이트 방문과 같은 [다른 측정기준]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)을 사용하여 이메일 마케팅의 성공 여부를 측정하는 것도 고려해 보세요.
6. 이메일 캠페인에 숨겨진 링크를 추가하세요. 이 링크는 흰색 위에 흰색 텍스트나 구두점처럼 사람이 알아차리지 못할 것입니다. 봇은 모든 링크를 클릭하는 경향이 있으므로 보이지 않는 링크에서 클릭 이벤트를 생성하는 사용자는 실제로 NHI의 결과이므로 열기 또는 클릭이 반드시 긍정적인 참여를 의미하지는 않는다고 결론 내릴 수 있습니다.

{% elsif include.channel == "in-app message" %}

#### 인앱 메시지 측정기준

여기에서 분석에서 볼 수 있는 몇 가지 주요 인앱 메시지 측정기준이 있습니다. Braze에서 사용되는 모든 인앱 메시지 측정기준의 전체 정의를 보려면 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하세요.

{% alert note %}
_버튼 1 클릭_ 및 _버튼 2 클릭_에 대한 보고서는 인앱 메시지에서 **보고용 식별자**를 각각 "0" 및 "1"로 지정할 때만 작동합니다.

!["보고용 식별자" 필드의 값이 "0"입니다.]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">본문 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">버튼 1 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">버튼 2 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">변환 (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">총 전환 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">전환율</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">닫기 메시지</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### 푸시 측정기준

여기 메시지 성능을 검토하는 동안 볼 수 있는 몇 가지 주요 측정기준에 대한 분석이 있습니다. 모든 푸시 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하고 푸시로 필터링하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>설명</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">반송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Bounces' %} <a href="#bounced-push">반송된 푸시 알림</a>을 참고하세요.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">직접 열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">열람 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> 알림의 전달은 Apple Push Notification 서비스(APNs)에 의한 "최선의 노력"입니다. 사용자에게 새로운 데이터가 사용 가능하다는 것을 알리기 위한 것이지, 앱에 데이터를 전달하기 위한 것이 아닙니다. 중요한 구별은 우리가 APN에 성공적으로 전달한 메시지 수를 표시할 것이며, 반드시 APN가 기기에 성공적으로 전달한 수는 아닙니다.

##### 추적 구독 취소

푸시 탈퇴는 캠페인 분석의 측정기준에 포함되지 않으며, Apple 또는 Google과 같은 제공업체의 사용자 푸시 상태 업데이트에 따라 달라집니다. 이러한 업데이트는 드물고 예측하기 어려울 수 있습니다. 따라서 푸시 구독 취소는 푸시 캠페인 분석의 지표로 포함되지 않습니다. 

하지만 수동으로 푸시 수신 취소를 추적하면 알림 빈도 및 콘텐츠 관련성에 대한 사용자 반응에 대한 귀중한 인사이트를 얻을 수 있습니다. 다음은 푸시 탈퇴를 추적하는 두 가지 옵션입니다: 세그먼트 필터 또는 커스텀 필터 사용.

{% tabs local %}
{% tab 세그먼트 필터 %}

푸시 인에이블먼트가 되지 않은 사용자, 즉 가입하거나 옵트인하지 않았고 [포그라운드 푸시 토큰이]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens) 없는 사용자를 식별하는 세그먼트를 만들 수 있습니다. 예를 들어 앱의 탈퇴 수를 확인하려면 다음 세그먼트의 조합을 사용합니다: 

- `Background or Foreground Push Enabled is false`
- `Has Uninstalled`

![앱에 대해 "앱에 대해 백그라운드 또는 포그라운드 푸시 인에이블먼트" 필터가 거짓이고 "제거됨" 필터가 선택된 세그먼트 빌더 섹션이]({% image_buster /assets/img/push_unsub_segment_example.png %})

세분화 필터는 대략적인 기준이며 날짜 및 캠페인에 구체적으로 연결될 수 없습니다.

{% endtab %}
{% tab 커스텀 필터 %}

{% alert important %}
구독 변경에 대한 커스텀 이벤트를 기록하면 [데이터 포인트가]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count) 기록됩니다. 또는 세그먼트 필터를 사용하여 푸시를 사용 설정하지 않은 사용자를 식별하고 타겟팅할 수 있습니다.
{% endalert %}

다른 해결 방법으로는 사용자의 푸시 사용 설정 상태가 `true` 또는 `false`인지에 따라 푸시 수신 거부 커스텀 이벤트를 생성하여 이 지표를 추적하는 것이 좋습니다.

{% endtab %}
{% endtabs %}

##### 이해는 열린다

비록 _Direct Opens_와 _Influenced Opens_가 "opens"라는 단어를 포함하고 있지만, 실제로는 서로 다른 측정기준입니다. _직접 열기_는 위의 표에 명시된 대로 푸시 알림의 직접 열기를 의미합니다. _영향을 받은 열람_은 푸시 알림을 받은 후 특정 시간 내에 푸시 알림을 열지 않고 앱을 여는 것을 의미합니다. 그래서 _Influenced Opens_는 푸시 알림 오픈이 아닌 앱 오픈을 의미합니다.

##### 푸시 전송이 고유 수신자를 초과할 수 있는 이유

_Sends_의 수는 다음과 같은 이유로 _Unique Recipients_의 수를 초과할 수 있습니다:

- **재자격 부여는 다음과 같습니다:** 캠페인 또는 캔버스 설정에서 재자격 부여가 활성화되면, 세그먼트 및 전달 기준을 충족하는 사용자에게 동일한 푸시 알림을 여러 번 받을 수 있습니다. 이로 인해 총 발송 수가 증가합니다.
- **사용자는 여러 장치를 가지고 있습니다.** 재자격이 활성화되지 않은 경우, 차이는 사용자가 자신의 프로필과 연결된 여러 장치를 가지고 있기 때문일 수 있습니다. 예를 들어, 사용자가 스마트폰과 태블릿을 모두 가지고 있을 수 있으며, 푸시 알림이 모든 등록된 장치로 전송되고 있습니다. 각 전달은 발송으로 계산되지만, 고유한 수신자만 기록됩니다.
- **사용자는 여러 앱에 할당됩니다:** 사용자가 여러 앱(예: 새 앱을 테스트할 때)과 연결되어 있는 경우, 각 앱에서 동일한 푸시 알림을 받을 수 있습니다. 이것은 더 많은 전송에 기여합니다.

##### 왜 바운스가 발생하나요 {#bounced-push}

{% tabs %}
{% tab 애플 푸시 알림 서비스 %}

바운스는 Apple Push Notification 서비스(APNs)에서 푸시 알림이 설치된 앱이 없는 기기로 전달을 시도할 때 발생합니다. APN는 또한 기기의 토큰을 임의로 변경할 권리가 있습니다. Braze가 앞서 사용자 토큰을 등록했을 때(예: Braze가 사용자 푸시 토큰을 등록할 경우 각 세션의 시작 시점)와 실제 전송 시점 사이에 푸시 토큰의 변경이 이루어진 사용자 기기를 대상으로 발송을 시도하면, 반송이 발생하게 됩니다.

사용자가 기기 설정에서 푸시를 비활성화하면 이후 앱을 열 때 SDK가 푸시가 비활성화되었음을 감지하고 Braze에 알립니다. 이 시점에서 우리는 푸시 활성화 상태를 비활성화로 업데이트할 것입니다. 장애인 사용자가 새로운 세션을 시작하기 전에 푸시 캠페인을 받으면, 캠페인은 성공적으로 전송되어 배달된 것으로 나타납니다. 이 사용자는 푸시가 튕기지 않을 것입니다. 후속 세션에서 사용자가 푸시를 보내려고 할 때, Braze는 우리가 포그라운드 토큰을 가지고 있는지 이미 알고 있으므로 알림이 전송되지 않습니다.

푸시 알림은 전달 전에 만료되면 실패로 간주되지 않으며 반송으로 기록되지 않습니다.

{% endtab %}
{% tab 파이어베이스 클라우드 메시징 %}

Firebase Cloud Messaging(FCM) 바운스는 세 가지 경우에 발생할 수 있습니다.

| 시나리오 | 설명 |
| -- | -- |
| 제거된 애플리케이션 | 메시지가 기기로 전달을 시도할 때, 해당 기기에 의도된 앱이 제거되어 있으면 메시지는 폐기되고 기기의 등록 ID는 무효화됩니다. 기기에 메시징을 시도하는 모든 미래의 시도는 NotRegistered 오류를 반환합니다. |
| 백업된 애플리케이션 | 애플리케이션이 백업될 때, 등록 ID는 애플리케이션이 복원되기 전에 유효하지 않을 수 있습니다. 이 경우, FCM은 더 이상 애플리케이션의 등록 ID를 저장하지 않으며 애플리케이션은 더 이상 메시지를 수신하지 않습니다. 따라서, 등록 ID는 애플리케이션이 백업될 때 **저장되지** 않아야 합니다. |
| 업데이트된 애플리케이션 | 애플리케이션이 업데이트되면 이전 버전의 등록 ID가 더 이상 작동하지 않을 수 있습니다. 따라서 업데이트된 애플리케이션은 기존 등록 ID를 대체해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS, MMS 및 RCS 측정기준

여기 메시지 성능을 검토하는 동안 볼 수 있는 몇 가지 주요 측정기준에 대한 분석이 있습니다. 모든 SMS, MMS 및 RCS 측정기준의 전체 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하고 SMS/MMS 및 RCS로 필터링하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">발송됨</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">전달 실패 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">확인된 전달</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">거부 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">옵트아웃</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">도움말</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">총 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### 웹훅 측정기준

여기에서 귀하의 분석에서 볼 수 있는 몇 가지 주요 웹훅 측정기준이 있습니다. Braze에서 사용되는 모든 웹훅 측정기준의 전체 정의를 보려면 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">고유 수신자</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">발송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">오류</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp 측정기준

여기 분석에서 볼 수 있는 몇 가지 주요 WhatsApp 측정기준이 있습니다. Braze에서 사용되는 모든 WhatsApp 측정기준의 전체 정의를 보려면 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)을 참조하십시오.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">발송 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">전달 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">읽기 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">실패 수</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### 최종 사용자 차단 및 보고 측정기준

추가 측정기준은 [WhatsApp 매니저 대시보드](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx)를 통해 접근할 수 있지만, 모든 사용 가능한 통찰력을 접근하기 위해서는 [접근 확인](https://www.facebook.com/business/help/218116047387456)이 필요합니다. 

{% endif %}

### 과거 성과

**과거 실적** 패널에서는 **메시지 실적** 패널의 메트릭을 시간 경과에 따른 그래프로 볼 수 있습니다. 패널 상단의 필터를 사용하여 그래프에 표시된 통계와 채널을 수정할 수 있습니다. 이 그래프의 시간 범위는 항상 페이지 상단에 지정된 시간 범위를 반영합니다. 

하루하루의 세부 정보를 얻으려면 <i class="fas fa-bars"></i> 햄버거 메뉴를 클릭하고 **CSV 다운로드**를 선택하여 보고서의 CSV 내보내기를 받으세요.

![2021년 2월부터 2022년 5월까지의 이메일에 대한 예제 통계가 포함된 역사적 성능 패널의 그래프입니다.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
최신 Braze 버전의 인앱 메시지(3세대)를 볼 수 있는 사용자에게만 전송하도록 선택하면, 귀하의 **타겟 오디언스**는 귀하의 선택을 반영하도록 조정되지 않습니다.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### 키워드 응답

**키워드 응답** 패널은 사용자가 메시지를 받은 후 회신한 인바운드 키워드의 타임라인을 보여줍니다.  

![캠페인 수준 SMS/MMS/RCS 키워드 응답 패널은 시간에 따른 키워드 분포의 선 그래프와 옵트인, 옵트아웃, 도움말, 기타, 더보기 및 코칭에 대한 선택된 체크박스가 있는 키워드 카테고리 섹션을 포함합니다.]({% image_buster /assets/img/sms/keyword_responses.png %})

여기에서 각 키워드 카테고리의 응답 분포를 확인하여 [리타겟팅]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns)에 대한 다음 단계를 결정하고 편리하게 [세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)를 생성할 수 있습니다.

![선 그래프 아래의 표에는 키워드 카테고리, 응답 분포 및 리타겟팅을 위한 열이 있으며, 여기에서 키워드 카테고리로 세그먼트를 생성할 수 있는 옵션이 제공됩니다.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### 전환 이벤트 세부 정보

**전환 이벤트 세부 정보** 패널에는 캠페인에 대한 전환 이벤트의 성과가 표시됩니다. 자세한 정보는 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results)를 참조하십시오.

![전환 이벤트 세부정보 패널.]({% image_buster /assets/img/cc-conversion.png %})

### 전환 상관관계

**전환 상관관계** 패널은 어떤 사용자 속성과 행동이 캠페인에 대해 설정한 결과에 도움이 되거나 해가 되는지에 대한 인사이트를 제공합니다. 자세한 내용은 [전환 상관관계]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/)를 참조하세요.

![전환 상관관계 패널은 주요 전환 이벤트에서 사용자 속성과 행동에 대한 분석을 제공합니다 - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### 메타 분석

Braze 분석 외에도 템플릿 수준의 분석은 WhatsApp 비즈니스 매니저에서 접근할 수 있습니다. 자세한 정보는 [메타의 설명서](https://www.facebook.com/business/help/218116047387456)를 확인하세요. 

{% endif %}

{% if include.channel == "SMS" %}

### SMS 커런츠 이벤트

이메일과 마찬가지로, Braze는 SMS 메시지가 사용자에게 전달되는 과정에서 사용자 수준의 이벤트를 수신합니다. 모든 수신 SMS 이벤트는 [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) 이벤트를 통해 Currents 이벤트로 전송됩니다. 이것은 사용자가 Braze 플랫폼 외부에서 텍스트하는 메시지에 대해 추가 작업이나 보고를 수행할 수 있도록 합니다. 

{% alert note %}
수신 메시지는 1,600자를 초과하면 잘립니다.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## 리텐션 보고서

유지 보고서는 특정 캠페인{% if include.channel != "banner" %} 또는 캔버스{% endif %}에서 시간에 따라 사용자가 선택한 유지 이벤트를 수행한 비율을 보여줍니다. 자세한 정보는 [Retention reports]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/)를 참조하십시오.

## 퍼널 보고서

퍼널 보고서는 캠페인{% if include.channel != "banner" %} 또는 캔버스{% endif %}를 받은 후 고객이 취하는 여정을 분석할 수 있는 시각적 보고서를 제공합니다. 캠페인 {% if include.channel != "banner" %} 또는 캔버스 {% endif %}가 대조군이나 여러 변형을 사용하는 경우, 다양한 변형이 전환 퍼널에 미친 영향을 더 세부적으로 이해하고 이 데이터를 기반으로 최적화할 수 있습니다.

자세한 정보는 [퍼널 보고서]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/)을 참조하십시오.

{% endif %}