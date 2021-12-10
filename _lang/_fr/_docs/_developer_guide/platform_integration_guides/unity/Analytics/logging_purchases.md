---
nav_title: Achats de journalisation
article_title: Achats pour l'unité de journalisation
platform:
  - Unité
  - iOS
  - Android
page_order: 3
description: "Cet article de référence explique comment enregistrer les achats sur la plateforme Unity."
---

# Achats de journalisation

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

Avant l'implémentation, assurez-vous d'examiner les exemples d'options de segmentation offertes par les événements personnalisés vs. attributs personnalisés par rapport aux événements d'achat dans notre section [Meilleures pratiques][5].

Pour utiliser cette fonctionnalité, ajoutez cette méthode d'appel après un achat réussi dans votre application :

```csharp
AppboyBinding.LogPurchase("productId", "currencyCode", prix(décimal));
```

La méthode ci-dessus enregistre un achat avec une quantité de 1. Si vous souhaitez passer en une quantité différente, vous pouvez appeler cette méthode :

```csharp
AppboyBinding.LogPurchase("productId", "currencyCode", prix(décimal), quantité(int));
```

La quantité doit être inférieure ou égale à 100. Braze prend également en charge l'ajout de métadonnées sur les achats en passant un `dictionnaire` de propriétés d'achat :

```csharp
AppboyBinding.LogPurchase("productId", "currencyCode", price(décimal), quantity(int), properties(Dictionary<string, object>));
```

## Codes des devises

Les symboles de devises pris en charge sont listés ci-dessous. Tout autre symbole de devise fourni donnera lieu à un avertissement et aucune autre action du SDK.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW et ZWL.

## Exemple de code

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## API REST

Vous pouvez également utiliser notre API REST pour enregistrer vos achats. Reportez-vous à la documentation [de l'API utilisateur][4] pour plus de détails.

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
