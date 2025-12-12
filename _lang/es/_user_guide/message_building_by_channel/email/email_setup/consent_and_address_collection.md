---
nav_title: Consentimiento y recogida de direcciones
article_title: Consentimiento y recogida de direcciones
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre las mejores prácticas para recopilar el consentimiento y las direcciones de correo electrónico de los usuarios, y define los diferentes estados posibles del suscriptor de usuario."
channel: email

---

# Consentimiento y recogida de direcciones

> Antes de enviar tus correos electrónicos iniciales, es importante obtener primero el permiso de tus clientes. Es una cortesía común y hace maravillas para tus tasas de apertura.

## Estados del suscriptor

Existen tres estados de suscripción por correo electrónico para un usuario: **adhesión voluntaria**, **suscripción** y **cancelación suscripción**. Para cambiar el estado de suscripción de un usuario, consulta nuestro artículo sobre cómo [cambiar las suscripciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) o utiliza nuestras [API de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Estado del suscriptor | Descripción |
|---|---|
| Adhesión voluntaria | Estos clientes han hecho clic en el enlace de un correo electrónico de confirmación y han optado activamente por recibir tus mensajes. |
| Suscrito | De forma predeterminada, los usuarios están suscritos al correo electrónico mientras tengan una dirección de correo electrónico válida almacenada en su perfil. Los usuarios permanecen suscritos hasta que se dan de baja o se suscriben voluntariamente. |
| Cancelar suscripción | Para ser marcado como no suscrito, un cliente se ha dado de baja explícitamente de tus correos electrónicos o ha marcado un correo como correo no deseado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Métodos de recogida de direcciones

Además de obtener el permiso de tus usuarios antes de la mensajería, existen varios métodos para recopilar estas direcciones de correo electrónico que pueden afectar a tu capacidad de entrega. 

### Listas de direcciones compradas

¡Enviar correos electrónicos a listas compradas o alquiladas es una violación de tu contrato Braze! Si estás comprando correos electrónicos, estás enviando mensajes totalmente no solicitados y te estás exponiendo a problemas de capacidad de entrega.

### Coinscripción

El co-registro se refiere a un acuerdo entre empresas para recopilar información del usuario. Es un método de recogida arriesgado. Hace que los usuarios reciban correos electrónicos de terceros, a veces sin el conocimiento o permiso del cliente. Si sigues este camino, asegúrate de que la información sea clara y de que se pueda cancelar la suscripción en el punto de recogida.

### Adhesión voluntaria preseleccionada o forzada

La adhesión voluntaria preseleccionada es un método de registro por correo electrónico en el que la casilla de registro de correo electrónico ya está marcada para que los suscriptores reciban tu correo electrónico. Al dejar la casilla marcada, los suscriptores están dando su adhesión voluntaria y su consentimiento para recibir tu correo electrónico. Este método tiene tendencia a molestar a la gente (también es ilegal para el correo enviado a Canadá o dentro de Canadá). Puede que acabes con una lista de correo electrónico de tamaño decente, pero realmente no puedes estar seguro de que estos usuarios quieran tus correos electrónicos de marketing.

### Adhesión voluntaria única

La adhesión voluntaria única se produce cuando los suscriptores se registran a través de un formulario de suscripción y se añaden inmediatamente a tu lista de correo electrónico. Con este método, los usuarios dan un solo paso para suscribirse, como escribir su dirección de correo electrónico en un campo de recogida o seleccionar una casilla como parte de una transacción.

### Adhesión voluntaria confirmada

Una adhesión voluntaria confirmada se produce cuando un usuario marca una casilla solicitando comunicación por correo electrónico, y a cambio se envía un mensaje de confirmación. Este método permite a los usuarios elegir el tipo y la frecuencia del contenido, lo que mejora la interacción. 

Para confirmar que sólo te diriges a los usuarios más comprometidos, también puedes utilizar el método de doble adhesión voluntaria confirmada. Este enfoque añade un paso adicional en el que el usuario debe hacer clic en un botón o enlace en el correo electrónico de confirmación para ser incluido en la lista de correo electrónico. 
