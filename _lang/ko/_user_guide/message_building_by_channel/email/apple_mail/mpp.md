---
nav_title: 애플 메일 개인정보 보호
article_title: iOS 15용 애플 메일 개인정보 보호
page_order: 1
description: "이 참조 문서에서는 애플 메일 개인정보 보호 업데이트, 영향을 받을 사람, 그리고 이 기능을 준비하기 위한 몇 가지 다음 단계를 다룹니다."
channel:
  - email

---

# 애플의 메일 개인정보 보호

## 애플의 메일 개인정보 보호 업데이트란 무엇인가요?

애플의 메일 개인정보 보호(MPP)는 iOS 15, iPadOS 15, macOS Monterey 및 watchOS 8에서 애플 메일 앱 사용자에게 제공되는 개인정보 업데이트로, 2021년 9월 중순에 출시되었습니다. MPP에 참여하기로 선택한 사용자(대부분의 사용자가 그렇게 할 것으로 예상됨)의 경우, 이메일은 이제 프록시 서버를 사용하여 미리 로드되며, 이미지를 캐시하고 메트릭과 같은 추적 픽셀을 활용하는 능력을 저해합니다 [오픈 추적]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel). 

브랜드는 MPP로 인해 이메일 배달 메트릭 및 이러한 메트릭에 따라 트리거되는 기존 캠페인 및 캔버스와 관련된 문제가 발생할 것으로 예상해야 합니다. 이메일 배달에 미치는 영향을 이해하려면 [이메일 보고]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)를 참조하세요.

### 누가 영향을 받을까요?

다음에서 기본 애플 메일 앱을 사용하는 모든 수신자:

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

이것은 애플 메일 앱에 메일 계정을 연결하고 보안 기능에 참여하기로 선택한 모든 사용자에게 적용됩니다. 이메일 서비스(Gmail, Outlook, Yahoo, AOL 등)에 관계없이. 이 영향은 Apple/iCloud/me.com 이메일 주소로 메일을 받는 구독자에게만 국한되지 않습니다.

{% alert important %}
이메일 배달에 대한 이러한 업데이트는 중요하지만, MPP는 이메일 및 배달을 규제하는 규칙을 근본적으로 변경하지 않습니다. 대신, 성공을 벤치마킹하는 방식과 앞으로 사용할 수 있는 이메일 도구 및 기능에 영향을 미칠 것입니다.
{% endalert %} 

## MPP에 대비하는 방법은 무엇인가요?

브랜드가 MPP와 그로 인한 이메일 마케팅 및 전반적인 고객 참여 노력에 미치는 잠재적 영향을 어떻게 대응할지 고민하기 시작하는 데 있어 시간은 매우 중요합니다. 사용자에게 다음을 권장합니다:

- MPP가 마케팅 노력에 미치는 위험을 평가하십시오.
- Braze 플랫폼에서 자동화 조정에 대한 대응 계획을 수립하고, 배달 최적 관행을 강화하며, 성과를 측정하기 위한 더 넓은 지표 세트를 개발하십시오.
- 가능한 한 빨리 그 대응 계획을 실행하십시오.

Apple의 메일 프라이버시 보호에 대비하는 방법에 대한 심층 개요는 [블로그 게시물](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)을 확인하세요. 
