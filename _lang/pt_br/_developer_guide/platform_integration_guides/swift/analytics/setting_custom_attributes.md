---
nav_title: Configuração de atributos personalizados
article_title: Definindo Atributos Personalizados para iOS
platform: Swift
page_order: 3
description: "Este artigo de referência mostra como definir atributos personalizados para o Swift SDK."

---

# Definição de atributos personalizados

> O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Atribuição de atribuições de usuário padrão

Para atribuir atributos de usuário, você precisa definir o campo apropriado no objeto compartilhado `ABKUser`.

A seguir está um exemplo de configuração do atributo nome:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "first_name")
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setFirstName:@"first_name"];
```

{% endtab %}
{% endtabs %}

Os seguintes atributos devem ser definidos no objeto `Braze.User`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `gender`

## Atribuição de atributos personalizados ao usuário

Além dos atributos de usuário padrão, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes. Veja nossa [coleta de dados de usuários]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) Para saber mais sobre as opções de segmentação que cada um desses atributos lhe oferecerá.

### Atributo personalizado com um valor da string

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor inteiro

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor duplo

Braze trata os valores `float` e `double` da mesma forma em nosso banco de dados.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor booleano

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor de data

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor de array

O número máximo de elementos em [arrays de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) é 25 por padrão. As matrizes que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos. O máximo para matrizes individuais pode ser aumentado para até 100. Se você gostaria que esse máximo fosse aumentado, entre em contato com seu gerente de atendimento ao cliente. 


{% tabs %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
// Setting a custom attribute with an array value
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[AppDelegate.braze.user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[AppDelegate.braze.user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[AppDelegate.braze.user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% endtabs %}

### Desativação de um atributo personalizado

Os atributos personalizados também podem ser desmarcados usando o seguinte método:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Incremento/decremento de atributos personalizados

Este código é um exemplo de um atributo personalizado de incremento. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro ou longo positivo ou negativo:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Definição de um atributo personalizado por meio da API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Consulte a [documentação da API do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

### Limites de valores de atributos personalizados

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

#### Informações adicionais

- Consulte a [`Braze.User` documentação](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class) para saber mais.

## Configuração de inscrções de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `set(emailSubscriptionState:)` ou `set(pushNotificationSubscriptionState:)`, respectivamente. Ambas as funções aceitam o tipo enum `Braze.User.SubscriptionState` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `optedIn` | Inscrição e aceitação explícita |
| `subscribed` | Inscrição feita, mas sem aceitação explícita |
| `unsubscribed` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Os usuários que concedem permissão para um app enviar notificações por push têm o status padrão de `optedIn`, pois o iOS exige uma aceitação explícita.

Os usuários serão configurados para `subscribed` automaticamente após o recebimento de um endereço de e-mail válido; no entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `optedIn` após o recebimento do consentimento explícito do seu usuário. Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

### Configuração de envios de e-mail

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(emailSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setEmailSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

### Configuração de inscrições de notificação por push

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(pushNotificationSubscriptionState: Braze.User.SubscriptionState)
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

