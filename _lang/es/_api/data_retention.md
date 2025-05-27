---
nav_title: Retención de datos
article_title: Retención de datos
alias: /data_retention/
description: "Este artículo de referencia cubre la información general sobre retención de datos de Braze."
page_type: reference
page_order: 2.5

---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Información sobre la retención de datos de Braze

*Última revisión el 1 de abril de 2024*

> Este artículo cubre la información general sobre retención de datos de Braze.<br><br>Los datos almacenados en Braze se conservan y pueden utilizarse para segmentación, personalización y orientación durante toda la vida de la cuenta del Cliente. Esto significa que datos como atributos de perfil de usuario, atributos personalizados, eventos personalizados y compras se almacenan indefinidamente para los usuarios activos, a menos que el Cliente los elimine, durante la vigencia del contrato.<br><br>Braze cuenta con características, procesos y API para implementar automáticamente buenas prácticas de higiene de datos orientadas al cumplimiento del RGPD y otras buenas prácticas. Se describen a continuación.

## Retención de datos gestionada por los clientes a través del panel o API de Braze

Braze habilita a sus clientes para que eliminen ellos mismos perfiles de usuario y datos de atributos completos de su espacio de trabajo.

Esto significa que puedes: 
- Eliminar perfiles de usuario mediante el [punto final de la API de eliminación de usuarios de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) 
- Eliminar (null) o modificar los atributos de los perfiles de usuario mediante el [punto final de la API de seguimiento de usuarios de Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)

Los eventos de comportamiento no se pueden eliminar de un perfil de usuario (eventos personalizados, sesiones, campañas, compras). Para eliminar esos eventos, debes borrar todo el perfil de usuario.

Por motivos de privacidad, es posible que debas eliminar todos los datos personales de un Usuario a petición de éste. Puedes encontrar instrucciones en nuestra página de [asistencia técnica sobre protección de datos]({{site.baseurl}}/help/dp-technical-assistance/#the-right-to-erasure).

{% alert note %}
Un usuario puede tener varios perfiles, y puede que necesites borrar varios perfiles para borrar todos los datos pertenecientes a un solo usuario. Sigue las instrucciones de la página de asistencia técnica de protección de datos sobre cómo eliminar completamente todos los datos relativos a un Usuario.
{% endalert %}

## Retención de datos gestionada por Braze para características específicas de los servicios Braze

#### Base de datos Braze: Archivo/eliminación automática de usuarios abandonados

Cada semana, Braze ejecuta un proceso para eliminar a los usuarios inactivos y latentes de los servicios Braze. En general, se trata de usuarios que no están localizables (por ejemplo, no tienen dirección de correo electrónico, número de teléfono, token de notificaciones push, no utilizan tus aplicaciones ni visitan tus sitios web), no han registrado actividad en su perfil de usuario y no han recibido mensajes ni han interactuado con ellos utilizando Braze. Esto se hace para cumplir los principios del RGPD y las mejores prácticas. Puedes leer más sobre este proceso en nuestra página [de definiciones de archivado de usuarios]({{site.baseurl}}/user_archival/).

{% alert note %}
Los clientes tienen pleno control sobre si un usuario está o no Inactivo o Dormido, y pueden evitar que se archiven los perfiles de usuario registrando un punto de datos a intervalos regulares. Braze Canvas ofrece la posibilidad de hacerlo automáticamente, lo que te permite desactivar de forma efectiva esta funcionalidad para algunos o todos tus usuarios inactivos o durmientes.
{% endalert %}

#### Datos de la campaña y de las interacciones con Canvas 

Los datos de interacción de mensajería se refieren a cómo interactúa un usuario con una campaña o Canvas que ha recibido (por ejemplo, cuando un usuario abre la campaña A o un usuario recibe la variante A). Estos datos se utilizan para reorientar. Puedes leer más sobre la [disponibilidad de datos de interacción de]({{site.baseurl}}/messaging_interaction_data/) mensajes en [Acerca de la disponibilidad de datos de interacción de mensajes]({{site.baseurl}}/messaging_interaction_data/).

## Retención de datos gestionada por Braze

Las siguientes políticas de retención están relacionadas con el cumplimiento por parte de Braze del RGPD y de la normativa sobre privacidad, y se refieren al almacenamiento transitorio de datos a medida que pasan por nuestros sistemas internos. Estas políticas de retención no afectan a los Servicios Braze y son informativas para tus equipos legales y de privacidad.

#### Servidores de Braze: Retención a corto plazo con fines de recuperación

Los datos enviados por Braze a determinados subprocesadores pueden seguir existiendo en los sistemas internos de Braze durante un máximo de 90 días.

#### Retención de datos en el lago de datos Braze

Los datos disponibles para los clientes en el panel de Braze están en su mayoría agregados. Los registros detallados se guardan en una base de datos independiente creada por Braze (el "Lago de Datos"). Los datos del Lago de Datos se utilizan para informes agregados y otras funciones avanzadas. Braze elimina la información de identificación personal de los datos de eventos almacenados en el Lago de Datos después de dos años (consulta más información en nuestra página de [Retención de Datos de Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention#snowflake-data-retention/) ).

Si utilizas nuestras API para eliminar perfiles de usuario o eliminar o modificar atributos de perfiles de usuario, pueden pasar hasta tres semanas hasta que esos datos se eliminen del Lago de Datos de Braze. La eliminación de datos en el Lago de Datos no afectará a la segmentación ni a la personalización, sino que garantiza que los datos se eliminan de todos los sistemas Braze.

#### Servidores de copia de seguridad Braze

Cuando se eliminan datos de tu instancia de producción, los datos permanecen en los servidores de copia de seguridad de Braze durante seis meses y luego se eliminan de acuerdo con nuestros procesos internos.
