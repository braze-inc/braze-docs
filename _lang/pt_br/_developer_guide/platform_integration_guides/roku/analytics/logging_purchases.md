---
nav_title: Registro de compras
article_title: Registrando Compras para Roku
platform: Roku
page_order: 3
page_type: reference
description: "Esta página apresenta métodos para registrar eventos de compra no Roku através do SDK da Braze."

---
 
# Registrando compras

> Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras que você reportar em uma moeda diferente de USD serão mostradas no dashboard em USD com base na taxa de câmbio na data em que foram reportadas.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nosso artigo de [Melhores Práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). Também recomendamos que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Rastreamento de compras e receitas

Para usar este recurso, adicione esta chamada de método após uma compra bem-sucedida no seu app:

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### Adicionando propriedades

Você pode adicionar metadados sobre compras passando um dicionário de propriedades com suas informações de compra.

Propriedades são definidas como pares chave-valor.  As chaves são objetos `String`, e os valores podem ser `String` ou `Integer`.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### API REST

Você também pode usar nossa API REST para registrar compras. Para saber mais, consulte a documentação da [API dos usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

