---
nav_title: 알림
article_title: 알림 모범 사례
description: "Braze 설명서에서 사용되는 알림 유형에 대한 정보, 가이드라인 및 예시입니다."
page_order: 2
noindex: true
---

# 알림 모범 사례

> 이 문서에는 Braze 설명서에서 사용되는 알림 유형에 대한 정보, 일반 가이드라인 및 예시가 포함되어 있습니다.

## 알림 유형 {#alert-types}

알림은 독자가 알아야 할 정보를 분류합니다. 설명서에서 사용할 수 있는 알림 유형은 네 가지입니다:

* 중요  
* 참고  
* 팁  
* 경고

## 알림을 사용해야 하는 경우 {#when-to-use-an-alert}

알림을 사용하여 중요한 정보에 독자의 주의를 끌어보세요. 콘텐츠는 짧고 핵심적으로 유지합니다. 독자가 해당 정보를 확실히 기억할 수 있도록 해야 합니다.

각 알림의 정의는 다음 표를 참조하세요:

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>알림 유형</th><th>정의</th></tr>
</thead>
<tbody>
<tr><td>중요</td><td>독자가 <strong>반드시</strong> 확인해야 하는 필수 정보를 포함하며, 예를 들면 다음과 같습니다: <ul><li>지원 중단된 기능</li><li>청구에 미치는 영향</li><li>관련 업데이트에 대한 정보</li><li>긴급한 기능 주의사항(예: 베타 기능)</li><li>기타 중요한 정보</li></ul></td></tr>
<tr><td>참고</td><td>독자가 알아야 할 일회성 정보를 포함하며, 예를 들면 다음과 같습니다: <ul><li>기능 주의사항</li><li>서식 안내</li><li>유용한 참고 사항</li><li>알림 콘텐츠의 심각도가 낮아져 중요 알림에서 강등된 정보(예: 오래된 중요 알림이 일반 참고로 전환되는 경우)</li></ul></td></tr>
<tr><td>팁</td><td>독자가 알아두면 좋은 보충 지식과 권장 사항을 포함하며, 예를 들면 다음과 같습니다: <ul><li>추가 문제 해결 문서</li><li>사용성을 높이는 데 도움이 되는 단계 및 단축키(예: 인앱 메시지의 추가 커스텀 설정)</li></ul></td></tr>
<tr><td>경고</td><td>독자가 반드시 확인해야 하는 필수 정보를 포함하며, 다음과 같은 내용이 포함될 수 있습니다: <ul><li>되돌릴 수 없는 결과(예: 캠페인 및 캔버스 삭제)</li><li>기능을 손상시키는 동작</li><li>데이터 손실</li><li>기타 중대한 경고</li></ul></td></tr>
</tbody>
</table>
{:/}

**알림 모범 사례**  
다음은 알림에 대한 일반 가이드라인과 모범 사례입니다.

일반적으로 문서 구조에 필수적인 콘텐츠(기능 소개, 설정 안내, 기능 사용 단계 등)에는 알림을 사용하지 않는 것이 좋습니다. 확실하지 않은 경우 피어 리뷰 시 팀과 상의하세요.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>가이드라인</th><th>예시</th></tr>
</thead>
<tbody>
<tr><td>알림의 정보를 명확하고 간결한 문장으로 설명합니다.</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">4단계: 세그먼트에 필터 추가 섹션의 참고 알림</a></td></tr>
<tr><td>같은 문서의 여러 섹션에 적용되는 알림의 경우, 반복적인 콘텐츠를 피하기 위해 해당 세부 정보를 담은 새 섹션을 만드는 것을 고려하세요.</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">메시지 참여 이벤트의 등록정보 세부 정보</a></td></tr>
<tr><td>알림 내에서 정보를 짧은 단락이나 목록으로 구분합니다.</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">이메일 목록 가져오기의 중요 알림</a></td></tr>
<tr><td>알림 표시에 영향을 줄 수 있는 추가 서식(코드 스니펫, 단계, 주변 이미지 등)을 고려합니다.</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">가격 인하 알림의 코드 스니펫이 포함된 팁 알림</a></td></tr>
<tr><td>문서 시작 부분에 알림이 오는 경우 줄 바꿈을 포함합니다.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="문서 시작 부분의 알림 예시."><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">콘텐츠 카드 구현 가이드</a></td></tr>
<tr><td>베타 기능에 대해 작성할 때는 베타 상태와 관련 Braze 연락처 정보를 안내하는 중요 알림을 포함합니다. 이 베타 알림은 개요 텍스트 뒤, 첫 번째 주요 제목 앞에 배치합니다.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="베타 기능에 대한 중요 알림 예시."></td></tr>
<tr><td>가능하면 두 개 이상의 알림을 연속으로 사용하지 않습니다. 대신 정보를 재구성하거나 본문의 일부로 포함합니다.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="피해야 할 두 개의 알림이 나란히 있는 예시."></td></tr>
<tr><td>알림이 길어지는 경우 정보를 목록으로 포함하는 새 섹션을 만드는 것을 고려하세요. 예를 들어, 알림에 문제 해결 단계를 포함하는 대신 문제 해결 섹션을 만들거나 관련 문서 링크를 제공하세요.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="새 콘텐츠 섹션의 예시."></td></tr>
</tbody>
</table>
{:/}

## 알림 예시 {#alert-examples}

각 알림 유형이 설명서에서 어떻게, 왜 사용되는지 다음 예시를 참조하세요.

### 중요 알림 {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **문서:** [웹 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **사용 사례:** 독자가 웹 푸시를 설정할 때 알아야 할 필수 기능 주의사항을 포함합니다.
* **알림 선택 이유:** 독자가 웹 푸시를 설정할 때 알아야 할 콘텐츠의 중요도가 높으므로 참고 알림 대신 중요 알림을 사용합니다.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **문서:** [이메일 설정]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **사용 사례:**
  - 청구 가능한 이메일이 두 배로 늘어날 수 있다는 중요한 기능 주의사항을 제공합니다.
  - 필요에 따라 고객 성공 매니저에게 문의하도록 독자를 안내합니다.
* **알림 선택 이유:** 이메일 설정의 BCC 주소에 대한 세부 정보를 전달하기 위해 중요 알림을 사용합니다. 이 정보를 누락해도 기능에 되돌릴 수 없는 영향(기능 손상, 영구적 데이터 손실 등)을 미치지 않으므로 경고 알림 대신 중요 알림이 적합합니다.

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **문서:** [고급 캠페인 설정]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **사용 사례:** 알림 우선순위에 대한 긴급한 기능 주의사항을 포함합니다. 독자를 새로운 정보로 안내합니다.
* **알림 선택 이유:** 독자를 최신 정보로 안내하고 해당 섹션이 특정 사용자에게만 적용됨을 강조하기 위해 중요 알림이 가장 적합합니다. 또한 섹션 제목 뒤에 배치되어 독자가 나머지 섹션을 읽기 전에 중요 알림을 먼저 확인하게 됩니다.

### 참고 알림 {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **문서:** [콘텐츠 카드 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **사용 사례:** 독자가 콘텐츠 카드에 대해 더 알아갈 때 인지해야 할 추가 정보를 포함합니다.
* **알림 선택 이유:** 이 참고 알림은 Braze가 사용자의 오래된 콘텐츠 카드를 순환하는 방식에 대한 배경 정보를 제공합니다. 독자가 알아두면 유용한 보충 정보이며, 중요 알림이나 팁 알림을 사용할 필요는 없습니다.

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **문서:** [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **사용 사례:** 독자가 알아야 할 일반 정보를 포함합니다. 관련 콘텐츠(시간 속성)에 대해 더 알아볼 수 있는 문서를 제공합니다.
* **알림 선택 이유:** 이 정보는 일반적인 정보를 제공하는 것이 목적이므로 중요 알림 대신 참고 알림으로 전달하는 것이 적합합니다. 이 정보를 무시해도 기능의 사용 편의성에 영향을 미치지 않습니다.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **문서:** [커스텀 데이터 관리]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **사용 사례:** 독자가 알아야 할 일반 정보를 포함합니다. 추가 정보를 위해 Braze 담당자에게 안내합니다.
* **알림 선택 이유:** 이 참고 알림은 독자가 커스텀 속성을 관리할 때 알아두면 유용한 데이터 저장에 대한 추가 정보를 제공합니다. 그러나 독자에게 더 강한 중요도를 나타낼 필요가 없으므로 참고 알림이 적합합니다.

### 팁 알림 {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **문서:** [SMS 및 RCS 청구 계산기]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **사용 사례:** 독자가 메시지 길이와 SMS 세그먼트 수를 이해할 수 있는 도구를 포함합니다. 문자 수 제한에 대한 이해에 도움이 될 수 있는 정보를 제공합니다.
* **알림 선택 이유:** 메시지가 몇 개의 세그먼트로 발송되는지 확인할 수 있도록 문구를 입력하는 공간을 제공하기 때문에 긴 팁 알림입니다. SMS 메시지 설정 과정에서 독자가 사용할 수 있는 유용한 생성기이므로 팁 알림이 가장 적합합니다.

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **문서:** [날짜별 일일 앱 삭제 KPI 내보내기]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **사용 사례:** 이 엔드포인트 사용 시 문제 해결 조언을 제공합니다.
* **알림 선택 이유:** 팁 알림은 독자에게 추가 지원을 제공합니다. 콘텐츠의 초점이 문제 해결 문서를 제공하여 독자를 돕는 것이므로 참고 알림 대신 팁 알림을 사용합니다.

### 경고 알림 {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **문서:** [고객 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **사용 사례:** Braze에서 고객 프로필을 생성할 때 독자가 하지 말아야 할 사항을 안내합니다.
* **알림 선택 이유:** 고유하게 식별하기 전에 external_id를 할당하지 않도록 독자에게 주의를 주기 위해 경고 알림을 사용합니다. 고객 프로필에 되돌릴 수 없는 결과를 초래할 수 있으므로 중요 알림 대신 경고 알림으로 전달하는 것이 적합합니다.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **문서:** [커런츠용 Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **사용 사례:** 커런츠 커넥터 생성 시 독자에게 주의를 줍니다. 커넥터를 잘못 생성했을 때의 결과를 포함합니다.
* **알림 선택 이유:** Braze Segment 커런츠 통합의 제한 사항을 설명하기 위해 경고 알림이 가장 적합합니다. 동일한 커런츠 커넥터를 잘못 여러 개 생성하면 데이터 손실이 발생할 수 있으므로 중요 알림 대신 경고 알림을 사용합니다.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **문서:** [캔버스 만들기]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **사용 사례:** 기능이 작동하지 않을 수 있는 정보를 나열합니다. 의도한 오디언스가 캠페인을 수신하지 못하거나 캔버스에 진입하지 못할 수 있는 상황을 자세히 설명합니다.
* **알림 선택 이유:** 기능이 잘못 작동할 수 있는 상황을 안내하기 위해 경고 알림을 사용합니다. 이 정보는 중요하며 캔버스 전달을 손상시킬 수 있으므로 중요 알림 대신 경고 알림으로 전달하는 것이 적합합니다.