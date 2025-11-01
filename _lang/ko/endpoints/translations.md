---
nav_title: 번역
article_title: 번역 엔드포인트
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "이 랜딩 페이지에는 Braze 번역 엔드포인트가 나열되어 있습니다."
page_type: landing

guide_top_header: "번역 엔드포인트"
guide_top_text: "Braze 번역 엔드포인트를 사용하여 캠페인과 캔버스에서 번역을 관리하고 업데이트하세요."

guide_featured_title: "캠페인 엔드포인트"
guide_featured_list:
  - name: "GET: 캠페인 번역 보기"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 캠페인의 모든 번역 보기"
    link: /docs/api/endpoints/translations/campaigns/get_bulk_translations_campaigns/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: 캠페인에서 번역 업데이트"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "GET: 캔버스에 대한 번역 보기"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 캔버스에 대한 모든 번역 보기"
    link: /docs/api/endpoints/translations/canvas/get_bulk_translations_canvases/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: 캔버스에서 번역 업데이트"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  
guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "GET: 소스 번역 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 특정 번역 및 로캘 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 모든 번역 및 로캘 보기"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: 이메일 템플릿에서 번역 업데이트"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
Braze 번역 엔드포인트는 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 번역 엔드포인트 작동 방식

당사의 번역 엔드포인트는 [다국어 구성과]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/) 함께 작동하며, 메시지를 받는 사용자에 따라 메시지가 다른 버전으로 렌더링될 수 있습니다.

### Prerequisites

이러한 엔드포인트를 사용하기 전에 [로캘을 추가해야]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale) 합니다.

### 번역을 테스트하는 방법

캠페인, 캔버스(개별 단계 포함) 및 이메일 템플릿에서 API 및 Braze 대시보드를 사용하여 번역 지원을 검증하는 방법에는 두 가지가 있습니다:

- 구성 중(출시 전)
- 출시 후(출시 후 초안 사용)

번역 업데이트를 테스트하기 전에 먼저 번역을 업데이트해야 합니다:

1. [로캘을 추가합니다]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. 메시지를 작성하고 적절한 경우 번역 태그를 사용합니다.
3. 메시지를 저장합니다.
4. 포함할 로캘을 선택합니다.
