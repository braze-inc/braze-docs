{% multi_lang_include developer_guide/prerequisites/web.md %}

## Atribuições padrão do usuário

### Métodos predefinidos

O Braze fornece métodos predefinidos para configurar as seguintes atribuições de usuário na [classe`User`:](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)

- Nome
- Sobrenome
- Idioma
- País
- Data de nascimento
- E-mail
- Gênero
- Cidade
- Número de telefone

### Definindo atributos padrão

{% tabs %}
{% tab usando métodos %}
Para definir um atributo padrão para um usuário, chame o método `getUser()` na sua instância Braze para obter uma referência ao usuário atual do seu app. Então você pode chamar métodos para definir um atributo do usuário.

{% subtabs local %}
{% subtab First name %}
```javascript
braze.getUser().setFirstName("SomeFirstName");
```
{% endsubtab %}
{% subtab Gender %}
```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```
{% endsubtab %}
{% subtab Date of birth %}
```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Google Tag Manager %}
Usando o Google Tag Manager, atributos padrão do usuário (como o primeiro nome de um usuário) devem ser registrados da mesma forma que atributos personalizados do usuário. Certifique-se de que os valores que está passando para as atribuições padrão correspondam ao formato esperado especificado na documentação da [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por exemplo, o atributo gender pode aceitar qualquer um dos seguintes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Portanto, para definir o gênero de um usuário como feminino, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

### Removendo atributos padrão

Para remover um atributo padrão do usuário, passe `null` para o método relacionado. Por exemplo:

{% tabs local %}
{% tab Primeiro nome %}
```javascript
braze.getUser().setFirstName(null);
```
{% endtab %}
{% tab Gênero %}
```javascript
braze.getUser().setGender(null);
```
{% endtab %}
{% tab Data de nascimento %}
```javascript
braze.getUser().setDateOfBirth(null, null, null);
```
{% endtab %}
{% endtabs %}

## Atributos personalizados do usuário

### Definindo atributos personalizados

{% tabs %}
{% tab usando métodos %}
Além dos métodos de atributos padrão do usuário, você também pode definir [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para seus usuários. Especificações completas dos métodos, veja [nossos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

{% subtabs local %}
{% subtab String %}
Para definir um atributo personalizado com um valor `string`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

{% endsubtab %}
{% subtab Integer %}
Para definir um atributo personalizado com um valor `integer`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_INT_VALUE
);

// Integer attributes may also be incremented using code like the following
braze.getUser().incrementCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  THE_INTEGER_VALUE_BY_WHICH_YOU_WANT_TO_INCREMENT_THE_ATTRIBUTE
);
```

{% endsubtab %}
{% subtab Date %}
Para definir um atributo personalizado com um valor `date`:

```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_DATE_VALUE
);

// This method will assign the current time to a custom attribute at the time the method is called
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date()
);

// This method will assign the date specified by secondsFromEpoch to a custom attribute
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  new Date(secondsFromEpoch * 1000)
);
```

{% endsubtab %}
{% subtab Array %}

Você pode ter até 25 elementos em arrays de atributos personalizados. Arrays individuais que são definidos manualmente (não detectados automaticamente) para **Tipo de Dados** podem ser aumentados até 100 no painel Braze em **Configurações de Dados** > **Atributos Personalizados**. Se você quiser que esse máximo seja aumentado, entre em contato com seu gerente de conta Braze.

[As matrizes]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos.

Para definir um atributo personalizado com um valor `array`:

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

{% alert important %}
As datas passadas para o Braze com esse método devem ser objetos JavaScript Date.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Chaves e valores de atributos personalizados podem ter no máximo 255 caracteres. Para mais informações sobre valores válidos de atributos personalizados, consulte a [documentação de referência](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
Os atributos personalizados do usuário não estão disponíveis devido a uma limitação na linguagem de script do Google Tag Manager. Para registrar atributos personalizados, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
O modelo GTM não oferece suporte a propriedades aninhadas em eventos ou compras. É possível usar o HTML anterior para registrar quaisquer eventos ou compras que exijam propriedades aninhadas.
{% endalert %}
{% endtab %}
{% endtabs %}

### Removendo atributos personalizados

Para remover um atributo personalizado, passe `null` para o método relacionado.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Aninhando atributos personalizados

Você também pode aninhar propriedades dentro de atributos personalizados. No exemplo a seguir, um objeto `favorite_book` com propriedades aninhadas é definido como um atributo personalizado no perfil do usuário. Para mais detalhes, consulte [Attributes Personalizados Aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support).

```javascript
import * as braze from "@braze/web-sdk";

const favoriteBook = {
  title: "The Hobbit",
  author: "J.R.R. Tolkien",
  publishing_date: "1937"
};

braze.getUser().setCustomUserAttribute("favorite_book", favoriteBook);
```

### Usando a API REST

Você também pode usar nossa API REST para definir ou remover atributos de usuários. Para saber mais, consulte [Pontos de Extremidade de Dados de Usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Definindo assinaturas de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções aceitam o tipo `enum` `braze.User.NotificationSubscriptionTypes` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrição e aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando um usuário é registrado para receber notificações por push, o navegador o obriga a optar por permitir ou bloquear notificações e, se ele optar por permitir o push, será definido como `OPTED_IN` por padrão. 

Visite [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitação explícita.

### Cancelando a inscrição de um usuário por e-mail

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelando a inscrição de um usuário de push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
