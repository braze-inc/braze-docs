---
nav_title: Desencadenantes de atributos
article_title: Desencadenantes de atributos
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los desencadenantes de atributos y cómo puedes utilizarlos para enviar mensajes basados en acciones a los usuarios."
tool:
  - Campaigns

---

# Desencadenantes de atributos

> Los desencadenantes de atributos te permiten enviar mensajes basados en acciones cuando cambia el estado de suscripción de un usuario o los valores de un atributo personalizado. 

Los desencadenadores de atributos están disponibles para los siguientes escenarios:

- Actualizaciones del estado de suscripción.
- Los valores de atributo personalizado booleano, entero, cadena o fecha cambian a cualquier valor.
- Los valores booleanos, enteros o de cadena del atributo personalizado cambian a un valor específico.

Para empezar a utilizar desencadenantes de atributos, crea una campaña o un componente Canvas y selecciona **Entrega basada en acciones** como método de entrega. A continuación, selecciona el desencadenador de atributos que quieras utilizar.

\!["Entrega basada en acciones" sección con un desplegable para seleccionar un desencadenante.]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Actualizar estado de suscripción

Utiliza el desencadenador `Update Subscription Status` para dirigirte a los usuarios cuando se actualice su estado de suscripción. 

Por ejemplo, puedes dirigirte a los usuarios cuando su estado de suscripción por correo electrónico o push cambie a adhesión voluntaria, y darles las gracias por ello. También puedes enviar un webhook a tus sistemas cada vez que un usuario cancele su suscripción de correo electrónico, para que tus sistemas internos estén al día de la información más reciente sobre el estado de la suscripción.

{% alert important %}
Este desencadenante no se aplica cuando se crea un nuevo usuario con el estado global de correo electrónico predeterminado de `subscribed` y hay una solicitud posterior para actualizar el estado a `subscribed`, ya que el estado de suscripción no ha cambiado.
{% endalert %}

### Actualizar estado del grupo de suscripción

Utiliza el desencadenador `Update Subscription Group Status` para dirigirte a los usuarios cuando se actualice el estado de su grupo de suscripción por correo electrónico, SMS o WhatsApp. 

Por ejemplo, puedes dirigirte a los usuarios con un mensaje SMS de bienvenida cuando se adhieran voluntariamente a tu programa. También puedes especificar el origen de la actualización para tener un control más preciso sobre cuándo se dispara un mensaje. 

Las fuentes de actualización disponibles varían según el canal:
- Paso en Canvas para actualizar usuarios
- Importación CSV
- Lista- Cancelar suscripción
- Centro de preferencias
- API REST
- SDK
- Shopify (correo electrónico, SMS)
- Mensaje entrante (SMS)

Por ejemplo, tal vez quieras enviar tu SMS de bienvenida sólo cuando la actualización proceda de la API REST y no de un mensaje entrante, puesto que Braze ya responde automáticamente a determinados SMS entrantes.

### Cambiar valor de atributo personalizado

Para el atributo de cambio, se evalúa primero el desencadenante y luego los criterios de audiencia. Esto difiere del comportamiento predeterminado de evaluar primero los criterios de audiencia y luego desencadenar. Para evitar una condición de carrera, asegúrate de que el atributo utilizado como desencadenante no sea el mismo que el utilizado para calificar a tu audiencia.

#### Cualquier opción de valor nuevo

Utiliza el desencadenador `Change Custom Attribute Value` con la opción `any new value` para dirigirte a los usuarios cuando un valor booleano, entero, de cadena o de fecha cambie a cualquier nuevo valor.

Por ejemplo, dirígete a los usuarios cuando cambie su número de puntos de recompensa para informarles de cuántos puntos tienen ahora. En este ejemplo, digamos que un usuario tiene 85 puntos de recompensa y has configurado una campaña para que se desencadene cuando el atributo de puntos de recompensa cambie a cualquier nuevo valor. Si el valor del atributo de puntos de recompensa de este usuario cambia a cualquier valor nuevo (como 83, 84, 86, etc.), se desencadenará la campaña.

Considera el siguiente ejemplo de caso de uso con una notificación de actualización de niveles. Puede que quieras avisar a los usuarios si cambia su nivel de recompensa. Para llevar a cabo este caso de uso, configura una campaña que se desencadene a partir de `Change Custom Attribute Value` y configúrala para que se desencadene cuando el nivel de recompensa del atributo personalizado cambie a cualquier valor nuevo.

{% alert important %}
Los desencadenadores de atributos no están disponibles actualmente para los atributos de matriz.
{% endalert %}

\![Un desencadenador "Cambiar valor de atributo personalizado" para que "AA_current_rewards_tier" cambie a cualquier valor.]({% image_buster /assets/img_archive/any_value.png %})

También puedes utilizar Liquid para personalizar el cuerpo del mensaje con el nuevo nivel de recompensa del cliente y proporcionarle más información sobre el cambio.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

#### Valor específico

Utiliza el desencadenador `Change Custom Attribute Value` con la opción `specific value` para dirigirte a los usuarios cuando un atributo personalizado booleano, entero o de cadena cambie a un valor específico. 

Por ejemplo, dirígete a los usuarios cuando su nivel de recompensa cambie al mejor nivel. Para este ejemplo, digamos que el mejor nivel de recompensa es Super VIP. Puedes configurar campañas para que se desencadenen cuando el atributo personalizado del nivel de recompensa de un usuario cambie a `Super VIP`, de forma que puedas felicitar al usuario por convertirse en Super VIP.

\![Un desencadenador de "Cambiar valor de atributo personalizado" para que "AA_current_rewards_tier" cambie al valor específico de "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Los desencadenadores de atributos para valores específicos de atributos personalizados no están disponibles para los atributos personalizados de matriz y fecha.
- El desencadenante de cambio de valores de atributo personalizado no se desencadena cuando el valor del atributo personalizado se actualiza a null.  
- El desencadenador de cambio de valores de atributo personalizado sólo se desencadenará cuando cambie el valor de un atributo personalizado. Si el valor actual de un atributo personalizado se reenvía a Braze (e.g el valor del atributo color favorito es rojo, y reenvías el valor rojo a Braze), no se producirá el desencadenante de cambio de valores del atributo personalizado.
- El desencadenante de cambio de valores de atributos personalizados también se aplica a los nuevos usuarios creados.
{% endalert %}

