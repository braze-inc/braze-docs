---
nav_title: 링크 단축
article_title: 링크 단축
page_order: 3
description: "이 참조 문서에서는 SMS 메시지에서 링크 단축을 켜는 방법과 자주 묻는 질문에 대해 설명합니다."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# 링크 단축

> 이 페이지에서는 SMS 및 RCS 메시지에서 링크 단축을 켜고, 단축 링크를 테스트하고, 단축 링크에 커스텀 도메인을 사용하는 방법 등에 대해 설명합니다.

{% alert important %}
Braze는 [통합 링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified)을 점진적으로 출시하고 있으며, 이를 통해 모든 SMS 및 RCS 단축 링크를 단일 개인화된 링크 형식(예: `brz.ai/abcdefgh`)으로 통합합니다.
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}