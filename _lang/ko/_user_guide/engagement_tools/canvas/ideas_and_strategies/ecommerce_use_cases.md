---
nav_title: 전자상거래 사용 사례
article_title: 전자상거래 사용 사례
alias: /ecommerce_use_cases/
page_order: 4
description: "이 참고 문서에서는 이커머스 마케터를 위해 특별히 맞춤화된 몇 가지 사전 구축된 Braze 템플릿을 통해 필수 전략을 쉽게 구현할 수 있습니다."
toc_headers: h2
---

# 전자상거래 추천 이벤트 사용 방법

> 이 페이지에서는 Braze 전자상거래 캔버스 템플릿 사용 방법을 포함하여 플랫폼 전반에서 전자상거래 추천 이벤트를 어떻게 그리고 어디에서 사용할 수 있는지 설명합니다.

{% alert important %}
[전자상거래 추천 이벤트는]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 고객 성공 관리자에게 문의하세요. <br><br>새로운 Shopify 커넥터를 사용하는 경우 통합을 통해 전자상거래 추천 이벤트를 자동으로 사용할 수 있습니다.
{% endalert %}

## 캔버스 템플릿 사용

캔버스 템플릿을 사용하려면
1. **메시징** > **캔버스로** 이동합니다.
2. **캔버스 만들기** > **캔버스 템플릿 사용을** 선택합니다.
3. **Braze 템플릿** 탭에서 사용하려는 템플릿을 찾아봅니다. 템플릿의 이름을 선택하여 미리 볼 수 있습니다.
4. 사용하려는 템플릿에 대해 **템플릿 적용을** 선택합니다.<br><br>!["캔버스 템플릿" 페이지가 "Braze 템플릿" 탭으로 열리고 최근 사용된 템플릿 목록과 선택 가능한 Braze 템플릿이 표시됩니다.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eCommerce 캔버스 템플릿

Braze는 네 가지 전자상거래 캔버스 템플릿을 제공합니다.

{% multi_lang_include canvas/ecommerce_templates.md %}

## 메시지 개인화

[Liquid는]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 고객을 위한 역동적이고 개인화된 콘텐츠를 제작할 수 있는 강력한 템플릿 언어로, Braze에서 사용합니다. Liquid 태그를 사용하면 고객 데이터, 제품 정보 및 기타 변수를 기반으로 메시지를 사용자 지정하여 쇼핑 경험을 개선하고 참여를 유도할 수 있습니다.

### Liquid의 주요 기능

- **동적 콘텐츠:** 이름, 주문 세부 정보, 기본 설정 등 고객별 정보를 메시지에 삽입하세요.
- **조건부 논리:** 특정 조건(예: 고객 위치 및 구매 내역)에 따라 다른 콘텐츠를 표시하려면 if/else 문을 사용합니다.
- **루프:** 제품 또는 고객 데이터 컬렉션을 반복하여 항목의 목록 또는 그리드를 표시합니다.

### Liquid 시작하기

Liquid 태그를 사용하여 메시지를 맞춤 설정하려면 다음 리소스를 참조하세요:

- 사전 정의된 리퀴드 태그가 포함된 [Shopify 데이터]({{site.baseurl}}/shopify_features/#shopify-data) 참조
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## 세분화

Braze 세그먼트를 사용하여 특정 속성 및 행동을 기반으로 타겟 고객 세그먼트를 생성하고 개인화된 메시지와 캠페인을 전달할 수 있습니다. 이 강력한 기능을 사용하면 적시에 적절한 메시지를 적절한 대상에게 전달하여 고객의 참여를 효과적으로 유도할 수 있습니다.

세그먼트 시작하기에 대한 자세한 내용은 [브레이즈 세그먼트 소개를]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments) 참조하세요.

### 추천 이벤트

이커머스 이벤트는 [추천 이벤트를]({{site.baseurl}}/recommended_events/) 기반으로 합니다.
추천 이벤트는 사용자 지정 이벤트이므로 [사용자 지정 이벤트 필터를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters) 선택하여 추천 이커머스 이벤트 이름을 검색할 수 있습니다.

### 전자상거래 필터

세분화 도구 내의 **전자상거래** 섹션으로 이동하여 **전자상거래 소스** 및 **총 수익과** 같은 전자상거래 필터를 사용하여 사용자를 세분화합니다. 

전자상거래 필터 및 정의 목록은 [세그먼트 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)를 참조하고 "전자상거래" 검색 카테고리를 선택하십시오.

!["전자상거래" 필터가 있는 세그먼트 필터 드롭다운.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## 중첩된 이벤트 속성

중첩된 이벤트 속성을 기준으로 [세그먼트하려면 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) 활용하면 됩니다. 예를 들어 세그먼트 확장을 사용하여 지난 90일 동안 'SKU-123' 제품을 구매한 사람을 찾을 수 있습니다.

## 분석

### 커스텀 이벤트 보고서

전자상거래 추천 이벤트 수량을 [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics)에서 추적할 수 있습니다. **커스텀 이벤트 수행**로 필터링한 다음, 성과를 시간에 따라 보기 위해 [전자상거래 추천 이벤트 이름]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events)을 지정하십시오.

![여섯 개의 선택된 이벤트에 대한 결과를 표시하는 커스텀 이벤트 차트.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### 대시보드

#### 전환 대시보드

"주문하기" 전환 이벤트를 사용하여 캠페인이나 캔버스를 시작한 후, 성과를 추적하기 위해 해당하는 [전환 보고서]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#setting-up-your-report)를 생성할 수 있습니다.

![캠페인 및 캔버스와 관련된 전환 통계가 포함된 전환 세부정보 테이블.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### 전자상거래 매출 대시보드

사용자가 주문하기 전에 상호작용한 마지막 캠페인 또는 캔버스에 귀속된 매출에 대한 통찰력을 얻으려면 [전자상거래 매출 대시보드]({{site.baseurl}}/ecommerce_revenue_dashboard/)를 사용하고 전환 창을 선택하십시오.

### 매출 보고서 

이 새로운 이벤트의 데이터를 분석하려면 [대시보드 빌더]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/)로 가서 [**전자상거래 매출 - 마지막 터치 기여도** 대시보드]({{site.baseurl}}/ecommerce_revenue_dashboard/)를 확인하십시오.
