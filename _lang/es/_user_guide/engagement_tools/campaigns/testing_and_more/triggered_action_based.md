---
nav_title: Campañas desencadenadas por API y basadas en acciones
article_title: Probar campañas desencadenadas por API y basadas en acciones
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo probar campañas desencadenadas por API y basadas en acciones."

---

# Campañas desencadenadas por API y basadas en acciones

> Al configurar campañas, siempre es una buena práctica probar tus mensajes antes de lanzarlos. Este artículo de referencia trata sobre la creación de un segmento de usuario de prueba que te permitirá inspeccionar las solicitudes de la API, las cargas útiles y ver los registros de capacidad de entrega.

## Paso 1: Crea un segmento de usuarios de prueba

La única forma de probar el desencadenamiento de una campaña con la API o un evento personalizado es empujar la campaña en vivo. Como parte del despliegue de una nueva campaña, recomendamos encarecidamente añadir un segmento de usuario de prueba a las campañas cuando se pruebe desencadenar la capacidad de entrega. Esto proporcionará una red de seguridad, asegurando que incluso si una campaña se envía accidentalmente, sólo llegará a los usuarios internos.

1. **Importar usuarios de prueba**<br>Los usuarios de prueba pueden importarse a Braze mediante un CSV o una solicitud única por lotes a través de [Postman]({{site.baseurl}}/api/postman_collection/). Al importar estos usuarios, recomendamos establecer un atributo personalizado en sus perfiles (como `internal_test_user: true`) que pueda utilizarse para construir un segmento de grupo de prueba. <br><br>
2. **Añadir usuarios de prueba como usuarios de prueba reconocidos por Braze**<br>[Marcar a tus usuarios de prueba como usuarios de prueba reconocidos por Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) en el panel te da acceso a un registro detallado para cada usuario, lo que te permite inspeccionar las solicitudes de API, sus cargas útiles y ver los registros de capacidad de entrega. Estos registros pueden ayudarte a determinar si hubo algún problema al entregar las campañas a los usuarios finales. <br><br>
3. **Crear segmento**<br>Para crear un segmento de usuarios de prueba, crea un segmento de usuarios con el atributo personalizado `internal_test_user` establecido en `true`. Este segmento puede eliminarse cuando la campaña esté en vivo. 

## Paso 2: Prueba envía

A continuación, puedes hacer un envío de prueba desde el panel de Braze o utilizar Inbox Vision (sólo correo electrónico) para ver cómo será el diseño mientras la campaña está todavía en modo borrador. A continuación, puedes enviar la campaña a tu segmento de usuarios de prueba para comprobar que se comporta como esperas. Independientemente de si la campaña está desencadenada por la API o basada en acciones, utiliza Postman para enviar una única solicitud a la API de Braze, desencadenando la campaña. 

## Paso 3: Utiliza el registro Braze para inspeccionar los resultados de entrada

Utiliza el registro Braze para solucionar problemas de desencadenamiento, envío y eventos. 
- El [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) te mostrará la carga útil sin procesar de la solicitud de activación de la API, el evento personalizado que desencadena la campaña y cualquier propiedad del evento o activación asociada.
- El [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) registrará cualquier error y te ayudará a entender por qué puede no haberse entregado un mensaje concreto.

## Paso 4: Elimina el segmento de prueba y lanza la campaña

Cuando el mensaje se desencadene y se muestre correctamente con todos los enlaces registrados, puedes eliminar el segmento y actualizar la campaña. Si prefieres empezar la campaña desde cero para que no se incluyan las pocas impresiones de usuarios de prueba, puedes duplicar la campaña y reiniciarla sin el segmento de usuarios de prueba. 
