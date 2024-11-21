---
nav_title: 개요
article_title: 개요
description: "이 참조 문서에서는 행동 트리거, 세분화 등을 기반으로 광고를 전달하기 위해 Facebook에 Braze 오디언스 동기화를 사용하는 방법을 다룹니다."
page_order: 0
Tool:
  - Canvas

---

# 오디언스 동기화 개요

> Braze 오디언스 동기화 기능을 통해 다수의 주요 소셜 및 광고 기술로 캠페인의 도달 범위를 확장할 수 있습니다. [Braze 캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas)를 통해 브랜드는 마케팅 및 운영 효율성을 높이기 위해 광고 생태계에 퍼스트파티 사용자 데이터를 동적으로 안전하게 동기화할 수 있습니다.

## 사용 사례

- 구매 또는 인게이지먼트를 유도하도록 소유 채널 및 유료 채널을 통해 가치가 높은 사용자 타겟팅.
- 가치가 높은 사용자의 유사한 오디언스를 생성하여 신규 사용자 획득 비용과 전환율 최적화.
- 다른 마케팅 채널에 대한 반응성이 낮은 사용자를 광고로 리타겟팅.
- 브랜드의 충성 소비자인 사용자는 광고를 받지 않도록 억제 오디언스 생성.

## 기능 가용성

모든 Braze 고객은 즉시 Google 및 Facebook에 오디언스 동기화 기능에 액세스할 수 있습니다. 추가 오디언스 동기화 대상(예: TikTok, Pinterest, Snapchat 또는 Criteo)을 잠금 해제하려면 Audience Sync Pro를 구매해야 합니다. 자세한 내용은 Braze 계정 매니저에게 문의하십시오.

## 작동 방식

Google 또는 Facebook에 오디언스 동기화를 사용하려면 **기술 파트너** 페이지에서 파트너를 검색하여 광고 계정을 연결합니다.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

광고 계정을 연결한 후, 오디언스 동기화 단계가 포함된 캔버스를 생성할 수 있습니다.

![][22]{: style="max-width:75%;"}

다음으로, 오디언스를 동기화할 파트너를 선택합니다.

![][19]{: style="max-width:85%;"}

각 파트너에 대해 오디언스 동기화 단계의 일부로 다음을 구성해야 합니다. 
- 광고 계정
- 오디언스 
- 사용자를 추가하거나 제거하는 작업 
- 일치하는 필드 

Braze는 사용자가 캔버스 내 오디언스 동기화 단계에 진입하면 즉시 사용자를 동기화합니다. 

각 오디언스 동기화 대상에 대해 파트너는 보낼 수 있는 필드에 대해 다른 요구 사항을 적용할 수 있습니다. 자세한 내용은 특정 파트너 설명서를 참조하세요. 

### Audience Sync Pro

Audience Sync Pro 파트너(예: TikTok, Pinterest, Snapchat, Criteo)를 사용하려면 **Audience Sync Pro** 섹션의 **기술 파트너** 페이지에서 Audience Sync Pro 구매 할당량에 따라 파트너를 선택할 수 있습니다.

![][5]{: style="max-width:75%;"}

먼저, 파트너 선택을 선택하여 사용하려는 파트너를 선택합니다. Audience Sync Pro를 구매할 때마다 3개의 할당된 Audience Sync Pro 대상이 제공되며, 이는 대시보드 내 각 워크스페이스에서 사용할 수 있습니다.

![][6]{: style="max-width:65%;"}

Audience Sync Pro 대상을 선택한 후, 파트너 타일을 클릭하여 선택한 파트너 광고 계정을 연결합니다.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

마지막으로, 이 Audience Sync Pro 대상을 사용하여 캔버스에서 오디언스 동기화 단계를 생성합니다.

## 데이터 프라이버시 고려사항

{% alert important %}
이 설명서는 법률 자문을 제공하기 위한 것이 아니며, 법률 자문을 제공하는 것으로 간주되어서는 안 됩니다. 오디언스 동기화 사용은 특정 법률 요구 사항에 종속됩니다. 적용 가능한 모든 법률을 준수하여 사용하고 있는지 확인하려면 법률 자문위원의 조언을 구해야 합니다.
{% endalert %}

광고 추적을 위한 잠재 고객을 구축할 때 사용자의 선호도에 따라 특정 사용자를 포함하거나 제외하고, [CCPA](https://oag.ca.gov/privacy/ccpa)에 따른 "판매 또는 공유 금지" 권리와 같은 개인정보 보호법을 준수하고자 할 수 있습니다. 마케터는 캔버스 진입 기준 내에서 사용자의 자격에 맞는 관련 필터를 구현해야 합니다. 아래에는 몇 가지 옵션이 나와 있습니다.

[Braze SDK를 통해 iOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)를 수집한 경우, '광고 추적 활성화됨' 필터를 사용할 수 있습니다. 값을 `true`로 선택하면 사용자가 옵트인한 오디언스 동기화 대상으로만 사용자를 보낼 수 있습니다.

![][2]

`opt-ins`, `opt-outs`, `Do Not Sell Or Share` 또는 기타 관련 커스텀 속성을 수집하는 경우 캔버스 진입 기준에 필터로 포함해야 합니다.

!['opted_in_marketing' 진입 오디언스가 'true'인 캔버스.][1]

이러한 데이터 보호 법을 준수하는 방법에 대해 Braze 플랫폼 내에서 자세히 알아보려면 [데이터 보호 기술 지원]({{site.baseurl}}/dp-technical-assistance/)을 참조하십시오.

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}