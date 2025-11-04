---
nav_title: API 및 식별자
article_title: API 및 식별자
page_order: 3
page_type: reference
description: "이 문서에서는 워크스페이스의 API 식별자를 표시하는 API 및 식별자 페이지에 대해 설명합니다."

---

# API 키

> **API 및 식별자** 페이지는 모든 REST API 키를 한 곳에서 관리할 수 있는 중앙 집중식 허브입니다. 여기에서 각 워크스페이스의 API 키 및 앱 식별자 집합에 액세스할 수 있습니다.

**설정에서** **API 및 식별자** 페이지를 찾을 수 있습니다.

### API 키

이 섹션에서는 워크스페이스의 데이터에 액세스할 수 있는 고유 식별자인 워크스페이스 REST API 키를 제공합니다. Braze API를 요청할 때마다 REST API 키가 필요합니다. API 키 생성 및 사용에 대한 자세한 내용은 [REST API 키 개요]({{site.baseurl}}/api/api_key/)를 참조하세요.

#### API IP 허용 목록

보안을 강화하기 위해 특정 REST API 키에 대해 REST API 요청을 보내도록 허용할 IP 주소와 서브넷 목록을 지정할 수 있습니다. 이를 허용 목록 또는 화이트리스트라고 합니다. 특정 IP 주소나 서브넷을 허용하려면 REST API 키를 새로 생성할 때 **화이트리스트 IP** 섹션에 추가하세요. 

![API IP Whitelisting section of creating a new API key]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

지정하지 않으면 모든 IP 주소에서 요청을 보낼 수 있습니다.

{% alert tip %}
Braze-Braze 웹훅을 생성하고 허용 목록을 사용하려면? [화이트리스트에 추가할 IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) 목록을 확인하세요.
{% endalert %}

### 앱 식별자

이 섹션에는 Braze API에 대한 요청에서 특정 앱을 참조하는 데 사용되는 식별자 목록이 포함되어 있습니다. 애플리케이션 식별자에 대해 자세히 알아보려면 [앱 식별자 API 키]({{site.baseurl}}/api/identifier_types/)를 참조하세요.

### 기타 식별자

API와 통합하려면 Braze 외부 API에서 액세스하려는 세그먼트, 캠페인, 콘텐츠 카드 등과 관련된 식별자를 검색할 수 있습니다. All messages should follow [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding. 이 중 하나를 선택하면 드롭다운 메뉴 아래에 식별자가 표시됩니다.

자세한 내용은 [API 식별자 유형]({{site.baseurl}}/api/identifier_types/)을 참조하세요.

