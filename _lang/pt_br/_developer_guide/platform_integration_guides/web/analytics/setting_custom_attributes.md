---
nav_title: Configuração de atributos personalizados
article_title: Configuração de atributos personalizados para a Web
platform: Web
page_order: 3
description: "Este artigo de referência aborda como atribuir e definir atributos personalizados para a Web."

---

# Definição de atributos personalizados

> O Braze fornece métodos para atribuir atribuições aos usuários. Você pode filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

Antes da implementação, examine exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [práticas recomendadas]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices).

Para atribuir atribuições aos seus usuários, chame o método `braze.getUser()` para obter uma referência ao usuário atual do seu app. Depois de ter uma referência ao usuário atual, é possível chamar métodos para definir atributos predefinidos ou personalizados.

## Atribuição de atribuições de usuário predefinidas

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

### Exemplos de implementação

#### Definição de um nome

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### Definição de um gênero

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### Definição de uma data de nascimento

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## Atribuição de atributos personalizados ao usuário

Além de nossos métodos predefinidos de atributos de usuários, o Braze também fornece [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para rastrear dados de seus aplicativos. 

As especificações completas do método para atributos personalizados podem ser encontradas aqui no [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

### Comprimento do atributo personalizado

As chaves e os valores de atributos personalizados têm um comprimento máximo de 255 caracteres. Consulte a [documentação técnica completa](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) para obter detalhes sobre os valores válidos de atributos personalizados.

### Exemplos de implementação

#### Definição de um atributo personalizado com um valor de string
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Definição de um atributo personalizado com um valor inteiro
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

#### Definição de um atributo personalizado com um valor de data
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
>  As datas passadas para o Braze com esse método devem ser objetos JavaScript Date.

#### Definição de um atributo personalizado com um valor de matriz

O número máximo de elementos em matrizes de atributos personalizados tem como padrão 25. As matrizes individuais podem ser aumentadas até 100 no dashboard da Braze, em **Configurações de dados** > **Atributos personalizados**. Se quiser aumentar esse máximo, entre em contato com o gerente de atendimento ao cliente. [As matrizes]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) que excederem o número máximo de elementos serão truncadas para conter o número máximo de elementos.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### Desativação de um atributo personalizado

Os atributos personalizados podem ser desativados definindo seu valor como `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Definição de um atributo personalizado por meio da API REST

Você também pode usar nossa API REST para definir atribuições de usuário. Consulte a documentação [da API dos usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para obter detalhes.

## Configuração de inscrições de usuários

Para configurar uma inscrição para seus usuários (envio de e-mail ou push), chame as funções `setEmailNotificationSubscriptionType()` ou `setPushNotificationSubscriptionType()`, respectivamente. Ambas as funções usam o tipo `enum` `braze.User.NotificationSubscriptionTypes` como argumentos. Esse tipo tem três estados diferentes:

| Status da inscrição | Definição |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Inscrição e aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Inscrição feita, mas sem aceitação explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | Cancelamento da inscrição e/ou aceitação explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando um usuário é registrado para receber notificações por push, o navegador o obriga a optar por permitir ou bloquear notificações e, se ele optar por permitir o push, será definido como `OPTED_IN` por padrão. 

Visite [Gerenciar inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para saber mais sobre a implementação de inscrições e aceitação explícita.

### Exemplo de código

#### Cancelar inscrição de um usuário no e-mail:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Cancelar inscrição de um usuário no push:
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

