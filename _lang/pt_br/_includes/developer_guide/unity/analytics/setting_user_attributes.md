{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Atribuições padrão do usuário

Para definir as atribuições do usuário, é necessário chamar o método apropriado no objeto `BrazeBinding`. A seguir, há uma lista de atribuições internas que podem ser chamadas usando esse método.

| Atributo                 | Exemplo de código |
|---------------------------|-------------|
| Nome                | `AppboyBinding.SetUserFirstName("first name");` |
| Sobrenome                 | `AppboyBinding.SetUserLastName("last name");` |
| E-mail do usuário                | `AppboyBinding.SetUserEmail("email@email.com");` |
| Gênero                    | `AppboyBinding.SetUserGender(Appboy.Models.Gender);` |
| Data de nascimento                | `AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");` |
| País do usuário              | `AppboyBinding.SetUserCountry("country name");` |
| Cidade de origem do usuário            | `AppboyBinding.SetUserHomeCity("city name");` |
| Envio de e-mail para o usuário   | `AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Inscrição push do usuário    | `AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);` |
| Número de telefone do usuário         | `AppboyBinding.SetUserPhoneNumber("phone number");` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Atributos personalizados do usuário

Além dos atributos padrão de usuários, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes. Para saber mais sobre a opção de segmentação de cada atributo, consulte [Coleta de dados de usuários]({{site.baseurl}}/developer_guide/analytics).

### Definindo atributos personalizados

{% tabs %}
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}

{% tab Inteiro %}

```csharp
// Set Integer Attribute
AppboyBinding.SetCustomUserAttribute("custom int attribute key", 'integer value');
// Increment Integer Attribute
AppboyBinding.IncrementCustomUserAttribute("key", increment(int))
```
{% endtab %}

{% tab Double %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom double attribute key", 'double value');
```

{% endtab %}

{% tab Booleano %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
```
{% endtab %}

{% tab Data %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

{% alert note %}
As datas passadas para o Braze devem estar no formato [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) (como `2013-07-16T19:20:30+01:00`) ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ` (como`2016-12-14T13:32:31.601-0800`).
{% endalert %}

{% endtab %}

{% tab Vetor %}

```csharp
// Setting An Array
AppboyBinding.SetCustomUserAttributeArray("key", array(List), sizeOfTheArray(int))
// Adding to an Array
AppboyBinding.AddToCustomUserAttributeArray("key", "Attribute")
// Removing an item from an Array
AppboyBinding.RemoveFromCustomUserAttributeArray("key", "Attribute")
```
{% endtab %}
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Desativação de atributos personalizados

Para cancelar a definição de um atributo personalizado de usuário, use o seguinte método:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

### Usando a API REST

Também é possível usar nossa API REST para definir ou cancelar as atribuições do usuário. Para saber mais, consulte [Pontos de extremidade de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuração de inscrições de usuários

Para configurar uma inscrição por e-mail ou push para seus usuários, chame uma das seguintes funções.

```csharp
// Email notifications
AppboyBinding.SetUserEmailNotificationSubscriptionType()

// Push notifications
AppboyBinding.SetPushNotificationSubscriptionType()`
```

Ambas as funções recebem `Appboy.Models.AppboyNotificationSubscriptionType` como argumentos, que tem três estados diferentes:

| Status de inscrição | Definição |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrição e aceitação explícita |
| `SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Nenhuma aceitação explícita é exigida pelo Windows para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Para saber mais, consulte nossa documentação sobre a [implementação de inscrições e aceitações explícitas]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).
{% endalert %}

| Tipo de inscrição                        | Descrição |
|------------------------------------------|-------------|
| `EmailNotificationSubscriptionType`      | Os usuários serão configurados para `SUBSCRIBED` automaticamente após o recebimento de um endereço de e-mail válido. No entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OPTED_IN` após o recebimento do consentimento explícito do usuário. Visite nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para obter mais detalhes. |
| `PushNotificationSubscriptionType`       | Os usuários serão configurados para `SUBSCRIBED` automaticamente mediante registro push válido. No entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OPTED_IN` após o recebimento do consentimento explícito do usuário. Visite nosso documento [Alterando inscrições de usuários]({{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions) para obter mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Esses tipos se enquadram em `Appboy.Models.AppboyNotificationSubscriptionType`.
{% endalert %}

### Configuração de envios de e-mail

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Configuração de inscrições de notificação por push

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```
