---
nav_title: 딥링킹을 위한 Branch
article_title: 딥링킹을 위한 Branch
alias: /partners/branch_for_deeplinking/
page_type: partner
description: "이 참조 문서에서는 Branch와 Braze 간의 파트너십과 이를 사용하여 딥링킹 실습을 지원하는 방법을 설명합니다."
search_tag: Partner

---

# 딥링킹을 위한 Branch {#branch}

{% multi_lang_include video.html ID="PwGKqfwV-Ss" align="right" %}

> 모바일 연결 플랫폼인 [Branch][1]는 모든 사용자 터치포인트에 대한 종합적인 관점을 제시하므로, 모든 기기와 채널, 플랫폼에서의 고객 유치, 참여, 측정에 효과적입니다.

_이 통합은 Branch에서 유지 관리합니다._

## 통합 정보

Braze와 Branch 통합을 통해 사용자의 여정 초반에 올바르게 [기여도]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_attribution/)를 평가하고 딥링크를 통해 원하는 위치로 연결하여 고객에게 더 나은 경험을 제공할 수 있습니다.

## 통합

[Branch의 SDK 통합 가이드](https://help.branch.io/developers-hub/docs/native-sdks-overview)를 따라 Branch 통합을 시작하고 실행합니다. 다음의 추가 사용 사례를 참조하십시오.

### iOS 유니버설 링크 지원

Braze 내에서 iOS 유니버설 링크를 딥링크로 보내는 것을 지원하려면 다음을 수행합니다.

1. Branch의 설명서를 따라 [유니버설 링크][3]를 설정하십시오.
2. Braze SDK 통합에서 [`BrazeDelegate`][4] 메서드 [braze(_:shouldOpenURL:)][5]를 구현하여 앱 내에서 [유니버설 링크를 라우팅][6]합니다.

### 이메일에서 딥링킹

[유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)에 대한 설명서를 참조하십시오
또는 [Branch 설명서](https://help.branch.io/developers-hub/docs/ios-universal-links#apps-that-always-work)를 참조하여 Braze를 통해 발송된 이메일에서 딥링킹을 설정합니다.

전화번호에 연결(`tel`을 `href`에 추가) 기능은 사용자가 앱에 통화 권한을 부여하지 않는 한 iOS용 Gmail 앱에서 지원되지 않습니다.

ESP에 따라 클릭 추적 유니버설 링크를 지원하려면 추가 사용자 지정이 필요할 수 있습니다. 이 정보는 해당 문서에서 간략히 설명합니다. 다음 참고 자료를 참조하여 더 자세히 알아볼 수 있습니다:

- [SendGrid][7]
- [SparkPost][9]


[1]: https://branch.io/
[2]: {{site.baseurl}}/partners/branch_for_attribution/
[3]: https://help.branch.io/developers-hub/docs/ios-universal-links
[4]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[5]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:shouldopenurl:)-6xxc5
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/#linking-handling-customization
[7]: https://help.branch.io/using-branch/page/braze-sendgrid
[9]: https://help.branch.io/using-branch/page/braze-sparkpost
