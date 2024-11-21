---
nav_title: Configuración de atributos personalizados
article_title: Configuración de atributos personalizados para Roku
platform: Roku
page_order: 4
page_type: reference
description: "Este artículo de referencia describe métodos para asignar atributos personalizados para Roku a los usuarios a través del SDK de Braze."

---

# Configuración de atributos personalizados

> Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

Antes de la implementación, asegúrate de revisar ejemplos de las opciones de segmentación que ofrecen los eventos personalizados, los atributos de usuario y los eventos de compra en nuestras [Mejores prácticas]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection). También te recomendamos que te familiarices con nuestras [convenciones de nomenclatura de Eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Asignar atributos predeterminados al usuario

Los atributos de usuario se asignarán al usuario activo en ese momento. Se pueden configurar los siguientes campos predeterminados:

- `FirstName`
- `LastName`
- `Email`
- `Gender`
- `DateOfBirth`
- `Country`
- `Language`
- `HomeCity`
- `PhoneNumber`

**Ejemplo de aplicación**<br>Así se vería en código la configuración del nombre de pila:

```brightscript
m.Braze.setFirstName("User's First Name")
```

## Asignar atributos personalizados al usuario

Además de los atributos predeterminados de usuario, Braze también te permite definir atributos personalizados utilizando varios tipos de datos diferentes.

### Configuración de valores de atributos personalizados
{% tabs %}
{% tab Booleano %}
```brightscript
m.Braze.setCustomAttribute("boolAttribute", true)
```
{% endtab %}
{% tab Entero %}
```brightscript
m.Braze.setCustomAttribute("intAttribute", 5)
```
{% endtab %}
{% tab Flotante o Doble %}
```brightscript
m.Braze.setCustomAttribute("floatAttribute", 3.5)
```
Braze trata los valores FLOAT y DOUBLE exactamente igual dentro de nuestra base de datos.
{% endtab %}
{% tab Cadena %}
```brightscript
m.Braze.setCustomAttribute("stringAttribute", "stringValue")
```
{% endtab %}
{% tab Fecha %}
```brightscript
dateAttribute = CreateObject("roDateTime")
dateAttribute.fromISO8601String("1992-11-29 00:00:00.000")
m.Braze.setCustomAttribute("dateAttribute", dateAttribute)
```
{% endtab %}
{% tab Matriz %}
```brightscript
stringArray = createObject("roArray", 3, true)
stringArray.Push("string1")
stringArray.Push("string2")
stringArray.Push("string3")
m.Braze.setCustomAttribute("arrayAttribute", stringArray)
```
{% endtab %}
{% endtabs %}

### Aumentar/disminuir atributos personalizados

Este código es un ejemplo de atributo personalizado que se incrementa. Puedes incrementar el valor de un atributo personalizado en cualquier valor entero positivo o negativo.

```brightscript
m.Braze.incrementCustomUserAttribute("intAttribute", 3)
```

### Desactivar un atributo personalizado

Los atributos personalizados también se pueden desactivar utilizando el siguiente método:

```brightscript
m.Braze.unsetCustomAttribute("attributeName")
```

### Configuración de un atributo personalizado a través de la API REST

También puedes utilizar nuestra API REST para establecer atributos de usuario. Consulta la documentación de [la API de usuario]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) para más detalles.

### Límites del valor del atributo personalizado

Los valores de atributos personalizados tienen una longitud máxima de 255 caracteres.

## Gestión del estado de las suscripciones por correo electrónico

Puedes configurar los siguientes estados de suscripción por correo electrónico para tus usuarios mediante programación a través del SDK.

| Estado de la suscripción | Definición |
| ------------------- | ---------- |
| `OptedIn` | Suscrito y con adhesión voluntaria explícita |
| `Subscribed` | Suscrito, pero sin adhesión voluntaria explícita |
| `UnSubscribed` | No suscrito y/o sin adhesión voluntaria explícita |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

>  Estos tipos se clasifican en `BrazeConstants().SUBSCRIPTION_STATES`

El método para configurar el estado de la suscripción por correo electrónico es `setEmailSubscriptionState()`. Los usuarios se configurarán en `Subscribed` automáticamente al recibir una dirección de correo electrónico válida, sin embargo, te sugerimos que establezcas un proceso de adhesión voluntaria explícito y configures este valor en `OptedIn` al recibir el consentimiento explícito de tu usuario. Para más detalles, visita [Gestionar las suscripciones de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions).

Ejemplo de uso:
```brightscript
m.Braze.setEmailSubscriptionState(BrazeConstants().SUBSCRIPTION_STATES.OPTED_IN)
```

