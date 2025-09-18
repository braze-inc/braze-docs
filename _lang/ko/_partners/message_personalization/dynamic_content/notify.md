---
nav_title: 알림
article_title: 알림
description: "이 참고 기사는 Braze와 Notify 간의 파트너십을 설명합니다. Notify는 고객 생애주기 전반에 걸쳐 개인화를 제공하는 실시간 옴니채널 개인화 솔루션입니다."
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# 알림

> [알림](https://fr.notify-group.com/)은 고객 관계 관리 도구와 원활하게 통합되어 마케팅 전략을 향상시키고 여러 채널에서 참여를 촉진하는 AI 기반 소프트웨어 솔루션입니다.

브레이즈 및 알림 통합은 마케터가 다양한 플랫폼에서 효과적으로 참여를 유도할 수 있도록 합니다. 기존 마케팅 방식에 의존하는 대신, Braze API로 트리거되는 캠페인은 Notify의 기능을 활용하여 이메일, SMS, 푸시 알림 등 여러 채널을 통해 개인화된 메시지를 전달할 수 있습니다.

## 필수 조건

시작하기 전에 다음이 필요합니다:

| 요구 사항          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Braze REST API 키  | `users.export.segment` 및 `campaigns.trigger.send` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| CNAME 구성 | 이메일에서 사용되는 추적 픽셀에 대한 서브도메인이 생성되어야 하며, Notify는 메시징을 통해 사용자 참여를 추적하여 모델을 더욱 알리기 위해 사용됩니다. 서브도메인 URL이 생성된 후 Notify와 공유하세요. |
| 데이터베이스 옵트인 내보내기 | 지난 1년(12개월) 동안의 캠페인 및 구매 데이터를 Notify로 전송하세요. ​이 수출은 Notify 예측 모델을 훈련하는 데 사용될 것입니다. <br><br> **필드:** <br><br> **이메일:** 이메일의 SHA256 해시로, 소문자로 변환하고 앞뒤의 공백을 제거합니다.<br><br>**세그먼트:** 활동 수준(활성 또는 비활성)을 정의하는 세그먼트 정보.<br><br>**하위 세그먼트:** 구매 활동 수준과 같은 기타 관련 활동 정보.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 캠페인 만들기

Braze에서 [API 트리거 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery)을 생성합니다. 그런 다음, Notify와 함께 캠페인 `api_identifier`를 공유하세요.

### 2단계: Braze에서 세그먼트를 생성하세요

다음으로, [Step 1](#step-1-create-your-campaign)에서 생성된 캠페인으로 타겟하고자 하는 사용자 세그먼트를 생성합니다. 그런 다음 세그먼트 ID를 Notify와 공유하십시오.

### 3단계: 세그먼트를 가져오세요

그런 다음, Notify는 캠페인에 첨부된 세그먼트의 사용자들을 내보낼 것입니다.

### 4단계: 알림은 캠페인을 시작합니다.

`/campaigns/trigger/send` 엔드포인트를 사용하여 Notify의 AI는 [Step 1](#step-1-create-your-campaign)에서 생성된 Braze 캠페인을 트리거하여 사용자가 참여할 가능성이 가장 높은 시점에 전송합니다.
