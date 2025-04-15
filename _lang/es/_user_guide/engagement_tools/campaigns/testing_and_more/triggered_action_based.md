---
nav_title: Campañas activadas por API y basadas en acciones
article_title: Probar campañas activadas por API y basadas en acciones
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo probar campañas activadas por API y basadas en acciones."

---

# Campañas activadas por API y basadas en acciones

> Al configurar campañas, siempre es una buena práctica probar los mensajes antes de lanzarlos. Este artículo de referencia trata sobre la creación de un segmento de usuario de prueba que le permitirá inspeccionar las solicitudes de API, las cargas útiles y ver los registros de entregabilidad.

## Paso 1: Crear un segmento de usuarios de prueba

La única forma de probar la activación de una campaña con la API o un evento personalizado es lanzar la campaña en directo. Como parte del despliegue de una nueva campaña, recomendamos encarecidamente añadir un segmento de usuarios de prueba a las campañas cuando se pruebe la capacidad de entrega. Esto proporcionará una red de seguridad, asegurando que incluso si una campaña se envía accidentalmente, sólo llegará a los usuarios internos.

1. **Importar usuarios de prueba**<br>Los usuarios de prueba pueden importarse a Braze mediante un CSV o una solicitud única por lotes a través de [Postman]({{site.baseurl}}/api/postman_collection/). Al importar estos usuarios, recomendamos establecer un atributo personalizado en sus perfiles (como `internal_test_user: true`) que pueda utilizarse para crear un segmento de grupo de prueba. <br><br>
2. **Añadir usuarios de prueba como usuarios de prueba reconocidos por Braze**<br>[Si marca a sus usuarios de prueba como usuarios de prueba reconocidos por Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) en el panel de control, tendrá acceso a un registro detallado de cada usuario, lo que le permitirá inspeccionar las solicitudes de API, sus cargas útiles y ver los registros de entregabilidad. Estos registros pueden ayudarle a determinar si hubo algún problema en la entrega de campañas a los usuarios finales. <br><br>
3. **Crear segmento**<br>Para crear un segmento de usuarios de prueba, cree un segmento de usuarios con el atributo personalizado `internal_test_user` establecido en `true`. Este segmento puede eliminarse cuando la campaña se ponga en marcha. 

## Paso 2: Probar los envíos

A continuación, puede realizar un envío de prueba desde el panel de control de Braze o utilizar Inbox Vision (sólo correo electrónico) para ver el aspecto que tendrá el diseño mientras la campaña aún está en modo borrador. A continuación, puede enviar la campaña a su segmento de usuarios de prueba para comprobar que se comporta como se espera. Independientemente de si la campaña está activada por la API o basada en acciones, utilice Postman para enviar una única solicitud a la API de Braze y activar la campaña. 

## Paso 3: Utilice el registro Braze para inspeccionar los resultados de entrada

Utiliza el registro Braze para solucionar problemas de desencadenamiento, envío y eventos. 
- El [registro de usuario de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) le mostrará la carga útil sin procesar de la solicitud de activación de API, el evento personalizado que activa la campaña y cualquier propiedad de activación o evento asociada.
- El [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) registrará cualquier error y le ayudará a entender por qué un mensaje en particular puede no haber sido entregado.

## Paso 4: Eliminar el segmento de prueba y lanzar la campaña

Una vez que el mensaje se active y se muestre correctamente con todos los enlaces registrados, puede eliminar el segmento y actualizar la campaña. Si prefiere iniciar la campaña desde cero para que no se incluyan las pocas impresiones del usuario de prueba, puede duplicar la campaña y reiniciarla sin el segmento del usuario de prueba. 
