---
nav_title: Configuração de atributos personalizados
article_title: Definindo Atributos Personalizados para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência mostra como definir atributos personalizados em seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definição de atributos personalizados para iOS

O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection), bem como nossas notas sobre [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Atribuição de atribuições de usuário padrão

Para atribuir atributos de usuário, você precisa definir o campo apropriado no objeto compartilhado `ABKUser`.

A seguir está um exemplo de configuração do atributo nome:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy sharedInstance].user.firstName = @"first_name";
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.firstName = "first_name"
```

{% endtab %}
{% endtabs %}

Os seguintes atributos devem ser definidos no objeto `ABKUser`:

- `firstName`
- `lastName`
- `email`
- `dateOfBirth`
- `country`
- `language`
- `homeCity`
- `phone`
- `userID`
- `gender`

## Atribuição de atributos personalizados ao usuário

Além dos atributos de usuário padrão, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes. Veja nossa [coleta de dados de usuários]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/) Para saber mais sobre as opções de segmentação que cada um desses atributos lhe oferecerá.

### Atributo personalizado com um valor da string

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andStringValue:"your_attribute_value"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andStringValue: "your_attribute_value")
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor inteiro

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andIntegerValue: yourIntegerValue)
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor duplo

Braze trata os valores `float` e `double` da mesma forma em nosso banco de dados.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDoubleValue: yourDoubleValue)
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor booleano

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andBOOLValue: yourBoolValue)
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor de data

As datas passadas para a Braze com esse método devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (e.g `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (`2016-12-14T13:32:31.601-0800`).

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setCustomAttributeWithKey("your_attribute_key", andDateValue:yourDateValue)
```

{% endtab %}
{% endtabs %}

### atributo personalizado com um valor de array

O número máximo de elementos em [arrays de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) é 25 por padrão. As matrizes que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos. O máximo para matrizes individuais pode ser aumentado para até 100. Se você gostaria que esse máximo fosse aumentado, entre em contato com seu gerente de atendimento ao cliente. 


{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Setting a custom attribute with an array value
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:@[@"value1",  @"value2"]];
// Adding to a custom attribute with an array value
[[Appboy sharedInstance].user addToCustomAttributeArrayWithKey:@"array_name" value:@"value3"];
// Removing a value from an array type custom attribute
[[Appboy sharedInstance].user removeFromCustomAttributeArrayWithKey:@"array_name" value:@"value2"];
// Removing an entire array and key
[[Appboy sharedInstance].user setCustomAttributeArrayWithKey:@"array_name" array:nil];
```

{% endtab %}
{% tab swift %}

```swift
// Setting a custom attribute with an array value
Appboy.sharedInstance()?.user.setCustomAttributeArrayWithKey("array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
Appboy.sharedInstance()?.user.addToCustomAttributeArrayWithKey("array_name", value: "value3")
// Removing a value from an array type custom attribute
Appboy.sharedInstance()?.user.removeFromCustomAttributeArrayWithKey("array_name", value: "value2")
```

{% endtab %}
{% endtabs %}

### Desativação de um atributo personalizado

Os atributos personalizados também podem ser desmarcados usando o seguinte método:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.unsetCustomAttributeWithKey("your_attribute_key")
```

{% endtab %}
{% endtabs %}

### Incremento/decremento de atributos personalizados

Este código é um exemplo de um atributo personalizado de incremento. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro ou longo positivo ou negativo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.incrementCustomUserAttribute("your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% endtabs %}

### Definição de um atributo personalizado por meio da API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Consulte a [documentação da API do usuário]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

### Limites de valores de atributos personalizados

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

#### Informações adicionais

- Mais detalhes podem ser encontrados no [arquivo`ABKUser.h` ](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
- Consulte a [`ABKUser` documentação](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html) para saber mais.

## Configuração de inscrções de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `setEmailNotificationSubscriptionType` ou `setPushNotificationSubscriptionType`, respectivamente. Ambas as funções aceitam o tipo enum `ABKNotificationSubscriptionType` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `ABKOptedin` | Inscrição e aceitação explícita |
| `ABKSubscribed` | Inscrição feita, mas sem aceitação explícita |
| `ABKUnsubscribed` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Os usuários que concedem permissão para um app enviar notificações por push têm o status padrão de `ABKOptedin`, pois o iOS exige uma aceitação explícita.

Os usuários serão configurados para `ABKSubscribed` automaticamente após o recebimento de um endereço de e-mail válido; no entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `OptedIn` após o recebimento do consentimento explícito do seu usuário. Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

### Configuração de envios de e-mail

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setEmailNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setEmailNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

### Configuração de inscrições de notificação por push

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].user setPushNotificationSubscriptionType: ABKNotificationSubscriptionType]
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.user.setPushNotificationSubscriptionType(ABKNotificationSubscriptionType)
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).

