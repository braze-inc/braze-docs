---
nav_title: RevenueCat
article_title: RevenueCat
description: "RevenueCat과 Braze의 통합을 통해 고객의 구매 및 구독 생애주기 이벤트를 여러 플랫폼에서 자동으로 동기화할 수 있습니다. 이를 통해 무료 평가판 사용 중 옵트아웃한 고객과 소통하거나 청구 문제가 있는 고객에게 알림을 보내는 등 고객의 구독 라이프사이클 단계에 따라 반응하는 캠페인을 구축할 수 있습니다."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/)은 iOS, Android 및 웹에서 구독 상태를 확인할 수 있는 단일 소스입니다. 새로운 앱을 개발 중이거나 이미 수백만 명의 구독자를 보유하고 있는 경우 서버 코드 없이도 RevenueCat을 사용하여 크로스 플랫폼 인앱 구매를 구축하고, 제품 및 구독자를 관리하고, 데이터를 분석할 수 있습니다.

_This integration is maintained by RevenueCat._

## 통합 정보

RevenueCat과 Braze의 통합을 통해 고객의 구매 및 구독 생애주기 이벤트를 여러 플랫폼에서 자동으로 동기화할 수 있습니다. 이를 통해 무료 평가판 사용 중 옵트아웃한 고객과 소통하거나 청구 문제가 있는 고객에게 알림을 보내는 등 고객의 구독 라이프사이클 단계에 따라 반응하는 캠페인을 구축할 수 있습니다.

## 필수 조건

최소한 RevenueCat 대시보드에서 통합을 활성화하여 RevenueCat을 Braze에 연결해야 합니다. Braze SDK를 사용하는 경우, 두 시스템에서 동일한 고객 식별자가 사용되고 있는지 확인하여 통합을 강화하기 위해 RevenueCat과 Braze SDK를 함께 사용할 수 있습니다.

| 요구 사항 | 설명 |
|---|---|
| RevenueCat 계정 및 앱 | 이 파트너십을 활용하려면 [RevenueCat 계정][9]이 필요합니다. 또한 RevenueCat 앱이 구성되어 있어야 합니다. |
| RevenueCat SDK | 필수 Braze SDK 외에도 [RevenueCat SDK][8]를 설치하여 RevenueCat에 사용자 별칭을 제공하는 것이 좋습니다. |
| 브레이즈 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저로부터 가져오거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다.<br><br>RevenueCat에서는 Braze 인스턴스가 서버 측을 올바른 Braze REST 엔드포인트로 전해야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze 테스트 REST API 키(선택 사항) | 테스트 API 키는 해당 요청을 별도의 Braze 인스턴스로 전송하려는 경우 테스트 및 프로덕션 구매에 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 활용 사례 

- 고객이 무료 평가판을 시작할 때 프리미엄 기능을 강조 표시하는 온보딩 캠페인을 트리거합니다.
- '청구 문제' 이벤트가 수신되면 청구 정보를 업데이트하라는 알림을 보냅니다.
- 고객이 무료 체험을 취소한 후 피드백 설문조사를 보내세요. 

## 통합

### 1단계: Braze 사용자 ID 설정

Braze SDK에서 Braze 사용자 ID를 RevenueCat 앱 사용자 ID와 일치하도록 설정하여 Braze와 RevenueCat에서 전송된 이벤트가 동일한 사용자로 동기화될 수 있도록 합니다.

RevenueCat과 동일한 앱 사용자 ID로 Braze SDK를 구성하거나 Braze SDK `.changeUser()` 메서드를 사용합니다.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### 사용자 별칭 객체를 Braze로 보내기(선택 사항) 

RevenueCat 앱 사용자 ID와 다른 대체 고유 사용자 식별자를 보내려면 다음 데이터를 사용하여 RevenueCat 가입자 속성으로 사용자를 업데이트합니다.

| 키 | 설명 |
|---|---|
| `$brazeAliasName` | [사용자 별칭 개체의][2] Braze `alias_name`  |
| `$brazeAliasLabel` | [사용자 별칭 개체의][2] Braze `alias_label`  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이벤트 데이터와 함께 [사용자 별칭 오브젝트][2]를 전송하려면 두 속성 모두 필요합니다. 이러한 속성정보는 다른 [RevenueCat 가입자 속성][4]과 마찬가지로 수동으로 설정할 수 있습니다. 코드 스니펫 예제는 1단계에 나와 있습니다.

### 2단계: RevenueCat 이벤트를 Braze로 보내기

RevenueCat 구매 SDK와 Braze SDK가 동일한 사용자 ID를 사용하도록 설정한 후에는 RevenueCat 대시보드에서 통합을 켜고 이벤트 이름을 구성할 수 있습니다.

1. RevenueCat 대시보드에서 프로젝트로 이동하고 왼쪽 메뉴에서 **통합** 카드를 찾습니다. **\+ 새로 만들기**를 선택합니다.
2. 그런 다음, 사용 가능한 통합에서 **Braze**를 선택하고 Braze 인스턴스와 Braze REST API 키를 추가합니다. 
3. RevenueCat이 전송할 이벤트 이름을 입력하거나 기본 이벤트 이름을 선택합니다. 사용 가능한 이벤트에 대한 자세한 내용은 [3단계](#configure-event-names)에서 확인할 수 있습니다.
4. RevenueCat에서 수익금(앱 스토어 삭감 후)을 보고할지, 매출(총 판매액)을 보고할지 선택합니다.

![Braze 인스턴스, API 키 식별자, 샌드박스 식별자에 대한 필드가 있는 RevenueCat의 Braze 설정.][3]

### 3단계: 이벤트 이름 구성 {#configure-event-names}

RevenueCat이 전송할 이벤트 이름을 입력하거나 **기본 이벤트 이름 사용**을 선택하여 기본 이벤트 이름 중에서 선택합니다. RevenueCat이 전송을 지원하는 이벤트는 다음 차트에 설명되어 있습니다.

| 이벤트 | 설명 |
|---|---|
| 초기 구매 | 무료 평가판이 포함되지 않은 자동 갱신 구독 제품을 처음 구매하는 경우. |
| 평가판 시작됨 | 자동 갱신되는 가입 제품 무료 평가판 시작. |
| 평가판 전환 | 자동 갱신 가입 제품이 무료 평가판에서 일반 유료 기간으로 전환되는 경우. |
| 평가판 취소됨 | 사용자가 무료 평가판 기간 동안 자동 갱신되는 정기구독 제품의 갱신을 해제하는 경우. |
| 갱신 | 자동 갱신 가입 제품이 갱신되거나 가입 기간이 만료된 후 사용자가 자동 갱신 가입 제품을 재구매하는 경우. |
| 취소 | 사용자가 정상적인 유료 기간 동안 자동 갱신되는 정기구독 제품의 갱신을 해제하는 경우. |
| 비구독 구매 | 자동 갱신 가입이 아닌 모든 제품의 구매. |
| 만료 | 구독이 만료되는 경우. |
| 청구 문제 | 사용자에게 비용을 청구하는 데 문제가 발생한 경우. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

매출이 포함된 이벤트의 경우, RevenueCat은 평가판 전환 및 갱신과 같은 Braze의 이벤트와 함께 이 금액을 자동으로 기록합니다.

## 이 통합 사용

RevenueCat에서 Braze 설정을 구성한 후 사용자 측에서 별도의 작업 없이도 이벤트가 자동으로 RevenueCat에서 Braze로 전송되기 시작합니다.

## 사용자 지정

### 테스트를 위한 샌드박스 API 키 추가

RevenueCat에 하나의 Braze REST API 키만 제공하면 프로덕션 이벤트만 전송됩니다. 샌드박스 테스트 이벤트도 보내려면 [다른 Braze REST API 키를 생성][11]하고 RevenueCat의 Braze 설정에 추가합니다.


[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]:https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]:https://docs.revenuecat.com/docs/configuring-sdk
[9]:https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
