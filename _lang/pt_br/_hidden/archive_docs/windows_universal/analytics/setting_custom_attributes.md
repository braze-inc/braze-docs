---
nav_title: Definindo Atributos Personalizados
article_title: Definindo Atributos Personalizados para Windows Universal
platform: Windows Universal
page_order: 3
description: "Este artigo de referência cobre como definir atributos personalizados na Plataforma Universal do Windows."
hidden: true
---

# Definindo atributos personalizados
{% multi_lang_include archive/windows_deprecation.md %}

Braze fornece métodos para atribuir atributos aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com esses atributos no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [Melhores práticas][7].

Os atributos do usuário podem ser atribuídos ao atual `IAppboyUser`. Para obter uma referência ao `IAppboyUser` atual, chame `Appboy.SharedInstance.AppboyUser`

## Atribuindo atributos de usuário padrão

Os seguintes atributos devem ser definidos como propriedades do `IAppboyUser`:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `HomeCity`
- `PhoneNumber`

**Exemplo de Implementação**

```csharp
Appboy.SharedInstance.AppboyUser.FirstName = "User's First Name"
```

## Atribuindo atributos personalizados ao usuário

Além dos atributos de usuário padrão, a Braze também permite que você defina atributos personalizados usando vários tipos diferentes de dados. Para saber mais sobre as opções de segmentação e como cada um desses atributos afetará você, consulte nossas [Melhores práticas]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices-and-notes).

### Definindo valores de atributo personalizado

{% tabs %}
{% tab Booleano %}
```csharp
bool SetCustomAttribute(STRING_KEY, BOOL_VALUE);
```
{% endtab %}
{% tab Inteiro %}
```csharp
bool SetCustomAttribute(STRING_KEY, INT_VALUE);
```
{% endtab %}
{% tab Double ou Float %}
```csharp
bool SetCustomAttribute(STRING_KEY, DOUBLE_VALUE);
```
Braze trata os valores FLOAT e DOUBLE exatamente da mesma forma em nosso banco de dados.
{% endtab %}
{% tab string %}
```csharp
bool SetCustomAttribute(STRING_KEY, "STRING_VALUE");
```
{% endtab %}
{% tab Long %}
```csharp
bool SetCustomAttribute(STRING_KEY, LONG_VALUE);
```
{% endtab %}
{% tab Data %}
```csharp
bool SetCustomAttribute(STRING_KEY, "DATE_VALUE");
```
>  As datas transmitidas à Braze devem estar no formato [ISO 8601][2], e.g `2013-07-16T19:20:30+01:00` ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`  e.g `2016-12-14T13:32:31.601-0800`
{% endtab %}
{% tab Vetor %}
```csharp
// Setting a custom attribute with an array value
Appboy.SharedInstance.EventLogger.SetCustomAttributeArray("custom_attribute_array_test", testSetArray);
// Adding to a custom attribute with an array value
Appboy.SharedInstance.EventLogger.AddToCustomAttributeArray("custom_attribute_array_test", testAddString);
// Removing a value from an array type custom attribute
Appboy.SharedInstance.EventLogger.RemoveFromCustomAttributeArray("custom_attribute_array_test", testRemString);
```
{% endtab %}
{% endtabs %}

### Incrementando/decrementando atributos personalizados

Este código é um exemplo de um atributo personalizado incrementando. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro positivo ou negativo.

```csharp
bool IncrementCustomAttribute(STRING_KEY, INCREMENT_INTEGER_VALUE);
```

### Desconfigurando um atributo personalizado

Atributos personalizados também podem ser desfeitos usando o seguinte método:

```csharp
bool UnsetCustomAttribute(STRING_KEY);
```

### Definindo um atributo personalizado via a API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Consulte a documentação da [API de usuários][4] para obter detalhes.

### limites de valor de atributo personalizado

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

## Gerenciamento do status de inscrição de notificações

Para configurar uma inscrição para seus usuários (seja e-mail ou push), você pode definir os seguintes status de inscrição como propriedades do `IAppboyUser`. Os status de inscrição na Braze têm três estados diferentes para e-mail e push:

| Status de inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrição e aceitação explícita |
| `Subscribed` | Inscrição feita, mas sem aceitação explícita |
| `UnSubscribed` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

- `EmailNotificationSubscriptionType`
  - Os usuários serão configurados para `Subscribed` automaticamente após o recebimento de um endereço de e-mail válido, no entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `OptedIn` após o recebimento do consentimento explícito do seu usuário.
- `PushNotificationSubscriptionType`
  - Os usuários serão configurados para `Subscribed` automaticamente após o registro válido de push, no entanto, sugerimos que você estabeleça um processo de aceitação explícita e defina este valor para `OptedIn` após o recebimento do consentimento explícito do seu usuário.

>  Esses tipos se enquadram em `AppboyPlatform.PCL.Models.NotificationSubscriptionType`. Para saber mais, consulte [Gerenciar inscrições de usuários][10].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_user_ids/#user-id-integration-best-practices--notes
[2]: http://en.wikipedia.org/wiki/ISO_8601
[4]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[7]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
