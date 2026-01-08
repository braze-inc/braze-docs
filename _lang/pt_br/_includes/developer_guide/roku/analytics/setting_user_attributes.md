{% multi_lang_include developer_guide/prerequisites/roku.md %}

## Atribuições padrão do usuário

### Métodos predefinidos

Braze fornece métodos predefinidos para definir os seguintes atributos de usuário usando o objeto `m.Braze`.

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

### Definindo atributos padrão

Para definir um atributo padrão, chame o método relevante no objeto `m.Braze`.

{% tabs local %}
{% tab Nome %}
```brightscript
m.Braze.setFirstName("Alex")
```
{% endtab %}
{% tab Sobrenome %}
```brightscript
m.Braze.setLastName("Smith")
```
{% endtab %}
{% tab e-mail %}
```brightscript
m.Braze.setEmail("alex@example.com")
```
{% endtab %}
{% tab Gênero %}
```brightscript
m.Braze.setGender("m") ' Accepts: "m", "f", "o", "n", "u", "p"
```
{% endtab %}
{% tab Data de nascimento %}
```brightscript
m.Braze.setDateOfBirth(1990, 5, 15) ' Year, month, day
```
{% endtab %}
{% tab País %}
```brightscript
m.Braze.setCountry("United States")
```
{% endtab %}
{% tab Idioma %}
```brightscript
m.Braze.setLanguage("en")
```
{% endtab %}
{% tab Cidade natal %}
```brightscript
m.Braze.setHomeCity("New York")
```
{% endtab %}
{% tab Número de telefone %}
```brightscript
m.Braze.setPhoneNumber("+1234567890")
```
{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário

Além dos atributos de usuário padrão, o Braze também permite que você defina atributos personalizados usando vários tipos de dados diferentes.

### Configurações de atributos personalizados

{% tabs %}
{% tab String %}
Para definir um atributo personalizado, um valor `string`:

```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}

{% tab Inteiro %}
Para definir um atributo personalizado com um valor `integer`:

```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}

{% tab Pontos flutuantes %}
Braze trata valores `float` e `double` exatamente da mesma forma. Para definir um atributo personalizado com qualquer um dos valores:

```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
{% endtab %}

{% tab Booleano %}
Para definir um atributo personalizado com um valor `boolean`:

```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}

{% tab Data %}
Para definir um atributo personalizado com um valor `date`:

```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}

{% tab Vetor %}
Para definir um atributo personalizado com um valor `array`:

```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

{% alert important %}
Os valores de atributos personalizados têm um comprimento máximo de 255 caracteres; valores mais longos serão truncados.
{% endalert %}

### Incrementando e decrementando atributos personalizados

Este código é um exemplo de um atributo personalizado incrementando. Você pode incrementar o valor de um atributo personalizado por qualquer valor inteiro positivo ou negativo.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Removendo atributos personalizados

Para remover um atributo personalizado, passe a chave do atributo relevante para o método `unsetCustomAttribute`.

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Usando a API REST

Você também pode usar nossa API REST para definir ou remover atributos de usuários. Para saber mais, consulte [Endpoints de Dados de Usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuração de envios de e-mail

É possível definir os seguintes status de envio de e-mail para seus usuários de forma programática por meio do SDK.

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `OptedIn` | Inscrição e aceitação explícita |
| `Subscribed` | Inscrição feita, mas sem aceitação explícita |
| `UnSubscribed` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Esses tipos se enquadram em `BrazeConstants().SUBSCRIPTION_STATES`.
{% endalert %}

O método para definir o status da inscrição de e-mail é `setEmailSubscriptionState()`. Os usuários serão definidos como `Subscribed` automaticamente após o recebimento de um endereço de e-mail válido; no entanto, sugerimos que você estabeleça um processo de aceitação explícito e defina esse valor como `OptedIn` após o recebimento do consentimento explícito do usuário. Para saber mais, acesse [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```
