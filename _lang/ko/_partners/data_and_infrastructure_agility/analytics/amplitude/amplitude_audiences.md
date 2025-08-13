---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "이 참조 문서에서는 제품 분석 및 비즈니스 인텔리전스 플랫폼인 Amplitude와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/)는 제품 분석 및 비즈니스 인텔리전스 플랫폼입니다.

Braze 및 Amplitude의 양방향 통합을 통해 Braze로 [Amplitude 코호트]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/), 사용자 특성 및 이벤트를 가져올 수 있으며, 향후 캠페인 또는 캔버스에서 사용자를 타겟팅할 수 있는 세그먼트를 생성할 수 있습니다. 또한 Braze 커런츠를 활용하여 [Amplitude로 Braze 이벤트를 내보내]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) 제품 및 마케팅 데이터에 대한 심층 분석을 수행할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Amplitude 계정 | 이 파트너십을 활용하려면 이 [Amplitude 계정](https://amplitude.com/)이 필요합니다. |
| 커런츠 | 데이터를 Amplitude로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## 통합을 선택하세요 

Amplitude와 Braze는 두 가지 다른 통합 방법을 제공합니다. 다음 설명서를 읽고 어떤 방법이 귀하의 요구에 맞는지 결정하십시오:

- Braze 이벤트 스트리밍: Amplitude 이벤트 원시 데이터를 Braze로 직접 전달할 수 있는 통합입니다.
- [코호트 가져오기]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/): Amplitude 코호트를 Braze로 전달할 수 있는 통합입니다.

## Braze 이벤트 스트리밍

### 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze REST API 키 | 모든 권한이 있는 Braze REST API 키.<br><br> 이것은 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
| Braze 앱 식별자 | 앱이 Amplitude 이벤트를 수신할 식별자. 이는 **Braze 대시보드 > 개발자 콘솔 > 설정** 내에서 찾을 수 있습니다. |

### Amplitude 설정

1. Amplitude에서 **데이터 대상**으로 이동한 다음, 'Braze - 이벤트 스트림'을 찾습니다.
2. 동기화 이름을 입력한 다음 **동기화 생성**을 클릭하십시오.
3. **편집**을 클릭하고 Braze REST API 엔드포인트, REST API 키 및 Braze 앱 식별자를 제공합니다.
4. 이벤트 전송 필터를 사용하여 전송할 이벤트를 선택합니다. 모든 이벤트를 전송할 수 있지만, Amplitude는 가장 중요한 이벤트를 선택하도록 권장합니다. 
5. 완료되면 대상을 활성화하고 저장하십시오. 

이 통합에 대한 자세한 내용은 [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/)을 참조하십시오.

## 사용자 특성 및 계산 동기화

Audiences를 사용하여 사용자 속성과 계산을 커스텀 속성으로 Braze에 전송합니다. 마지막 90일 동안 활동한 사용자에 대해 사용자 속성 또는 계산된 속성을 동기화할 수 있습니다.

사용자의 속성 또는 계산이 업데이트되면, Amplitude는 Braze에서 해당 사용자 속성 또는 계산과 동일한 이름의 커스텀 속성을 업데이트합니다.

사용자 특성 및 계산 동기화는 Braze 내에 아직 존재하지 않는 사용자 식별자에 대해 새로운 사용자를 생성합니다. 계산 및 사용자 특성은 사용자 식별자를 통해서만 동기화할 수 있습니다. 사용자 식별자는 다음 중 하나를 사용할 수 있습니다:
- 외부 ID
- Braze ID
- 사용자 별칭
- 이메일 주소

[속성, 추천 및 코호트를 서드파티 대상에 동기화](https://help.amplitude.com/hc/en-us/articles/360060055531)하는 방법에 대한 자세한 내용은 Amplitude의 설명서를 참조하세요.

#### 사용자 속성과 계산을 동기화하는 방법

Amplitude Audiences에서 **동기화 > 동기화 생성**을 선택합니다.

![]({% image_buster /assets/img/amplitude11.png %})

다음으로 사용자 속성정보, 계산, 코호트 또는 추천을 동기화하도록 선택합니다. 

{% tabs %}
{% tab 사용자 속성 동기화 %}

**사용자 속성**을 선택한 다음 동기화할 원하는 사용자 속성을 선택합니다.

![]({% image_buster /assets/img/amplitude7.png %})

다음으로, 사용자 속성을 동기화할 대상을 선택합니다.

![]({% image_buster /assets/img/amplitude8.png %})

마지막으로, 동기화 빈도를 정의하십시오.

![귀하의 주기를 일회성 동기화 또는 예약된 동기화로 정의하십시오.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab 계산 동기화 %}

**계산**을 선택한 다음 동기화할 원하는 계산을 선택하십시오

![]({% image_buster /assets/img/amplitude10.png %})

다음으로, 계산을 동기화할 대상을 선택합니다.

![]({% image_buster /assets/img/amplitude8.png %})

마지막으로, 동기화 빈도를 정의하십시오.

![귀하의 주기를 일회성 동기화 또는 예약된 동기화로 정의하십시오.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Amplitude 사용자 프로필 API 엔드포인트

연결된 콘텐츠와 함께 사용할 수 있는 일반적인 Amplitude API 엔드포인트를 확인하려면, 전용 [Amplitude API 설명서]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/)를 참조하세요.
