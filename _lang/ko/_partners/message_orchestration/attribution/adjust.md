---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "이 참조 문서에서는 모바일 어트리뷰션 및 분석 회사인 Braze와 Adjust의 파트너십을 통해 비오가닉 설치 어트리뷰션 데이터를 가져와 라이프사이클 캠페인 내에서 보다 지능적으로 세분화할 수 있는 방법을 설명합니다."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust는](https://www.adjust.com/) 광고 소스에 대한 어트리뷰션과 고급 분석을 결합하여 비즈니스 인텔리전스를 종합적으로 파악할 수 있는 모바일 어트리뷰션 및 분석 회사입니다.

_이 통합은 Adjust에서 유지 관리합니다._

## 통합 정보

Braze와 Adjust의 통합을 통해 비오가닉 설치 어트리뷰션 데이터를 가져와서 라이프사이클 캠페인 내에서 더욱 지능적으로 세분화할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| 계정 조정 | 이 파트너십을 활용하려면 Adjust 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항의 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| SDK 조정 | 필수 Braze SDK 외에도 [Adjust SDK](https://dev.adjust.com/en/sdk)를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 디바이스 ID 매핑

#### Android

Android 앱이 있는 경우, 조정에 고유한 Braze 디바이스 ID를 전달해야 합니다. 이 ID는 Adjust SDK의 `addGlobalPartnerParameter()` 메서드에서 설정할 수 있습니다. `Adjust.initSdk.`에서 SDK를 초기화하기 전에 다음 코드 스니펫을 포함해야 합니다.

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

iOS 앱이 있는 경우, Adjust에서 IDFV를 수집하여 Braze로 전송합니다. 이 ID는 Braze의 고유 기기 ID에 매핑됩니다.

Braze는 [iOS 업그레이드 가이드에]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/) 설명된 대로 Braze로 IDFA를 수집하는 경우 동의한 사용자에 대한 IDFA 값을 계속 저장합니다. 그렇지 않으면 IDFV가 사용자를 매핑하기 위한 대체 식별자로 사용됩니다.

{% endtab %}
{% tab Swift %}

iOS 앱이 있는 경우 `useUUIDAsDeviceId` 필드를 `false`로 설정하여 IDFV를 수집하도록 선택할 수 있습니다. 설정하지 않으면 iOS 기여도가 Adjust에서 Braze로 정확하게 매핑되지 않습니다. 자세한 내용은 [IDFV 수집]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)을 참조하세요.

{% endtab %}
{% endtabs %}

{% alert note %}
Adjust에서 Braze로 설치 후 이벤트를 보내려면 다음을 수행해야 합니다. <br><br>1) Adjust SDK 내에서 세션 및 이벤트 매개변수로 `external_id`를 추가해야 합니다. 매출 이벤트 전달의 경우 이벤트에 대한 매개변수로 `product_id`를 설정해야 합니다. 이벤트 전달을 위한 파트너 매개변수 정의에 대한 자세한 내용은 [Adjust 설명서](https://github.com/adjust/sdks)를 참조하세요.<br><br>2) Adjust에 입력할 새 API 키를 생성합니다. 이 작업은 Braze 대시보드의 Adjust 파트너 페이지에 있는 **API 키 생성** 버튼을 선택하여 수행할 수 있습니다.
{% endalert %}

### 2단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **통합** > **기술 파트너**로 이동하고 **Adjust**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Adjust의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.<br><br>![이 이미지는 Adjust 기술 페이지에 있는 '설치 경로에 대한 데이터 가져오기' 상자를 보여줍니다. 이 상자에는 데이터 가져오기 키와 REST 엔드포인트가 표시됩니다.]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### 3단계: Adjust에서 Braze 구성

1. Adjust의 대시보드에서 **앱 설정**으로 이동하여 **파트너 설정**으로 이동한 다음, **파트너 추가**를 클릭합니다.
2. **Braze(이전의 Appboy)** 를 선택하고 데이터 가져오기 키와 Braze REST 엔드포인트를 제공합니다.
3. **저장 후 닫기**를 클릭합니다.

### 4단계: 통합 확인

Braze가 Adjust로부터 기여도 데이터를 수신하면 Braze의 Adjust 기술 파트너 페이지에서 연결 상태 표시기가 '연결되지 않음'에서 '연결됨'으로 변경됩니다. 마지막으로 성공한 요청의 타임스탬프도 포함됩니다. 

기여도 설치에 대한 데이터가 수신될 때까지는 이 작업이 수행되지 않습니다. Adjust 포스트백에서 제외되어야 하는 유기적 설치는 API에서 무시되며, 연결이 성공적으로 설정되었는지 확인할 때 계산되지 않습니다.

## 사용 가능한 데이터 필드

제안된 대로 통합을 구성하면, Braze는 다음 표에서 설명한 대로 Adjust 데이터를 세그먼트 필터에 매핑합니다.

| 데이터 필드 조정 | 브레이즈 세그먼트 필터 |
| --- | --- |
| `{network_name}` | 기여도 소스 |
| `{campaign_name}` | 기여도 캠페인 |
| `{adgroup_name}` | 기여도 광고 그룹 |
| `{creative_name}` | 기여도 광고 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Facebook 및 X(이전 트위터) 어트리뷰션 데이터

Facebook 및 X(구 트위터) 캠페인의 어트리뷰션 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 서드파티와 기여도 데이터 공유를 허용하지 않으므로 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.

## Braze에서 클릭 추적 URL 조정(선택 사항)

Braze 캠페인에서 클릭 추적 링크를 사용하면 어떤 캠페인이 앱 설치와 재참여를 유도하는지 쉽게 파악할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 ROI를 극대화하기 위해 더 많은 리소스를 투자할 위치에 대해 데이터에 기반한 의사 결정을 내릴 수 있습니다.

클릭 추적 링크 조정을 시작하려면 해당 [문서를](https://help.adjust.com/tracking/attribution/tracker-urls) 참조하세요. 클릭 추적 조정 링크를 Braze 캠페인에 직접 삽입할 수 있습니다. 그런 다음, Adjust는 [확률적 기여도 방법론](https://www.adjust.com/blog/attribution-compatible-with-ios14/)을 사용하여 링크를 클릭한 사용자의 기여도를 측정합니다. Braze 캠페인에서 기여도의 정확성을 개선하기 위해 Adjust 추적 링크에 기기 식별자를 추가하는 것이 좋습니다. 이렇게 하면 링크를 클릭한 사용자에게 결정론적으로 어트리뷰션이 부여됩니다.

{% tabs local %}
{% tab Android %}
Android의 경우 Braze를 사용하면 고객이 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)에 옵트인할 수 있습니다. GAID도 Adjust SDK 통합을 통해 기본적으로 수집됩니다. 다음과 같은 리퀴드 로직을 활용하여 GAID를 클릭 추적 링크 조정에 포함할 수 있습니다:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 Adjust 모두 SDK 통합을 통해 기본적으로 IDFV를 자동으로 수집합니다. 디바이스 식별자로 사용할 수 있습니다. 다음과 같은 리퀴드 로직을 활용하여 Adjust 클릭 추적 링크에 IDFV를 포함할 수 있습니다:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**이 권장 사항은 순전히 선택 사항입니다.**<br>
현재 클릭 추적 링크에 IDFV 또는 GAID와 같은 기기 식별자를 사용하지 않거나 향후에도 사용할 계획이 없는 경우에도 Adjust는 확률적 모델링을 통해 이러한 클릭을 어트리뷰션할 수 있습니다.
{% endalert %}


