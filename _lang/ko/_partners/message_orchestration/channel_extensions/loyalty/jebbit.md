---
nav_title: Jebbit
article_title: Jebbit
description: "이 참조 문서에서는 사용자 데이터로 Jebbit 캠페인의 사용자 이메일과 속성을 실시간으로 Braze에 전달할 수 있는 PaaS인 Braze와 Jebbit 간의 파트너십에 대해 설명합니다."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/)은 사용자가 퍼스트파티 데이터를 수집하기 위해 매력적인 경험을 구축할 수 있는 PaaS입니다.

_이 통합은 Jebbit에서 유지 관리합니다._

## 통합 정보

Braze와 Jebbit의 통합을 통해 Jebbit 캠페인에서 사용자 이메일과 속성을 실시간으로 Braze에 사용자 데이터로 전달할 수 있습니다. 이 데이터는 개인화된 이메일 캠페인 및 트리거와 같은 마케팅 이니셔티브를 추진하는 데 사용될 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
|Jebbit 계정 | 이 파트너십을 이용하려면 Jebbit 계정이 필요합니다. |
| Braze REST API 키 | 모든 사용자 데이터 권한이 있는 Braze REST API 키입니다. <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
|Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의]({{site.baseurl}}/api/basics/#endpoints) Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Jebbit과의 통합을 요청할 때, 기한을 맞추기 어려운 부분이 있으면 알려주세요. 또한 Braze에 전달할 Jebbit 경험에 매핑된 속성이 있는지 확인합니다.

### 1단계: API 자격 증명 제공

Dropbox 파일 요청을 통해 API 자격 증명을 텍스트 파일로 Jebbit에 제공합니다.
다음 [Dropbox URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx)을 사용하여 파일을 제출합니다.

### 2단계: 시험 제출 확인

통합에 할당된 Jebbit 엔지니어가 Jebbit에서 Braze로 테스트 제출을 푸시하므로 Braze 환경에서 데이터가 표시되는 형태를 확인할 수 있습니다. 이것이 통합을 활성화하는 마지막 단계입니다. 이제 Jebbit 데이터가 설정되었으니, 이를 활용하여 마케팅 이니셔티브를 추진하세요.

{% alert note %}
Jebbit에서 설정한 속성 ID는 Braze에서 속성 필드 이름이 표시되는 방식입니다.
{% endalert %}

## 사용자 지정

현재 특별히 [사용자 데이터]({{site.baseurl}}/api/endpoints/user_data/) 엔드포인트를 지원하지만, 다른 엔드포인트에 대한 요청도 지원할 수 있습니다.

속성 필드 이름도 원하는 대로 사용자 지정할 수 있습니다.

Braze에서 Jebbit의 추가 속성을 원하는 경우, Jebbit 계정에서 새 속성을 매핑합니다. 해당 속성에 대한 데이터를 수집하면 해당 속성이 Braze에 자동으로 표시됩니다.

