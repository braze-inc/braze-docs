---
nav_title: Consentimiento y recogida de direcciones
article_title: Consentimiento y recogida de direcciones
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para recopilar el consentimiento y las direcciones de correo electrónico de los usuarios y define los diferentes estados posibles de los suscriptores de los usuarios."
channel: email

---

# Consentimiento y recopilación de direcciones

> Antes de enviar los primeros correos electrónicos, es importante obtener el permiso de los clientes. Es un gesto de cortesía y hace maravillas en tus tasas de apertura.

## Estados del suscriptor

Hay tres estados de suscripción de correo electrónico para un usuario: **opted in**, **subscribed**, y **unsubscribed**. Para cambiar el estado de suscripción de un usuario, consulte nuestro artículo sobre el [cambio de suscripciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) o utilice nuestras [API de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Estado del suscriptor | Descripción |
|---|---|
| Optado | Estos clientes han hecho clic en el enlace de un correo electrónico de confirmación y han optado activamente por recibir sus mensajes. |
| Suscrito | Por defecto, los usuarios están suscritos al correo electrónico mientras tengan una dirección de correo electrónico válida almacenada en su perfil. los usuarios permanecen suscritos hasta que se dan de baja o se dan de alta. |
| No suscrito | Para ser marcado como desuscrito, un cliente debe haberse dado de baja explícitamente de sus correos electrónicos o haber marcado un correo como spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de recogida de direcciones

Además de obtener el permiso de los usuarios antes de enviar el mensaje, existen varios métodos para recopilar estas direcciones de correo electrónico que pueden afectar a la capacidad de entrega. 

### Listas de direcciones adquiridas

El envío de correos electrónicos a listas compradas o alquiladas constituye una infracción del contrato Braze. Si estás comprando correos electrónicos, estás enviando mensajes totalmente no solicitados y te estás exponiendo a problemas de capacidad de entrega.

### Coinscripción

El corregistro se refiere a un acuerdo entre empresas para recopilar información sobre los usuarios. Se trata de un método de recaudación arriesgado. Permite a los usuarios recibir correos electrónicos de terceros, a veces sin su conocimiento o permiso. Si opta por esta vía, asegúrese de que la información sea clara y de que se pueda cancelar la suscripción en el punto de recogida.

### Adhesión voluntaria preseleccionada o forzada

El opt-in preseleccionado es un método de registro de correo electrónico en el que la casilla de registro de correo electrónico ya está marcada para que los suscriptores reciban su correo electrónico. Al dejar la casilla marcada, los suscriptores están dando su adhesión voluntaria y su consentimiento para recibir tu correo electrónico. Este método tiende a molestar a la gente (también es ilegal para el correo enviado a Canadá o dentro de este país). Puede que acabe teniendo una lista de correo electrónico de tamaño decente, pero no puede estar seguro de que estos usuarios quieran sus correos electrónicos de marketing.

### Adhesión voluntaria única

El opt-in único se produce cuando los suscriptores se registran a través de un formulario de suscripción y se añaden inmediatamente a su lista de correo electrónico. Con este método, los usuarios dan un solo paso para suscribirse, como escribir su dirección de correo electrónico en un campo de recogida o seleccionar una casilla como parte de una transacción.

### Adhesión voluntaria confirmada

Un opt-in confirmado se produce cuando un usuario marca una casilla solicitando comunicación por correo electrónico, y a cambio se envía un mensaje de confirmación. Este método permite a los usuarios elegir el tipo y la frecuencia del contenido mejora el compromiso. 

Para confirmar que sólo te diriges a los usuarios más comprometidos, también puedes utilizar el método de doble adhesión voluntaria confirmada. Este enfoque añade un paso adicional en el que el usuario debe hacer clic en un botón o enlace en el correo electrónico de confirmación para ser incluido en la lista de correo electrónico. 
