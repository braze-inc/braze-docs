---
nav_title: Appsflyer 오디언스
article_title: Appsflyer 오디언스
alias: /partners/appsflyer_audiences/
description: "이 참조 문서에서는 오디언스 세그먼트를 효율적으로 구축하고 파트너 네트워크에 연결할 수 있도록 지원하는 Appsflyer 플랫폼의 기능인 Appsflyer 오디언스와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Appsflyer 오디언스

> 이 문서에서는 [AppsFlyer Audiences][2] 통합을 사용하여 AppsFlyer에서 Braze로 사용자 코호트를 가져오는 방법을 설명합니다. Appsflyer 및 모바일 기여도와 같은 기타 기능 통합에 대한 자세한 내용은 주요 [Appsflyer 문서][3]를 참조하세요.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Appsflyer 계정 | 이 파트너십을 활용하려면 Appsflyer 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. 이러한 요구 사항의 세부 정보는 통합 프로세스의 1단계에서 확인할 수 있습니다. |
| AppsFlyer SDK | 필수 Braze SDK 외에도 [Appsflyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview)를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 데이터 가져오기 통합

### 1단계: AppsFlyer SDK 구성

이 통합을 사용하려면 Appsflyer SDK의 `setPartnerData()` 기능을 사용하여 사용자의 Braze 외부 ID를 Appsflyer로 전달해야 합니다.

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### 2단계: Braze 데이터 가져오기 키 가져오기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Appsflyer**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Appsflyer의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.<br><br>![Appsflyer 기술 페이지의 '코호트 가져오기를 사용한 데이터 가져오기' 상자. 이 상자에 데이터 가져오기 키와 REST 엔드포인트가 표시됩니다.][5]{: style="max-width:90%;"}

### 3단계: AppsFlyer Audiences에서 Braze 연결 구성

1. [Appsflyer 오디언스][4]에서 **연결** 탭으로 이동하여 **파트너 연결 추가**를 클릭합니다.
2. Braze를 파트너로 선택하고 연결에 이름을 지정합니다.
3. 데이터 가져오기 키와 Braze REST 엔드포인트를 제공하십시오.
4. 연결을 저장하면 새 오디언스 또는 기존 오디언스에 연결할 수 있습니다.

![Appsflyer 오디언스 플랫폼 파트너 연결 구성 페이지. 이미지의 하단에서는 Braze 외부 ID 상자가 선택되어 있음을 보여줍니다.][6]{: style="max-width:80%;"}

### 4단계: Braze에서 Appsflyer Audiences 코호트 사용

AppsFlyer 오디언스가 Braze에 업로드되면 Braze에서 세그먼트를 정의할 때 **AppsFlyer Cohorts** 필터를 선택하여 필터로 사용할 수 있습니다.

![사용자 속성 필터 "Appsflyer 코호트" 선택됨.][7]

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.

[1]: https://www.appsflyer.com/
[2]: https://www.appsflyer.com/product/audiences/
[3]: {{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/
[4]: https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections
[5]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}
[6]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}
[7]: {% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %}