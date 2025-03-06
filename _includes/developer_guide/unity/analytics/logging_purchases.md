## Tracking purchases and revenue

To tracking purchases and review, call the `logPurchase` method after a successful purchase in your app.

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

This method logs a purchase with a quantity of one. If you want to pass in a different quantity, you can call the following method:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

Quantity must be less than or equal to one hundred. Braze also supports adding metadata about purchases by passing a `Dictionary` of purchase properties:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## Log purchases at the order level
If you want to log purchases at the order level instead of the product level, you can use order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

## Currency codes

The following codes are supported currency symbols. Any other provided currency symbol will result in a logged warning and no other action taken by the SDK.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW and ZWL.

## Example code

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## REST API

You can also use our REST API to record purchases. Refer to the [users API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) documentation for details.

