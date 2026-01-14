---
nav_title: 로플랫
article_title: 로플랫
description: "이 참조 기사에서는 Braze와 오프라인 위치 기반 마케팅 플랫폼인 loplat 간의 파트너십을 설명하여 위치 컨텍스트를 추가하여 근접 마케팅 캠페인을 실행할 수 있도록 합니다."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# 로플랫

> [Loplat](https://www.loplat.com/) is the leading offline location-based platform. loplat 소프트웨어 개발 키트를 사용하여 매장의 유동 인구를 스마트하게 증가시키고 매장 내 구매를 유도하는 마케팅 캠페인을 실행하세요. 캠페인이 끝난 후 유동 인구 분석을 통해 매장 성능을 측정할 수 있습니다.

_This integration is maintained by Loplat._

## 통합 정보

Braze와 loplat 통합을 통해 loplat의 위치 서비스(매장 POI 및 커스텀 지오펜스)를 사용하여 지오-상황별 마케팅 캠페인을 트리거하고 오프라인 세분화를 사용하여 커스텀 이벤트를 생성할 수 있습니다. 사용자가 loplat X에서 설정한 타겟 위치를 방문하면, 캠페인과 위치 정보가 Braze로 즉시 전송됩니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| loplat X 계정 | 이 통합을 활용하려면 loplat X 계정이 필요합니다.<br><br>Email [support@loplat.com](mailto:support@loplat.com) to request a loplat X account. |
| loplat SDK | loplat SDK는 사용자의 스토어 방문을 인식하고, 위치 이벤트를 처리하며, 사용자가 장소에 머무르는지 이동 중인지 구별합니다. 귀하는 loplat 소프트웨어 개발 키트를 사용하여 상점의 유동 인구를 분석하고 사용자가 상점에 들어올 때 푸시 메시지를 보내는 등의 작업을 수행할 수 있습니다.<br><br>SDK는 Android 및 iOS에서만 사용할 수 있습니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키입니다:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

loplat에서 제공하는 커스텀 이벤트 위치 정보는 캠페인에서 다음과 같은 사용 사례를 달성하는 데 사용할 수 있습니다.

- [Duty-free promotion alert](https://www.loplat.com/loplat-x#usecase)
    - 공항 탑승구 근처에 있는 사용자에게 면세점 할인 쿠폰을 보내세요.
- 전기차 (EV) 충전소 위치 푸시
    - EV 충전소 주변에 지오펜스를 설정하고 사용자가 충전소 근처에 있을 때 알림을 보내 충전을 권장합니다.

## 통합

### 1단계: SDK 통합

Integrate the loplat SDK and the Braze SDK in your app using the steps provided in the [loplat-Braze integration](https://developers.loplat.com/braze/) documentation.

### 2단계: Braze와 loplat X 대시보드를 동기화하고 캠페인을 만드세요

Braze 대시보드에서 새 API 키를 생성하세요. API 키를 복사하여 loplat X 대시보드의 **설정 > API 설정**에 붙여넣으세요. 자세한 내용은 [loplat X 사용 설명서](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25)를 참조하십시오.

#### API 트리거 전달

1. Braze 캠페인 또는 캔버스를 생성하여 **API-Triggered 전달**로 보내고 캠페인 ID를 복사합니다.
2. 모든 단계를 완료한 후 Braze에서 캠페인을 시작하세요.
3. Go to loplat X and create a campaign following the instructions in the [loplat X user's guide](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. **캠페인 메시지 설정**에 Braze 캠페인 ID를 붙여넣고 캠페인을 시작하세요.

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### 실행 기반 전달

통합을 통해 지오펜스 정보, 지역, 브랜드 이름 또는 스토어 이름을 보내 위치 조건을 적용할 수 있습니다. 또한 생성한 커스텀 이벤트로 세그먼트를 추가하거나 전환을 할당할 수 있습니다.
1. Create a loplat X campaign following the instructions in the [loplat X user's guide](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. **캠페인 메시지 설정**에서 커스텀 이벤트를 추가하고 캠페인을 시작하세요.
3. Braze 대시보드로 이동하여 **실행 기반 전달**로 전송되는 캠페인 또는 캔버스를 만드세요.
4. loplat X에서 생성한 커스텀 이벤트를 선택하여 위치 트리거 동작을 설정합니다.

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})


