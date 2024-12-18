---
nav_title: Configuração de atributos personalizados
article_title: Configuração de atributos personalizados para o Roku
platform: Roku
page_order: 4
page_type: reference
description: "Este artigo de referência descreve os métodos para atribuir atributos personalizados do Roku aos usuários por meio do SDK da Braze."

---

# Definição de atributos personalizados

> O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

Antes da implementação, não deixe de analisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos de usuário e eventos de compra em nossas [práticas recomendadas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). Recomendamos também que você se familiarize com as nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Atribuição de atribuições de usuário padrão

As atribuições do usuário serão atribuídas ao usuário ativo no momento. Os seguintes campos padrão podem ser definidos:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**Exemplo de implementação**<br>Esta é a aparência da configuração de um nome no código:

```brightscript
m.Braze.setFirstName("User's First Name")
```

## Atribuição de atributos personalizados ao usuário

Além dos atributos de usuário padrão, o Braze também permite definir atributos personalizados usando vários tipos de dados diferentes.

### Configurações de valores de atributos personalizados
{% tabs %}
{% tab Booleano %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Inteiro %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Float ou Double %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
O Braze trata os valores FLOAT e DOUBLE exatamente da mesma forma em nosso banco de dados.
{% endtab %}
{% tab String %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Data %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Vetor %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Incremento/decremento de atributos personalizados

Este código é um exemplo de um atributo personalizado de incremento. Você pode incrementar o valor de um atributo personalizado em qualquer valor inteiro positivo ou negativo.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Desativação de um atributo personalizado

Os atributos personalizados também podem ser desmarcados usando o seguinte método:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Definição de um atributo personalizado por meio da API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Consulte a documentação [da API dos usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

### Limites de valores de atributos personalizados

Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres.

## Gerenciar o status da inscrição de e-mail

É possível definir os seguintes status de envio de e-mail para seus usuários de forma programática por meio do SDK.

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrição e aceitação explícita |
| `Subscribed` | Inscrição feita, mas sem aceitação explícita |
| `UnSubscribed` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Esses tipos se enquadram em `BrazeConstants().SUBSCRIPTION_STATES`

O método para definir o status da inscrição de e-mail é `setEmailSubscriptionState()`. Os usuários serão definidos como `Subscribed` automaticamente após o recebimento de um endereço de e-mail válido; no entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OptedIn` após o recebimento do consentimento explícito do usuário. Para saber mais, acesse [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

Exemplo de uso:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

