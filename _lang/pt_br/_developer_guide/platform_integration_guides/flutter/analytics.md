---
nav_title: Análise de dados
article_title: Análise de dados para o Flutter
platform: Flutter
page_order: 5
description: "Este artigo aborda como configurar e rastrear análises básicas de dados no app Flutter."

---
 
# Análise de dados do Flutter

> Este artigo aborda como configurar e rastrear análises básicas de dados em seu app Flutter.

Antes de começar, leia nosso artigo [Visão geral das análises de dados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) para saber mais sobre as análises do Braze e o que já é rastreado por padrão. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Rastreamento de sessão

O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Com base na semântica de sessão a seguir, nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que levam em conta a duração da sessão e as contagens de sessão visíveis no dashboard do Braze.

Para definir um ID de usuário ou iniciar uma sessão, use o método `changeUser`, que recebe um parâmetro de ID de usuário.

```dart
braze.changeUser('user_id');
```

## Registro de eventos personalizados

Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

```dart
braze.logCustomEvent('my_custom_event');
```

Você pode adicionar metadados sobre o evento passando um objeto de propriedades com seu evento personalizado.

```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```

## Registro de atributos personalizados

O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

### Atribuições padrão do usuário

Para atribuir atribuições de usuário coletadas automaticamente pela Braze, você pode usar os métodos setter fornecidos com o SDK.

```dart
braze.setFirstName('Name');
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

### Definição de valores de atributos personalizados

Além dos atributos de usuário padrão, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes:

{% tabs %}
{% tab Valor booleano %}

```dart
braze.setBoolCustomUserAttribute("custom boolean attribute key", boolean);
```

{% endtab %}
{% tab Inteiro %}

```dart
// Set Integer Attribute
braze.setIntCustomUserAttribute("custom int attribute key", integer);
// Increment Integer Attribute
braze.incrementCustomUserAttribute("key", integer);
```

{% endtab %}
{% tab Double %}
```dart
braze.setDoubleCustomUserAttribute("custom double attribute key", double);
```

{% endtab %}
{% tab String %}

```dart
braze.setStringCustomUserAttribute("custom string attribute", "string custom attribute");
```

{% endtab %}
{% tab Data %}

```dart
braze.setDateCustomUserAttribute("custom date attribute key", date);
```
{% endtab %}
{% tab Vetor %}

```dart
// Adding to an Array
braze.addToCustomAttributeArray("key", "attribute");
// Removing an item from an Array
braze.removeFromCustomAttributeArray("key", "attribute");
```
{% endtab %}
{% endtabs %}

### Desativação de um atributo personalizado

```dart
braze.unsetCustomUserAttribute('attribute_key');
```

## Registro de compras

Registre as compras no app para poder rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

```dart
braze.logPurchase(productId, currencyCode, price, quantity, properties: properties);
```

Por exemplo:

```dart
braze.logPurchase('product_id', 'USD', 9.99, 1, properties: {
    'key1': 'value'
});
```

{% alert tip %}
Se você passar um valor de `10 USD` e uma quantidade de `3`, isso registrará três compras de 10 dólares, totalizando 30 dólares no perfil do usuário. As quantidades devem ser menores ou iguais a 100. Os valores das compras podem ser negativos.
{% endalert %}

### Registre as compras no nível do pedido
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Chaves reservadas

As seguintes chaves são reservadas e não podem ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

