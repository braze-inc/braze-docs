---
nav_title: Käufe protokollieren
article_title: Käufe für Unity protokollieren
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie Einkäufe auf der Unity-Plattform protokollieren."

---
 
# Einkäufe protokollieren

> Erfassen Sie In-App-Käufe, damit Sie Ihre Einnahmen im Laufe der Zeit und über verschiedene Einnahmequellen hinweg verfolgen und Ihre Nutzer nach ihrem Lifetime-Value segmentieren können.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

Sehen Sie sich vor der Implementierung unbedingt in unseren [Best Practices][5] die Beispiele für die Segmentierungsoptionen von angepassten Events, angepassten Attributen und Kauf-Events an.

Um dieses Feature zu nutzen, fügen Sie den folgenden Methodenaufruf nach einem erfolgreichen Kauf in Ihrer App hinzu:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

Diese Methode protokolliert einen Kauf mit einer Menge von eins. Wenn Sie eine andere Menge übergeben möchten, können Sie die folgende Methode aufrufen:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

Die Menge muss weniger als oder gleich hundert sein. Braze unterstützt auch das Hinzufügen von Metadaten über Käufe, indem Sie ein `Dictionary` mit den Kauf-Details übergeben:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## Währung Codes

Die folgenden Codes werden als Währungssymbole unterstützt. Jedes andere angegebene Währungssymbol führt zu einer protokollierten Warnung und zu keiner weiteren Aktion durch das SDK.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW und ZWL.

## Beispiel-Code

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## REST API

Sie können auch unsere REST API verwenden, um Einkäufe zu erfassen. Einzelheiten finden Sie in der [API-Dokumentation für Benutzer][4].

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
