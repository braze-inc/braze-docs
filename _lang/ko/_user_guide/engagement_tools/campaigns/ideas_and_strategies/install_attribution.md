---
nav_title: 사용자 설치 이해
article_title: 사용자 설치 이해 
page_order: 7
page_type: reference
description: "이 참조 문서에서는 사용자 설치(설치 어트리뷰션 추적)와 캠페인 내에서 이 정보를 적용하는 다양한 방법에 대해 설명합니다."
tool:
  - Campaigns
  - Segments
---

# 사용자 설치 이해

> 설치 어트리뷰션 추적은 사용자와의 초기 관계를 개선할 수 있는 좋은 방법입니다. 사용자가 앱을 설치하는 방법, 위치, 더 중요한 이유는 무엇인지 알면 사용자가 어떤 사람인지, 어떻게 앱을 소개해야 하는지 더 잘 이해할 수 있습니다. 

While Braze does not provide install attribution tracking, we can integrate with [services]({{site.baseurl}}/partners/message_orchestration/) such as Branch and AppsFlyer to seamlessly provide you with install data.

## 사용자 세분화

Once your user installs your app, you can begin segmenting them based on the following [install attribution filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution). 예를 들어, 여행 앱에서 해변 휴가 상품과 관련된 광고를 통해 유입된 사용자를 '해변 애호가' 세그먼트에 추가할 수 있습니다. 마찬가지로, 음악 앱은 설치를 유도한 광고에 표시된 음악 장르에 따라 사용자를 세분화할 수 있습니다.

## 모범 사례

### 개인화된 온보딩

이제 사용자에 대한 더 많은 정보를 확보했으므로 온보딩 프로세스를 개인화할 수 있습니다. 이는 사용자의 선호도에 맞게 메시지의 이미지를 변경하는 것처럼 간단할 수도 있고, 설치로 이어질 수 있는 각 광고에 대해 고유한 사용자 온보딩을 생성하는 것처럼 복잡할 수도 있습니다. To scale out a fully comprehensive sequence of messages that can take user behavior into consideration, refer to our documentation on [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### 광고의 참조 데이터

사용자는 프로모션 제안이나 경품을 통해 앱에 매력을 느낄 수 있습니다. 설치 어트리뷰션 데이터를 사용하면 이러한 프로모션으로 인해 설치한 사용자에게만 할인 코드나 오퍼가 포함된 캠페인을 보낼 수 있습니다. In a similar manner, if your ad contains information on a particular product (such as a specific movie in a video app or sale in an eCommerce app), you can send campaigns directing users to the correct page of your app.

## 광고 활동 평가

설치 경로 데이터는 다양한 마케팅 캠페인의 효과를 평가하는 데 유용할 수 있습니다. 어떤 광고와 캠페인이 가장 많은 인스톨을 유도하고 어떤 광고와 캠페인이 뒤처지는지 확인하면 가장 매력적인 광고에 리소스를 집중하는 데 활용할 수 있습니다.

