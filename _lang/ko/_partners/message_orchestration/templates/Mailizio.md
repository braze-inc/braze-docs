---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "이 참고 문서에서는 재사용 가능하고 브랜드에 안전한 콘텐츠를 디자인하여 Braze로 내보낼 수 있는 이메일 제작 및 관리 플랫폼인 Mailizio와 Braze의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio는](https://mailizio.com/) 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인을 배포할 수 있습니다.

_이 통합은 Mailizio에서 유지 관리합니다._

## 통합 정보

Mailizio와 Braze의 통합을 통해 Mailizio의 편집기를 사용하여 동적 이메일 템플릿을 디자인하고, Braze 구성에 사용된 Liquid 변수를 활용하고, 이를 Braze로 푸시하여 캠페인을 간소화할 수 있습니다.

## 사용 사례

- 캠페인 및 트랜잭션 메시지를 위해 바로 보낼 수 있는 이메일 템플릿을 Braze에 푸시하세요.
- 재사용 가능한 콘텐츠 모듈(헤더, 푸터, 프로모션 등)을 구축하여 여러 캠페인과 채널에서 제작을 간소화하세요.
- 이메일에서 인앱 메시지를 생성하세요: Mailizio는 이메일의 관련 섹션을 식별하고 인앱 캠페인에 사용할 수 있도록 HTML을 내보낼 수 있습니다.
- 이메일과 인앱 메시지 모두에서 Braze와 호환되는 Liquid 변수를 사용하여 대규모로 개인화할 수 있습니다.
- Mailizio에서 크리에이티브 자산을 관리하고 한 번의 내보내기로 Braze에서 업데이트하여 브랜딩의 일관성을 유지하세요.

## 필수 조건

| Requirement | 설명 |                          
| ----------- | ----------- |  
| Mailizio 계정 | 이 파트너십을 이용하려면 Mailizio 계정이 필요합니다. |  
| Braze REST API key | A Braze REST API key with full **Templates** permissions.<br><br>**설정** > **API 키에서** Braze 대시보드의 REST API 키를 생성할 수 있습니다. |  
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Mailizio 고객 성공 매니저에게 Braze REST API 키와 클러스터 인스턴스를 제공하세요. 그런 다음 Mailizio 팀이 초기 통합을 설정합니다.

{% alert important %}
이 설정은 일회성 설정이며 향후 모든 내보내기는 이 API 키를 자동으로 사용합니다.
{% endalert %}

### 1단계: 메일리지오에서 이메일 만들기

Mailizio에서 드래그 앤 드롭 편집기를 사용하여 브랜드 아이덴티티를 반영한 이메일을 구축한 다음 **저장을** 클릭하여 작업을 보존하세요.

![드래그 앤 드롭 편집기 스크린샷]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### 2단계: Export your email template to Braze

준비가 되면 **뉴스레터 내보내기를** 클릭합니다. 팝업에서 **Braze 이메일을** 선택하고 내보내기를 확인합니다.

나중에 콘텐츠를 업데이트하는 경우 Mailizio에서 내보내기를 다시 수행하여 Braze에서 새로고침하세요.

![모달 스크린샷 내보내기]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
Mailizio의 **모듈** 편집기를 사용하여 동일한 방식으로 콘텐츠 블록을 생성하고 내보낼 수 있습니다.  
{% endalert %}

## Usage

Braze 계정의 **템플릿 & 미디어 > 이메일 템플릿** 섹션에서 업로드한 메일리지오 템플릿을 찾으세요. You can now use this email template to start sending engaging email messages to your customers!
