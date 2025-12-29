---
nav_title: Eventos
article_title: Eventos
page_order: 0
page_type: reference
description: "Este artículo describe los diferentes eventos en Braze -eventos estándar, eventos de compra y eventos personalizados- y su finalidad."
---

# Eventos 

> Esta página cubre los diferentes acontecimientos en Braze y su finalidad.

Braze utiliza algunos tipos de eventos diferentes para proporcionar una comprensión exhaustiva del comportamiento y la interacción de los usuarios con tu marca. Cada tipo de acto tiene una finalidad única:

- [Eventos estándar](#standard-events): Proporciona una comprensión básica de la interacción del usuario con tu aplicación o sitio web.
- [Compra eventos](#purchase-events): Crucial para comprender el comportamiento de compra del usuario y para el seguimiento de los ingresos. 
- [Eventos personalizados](#custom-events): Proporciona información más profunda sobre los comportamientos de los usuarios que son únicos para tu aplicación o negocio.

Mediante el seguimiento de estos diferentes tipos de eventos, puedes obtener un conocimiento más profundo de tus usuarios, lo que puede informar tus estrategias de marketing, ayudarte a optimizar tu aplicación y permitirte ofrecer una experiencia de usuario más personalizada. ¡Vamos a sumergirnos!

## Eventos estándar

En Braze, los eventos estándar son acciones predefinidas que los usuarios pueden realizar dentro de tu aplicación y que Braze sigue automáticamente tras integrar el SDK de Braze. He aquí algunos ejemplos de actos estándar:

- Lanzamiento de la aplicación
- [Comprar](#purchase-events)
- Inicio de la sesión
- Fin de sesión
- Notificación push con un clic
- Correo electrónico abierto

Como especialista en marketing, puedes utilizar estos eventos estándar para comprender el comportamiento del usuario y su interacción con tu aplicación. Por ejemplo, puedes ver con qué frecuencia los usuarios lanzan tu aplicación o cuántas compras se realizan. Esta información puede ser muy valiosa a la hora de crear campañas de marketing específicas.

Es importante tener en cuenta que, aunque Braze hace un seguimiento automático de los eventos estándar, los eventos de compra, los eventos personalizados y los atributos personalizados deben ser configurados por tu equipo de desarrolladores en función de tus necesidades y objetivos específicos.

## Eventos de compra

Los eventos de compra son una forma de registrar y hacer un seguimiento de las compras realizadas por tus usuarios. Son un tipo de evento estándar que está disponible por defecto después de integrar el SDK de Braze. Por ello, cuando utilizas eventos de compra para hacer un seguimiento de las compras, puedes controlar tus ingresos a lo largo del tiempo y a través de diferentes fuentes de ingresos directamente desde Braze.

Los eventos de compra registran la siguiente información clave sobre una compra:

- ID del producto (normalmente el nombre o la categoría del producto)
- Moneda
- Precio
- Cantidad

A continuación, puedes utilizar estos datos para segmentar a tus usuarios en función de su valor de duración, frecuencia de compra, compras específicas, etc.

Braze también admite compras en varias divisas. Si se informa de una compra en una moneda distinta del USD, se mostrará en el panel de Braze en USD, según la tasa de cambio en la fecha en que se informó de la compra.

Para saber más, visita nuestro artículo dedicado a [los actos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/).

{% details Example implementation %}

Ten en cuenta que la implementación real de los eventos de compra requerirá algunos conocimientos técnicos, ya que implica la integración del SDK de Braze con tu aplicación. Tu administrador del éxito del cliente guiará a tu equipo a través de este proceso como parte de tu incorporación, pero los pasos generales son los siguientes:

1. **Integra el SDK de Braze:** Antes de registrar cualquier evento, tienes que integrar el SDK de Braze en tu aplicación.
2. **Registra el evento de compra:** Una vez integrado el SDK, puedes registrar un evento de compra cada vez que un usuario realice una compra en tu aplicación. Esto suele hacerse en la función o método al que se llama cuando se completa una compra.

Aquí tienes un ejemplo de cómo registrar un evento de compra en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

En este ejemplo, "product_name" es el nombre del producto que se compró, "USD" es la moneda de la compra, "1,99" es el precio del producto y "1" es la cantidad comprada.

{:start="3"}
3\. **Visualiza el evento de compra en el panel de Braze:** Una vez registrado el evento de compra, puedes verlo en el panel de Braze. Puedes utilizar estos datos para analizar tus ingresos, segmentar a tus usuarios y mucho más.

Recuerda que la implementación exacta puede variar en función de la plataforma (iOS, Android, Web) y de los requisitos específicos de tu aplicación. 

{% enddetails %}

## Eventos personalizados

Los eventos personalizados son eventos que defines en función de las acciones específicas que quieres seguir dentro de tu aplicación o sitio web. Braze no los sigue automáticamente: debes configurar manualmente estos eventos en tu implementación del SDK de Braze. Los eventos personalizados pueden ser cualquier cosa, desde que un usuario complete un nivel en un juego hasta que actualice la información de su perfil.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

En este ejemplo, "completed_level" es el nombre del evento personalizado que se registra cuando un usuario completa un nivel en un juego. Ese evento personalizado se registra entonces en su perfil de usuario en Braze, que puedes utilizar para desencadenar campañas y personalizar la mensajería.

Para saber más, visita nuestro artículo dedicado a [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

{% details Example implementation %}

Al igual que los eventos de compra, los eventos personalizados requieren una configuración adicional. He aquí un proceso general para implementar eventos personalizados en Braze:

1. **Integra el SDK de Braze:** Antes de poder registrar cualquier evento, tienes que integrar el SDK de Braze en tu aplicación.
2. **Define tu evento personalizado:** Decide qué acción de tu aplicación quieres seguir como evento personalizado. Puede ser cualquier cosa significativa para tu aplicación, como un usuario que completa un nivel en un juego, un usuario que actualiza su perfil o un usuario que realiza un tipo específico de compra.
3. **Registra el evento personalizado:** Después de definir tu evento personalizado, puedes registrarlo en el código de tu aplicación. Esto suele hacerse en la función o método al que se llama cuando se produce la acción.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

En este ejemplo, "updated_profile" es el nombre del evento personalizado que se registra cuando un usuario actualiza su perfil.

{:start="4"}
4\. **Añade propiedades a tu evento personalizado (opcional):** Si quieres capturar detalles adicionales sobre el evento personalizado, puedes añadirle propiedades. Esto se hace pasando un diccionario de propiedades cuando registras el evento.

He aquí un ejemplo de cómo registrar un evento personalizado con propiedades en una aplicación iOS utilizando Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

En este ejemplo, el evento personalizado tiene una propiedad llamada "Nombre de propiedad" con un valor de "Valor de propiedad".

{:start="5"}
5\. **Ver el evento personalizado en el panel de Braze:** Una vez registrado el evento personalizado, puedes verlo en el panel de Braze. Puedes utilizar estos datos para analizar el comportamiento de los usuarios, segmentar a tus usuarios y mucho más.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


