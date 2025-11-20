---
nav_title: API 및 SDK 엔드포인트
article_title: API 및 SDK 엔드포인트
page_order: 1
page_type: reference
description: "이 참조 문서에는 사용 가능한 Braze 인스턴스에 대한 대시보드 URL, API 엔드포인트 및 SDK 엔드포인트가 나열되어 있습니다."

---

# API 및 SDK 엔드포인트

> Braze 인스턴스는 Braze에 로그인하고, API에 액세스하고, SDK를 통합하는 데 필요한 URL을 결정합니다. Braze 학습 과정인 [Braze 101에서](https://learning.braze.com/braze-101) 소프트웨어 개발 키트에 대해 자세히 알아보세요.

Braze는 "클러스터"라고 부르는 대시보드, SDK 및 REST 엔드포인트에 대한 다양한 인스턴스를 관리합니다. Braze 온보딩 매니저가 어느 클러스터에 속해 있는지 알려줄 것입니다.

에서 로그인하면 [dashboard.braze.com](https://dashboard.braze.com) 에 로그인하면 자동으로 올바른 클러스터 주소로 이동합니다.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
SDK를 통합할 때는 SDK 엔드포인트를 사용하세요. REST API를 호출할 때는 REST 엔드포인트를 사용하세요.
{% endalert %}

API 액세스에 대한 자세한 내용은 [API 개요 문서를]({{site.baseurl}}/api/basics/) 참조하세요. 
