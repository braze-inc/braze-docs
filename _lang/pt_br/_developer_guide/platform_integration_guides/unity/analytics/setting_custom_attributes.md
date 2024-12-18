---
nav_title: Configuração de atributos personalizados
article_title: Configuração de atributos personalizados para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Este artigo de referência aborda como definir e desinstalar atributos personalizados na plataforma Unity."

---

# Definição de atributos personalizados

> O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

Antes da implementação, não deixe de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [práticas recomendadas][1].

## Atribuição de atribuições de usuário padrão

Para atribuir atribuições ao usuário, é necessário chamar o método apropriado no objeta BrazeBinding. A seguir, há uma lista de atribuições internas que podem ser chamadas usando esse método.

### Nome
`AppboyBinding.SetUserFirstName("first name");`

### Sobrenome
`AppboyBinding.SetUserLastName("last name");`

### E-mail do usuário
`AppboyBinding.SetUserEmail("email@email.com");`

>  Ainda é importante definir os endereços de e-mail mesmo que não esteja enviando e-mails pelo Braze. O envio de e-mail facilita a pesquisa de perfis de usuários individuais e a solução de problemas à medida que eles surgem.

### Gênero
`AppboyBinding.SetUserGender(Appboy.Models.Gender);`

### Data de nascimento
`AppboyBinding.SetUserDateOfBirth("year(int)", "month(int)", "day(int)");`

### País do usuário
`AppboyBinding.SetUserCountry("country name");`

### Cidade de origem do usuário
`AppboyBinding.SetUserHomeCity("city name");`

### Envio de e-mail para o usuário
`AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Inscrição push do usuário
`AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType);`

### Número de telefone do usuário
`AppboyBinding.SetUserPhoneNumber("phone number");`

## Atribuição de atributos personalizados ao usuário

Além dos atributos de usuário padrão, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes:
Para saber mais sobre as opções de segmentação que cada um desses atributos lhe proporcionará, consulte nossa [ documentação de "Práticas recomendadas"][1] nesta seção.

### Definição de valores de atributos personalizados

{% tabs %}
{% tab Valor booleano %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom boolean attribute key", 'boolean value');
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
{% tab String %}

```csharp
AppboyBinding.SetCustomUserAttribute("custom string attribute key", "string custom attribute");
```

{% endtab %}
{% tab Data %}

```csharp
AppboyBinding.SetCustomUserAttributeToNow("custom date attribute key");
```

```csharp
AppboyBinding.SetCustomUserAttributeToSecondsFromEpoch("custom date attribute key", 'integer value');
```

>  As datas transmitidas à Braze devem estar no formato [ISO 8601][2], e.g `2013-07-16T19:20:30+01:00` ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`  e.g `2016-12-14T13:32:31.601-0800`

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
{% endtabs
%}
### Desativação de um atributo personalizado

Os atributos personalizados também podem ser desmarcados usando o seguinte método:

```csharp
AppboyBinding.UnsetCustomUserAttribute("custom attribute key");
```

## Definição de um atributo personalizado por meio da API REST
Você também pode usar nossa API REST para definir atribuições de usuário. Para fazer isso, consulte a [documentação da API do usuário][3].

## Limites de valores de atributos personalizados
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.

## Configuração de inscrições de usuários

Para configurar uma inscrição para seus usuários (por e-mail ou push), chame as funções     
`AppboyBinding.SetUserEmailNotificationSubscriptionType()` ou `AppboyBinding.SetPushNotificationSubscriptionType()`, respectivamente. Ambas as funções recebem os parâmetros `Appboy.Models.AppboyNotificationSubscriptionType` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OPTED_IN` | Inscrição e aceitação explícita |
| `SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Nenhuma aceitação explícita é exigida pelo Windows para enviar notificações por push aos usuários. Quando um usuário é registrado para push, ele é definido como `SUBSCRIBED` em vez de `OPTED_IN` por padrão. Para saber mais, consulte nossa documentação sobre a [implementação de inscrições e aceitações explícitas][10].

- `EmailNotificationSubscriptionType`
  - Os usuários serão configurados para `SUBSCRIBED` automaticamente após o recebimento de um endereço de e-mail válido. No entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OPTED_IN` após o recebimento do consentimento explícito do usuário. Visite nosso documento [Alterando inscrições de usuários][8] para obter mais detalhes.
- `PushNotificationSubscriptionType`
  - Os usuários serão configurados para `SUBSCRIBED` automaticamente mediante registro push válido. No entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OPTED_IN` após o recebimento do consentimento explícito do usuário. Visite nosso documento [Alterando inscrições de usuários][8] para obter mais detalhes.

>  Esses tipos se enquadram em `Appboy.Models.AppboyNotificationSubscriptionType`.

## Exemplo de código

### Envio de e-mail:

```csharp
AppboyBinding.SetUserEmailNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

### Inscrição de notificações por push:

```csharp
AppboyBinding.SetUserPushNotificationSubscriptionType(AppboyNotificationSubscriptionType.OPTED_IN);
```

[1]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection
[2]: http://en.wikipedia.org/wiki/ISO_8601
[3]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[8]: {{site.baseurl}}/user_guide/administrative/manage_your_users/managing_user_subscriptions/#changing-subscriptions
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
