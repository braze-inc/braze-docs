---
nav_title: Registro de compras
article_title: Registro de compras para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "Este artigo de referência aborda como registrar compras na plataforma Unity."

---
 
# Registrando compras

> Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras que você relatar em uma moeda diferente do USD serão mostradas no dashboard em USD com base na taxa de câmbio na data em que foram relatadas.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [Melhores práticas][5].

Para usar esse recurso, adicione a seguinte chamada de método após uma compra bem-sucedida em seu app:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

Este método registra uma compra com uma quantidade de um. Se quiser passar uma quantidade diferente, você pode chamar o método a seguir:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

A quantidade deve ser menor ou igual a cem. A Braze também oferece suporte à adição de metadados sobre compras, passando um `Dictionary` de propriedades de compra:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

## Códigos de moeda

Os códigos a seguir são símbolos de moeda compatíveis. Qualquer outro símbolo de moeda fornecido resultará em um aviso registrado e nenhuma outra ação será realizada pelo SDK.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW e ZWL.

## Exemplo de código

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## API REST

Você também pode usar nossa API REST para registrar compras. Para saber mais, consulte a documentação da [API dos usuários][4].

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
