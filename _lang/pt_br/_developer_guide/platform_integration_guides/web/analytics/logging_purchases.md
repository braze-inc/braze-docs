---
nav_title: Registro de compras
article_title: Registro de compras para Web
platform: Web
page_order: 4
page_type: reference
description: "Este artigo descreve como registrar compras e adicionar propriedades a essas compras para a Web."

---
 
# Registrando compras

> Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles. 

O Braze oferece suporte a compras em várias moedas. As compras que você relatar em uma moeda diferente do USD serão mostradas no dashboard em USD com base na taxa de câmbio na data em que foram relatadas.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [Melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection).

Para usar este recurso, adicione a chamada [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) após uma compra bem-sucedida no seu app: Note que `quantity` deve ser menor ou igual a 100.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## Adicionando propriedades

Você pode adicionar [metadados](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) sobre compras passando um [array de propriedades de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) ou passando um objeto de pares chave-valor com suas informações de compra. 

#### Formatação de objeto

As chaves são objetos `string` e os valores podem ser objetos `string`, `numeric`, `boolean` ou `Date`.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

## API REST

Você também pode usar nossa API REST para registrar compras. Para saber mais, consulte a documentação da [API dos usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

