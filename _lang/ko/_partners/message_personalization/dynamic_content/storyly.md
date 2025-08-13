---
nav_title: Storyly
article_title: Storyly
description: "이 참조 문서에서는 앱 소유자가 세그먼트를 타겟팅하고 Braze에 더 많은 퍼스트파티 데이터를 제공할 수 있도록 지원하는 경량형 SDK인 Storyly와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/)는 스토리를 앱이나 웹사이트에 가져오는 경량 SDK입니다. 직관적인 디자인 스튜디오, 통찰력 있는 분석 및 원활한 연결을 통해 Storyly는 오디언스 경험을 풍부하게 하는 강력한 툴입니다. 

_This integration is maintained by Storyly._

## 통합 정보

Braze와 Storyly 통합을 통해 Braze의 세그먼트를 Storyly 플랫폼의 오디언스로 사용할 수 있습니다. 이 통합을 통해 다음을 수행할 수 있습니다.
- 특정 스토리로 세그먼트를 타겟팅하세요
- 사용자 속성을 사용하여 스토리 콘텐츠를 개인화하세요

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Storyly 계정 | 이 파트너십을 활용하려면 Storyly 계정이 필요합니다. |
| Storyly 소프트웨어 개발 키트 | [Storyly 소프트웨어 개발 키트](https://integration.storyly.io/)를 설치해야 합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키 <br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 Storyly 통합을 통해 앱 소유자는 Braze의 모든 세그먼트에 스토리를 표시하고 사용자 속성으로 스토리를 개인화할 수 있습니다.

일반적인 사용 사례는 다음과 같습니다:

__Storyly에서 Braze 세그먼트 타겟팅__<br>통합이 완료되면 Braze 세그먼트를 기반으로 Storyly 오디언스를 생성할 수 있습니다. 이것은 인구 통계적 또는 행동적 세그먼트일 수 있습니다. 예를 들어 특정 위치에 거주하는 사용자, 귀하의 앱에서 특정 작업을 수행하는 사용자 또는 특정 스토리가 있는 특정 제품에 관심이 있는 사용자를 타겟팅하여 전환을 늘립니다.<br>
__개인화된 stories with user attributes__<br>Braze 사용자 속성은 동적 스토리를 생성하기 위해 Storyly에서도 사용할 수 있습니다. 사용자 이름, 장바구니에 담긴 제품 또는 즐겨찾는 제품을 포함하여 사용자에게 고유한 개인화된 스토리를 제공할 수 있습니다. 개인화는 스토리의 전환율과 전체 스토리 참여율을 높이는 데 도움이 됩니다.

## 데이터 내보내기 통합

Braze Storyly 통합은 다음 비디오에서 설명됩니다:

{% multi_lang_include video.html ID="3-OEqQs48Zw" source="youtube" %}

귀하의 Storyly 통합이 커스텀 매개변수를 포함하도록 하십시오. 이 매개변수는 Braze `external id` 사용자 속성과 일치합니다. 커스텀 매개변수 구현은 [iOS](https://integration.storyly.io/ios/personalization-customaudience.html), [Android](https://integration.storyly.io/android/personalization-customaudience.html), [React Native](https://integration.storyly.io/react-native/personalization-customaudience.html), [Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html), 및 [웹](https://integration.storyly.io/web/personalization-customaudience.html)에 대해 여기에 설명되어 있습니다.

또한 자세한 내용은 [Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) 설명서를 참조할 수 있습니다.

### 1단계: Storyly 대시보드에서 통합을 설정하세요

통합은 **Storyly 대시보드 > 설정 > 통합 > Braze와 연결** 내에서 생성됩니다. 여기에서 Braze REST API 키와 Braze REST 엔드포인트가 필요합니다. 

### 2단계: 세그먼트를 가져오세요 

다음으로, Braze 세그먼트를 사용하여 Storyly 오디언스를 만들 수 있습니다. 이는 **Storyly 대시보드 > 설정 > 오디언스 > 새로운 오디언스 > Braze로 오디언스 생성** 내에서 생성할 수 있습니다.

여기에는 두 가지 동기화 옵션이 있습니다. 특정 캠페인 스토리에 대해 **일회성 동기화**를 선택하거나 장기 스토리에 대해 **일일 동기화**를 선택하세요.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints