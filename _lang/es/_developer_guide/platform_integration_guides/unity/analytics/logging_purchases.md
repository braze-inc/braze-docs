---
nav_title: Registrar compras
article_title: Registro de compras para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "Este artículo de referencia explica cómo registrar compras en la plataforma Unity."

---
 
# Registrar compras

> Registra las compras dentro de la aplicación para que puedas hacer un seguimiento de tus ingresos a lo largo del tiempo y de las distintas fuentes de ingresos, así como segmentar a tus usuarios por su valor de duración del ciclo de vida.

Braze admite compras en varias divisas. Las compras que notifiques en una divisa distinta del USD se mostrarán en el panel en USD según la tasa de cambio en la fecha en que se notificaron.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Mejores prácticas][5].

Para utilizar esta característica, añade en tu aplicación la siguiente llamada al método después de una compra satisfactoria:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal));
```

Este método registra una compra con una cantidad de uno. Si quieres pasar una cantidad diferente, puedes llamar al método siguiente:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int));
```

La cantidad debe ser inferior o igual a cien. Braze también admite añadir metadatos sobre las compras pasando un `Dictionary` de propiedades de la compra:

```csharp
AppboyBinding.LogPurchase("product_id", "currencyCode", price(decimal), quantity(int), properties(Dictionary<string, object>));
```

## Registrar las compras a nivel de pedido
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

## Códigos de moneda

Los siguientes códigos son símbolos de moneda admitidos. Cualquier otro símbolo de moneda proporcionado dará lugar a una advertencia registrada y el SDK no tomará ninguna otra medida.

- USD, AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EEK, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MTL, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TWD, TZS, UAH, UGX, UYU, UZS, VEF, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMK, ZMW y ZWL.

## Ejemplo de código

```csharp
AppboyBinding.LogPurchase("product ID", "USD", 12.5m);
```

## API REST

También puedes utilizar nuestra API REST para registrar las compras. Consulta la documentación de [la API de usuario][4] para más detalles.

[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[5]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
