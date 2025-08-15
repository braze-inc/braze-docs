---
nav_title: Eventos
article_title: Eventos
page_order: 0
page_type: reference
description: "Este artículo describe los distintos eventos de Braze -eventos estándar, eventos de compra y eventos personalizados- y su finalidad."
---

# Eventos 

> Esta página cubre los diferentes acontecimientos en Braze y su finalidad.

Braze utiliza algunos tipos de eventos diferentes para proporcionar una comprensión exhaustiva del comportamiento y la interacción de los usuarios con tu marca. Cada tipo de acto tiene una finalidad única:

- [Eventos estándar](#standard-events): Proporcionar una comprensión básica del compromiso del usuario con su aplicación o sitio.
- [Eventos de compra](#purchase-events): Crucial para comprender el comportamiento de compra de los usuarios y hacer un seguimiento de los ingresos. 
- [Eventos personalizados](#custom-events): Proporcione una visión más profunda de los comportamientos de los usuarios que son exclusivos de su aplicación o negocio.

Mediante el seguimiento de estos diferentes tipos de eventos, puedes obtener un conocimiento más profundo de tus usuarios, lo que puede informar tus estrategias de marketing, ayudarte a optimizar tu aplicación y permitirte ofrecer una experiencia de usuario más personalizada. ¡Vamos a sumergirnos!

## Eventos estándar

En Braze, los eventos estándar son acciones predefinidas que los usuarios pueden realizar dentro de su aplicación y que Braze rastrea automáticamente después de integrar el SDK de Braze. He aquí algunos ejemplos de eventos estándar:

- Lanzamiento de la aplicación
- [Compra](#purchase-events)
- Inicio de la sesión
- Fin de la sesión
- Notificación push pulsada
- Correo electrónico abierto

Como vendedor, puede utilizar estos eventos estándar para comprender el comportamiento del usuario y el compromiso con su aplicación. Por ejemplo, puedes ver con qué frecuencia los usuarios inician tu aplicación o cuántas compras se realizan. Esta información puede ser muy valiosa a la hora de crear campañas de marketing específicas.

Es importante tener en cuenta que, si bien Braze realiza un seguimiento automático de los eventos estándar, los eventos de compra, los eventos personalizados y los atributos personalizados deben ser configurados por su equipo de desarrollo en función de sus necesidades y objetivos específicos.

## Eventos de compra

Los eventos de compra son una forma de registrar y realizar un seguimiento de las compras realizadas por sus usuarios. Son un tipo de evento estándar que está disponible por defecto tras integrar el SDK de Braze. Por ello, cuando utiliza eventos de compra para realizar un seguimiento de las compras, puede supervisar sus ingresos a lo largo del tiempo y a través de diferentes fuentes de ingresos directamente desde Braze.

Los eventos de compra registran la siguiente información clave sobre una compra:

- ID del producto (normalmente el nombre o la categoría del producto)
- Divisa
- Precio
- Cantidad

A continuación, puede utilizar estos datos para segmentar a sus usuarios en función de su valor de vida, frecuencia de compra, compras específicas, etc.

Braze también admite compras en varias divisas. Si una compra se notifica en una moneda distinta del USD, se mostrará en el panel de control de Braze en USD, según el tipo de cambio vigente en la fecha en que se notificó la compra.

Para saber más, visite nuestro artículo dedicado a [los eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/).

{% details Ejemplo de aplicación %}

Ten en cuenta que la implementación real de los eventos de compra requerirá algunos conocimientos técnicos, ya que implica la integración del SDK de Braze con tu aplicación. Su gestor de éxito de clientes guiará a su equipo a través de este proceso como parte de su incorporación, pero los pasos generales son los siguientes:

1. **Integrar el SDK Braze:** Antes de registrar cualquier evento, tienes que integrar el SDK de Braze en tu aplicación.
2. **Registrar el evento de compra:** Una vez integrado el SDK, podrá registrar un evento de compra cada vez que un usuario realice una compra en su aplicación. Esto se hace normalmente en la función o método llamado cuando se completa una compra.

Aquí tienes un ejemplo de cómo registrar un evento de compra en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

En este ejemplo, "nombre_producto" es el nombre del producto que se compró, "USD" es la moneda de la compra, "1,99" es el precio del producto y "1" es la cantidad comprada.

{:start="3"}
3\. **Ver el evento de compra en el panel de Braze:** Una vez registrado el evento de compra, puede verlo en el panel de control de Braze. Puede utilizar estos datos para analizar sus ingresos, segmentar a sus usuarios y mucho más.

Recuerde que la implementación exacta puede variar en función de la plataforma (iOS, Android, Web) y de los requisitos específicos de su aplicación. 

{% enddetails %}

## Eventos personalizados

Los eventos personalizados son eventos que usted define en función de las acciones específicas que desea rastrear dentro de su aplicación o sitio. Braze no los sigue automáticamente: debes configurar manualmente estos eventos en tu implementación del SDK de Braze. Los eventos personalizados pueden ser cualquier cosa, desde que un usuario complete un nivel en un juego hasta que actualice la información de su perfil.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

En este ejemplo, "nivel_completado" es el nombre del evento personalizado que se registra cuando un usuario completa un nivel en un juego. Ese evento personalizado se registra entonces en su perfil de usuario en Braze, que puede utilizar para activar campañas y personalizar los mensajes.

Para más información, visite nuestro artículo dedicado a [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

{% details Ejemplo de aplicación %}

Al igual que los eventos de compra, los eventos personalizados requieren una configuración adicional. Este es un proceso general para implementar eventos personalizados en Braze:

1. **Integrar el SDK Braze:** Antes de poder registrar cualquier evento, tienes que integrar el SDK de Braze en tu aplicación.
2. **Definir tu evento personalizado:** Decida qué acción de su aplicación desea seguir como evento personalizado. Puede tratarse de cualquier cosa que sea significativa para su aplicación, como que un usuario complete un nivel en un juego, que actualice su perfil o que realice un tipo específico de compra.
3. **Registra el evento personalizado:** Una vez definido el evento personalizado, puedes registrarlo en el código de tu aplicación. Esto se hace normalmente en la función o método que se llama cuando se produce la acción.

Aquí tienes un ejemplo de cómo registrar un evento personalizado en una aplicación iOS utilizando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

En este ejemplo, "perfil_actualizado" es el nombre del evento personalizado que se registra cuando un usuario actualiza su perfil.

{:start="4"}
4\. **Añada propiedades a su evento personalizado (opcional):** Si desea capturar detalles adicionales sobre el evento personalizado, puede añadirle propiedades. Esto se hace pasando un diccionario de propiedades cuando se registra el evento.

Aquí tienes un ejemplo de cómo registrar un evento personalizado con propiedades en una app iOS usando Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

En este ejemplo, el evento personalizado tiene una propiedad llamada "Nombre de la propiedad" con un valor de "Valor de la propiedad".

{:start="5"}
5\. **Ver el evento personalizado en el panel de Braze:** Una vez registrado el evento personalizado, puede verlo en el panel Braze. Puede utilizar estos datos para analizar el comportamiento de los usuarios, segmentarlos y mucho más.

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


