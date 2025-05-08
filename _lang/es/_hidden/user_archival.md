---
nav_title: Archivado de usuarios
article_title: Archivado de usuarios
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Este artículo de referencia cubre las definiciones de archivado de usuarios, el bloqueo de correo no deseado y cómo personalizar tu política de archivado de usuarios."

---
# Archivado de usuarios

> Cada semana, el domingo a las 5:30 am EST, Braze ejecuta un proceso para eliminar usuarios inactivos y usuarios inactivos de los Servicios Braze. Ten en cuenta que Braze no archiva usuarios a menos que el número de usuarios del espacio de trabajo alcance el umbral de 250.000. 

Este proceso pretende ayudar a Braze a proporcionar estadísticas precisas sobre las audiencias alcanzables por las campañas. También sirve de acuerdo con dos conceptos clave [del RGPD][1]:

1. Principio de limitación del almacenamiento: los datos personales tratados y almacenados no deben conservarse más tiempo del necesario.
2. Tener un fin comercial legítimo para procesar datos personales.

Es decir, los datos personales procesados y almacenados no deben conservarse más tiempo del necesario y los datos personales sólo deben procesarse con fines comerciales legítimos. También se eliminará el estado de cancelar suscripción de los usuarios archivados en cumplimiento del RGPD.

{% alert note %} Los clientes tienen pleno control sobre si un usuario está inactivo o no. Braze Canvas ofrece la posibilidad de hacerlo automáticamente, lo que te permite desactivar de forma efectiva esta funcionalidad para algunos o para todos tus usuarios inactivos. {% endalert %}

## Definiciones de archivado de usuarios

### Usuarios activos

Braze define a un "usuario activo" durante un periodo de tiempo determinado como cualquier usuario que haya registrado una sesión en una aplicación móvil o sitio web, se haya actualizado, haya recibido un mensaje o haya interactuado con un mensaje.

Si configuras ID de usuario para identificar a los usuarios, cuando un nuevo usuario se conecte se contará como un usuario activo distinto. Los usuarios que se actualicen a través de la API también se contarán como usuarios activos en el periodo de tiempo en que se actualicen.

{% alert important %}
Tanto los usuarios inactivos como los inactivos serán archivados a menos que el usuario sea excluido del archivo por las razones que se indican a continuación.
{% endalert %}

### Usuarios inactivos

Los "usuarios inactivos" son usuarios a los que no se puede acceder y que probablemente han abandonado. Los usuarios inactivos son aquellos que cumplen todos estos criterios:

- No puedo recibir el correo electrónico. Por ejemplo, no tienen dirección de correo electrónico o se han dado de baja de todas las listas de correo electrónico.
- No puedo recibir SMS. Por ejemplo, no tienen un número de teléfono válido o se han dado de baja de todos los grupos de suscripción a SMS.
- No puedo recibir notificaciones push. Por ejemplo, han desinstalado la aplicación o han desactivado los permisos push.
- No puedo recibir un mensaje de WhatsApp. Por ejemplo, no tienen un número de teléfono válido o se han dado de baja de todos los grupos de suscripción de WhatsApp.
- No puedo recibir un mensaje de LINE. Por ejemplo, no tienen un ID de LINE o se han dado de baja de todos los grupos de suscripción de LINE.
- No has utilizado ninguna aplicación móvil o visitado un sitio web en un espacio de trabajo en más de seis meses.
- Hace más de seis meses que no recibo mensajes de un espacio de trabajo.
- No se ha actualizado en más de seis meses.

En este caso, estos usuarios no pueden recibir mensajes y no están interactuando con tu marca. Estos usuarios han abandonado efectivamente.

### Usuarios inactivos

"Usuarios inactivos" son los usuarios que no han tenido actividad en los últimos doce meses y:

- No has utilizado ninguna aplicación móvil o visitado un sitio web en un espacio de trabajo en más de 12 meses.
- No has recibido ningún mensaje de un espacio de trabajo en más de 12 meses.
- No se han actualizado en más de 12 meses.

## Usuarios del grupo de control global

Los usuarios del grupo de control global nunca serán archivados, aunque cumplan la definición de usuarios inactivos o inactivos. 

### Grupo de muestra de tratamiento

Los usuarios del grupo de muestra de tratamiento en un Informe de grupo de control global están excluidos del archivo.

## Usuarios de prueba

Los usuarios de prueba nunca se archivarán, aunque se ajusten a la definición de usuarios inactivos o durmientes.

## Bloqueo de correo no deseado

Braze bloquea a los usuarios individuales con más de 5 millones de sesiones ("usuarios ficticios"), y ya no ingiere sus eventos SDK, porque suelen ser el resultado de una integración incorrecta. Si descubres que esto le ha ocurrido a un usuario legítimo, presenta un ticket [al soporte de]({{site.baseurl}}/braze_support/) Braze.

Para encontrar los usuarios ficticios de tu panel, realiza los siguientes pasos:

1. Crea un [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Selecciona el filtro `Session Count` y configúralo en `more than 5,000,000`.
3. Exporta el segmento mediante CSV.

Si es necesario, puedes eliminar a los usuarios a través del [punto final`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}

## Personaliza tu política de archivado de usuarios

Braze proporciona características de orquestación de datos que te permiten personalizar tu política de archivado de usuarios. Crea una política de archivado de usuarios que te ofrezca lo mejor de ambos mundos con el componente de [actualización de usuarios de]({{site.baseurl}}/user_update/) Canvas.

Esto te permite lo siguiente:

- Adhiérete al RGPD y a las mejores prácticas de privacidad eliminando los perfiles de usuario que ya no sean valiosos.
- Conserva cualquier perfil de usuario para el que tengas una necesidad empresarial legítima.

### Pasos

1. Dirígete a usuarios que cumplan los criterios de archivo de tu marca y que te gustaría conservar. Por ejemplo, podrías retener a los usuarios que:
    - La última vez que recibiste un mensaje fue hace más de 23 semanas o nunca has recibido un mensaje<br>Y<br>
    - Utilizó tu aplicación por última vez hace más de 23 semanas o tuvo cero sesiones en tu aplicación<br><br>
      ![Dirígete a usuarios que recibieron por última vez cualquier mensaje hace más de 23 semanas, que nunca han recibido un mensaje de una campaña o paso en Canvas, que utilizaron por última vez estas aplicaciones hace más de 23 semanas y que han utilizado estas aplicaciones exactamente cero veces.][2]<br><br>
2. Establece que la nueva elegibilidad dure algo menos de 6 meses.<br><br>
      ![Controles de entrada con la reelegibilidad activada y la ventana de reelegibilidad fijada en 23 semanas.][3]<br><br>
3. Configura el paso Actualización de usuario para añadir un evento a cada perfil.<br><br>
      ![Paso de actualización de usuario que añade el evento "do_not_archive" al perfil del usuario.][4]
{% details Ejemplo de objeto de actualización de usuario %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}
