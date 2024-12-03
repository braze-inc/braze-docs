---
nav_title: Configuración de atributos personalizados
article_title: Configuración de atributos personalizados para la Web
platform: Web
page_order: 3
description: "Este artículo de referencia explica cómo asignar y establecer atributos personalizados para la Web."

---

# Configuración de atributos personalizados

> Braze proporciona métodos para asignar atributos a los usuarios. Puedes filtrar y segmentar a tus usuarios según estos atributos en el panel.

Antes de la implementación, revisa ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos personalizados y los eventos de compra en nuestras [Buenas prácticas]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices).

Para asignar atributos a tus usuarios, llama al método `braze.getUser()` para obtener una referencia al usuario actual de tu aplicación. Después de tener una referencia al usuario actual, puedes llamar a métodos para establecer atributos predefinidos o personalizados.

## Asignar atributos de usuario predefinidos

Braze proporciona métodos predefinidos para configurar los siguientes atributos de usuario dentro de la [clase`User`:](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)

- Nombre
- Apellido
- Idioma
- País
- Fecha de nacimiento
- Correo electrónico
- Género
- Ciudad natal
- Número de teléfono

### Ejemplos de aplicación

#### Configuración de un nombre de pila

```javascript
braze.getUser().setFirstName("SomeFirstName");
```

#### Configuración de un género

```javascript
braze.getUser().setGender(braze.User.Genders.FEMALE);
```

#### Configuración de una fecha de nacimiento

```javascript
braze.getUser().setDateOfBirth(2000, 12, 25);
```

## Asignar atributos personalizados al usuario

Además de nuestros métodos predefinidos de atributos de usuario, Braze también proporciona [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para hacer un seguimiento de los datos de tus aplicaciones. 

Las especificaciones completas de los métodos para los atributos personalizados se encuentran aquí, en [los JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

### Longitud del atributo personalizado

Las claves y valores de los atributos personalizados tienen una longitud máxima de 255 caracteres. Consulta la [documentación técnica completa](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) para obtener información detallada sobre los valores de atributos personalizados válidos.

### Ejemplos de aplicación

#### Configuración de un atributo personalizado con un valor de cadena
```javascript
braze.getUser().setCustomUserAttribute(
  YOUR_ATTRIBUTE_KEY_STRING,
  YOUR_STRING_VALUE
);
```

#### Establecer un atributo personalizado con un valor entero
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

#### Establecer un atributo personalizado con un valor de fecha
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
>  Las fechas pasadas a Braze con este método deben ser objetos Date de JavaScript.

#### Establecer un atributo personalizado con un valor de matriz

El número máximo de elementos de las matrices de atributos personalizadas está predeterminado en 25. Las matrices individuales pueden aumentarse hasta 100 en el panel de Braze, en **Configuración de datos** > **Atributos personalizados**. Si quieres aumentar este máximo, ponte en contacto con el administrador del servicio de atención al cliente. [Las matrices]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#arrays) que superen la cantidad máxima de elementos se truncarán para contener el número máximo de elementos.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, YOUR_ARRAY_OF_STRINGS);

// Adding a new element to a custom attribute with an array value
braze.getUser().addToCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "new string");

// Removing an element from a custom attribute with an array value
braze.getUser().removeFromCustomAttributeArray(YOUR_ATTRIBUTE_KEY_STRING, "value to be removed");
```

### Desactivar un atributo personalizado

Los atributos personalizados pueden desactivarse estableciendo su valor en `null`.

```javascript
braze.getUser().setCustomUserAttribute(YOUR_ATTRIBUTE_KEY_STRING, null);
```

### Configuración de un atributo personalizado a través de la API REST

También puedes utilizar nuestra API REST para establecer atributos de usuario. Consulta la documentación de [la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

## Configuración de las suscripciones de los usuarios

Para configurar una suscripción para tus usuarios (por correo electrónico o push), llama a las funciones `setEmailNotificationSubscriptionType()` o `setPushNotificationSubscriptionType()`, respectivamente. Estas dos funciones toman como argumento el tipo `enum` `braze.User.NotificationSubscriptionTypes` . Este tipo tiene tres estados diferentes:

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `braze.User.NotificationSubscriptionTypes.OPTED_IN` | Suscrito y con adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.SUBSCRIBED` | Suscrito, pero sin adhesión voluntaria explícita |
| `braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando un usuario se registra para recibir notificaciones push, el navegador le obliga a elegir entre permitir o bloquear las notificaciones, y si elige permitir las notificaciones push, éstas se configuran por defecto en `OPTED_IN`. 

Visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) para obtener más información sobre la implementación de las suscripciones y las adhesiones voluntarias explícitas.

### Ejemplo de código

#### Cancelar suscripción de un usuario a un correo electrónico:
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

#### Cancelar suscripción de un usuario desde push:
```java
braze.getUser().setPushNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.UNSUBSCRIBED);
```

