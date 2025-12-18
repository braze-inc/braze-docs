{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Atribuições padrão do usuário

### Atribuições suportadas

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

### Definindo atributos padrão

Para definir um atributo de usuário padrão, defina o campo apropriado no objeto compartilhado `Braze.User`. A seguir está um exemplo de configuração do atributo nome:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: "Alex")
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:@"Alex"];
```

{% endtab %}
{% endtabs %}

### Removendo atributos padrão

Para remover um atributo de usuário padrão, passe `nil` para o método relevante.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.set(firstName: nil)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user setFirstName:nil];
```

{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes. Para mais informações sobre a opção de segmentação de cada atributo, consulte [Coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics/).

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados. Para mais informações, consulte [`Braze.User`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class).
{% endalert %}

### Definindo atributos personalizados

{% tabs local %}
{% tab string %}
Para definir um atributo personalizado com um valor `string`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: "your_attribute_value")
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" stringValue:"your_attribute_value"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab inteiro %}
Para definir um atributo personalizado com um valor `integer`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourIntegerValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andIntegerValue:yourIntegerValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab pontos flutuantes %}
Braze trata os valores `float` e `double` da mesma forma em nosso banco de dados. Para definir um atributo personalizado com um valor duplo:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute(key: "your_attribute_key", value: yourDoubleValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDoubleValue:yourDoubleValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab booleano %}
Para definir um atributo personalizado com um valor `boolean`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", value: yourBoolValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andBOOLValue:yourBOOLValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab data %}
Para definir um atributo personalizado com um valor `date`:

{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.user.setCustomAttribute("your_attribute_key", dateValue:yourDateValue)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
[AppDelegate.braze.user setCustomAttributeWithKey:@"your_attribute_key" andDateValue:yourDateValue];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab array %}
O número máximo de elementos em [arrays de atributos personalizados]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) é 25 por padrão. As matrizes que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos. O máximo para matrizes individuais pode ser aumentado para até 100. Se você gostaria que esse máximo fosse aumentado, entre em contato com seu gerente de atendimento ao cliente.

Para definir um atributo personalizado com um valor `array`:

{% subtabs %}
{% subtab swift %}
```swift
// Setting a custom attribute with an array value
AppDelegate.braze?.user.setCustomAttributeArray(key: "array_name", array: ["value1",  "value2"])
// Adding to a custom attribute with an array value
AppDelegate.braze?.user.addToCustomAttributeArray(key: "array_name", value: "value3")
// Removing a value from an array type custom attribute
AppDelegate.braze?.user.removeFromCustomAttributeArray(key: "array_name", value: "value2")
```
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Incrementando ou decrementando atributos personalizados

Este código é um exemplo de um atributo personalizado incrementando. Você pode incrementar o valor de um atributo personalizado por qualquer valor `integer` ou `long`:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.user.incrementCustomUserAttribute(key: "your_attribute_key", by: incrementIntegerValue)
```

{% endtab %}
{% tab objective-c %}

```objc
[AppDelegate.braze.user incrementCustomUserAttribute:@"your_attribute_key" by:incrementIntegerValue];
```

{% endtab %}
{% endtabs %}

### Removendo atributos personalizados

{% tabs %}
{% tab swift %}
Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttribute`.

```swift
AppDelegate.braze?.user.unsetCustomAttribute(key: "your_attribute_key")
```

{% endtab %}
{% tab objective-c %}
Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttributeWithKey`.

```objc
[AppDelegate.braze.user unsetCustomAttributeWithKey:@"your_attribute_key"];
```

{% endtab %}
{% endtabs %}

### Aninhando atributos personalizados

Você também pode aninhar propriedades dentro de atributos personalizados. No exemplo a seguir, um objeto `favorite_book` com propriedades aninhadas é definido como um atributo personalizado no perfil do usuário. Para mais detalhes, consulte [Nested Custom Attributes]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

{% tabs %}
{% tab swift %}
```swift
let favoriteBook: [String: Any?] = [
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
]

braze.user.setCustomAttribute(key: "favorite_book", dictionary: favoriteBook)
```
{% endtab %}

{% tab objective-c %}
```objc
NSDictionary *favoriteBook = @{
  @"title": @"The Hobbit",
  @"author": @"J.R.R. Tolkien",
  @"publishing_date": @"1937"
};

[AppDelegate.braze.user setCustomAttributeWithKey:@"favorite_book" dictionary:favoriteBook];
```
{% endtab %}
{% endtabs %}

### Usando a API REST

Você também pode usar nossa API REST para definir ou remover atributos de usuários. Para saber mais, consulte [User Data Endpoints]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Definindo assinaturas de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `set(emailSubscriptionState:)` ou `set(pushNotificationSubscriptionState:)`, respectivamente. Ambas as funções usam o tipo de enum `Braze.User.SubscriptionState` como argumentos. Esse tipo tem três estados diferentes:

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
{% tab objective-c %}

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
{% tab objective-c %}

```objc
[AppDelegate.braze.user setPushNotificationSubscriptionState: BRZUserSubscriptionState]
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
