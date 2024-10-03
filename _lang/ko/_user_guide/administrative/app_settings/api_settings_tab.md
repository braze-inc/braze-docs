---
nav_title: API 키
article_title: API 키
page_order: 3
page_type: reference
description: "이 참고 문서에서는 워크스페이스의 API 식별을 표시하는 API 키 페이지에 대해 설명합니다."

---

# API 키

> **API 키** 페이지에는 워크스페이스의 API 식별이 표시됩니다. **서비스의** 첫 번째 섹션에는 Braze API의 다양한 용도[(사용자 데이터][3][, 메시징][4], [이메일 동기화][5] 및 [내보내기][6][)][3]에 대한 관련 문서가 나열되어 있습니다.

**API 키** 페이지는 다음 섹션으로 더 세분화되어 있습니다:

- REST API 키
- 식별 작업
- 추가 API 식별자

**설정에서** **API 키** 페이지를 찾을 수 있습니다.

{% alert note %}
이전 탐색을 사용하는 경우 이 페이지는 **API 설정이라고** 하며 **설정** > **설정 관리** 아래에 있습니다.
{% endalert %}

### REST API 키

이 섹션에서는 워크스페이스의 데이터에 액세스할 수 있는 고유 식별자인 워크스페이스 REST API 키를 제공합니다. Braze API를 요청할 때마다 REST API 키가 필요합니다. API 키 생성 및 사용에 대한 자세한 내용은 [REST API 키 개요를]({{site.baseurl}}/api/api_key/) 참조하세요.

#### API IP 허용 목록

보안을 강화하기 위해 주어진 REST API 키에 대해 REST API 요청을 할 수 있는 IP 주소 및 서브넷 목록을 지정할 수 있습니다. 이를 허용 목록 또는 화이트리스트라고 합니다. 특정 IP 주소 또는 서브넷을 허용하려면 새 REST API 키를 만들 때 **화이트리스트 IP** 섹션에 추가하세요: 

![새 API 키 생성의 API IP 화이트리스트 섹션][26]

지정하지 않으면 모든 IP 주소에서 요청을 보낼 수 있습니다.

{% alert tip %}
Braze-Braze 웹훅을 생성하고 허용 목록을 사용하려면? [화이트리스트에 추가할 IP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting) 목록을 확인하세요.
{% endalert %}

### 식별 작업

이 섹션에는 Braze API에 대한 요청에서 특정 앱을 참조하는 데 사용되는 식별자 목록이 포함되어 있습니다. 애플리케이션 식별자에 대해 자세히 알아보려면 [앱 식별자 API 키를]({{site.baseurl}}/api/identifier_types/) 참조하세요.

### 추가 API 식별자

API와 통합하려면 Braze 외부 API에서 액세스하려는 세그먼트, 캠페인, 콘텐츠 카드 등과 관련된 식별자를 검색할 수 있습니다. 모든 메시지는 [UTF-8][12] 인코딩을 따라야 합니다. 이 중 하나를 선택하면 드롭다운 메뉴 아래에 식별자가 표시됩니다.

자세한 내용은 [API 식별자 유형을]({{site.baseurl}}/api/identifier_types/) 참조하세요.

[3]: {{site.baseurl}}/api/endpoints/user_data/
[4]: {{site.baseurl}}/api/endpoints/messaging/
[5]: {{site.baseurl}}/api/endpoints/email/
[6]: {{site.baseurl}}/api/endpoints/export/
[12]: https://en.wikipedia.org/wiki/UTF-8 "위키백과: UTF-8"
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
