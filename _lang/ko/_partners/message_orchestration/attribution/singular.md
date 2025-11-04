---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "이 참조 문서에서는 유로 설치 경로 데이터를 가져올 수 있는 통합 마케팅 분석 플랫폼인 Singular와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Singular

> Singular는 기여도 분석, 비용 집계, 마케팅 분석, 크리에이티브 보고, 워크플로 자동화가 가능한 통합 마케팅 분석 플랫폼입니다.

_This integration is maintained by Singular._

## 통합 정보

Braze 및 Singular 통합을 통해 생애주기 캠페인 내에서 유료 설치 경로 데이터를 세그먼트에 지능적으로 가져올 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Singular 계정 | 이 파트너십을 활용하려면 Singular 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항의 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| Singular SDK | 필수 Braze SDK 외에도 [Singular SDK](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S)를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 사용자 ID 매핑

#### Android

Android 앱이 있는 경우 고유한 Braze 사용자 ID를 Singular에 전달하는 다음 코드 스니펫을 포함해야 합니다.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
2023년 2월 이전에, Singular 기여도 통합은 iOS 기여도 데이터를 일치시키기 위해 IDFV를 기본 식별자로 사용했습니다. Objective-C를 사용하는 Braze 고객은 서비스 중단이 발생하지 않으므로 설치 시 Braze `device_id`를 가져와 Singular로 전송할 필요가 없습니다.
{% endalert%}

Swift SDK v5.7.0 이상을 사용하는 경우 IDFV를 상호 식별자로 계속 사용하려면 `useUUIDAsDeviceId` 필드를 `false`로 설정하여 통합이 중단되지 않도록 해야 합니다. 

`true`로 설정한 경우, 앱 설치 시 Braze `device_id`를 Singular로 전달하여 Braze가 iOS 기여도와 적절히 일치하도록 Swift용 iOS 기기 ID 매핑을 구현해야 합니다.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### 2단계: Braze 데이터 가져오기 키 받기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Singular**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 만들거나 기존 키를 무효화할 수 있습니다. 

통합을 완료하려면 데이터 가져오기 키와 REST 엔드포인트를 Singular 계정 매니저에게 제공해야 합니다.<br><br>![이 이미지는 Singular 기술 페이지에 있는 '설치 경로에 대한 데이터 가져오기' 상자를 보여줍니다. In this box, you are shown the data import key and the REST endpoint.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### 3단계: 통합 확인

Braze가 Singular로부터 기여도 데이터를 수신하면 Braze의 Singular 기술 파트너 페이지에서 연결 상태 표시기가 '연결되지 않음'에서 '연결됨'으로 변경됩니다. 마지막으로 성공한 요청의 타임스탬프도 포함됩니다. 

기여도 설치에 대한 데이터가 수신될 때까지는 이 작업이 수행되지 않습니다. Singular 포스트백에서 제외되어야 하는 유기적 설치는 API에서 무시되며, 연결이 성공적으로 설정되었는지 확인할 때 계산되지 않습니다.

## Facebook 및 X(이전 트위터) 어트리뷰션 데이터

Facebook 및 X(구 트위터) 캠페인의 어트리뷰션 데이터는 파트너를 통해 제공되지 않습니다. 이러한 미디어 소스는 파트너가 서드파티와 기여도 데이터 공유를 허용하지 않으므로 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.

## Braze에서 단일 클릭 추적 URL(선택 사항)

Braze 캠페인에서 클릭 추적 링크를 사용하면 어떤 캠페인이 앱 설치와 재참여를 유도하는지 쉽게 파악할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 ROI를 극대화하기 위해 더 많은 리소스를 투자할 위치에 대해 데이터에 기반한 의사 결정을 내릴 수 있습니다.

Singular 클릭 추적 링크를 시작하려면, 그들의 [설명서](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true)를 방문하세요. Singular 클릭 추적 링크를 Braze 캠페인에 직접 삽입할 수 있습니다. 단수는 그런 다음 [확률적 기여도 방법론](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true)을 사용하여 링크를 클릭한 사용자를 속성화합니다. Braze 캠페인에서 기여도의 정확성을 개선하기 위해 Singular 추적 링크에 기기 식별자를 추가하는 것이 좋습니다. 이렇게 하면 링크를 클릭한 사용자에게 결정론적으로 어트리뷰션이 부여됩니다.

{% tabs local %}
{% tab Android %}
Android의 경우 Braze를 사용하면 고객이 [Google 광고 ID 수집(GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)에 옵트인할 수 있습니다. GAID도 Singular SDK 통합을 통해 기본적으로 수집됩니다. 다음 Liquid 논리를 사용하여 Singular 클릭 추적 링크에 GAID를 포함할 수 있습니다:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 Singular 모두 SDK 통합을 통해 기본적으로 IDFV를 자동으로 수집합니다. 디바이스 식별자로 사용할 수 있습니다. 다음 Liquid 논리를 사용하여 Singular 클릭 추적 링크에 IDFV를 포함할 수 있습니다:

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
기기 식별자(IDFV 또는 GAID 등)를 현재 클릭 추적 링크에 사용하지 않거나, 앞으로도 사용할 계획이 없는 경우에도 Singular는 확률적 모델링을 통해 이러한 클릭을 속성할 수 있습니다.
{% endalert %}


