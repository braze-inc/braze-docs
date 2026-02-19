---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "This reference article outlines the partnership between Braze and AppsFlyer Audiences, a feature of the AppsFlyer platform that allows you to efficiently build and connect audience segments to partner networks."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> This article describes how to import user cohorts from AppsFlyer to Braze by using the [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/) integration. For more information on integrating AppsFlyer and its other functionalities, such as mobile attribution see the main [AppsFlyer article]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/).

## Prerequisites

| Requirement | Description |
|---|---|
| AppsFlyer account | An AppsFlyer account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. Details on these requirements can be found in step 1 of the integration process. |
| AppsFlyer SDK | In addition to the required Braze SDK, you must install the [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

### 1단계: Configure the AppsFlyer SDK

To use this integration, you must pass the user's Braze external ID to AppsFlyer using the `setPartnerData()` function of the AppsFlyer SDK:

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

### 2단계: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **AppsFlyer**. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성할 수 있습니다. After the key is generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in AppsFlyer's dashboard.<br><br>![Appsflyer 기술 페이지의 '코호트 가져오기를 사용한 데이터 가져오기' 상자. 이 상자에 데이터 가져오기 키와 REST 엔드포인트가 표시됩니다.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### 3단계: Configure a Braze connection in AppsFlyer Audiences

1. In [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), go to the **Connections** tab and click **Add partner connection**.
2. Select Braze as the partner and give the connection a name.
3. Provide the data import key and Braze REST endpoint.
4. Save the connection, and it will be available to link to any new or existing audience.

![Appsflyer 오디언스 플랫폼 파트너 연결 구성 페이지. 이미지의 하단에서는 Braze 외부 ID 상자가 선택되어 있음을 보여줍니다.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### 4단계: Using AppsFlyer Audiences cohorts in Braze

AppsFlyer 오디언스가 Braze에 업로드되면 Braze에서 세그먼트를 정의할 때 **AppsFlyer Cohorts** 필터를 선택하여 필터로 사용할 수 있습니다.

![사용자 속성 필터 "Appsflyer 코호트" 선택됨.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

