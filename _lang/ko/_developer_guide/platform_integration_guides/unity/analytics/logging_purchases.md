---
nav_title: 구매 기록
article_title: Unity용 구매 기록
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "이 참고 문서에서는 Unity 플랫폼에서 구매를 기록하는 방법에 대해 설명합니다."

---
 
# 구매 기록

> 인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

구현하기 전에 [모범 사례][5]에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요.

이 기능을 사용하려면 앱에서 구매에 성공한 후 다음 메서드 호출을 추가합니다.

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

이 방법은 수량이 1개인 구매를 기록합니다. 다른 수량을 전달하려면 다음 메서드를 호출하면 됩니다:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

수량은 100보다 작거나 같아야 합니다. Braze는 구매 속성정보의 `Dictionary`를 전달하여 구매에 대한 메타데이터를 추가하는 기능도 지원합니다.

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## 주문 수준에서 구매 기록
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

## 통화 코드

다음 코드는 지원되는 통화 기호입니다. 제공된 다른 통화 기호를 사용하면 경고가 기록되고, SDK에서 다른 조치를 취하지 않습니다.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BDB, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LLS, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SSL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW 및 ZWL.

## 코드 예제

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## REST API

REST API를 사용하여 구매 내역을 기록할 수도 있습니다. 자세한 내용은 [사용자 API][4] 설명서를 참조하세요.

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
