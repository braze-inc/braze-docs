---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Braze와 Alpaco의 통합을 통해 Alpaco의 구문을 활용하여 데이터 기반 이메일 템플릿을 생성하고 Braze로 내보낼 수 있습니다."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/)는 새로운 차원의 디자인 및 출력 제어를 위한 드래그 앤 드롭 이메일 편집기를 제공하는 온라인 이메일 마케팅 툴입니다. Braze와 Alpaco의 통합을 통해 브랜드 및 데이터 기반 이메일을 Braze로 내보낼 수 있습니다. 

{% alert note %}
Alpaco는 [모든 Liquid](https://shopify.github.io/liquid/) 변수를 지원하므로, Braze 구성에 사용되는 모든 Liquid 변수도 완벽하게 지원합니다.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| ------------| ----------- |
| Alpaco 계정 | 이 파트너십을 활용하려면 Alpaco 계정이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| 클러스터 인스턴스 | Braze [클러스터 인스턴스]({{site.baseurl}}/api/basics/#endpoints)는 Braze 대시보드 및 REST 엔드포인트에 맞춰 조정됩니다. <br><br> 예를 들어 대시보드 URL이 `https://dashboard-03.braze.com`인 경우 엔드포인트는 `dashboard-03`입니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

Alpaco 고객 성공 팀에 Braze REST API 키와 클러스터 인스턴스를 제공합니다. 팀에서 초기 통합을 설정합니다.

{% alert note %}
이 설정은 일회성 설정이며 향후 모든 내보내기에서는 이 API 키를 자동으로 사용합니다.
{% endalert %}

## Alpaco 이메일을 Braze로 내보내기

### 1단계: Alpaco에서 이메일 템플릿 생성

Alpaco 플랫폼에서 다양한 설정과 옵션을 사용하여 브랜드 정체성을 표현하는 템플릿을 생성할 수 있습니다. 템플릿이 마음에 들면 **저장을** 선택합니다.

![Alpaco 템플릿 생성]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### 2단계: 이메일 만들기

템플릿이 생성되면 로비로 이동하여 템플릿이 포함된 이메일을 작성합니다. **검토**를 선택하여 모든 정보가 제대로 표시되는지 확인합니다.

![Alpaco 이메일 생성]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### 3단계: 이메일 검토 및 Braze로 내보내기

**내보내기**를 선택하고 Braze 통합을 선택하여 이메일 템플릿을 Braze로 내보냅니다. 

이메일 템플릿을 변경하려면 Alpaco에서 변경한 다음, 이메일을 Braze로 다시 내보냅니다. 이렇게 하면 변경 사항이 담긴 이메일이 Braze에 업데이트됩니다.

![Alpaco 이메일 내보내기]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Braze에서 Alpaco 이메일 템플릿 사용

Braze 대시보드에서 **템플릿 및 미디어 > 이메일 템플릿**으로 이동하여 업로드한 Alpaco 이메일을 찾습니다. 이제 이 템플릿을 사용하여 사용자에게 브랜드 및 데이터 기반 이메일을 보낼 수 있습니다.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
