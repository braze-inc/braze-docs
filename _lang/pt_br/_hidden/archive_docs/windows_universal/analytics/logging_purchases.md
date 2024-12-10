---
nav_title: Registro de compras
article_title: Registro de compras para o Windows Universal
platform: Windows Universal
page_order: 4
description: "Este artigo de referência aborda como registrar compras na Plataforma Universal do Windows."
hidden: true
---
 
# Registro de compras
{% multi_lang_include archive/windows_deprecation.md %}

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

Antes da implementação, não deixe de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nosso artigo [Práticas recomendadas][3]. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

Para usar esse recurso, adicione essa chamada de método após uma compra bem-sucedida em seu app:

As compras são registradas usando o `EventLogger`, que é uma propriedade exposta no IAppboy. Para obter uma referência do site `EventLogger`, chame `Appboy.SharedInstance.EventLogger`.

```csharp
bool LogPurchase(string productId, string currencyCode, decimal price)
```

## Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

## API REST

Também é possível usar nossa API REST para registrar compras. Consulte a documentação da [API de usuários][2] para obter detalhes.

[2]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[3]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
