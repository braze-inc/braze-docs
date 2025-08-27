---
nav_title: Activadores de atributos
article_title: Activadores de atributos
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artículo de referencia ofrece una visión general de los activadores de atributos y de cómo utilizarlos para enviar mensajes basados en acciones a los usuarios."
tool:
  - Campaigns

---

# Activadores de atributos

> Los activadores de atributos permiten enviar mensajes basados en acciones cuando cambia el estado de suscripción de un usuario o los valores de un atributo personalizado. 

Los activadores de atributos están disponibles para los siguientes escenarios:

- Actualizaciones del estado de suscripción.
- Los valores de los atributos personalizados booleano, entero, cadena o fecha cambian a cualquier valor.
- Los valores de los atributos personalizados booleanos, enteros o de cadena cambian a un valor específico.

Para empezar a utilizar los activadores de atributos, cree una campaña o un componente Canvas y seleccione **Entrega basada en acciones** como método de entrega. A continuación, selecciona el desencadenante de atributos que quieras utilizar.

![]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Actualizar el estado de la suscripción

Utilice el activador `Update Subscription Status` para dirigirse a los usuarios cuando se actualice su estado de suscripción. 

Por ejemplo, puedes dirigirte a los usuarios cuando su estado de suscripción por correo electrónico o push cambie a adhesión voluntaria, y darles las gracias por ello. También puede enviar un webhook a sus sistemas cada vez que un usuario se dé de baja del correo electrónico, de modo que sus sistemas internos estén actualizados con la información más reciente sobre el estado de la suscripción.

{% alert important %}
Este activador no se aplica cuando se crea un nuevo usuario con el estado global de correo electrónico predeterminado de `subscribed` y hay una solicitud posterior para actualizar el estado a `subscribed`, ya que el estado de suscripción no ha cambiado.
{% endalert %}

### Actualizar el estado del grupo de suscripción

Utilice el activador `Update Subscription Group Status` para dirigirse a los usuarios cuando se actualice el estado de su grupo de suscripción por correo electrónico, SMS o WhatsApp. 

Por ejemplo, puedes dirigirte a los usuarios con un mensaje SMS de bienvenida cuando se adhieran voluntariamente a tu programa. También puede especificar el origen de la actualización para tener un control más preciso sobre cuándo se dispara un mensaje. 

Las fuentes de actualización disponibles varían según el canal:
- Importar CSV
- Centro de preferencias
- API REST
- SDK
- Shopify (Correo electrónico, SMS)
- Mensaje entrante (SMS)

Por ejemplo, es posible que sólo desee enviar su SMS de bienvenida cuando la actualización proceda de la API REST y no de un mensaje entrante, puesto que Braze ya responde automáticamente a determinados SMS entrantes.

### Cambiar el valor de un atributo personalizado

Para el atributo de cambio, se evalúa primero el desencadenante y luego los criterios de audiencia. Esto difiere del comportamiento por defecto, en el que primero se evalúan los criterios de audiencia y luego se dispara. Para evitar una condición de carrera, asegúrese de que el atributo utilizado como disparador no es el mismo que el atributo utilizado para calificar a su audiencia.

#### Cualquier nueva opción de valor

Utilice el disparador `Change Custom Attribute Value` con la opción `any new value` para dirigirse a los usuarios cuando un valor booleano, entero, de cadena o de fecha cambie a cualquier nuevo valor.

Por ejemplo, diríjase a los usuarios cuando cambie su número de puntos de fidelidad para informarles de cuántos puntos tienen ahora. En este ejemplo, digamos que un usuario tiene 85 puntos de fidelidad y usted ha configurado una campaña para que se active cuando el atributo de puntos de fidelidad cambie a cualquier nuevo valor. Si el valor del atributo de puntos de fidelidad de este usuario cambia a cualquier nuevo valor (e.g 83, 84, 86, etc.), la campaña se activará.

Considere el siguiente ejemplo de uso con una notificación de actualización de nivel. Es posible que desee alertar a los usuarios si su nivel de fidelidad cambia. Para llevar a cabo este caso de uso, configure una campaña que se active desde `Change Custom Attribute Value` y configúrela para que se active cuando el atributo personalizado nivel de fidelización cambie a cualquier valor nuevo.

{% alert important %}
Los activadores de atributos no están disponibles actualmente para los atributos de matriz.
{% endalert %}

![Cualquier valor nuevo]({% image_buster /assets/img_archive/any_value.png %})

También puede utilizar Liquid para personalizar el cuerpo del mensaje con el nuevo nivel de fidelización del cliente y proporcionarle más información sobre el cambio.

{% raw %}
```liquid
Your loyalty tier was just changed to {{custom_attribute.${loyalty_tier}}}
```
{% endraw %}

#### Valor específico

Utilice el disparador `Change Custom Attribute Value` con la opción `specific value` para dirigirse a los usuarios cuando un atributo personalizado booleano, entero o de cadena cambie a un valor específico. 

Por ejemplo, diríjase a los usuarios cuando su nivel de fidelidad cambie al mejor nivel. Para este ejemplo, digamos que el mejor nivel de fidelidad es Super VIP. Puede configurar una campaña para que se active cuando el atributo personalizado de nivel de fidelización de un usuario cambie a `Super VIP`, de forma que pueda felicitar al usuario por convertirse en Super VIP.

![]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Los activadores de atributos para valores de atributos personalizados específicos no están disponibles para atributos personalizados de matriz y fecha.
- El activador de cambio de valores de atributos personalizados no se activa cuando el valor del atributo personalizado se actualiza a null.  
- El activador de cambio de valores de atributos personalizados sólo se activará cuando cambie el valor de un atributo personalizado. Si el valor actual de un atributo personalizado se reenvía a Braze (e.g el valor del atributo de color favorito es rojo, y usted reenvía el valor rojo a Braze), el activador de cambio de valores de atributo personalizado no se producirá.
- El activador de cambio de valores de atributos personalizados también se aplica a los nuevos usuarios creados.
{% endalert %}

