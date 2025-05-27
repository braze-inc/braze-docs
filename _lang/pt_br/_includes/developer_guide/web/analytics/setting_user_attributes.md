{% multi_lang_include developer_guide/prerequisites/web.md %}

## Atribuições padrão do usuário

{% tabs %}
{% tab implementação padrão %}
Para definir uma atribuição padrão para um usuário, chame o método `getCurrentUser()` em sua instância do Braze para obter uma referência ao usuário atual do seu aplicativo. Em seguida, é possível chamar métodos para definir uma atribuição de usuário.

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
Usando o Google Tag Manager, os atributos padrão do usuário (como o nome do usuário) devem ser registrados da mesma forma que os atributos personalizados do usuário. Certifique-se de que os valores que está passando para as atribuições padrão correspondam ao formato esperado especificado na documentação da [classe User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por exemplo, o atributo gender pode aceitar qualquer um dos seguintes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Portanto, para definir o gênero de um usuário como feminino, crie uma tag HTML personalizada com o seguinte conteúdo:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```
{% endtab %}
{% endtabs %}

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

## Atributos personalizados do usuário

{% tabs %}
{% tab implementação padrão %}
Além dos métodos padrão de atribuição de usuário, também é possível definir [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para seus usuários. Especificações completas do método, consulte [nossos JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

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

Você pode ter até 25 elementos em matrizes de atributos personalizados. As matrizes individuais que são definidas manualmente (não detectadas automaticamente) para o **Data Type** podem ser aumentadas em até 100 no dashboard do Braze em **Data Settings** > Custom Attributes. Se quiser aumentar esse máximo, entre em contato com o gerente da sua conta Braze.

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
As chaves e os valores de atributos personalizados só podem ter no máximo 255 caracteres. Para saber mais sobre valores válidos de atributos personalizados, consulte a [documentação de referência](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).
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

### Desconfigurando um atributo personalizado

Os atributos personalizados podem ser desativados definindo seu valor como `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Usando a API REST

Também é possível usar nossa API REST para definir ou cancelar as atribuições do usuário. Para saber mais, consulte [Pontos de extremidade de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).

## Configuração de inscrições de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções recebem o tipo `enum` `braze.User.NotificationSubscriptionTypes` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrição e aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando um usuário é registrado para receber notificações por push, o navegador o obriga a optar por permitir ou bloquear notificações e, se ele optar por permitir o push, será definido como `OPTED_IN` por padrão. 

Visite [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitação explícita.

### Cancelamento da inscrição de um usuário no envio de e-mail

```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

### Cancelar inscrição de um usuário no push

```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```
