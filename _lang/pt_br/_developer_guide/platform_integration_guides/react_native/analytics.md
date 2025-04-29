---
nav_title: Análise de dados
article_title: Análise de dados para React Native
platform: React Native
page_order: 5
description: "Este artigo aborda como configurar e rastrear análises básicas de dados, como rastreamento de sessão, registro de eventos personalizados e muito mais, no app React Native."

---
 
# Análise de dados do React Native

> Este artigo aborda como configurar e rastrear análises básicas de dados em seu app React Native.

Antes de começar, leia nosso artigo [Visão geral das análises de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) para saber mais sobre as análises do Braze e o que já é rastreado por padrão. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Rastreamento de sessão

O SDK do Braze relata dados de sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Com base na semântica de sessão a seguir, nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que contabilizam a duração da sessão e as contagens de sessão visíveis no dashboard do Braze.

Para definir um ID de usuário ou iniciar uma sessão, use o método `changeUser`, que recebe um parâmetro de ID de usuário.

```javascript
Braze.changeUser("user_id");
```

## Registro de eventos personalizados

Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

```javascript
Braze.logCustomEvent("react_native_custom_event");
```

Você pode adicionar metadados sobre o evento passando um objeto de propriedades com seu evento personalizado.

```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Registro de atributos personalizados

O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

### Atribuições padrão do usuário

Para atribuir atribuições de usuário coletadas automaticamente pela Braze, você pode usar os métodos setter fornecidos com o SDK.

```javascript
Braze.setFirstName("Name");
```

Há suporte para as seguintes atribuições:

- Nome
- Sobrenome
- Gênero
- Data de nascimento
- Cidade
- País
- Número de telefone
- Idioma
- E-mail

Todos os valores de string, como nome, sobrenome, país e cidade natal, estão limitados a 255 caracteres.

### Atributos personalizados do usuário

Além de nossos métodos predefinidos de atributos de usuários, o Braze também fornece [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para rastrear dados de seus aplicativos. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Desativação de um atributo personalizado


```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Matrizes de atributos personalizados

```javascript

// Adds a string to a custom atttribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

## Registro de compras

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

```javascript
Braze.logPurchase(productId, price, currencyCode, quantity, properties);
```

Por exemplo:

```javascript
Braze.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
Se você passar um valor de `10 USD` e uma quantidade de `3`, isso registrará três compras de 10 dólares, totalizando 30 dólares no perfil do usuário. As quantidades devem ser menores ou iguais a 100. Os valores das compras podem ser negativos.
{% endalert %}

### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Chaves reservadas

As seguintes chaves são **reservadas** e **não podem** ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

