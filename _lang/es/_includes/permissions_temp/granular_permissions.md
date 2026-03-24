{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Creación de un conjunto de permisos

Usa conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del dashboard que necesiten el mismo acceso en diferentes espacios de trabajo. Para crear un conjunto de permisos, ve a **Configuración** > **Configuración de permisos** y selecciona **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nombre|Permisos|
|-----------|----------------|
|Desarrolladores|«Ver claves de API», «Editar claves de API», «Ver grupos internos», «Editar grupos internos», «Ver registro de actividad de mensajes», «Ver registro de usuarios del evento», «Ver identificadores de API», «Ver panel de uso de API», «Ver límites de API», «Ver alertas de uso de API», «Editar alertas de uso de API», «Ver depurador de SDK», «Editar depurador de SDK».|
|Especialistas en marketing|«Ver campañas», «Editar campañas», «Archivar campañas», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver reglas de limitación de frecuencia», «Editar reglas de limitación de frecuencia», «Ver priorización de mensajes», «Editar priorización de mensajes», «Ver bloques de contenido», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver segmentos», «Editar segmentos», «Editar grupo de control global», «Ver plantillas de IAM», «Editar plantillas de IAM», «Archivar plantillas de IAM», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Archivar plantillas de correo electrónico», «Ver plantillas de webhook», «Editar plantillas de webhook», «Archivar plantillas de webhook», «Ver plantillas de enlaces de correo electrónico», «Editar plantillas de enlaces de correo electrónico», «Ver activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias», «Editar informes del dashboard», «Ver plantillas de banners», «Ver configuración de localización», «Usar Operator», «Ver agentes de Decisioning Studio», «Ver evento de conversión de Decisioning Studio».|
|Gestión de usuarios|«Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos».|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Crear un rol

Los roles permiten una mayor estructura al agrupar los permisos personalizados individuales con los controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un mismo dashboard. Con los roles, puedes añadir usuarios del dashboard a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol    | Espacio de trabajo | Permisos  
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | «Ver campañas», «Editar campañas», «Archivar campañas», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver bloques de contenido», «Editar bloques de contenido», «Archivar bloques de contenido», «Lanzar bloques de contenido», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver segmentos», «Editar segmentos», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias». |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |«Ver campañas», «Editar campañas», «Archivar campañas», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver bloques de contenido», «Editar bloques de contenido», «Archivar bloques de contenido», «Lanzar bloques de contenido», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver segmentos», «Editar segmentos», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias».|
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | «Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos»|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y los roles de los equipos?

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para agregar permisos de usuario a equipos

Es posible que encuentres dificultades al intentar guardar los permisos en el dashboard de Braze, especialmente al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tiene a nivel del espacio de trabajo. Esta restricción existe porque no tiene sentido tener un equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel del espacio de trabajo. En su lugar, asigna permisos exclusivamente a nivel de equipo.

## Usuarios limitados

Los usuarios limitados tienen permisos específicos que les permiten gestionar determinados aspectos del dashboard de Braze, pero con restricciones en comparación con los administradores de la empresa y los administradores del espacio de trabajo.

| Ámbito | Descripción |
| --- | --- |
| Permisos | Los usuarios limitados pueden editar los permisos de otros usuarios limitados si tienen el permiso «Editar usuarios del dashboard». También pueden crear nuevos usuarios limitados y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni gestionar cuentas de administrador de la empresa. |
| Limitaciones de roles | Si un usuario limitado tiene todos los permisos excepto «Administrador del espacio de trabajo», seguirá teniendo acceso a todos los demás permisos que normalmente se conceden a un administrador del espacio de trabajo. |
| Visibilidad de los permisos | Si un usuario limitado tiene el permiso «Editar usuarios del dashboard» para un espacio de trabajo (como Dev) pero no para otro (como Prod), no verá los permisos del espacio de trabajo Prod en la página de detalles de los usuarios del dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparación de usuarios limitados

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador del espacio de trabajo | Los administradores del espacio de trabajo tienen permisos específicos para gestionar los espacios de trabajo, pero no tienen la misma autoridad que los administradores de la empresa. Los usuarios limitados pueden heredar permisos similares a los de los administradores del espacio de trabajo si tienen marcados los permisos necesarios. |
| Administrador (administrador de la empresa) | Los administradores de la empresa tienen permisos más amplios, incluida la posibilidad de eliminar usuarios del dashboard. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de la empresa para realizar esa acción. |
| Acceso de solo lectura | Para acceder a algunas partes del dashboard, como la página de campañas, los usuarios deben tener asignados permisos de visualización.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Error de acceso limitado

Los usuarios pueden encontrar mensajes como «Necesitas permisos para "Ver páginas de inicio" para acceder a esta página». En tales casos, el usuario y el administrador de la cuenta deben verificar que se hayan concedido los permisos necesarios. Si es así, intenta resolver el problema desactivando y volviendo a habilitar los permisos del usuario. 

{% alert note %}
No es posible fusionar o importar permisos de usuario de un usuario del dashboard a otro.
{% endalert %}

## Editar los permisos de un usuario

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Usuarios de la empresa** y selecciona su nombre.

![La página «Usuarios de la empresa» en Braze muestra una tabla con los usuarios del dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador

Los administradores tienen acceso a todas las funciones y la posibilidad de modificar cualquier configuración de la empresa. Pueden:

- Cambiar [la configuración de aprobación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Añadir, editar, eliminar, suspender o anular la suspensión de otros [usuarios de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuarios de Braze como archivo CSV

Para conceder o eliminar privilegios de administrador, selecciona **Este usuario es un administrador** y luego selecciona **Actualizar usuario**.

![Los detalles del usuario seleccionado con la casilla de verificación de administrador activada.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, este no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o de espacio de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marca o desmarca la casilla junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

|Nombre del permiso|Descripción|
|----------|-----------|
|Administrar configuración de empresa|Permite a los usuarios modificar la configuración de permisos y la verificación del remitente.|
|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espacio de trabajo

Puedes dar a un usuario permisos diferentes para cada espacio de trabajo al que pertenezca en Braze. Para gestionar los permisos a nivel del espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y luego elige los permisos manualmente o asigna un [conjunto de permisos o un rol]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que hayas creado previamente. Si necesitas dar a un usuario permisos diferentes para distintos espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Permisos**, selecciona uno o varios permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado. Opcionalmente, puedes seleccionar **Asignar acceso de administrador al espacio de trabajo** si prefieres concederles permisos completos para este espacio de trabajo.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo seleccionados manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Conjuntos de permisos**, selecciona un conjunto de permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Rol**, elige un rol. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de un rol en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportación de permisos de usuario

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Usuarios de la empresa** y selecciona **Exportar usuarios**. En breve se enviará un archivo CSV a tu dirección de correo electrónico.

![La página «Usuarios de la empresa» en Braze con la opción «Exportar usuarios» resaltada.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permisos

| Permiso | Definición |
|-------------------------------------------------|---------------------|
| Ver datos de facturación                            | Ver detalles de facturación |
| Ver atributos personalizados marcados como PII            | Ver atributos personalizados marcados como PII |
| Ver PII                                        | Ver PII |
| Ver perfiles de usuario con cumplimiento de PII                | Acceder a la búsqueda de usuarios y ver perfiles de usuario con PII censurada |
| Ver datos de uso                                 | Ver datos de uso |
| Fusionar usuarios duplicados                           | Combinar usuarios duplicados en un solo usuario. Los duplicados se eliminan después de la fusión. |
| Vista previa de usuarios duplicados                         | Previsualizar qué perfiles de usuario son duplicados |
| Ver plantillas de Canvas                           | Ver plantillas de Canvas |
| Archivar plantillas de Canvas                        | Mover plantillas de Canvas al archivo |
| Lanzar bloques de contenido                           | Lanzar bloques de contenido |
| Lanzar centros de preferencias                       | Lanzar centros de preferencias |
| Editar integraciones de Currents                      | Crear, actualizar y eliminar integraciones de Currents |
| Ver integración de Currents                       | Ver integraciones de Currents |
| Ver campañas                                  | Ver campañas |
| Editar campañas                                  | Crear y actualizar campañas |
| Archivar campañas                               | Mover campañas al archivo |
| Lanzar campañas                                | Iniciar, detener, pausar o reanudar campañas existentes |
| Ver reglas de limitación de frecuencia                    | Ver reglas de limitación de frecuencia |
| Editar reglas de limitación de frecuencia                    | Crear y actualizar reglas de limitación de frecuencia |
| Ver Canvas                                   | Ver Canvas |
| Editar Canvas                                   | Crear y actualizar Canvas |
| Archivar Canvas                                | Mover Canvas al archivo |
| Lanzar Canvas                                 | Iniciar, detener, pausar o reanudar Canvas existentes |
| Ver bloques de contenido                             | Ver bloques de contenido |
| Editar bloques de contenido                             | Crear y actualizar bloques de contenido |
| Archivar bloques de contenido                          | Mover bloques de contenido al archivo |
| Ver conmutadores de características                              | Ver conmutadores de características |
| Editar conmutadores de características                              | Crear y actualizar conmutadores de características |
| Archivar conmutadores de características                           | Mover conmutadores de características al archivo |
| Ver plantillas de mensajes de WhatsApp                 | Permite a los usuarios ver [plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Editar plantillas de mensajes de WhatsApp | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el generador de plantillas. Esta característica está actualmente en acceso anticipado. |
| Ver segmentos                                   | Ver segmentos. Los usuarios deben tener el permiso «Ver segmentos» para tener el permiso «Editar segmentos» o «Archivar segmentos». |
| Archivar segmentos                                | Archivar y desarchivar segmentos. Los usuarios con el permiso «Archivar segmentos» también deben tener el permiso «Ver segmentos». |
| Editar segmentos                                   | Crear y actualizar segmentos. Los usuarios con el permiso «Editar segmentos» también deben tener el permiso «Ver segmentos». |
| Ver grupo de control global                       | Ver la página de configuración del grupo de control global |
| Editar grupo de control global                       | Crear y guardar cambios en el grupo de control global. Los usuarios con el permiso «Editar grupo de control global» también deben tener permisos para «Editar campañas» y «Editar Canvas». Los usuarios con el permiso «Editar grupo de control global» también obtienen el permiso «Ver grupo de control global». |
| Ver plantillas de banners                           | Ver plantillas de banners |
| Editar plantillas de banners                           | Crear y actualizar plantillas de banners |
| Archivar plantillas de banners                   	  | Mover plantillas de banners al archivo |
| Ver plantillas de correo electrónico                            | Ver plantillas de correo electrónico |
| Editar plantillas de correo electrónico                            | Crear y actualizar plantillas de correo electrónico |
| Archivar plantillas de correo electrónico                         | Mover plantillas de correo electrónico al archivo |
| Ver plantillas de enlaces de correo electrónico   	                  | Ver plantillas de enlaces sin realizar cambios |
| Editar plantillas de enlaces de correo electrónico	                      | Crear y actualizar plantillas de enlaces |
| Publicar páginas de inicio                           | Activar un borrador de página de inicio |
| Editar borradores de páginas de inicio                        | Crear y guardar borradores de páginas de inicio |
| Ver páginas de inicio			                  | Ver páginas de inicio |
| Editar plantillas de páginas de inicio	                  | Crear y actualizar plantillas de páginas de inicio |
| Ver plantillas de páginas de inicio	                  | Ver plantillas de páginas de inicio |
| Archivar plantillas de páginas de inicio 	              | Mover plantillas de páginas de inicio al archivo |
| Ver activos de la biblioteca multimedia                       | Ver activos de la biblioteca multimedia |
| Editar activos de la biblioteca multimedia                       | Crear y actualizar activos de la biblioteca multimedia |
| Eliminar activos de la biblioteca multimedia                     | Eliminar permanentemente activos de la biblioteca multimedia |
| Ver ubicaciones                                  | Ver ubicaciones |
| Editar ubicaciones                                  | Crear y editar ubicaciones |
| Archivar ubicaciones                               | Mover ubicaciones al archivo |
| Ver códigos promocionales                            | Ver códigos promocionales |
| Editar códigos promocionales                            | Crear y actualizar códigos promocionales |
| Exportar códigos promocionales                          | Descargar una lista de códigos promocionales desde el dashboard |
| Ver centros de preferencias                         | Ver centros de preferencias  |
| Editar centros de preferencias                         | Crear y actualizar centros de preferencias |
| Lanzar centros de preferencias	                      | Activar un borrador de centro de preferencias o actualizar uno existente |
| Ver claves de API                                   | Ver claves de API |
| Editar claves de API                                   | Crear y actualizar claves de API |
| Ver grupos internos                            | Ver grupos internos |
| Editar grupos internos                            | Crear y actualizar grupos internos |
| Eliminar grupos internos                          | Eliminar grupos internos |
| Ver registro de actividad de mensajes                       | Ver registros de actividad de mensajes |
| Ver registro de usuarios del evento                             | Ver registros de usuarios del evento |
| Ver identificadores de API                            | Ver identificadores de API y otros identificadores |
| Ver panel de uso de API                        | Ver el panel de uso de API |
| Ver límites de API                                 | Ver límites de velocidad de API |
| Ver alertas de uso de API                           | Ver alertas de uso de API |
| Editar alertas de uso de API                           | Crear y actualizar alertas de uso de API |
| Editar depurador de SDK                               | Crear y descargar sesiones del depurador de SDK |
| Ver depurador de SDK                               | Ver el depurador de SDK o sesiones de depuración |
| Ver configuración de la aplicación                               | Ver la página de configuración de la aplicación |
| Editar configuración de la aplicación                               | Crear, editar y actualizar aplicaciones dentro de la configuración de la aplicación |
| Ver catálogos                                   | Ver catálogos y selecciones |
| Editar catálogos                                   | Crear y actualizar catálogos y selecciones |
| Exportar catálogos                                 | Descargar catálogos desde el dashboard |
| Eliminar catálogos                                 | Eliminar catálogos de forma permanente |
| Editar usuarios del dashboard                            | Ver, crear y editar usuarios de la empresa |
| Ver configuración de correo electrónico                             | Ver preferencias de correo electrónico |
| Editar configuración de correo electrónico                             | Habilitar y actualizar preferencias de correo electrónico | 
| Editar cifrado a nivel de campo del identificador            | Habilitar y actualizar la configuración de cifrado a nivel de campo |
| Ver atributos personalizados                          | Ver atributos personalizados e informe de uso |
| Editar atributos personalizados                          | Crear y actualizar atributos personalizados |
| Bloquear atributos personalizados                     | Añadir atributos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Eliminar atributos personalizados                        | Eliminar permanentemente atributos personalizados |
| Exportar atributos personalizados                        | Descargar atributos personalizados desde el dashboard |
| Ver eventos personalizados                              | Ver eventos personalizados e informe de uso, y añadir eventos personalizados al correo electrónico del informe de análisis diario |
| Editar eventos personalizados                              | Crear y actualizar eventos personalizados |
| Bloquear eventos personalizados                         | Añadir eventos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Eliminar eventos personalizados                            | Eliminar permanentemente eventos personalizados |
| Exportar eventos personalizados                            | Descargar eventos personalizados desde el dashboard |
| Editar segmentación de propiedades de eventos personalizados         | Habilitar y deshabilitar la segmentación para propiedades de eventos personalizados |
| Ver productos                                   | Ver productos |
| Editar productos                                   | Crear y actualizar productos |
| Bloquear productos                              | Añadir productos a una lista de bloqueo que restringe su uso en el dashboard |
| Editar segmentación de propiedades de compra             | Habilitar y deshabilitar la segmentación para propiedades de eventos de compra |
| Editar socios tecnológicos                        | Crear y actualizar socios tecnológicos |
| Editar ingesta de datos en la nube                       | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Ver configuración de localización                      | Ver la página de configuración de idiomas múltiples |
| Editar configuración de localización                      | Crear configuraciones regionales de idiomas múltiples |
| Eliminar configuración de localización                    | Eliminar configuraciones regionales de idiomas múltiples |
| Editar suscripciones                              | Crear y actualizar grupos de suscripción |
| Ver etiquetas                                       | Ver etiquetas |
| Editar etiquetas                                       | Crear y actualizar etiquetas |
| Eliminar etiquetas                                     | Eliminar etiquetas de forma permanente |
| Ver equipos                                      | Ver equipos |
| Editar equipos                                      | Crear y actualizar equipos |
| Archivar equipos                                   | Mover equipos al archivo |
| Ver transformación de datos                        | Ver transformaciones de datos |
| Editar transformación de datos                        | Crear y actualizar transformaciones de datos |
| Editar plantillas de Canvas                           | Crear y actualizar plantillas de Canvas |
| Aprobar campañas                               | Aprobar o rechazar campañas. El [flujo de trabajo de aprobación de campañas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Aprobar Canvas                                | Aprobar o rechazar Canvas. El [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Ver ubicaciones de banners                                 | Ver ubicaciones de banners |
| Editar ubicaciones de banners                                 | Ver ubicaciones de banners sin realizar cambios |
| Archivar ubicaciones de banners                              | Mover ubicaciones de banners al archivo |
| Ver configuración de push                              | Ver configuración de push |
| Editar configuración de push                              | Crear y actualizar configuración de push |
| Editar informes del dashboard                          | Crear y actualizar informes |
| Ver importación de usuarios                               | Ver importaciones de usuarios en CSV sin realizar cambios |
| Importar usuarios                                    | Cargar usuarios al dashboard |
| Exportar datos de usuario                                | Descargar usuarios desde el dashboard |
| Editar datos de usuario                                  | Crear y actualizar datos de usuario |
| Ver fusión de usuarios                                | Ver una lista de registros de fusión de usuarios |
| Ver registros de eliminación de usuarios	            	  | Ver registros de eliminación de usuarios |
| Eliminar usuarios del dashboard	                  | Eliminar permanentemente usuarios del dashboard de forma individual o masiva. |      
| Ver agentes de IA personalizados                           | Permite a los usuarios ver agentes de IA personalizados. |
| Editar agentes de IA personalizados                           | Permite a los usuarios crear y actualizar agentes de IA personalizados. |
| Archivar agentes de IA personalizados                        | Permite a los usuarios archivar agentes de IA personalizados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }