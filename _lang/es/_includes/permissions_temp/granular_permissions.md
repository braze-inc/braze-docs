{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Creación de un conjunto de permisos

Utilice conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del panel que necesiten el mismo acceso en diferentes espacios de trabajo. Para crear un conjunto de permisos, vaya a **Configuración** > **Configuración de permisos** y, a continuación, seleccione **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nombre|Permisos
\|-----------|----------------|
|Desarrolladores|«Ver claves de API», «Editar claves de API», «Ver grupos internos», «Editar grupos internos», «Ver registro de actividad de mensajes», «Ver registro de usuarios del evento», «Ver identificadores de API», «Ver panel de uso de API», «Ver límites de API», «Ver alertas de uso de API», «Editar alertas de uso de API», «Ver depurador de SDK», «Editar depurador de SDK».|
|Especialistas en marketing|«Ver campañas», «Editar campañas», «Archivar campañas», «Ver lienzos», «Editar lienzos», «Archivar lienzos», «Ver reglas de limitación de frecuencia», «Editar reglas de limitación de frecuencia», «Ver priorización de mensajes», «Editar priorización de mensajes», «Ver bloques de contenido», «Ver indicadores de características», «Editar indicadores de características», «Archivar indicadores de características», «Ver segmentos», «Editar segmentos», «Editar grupo de control global», «Ver plantillas de IAM», «Editar plantillas de IAM», «Archivar plantillas de IAM», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Archivar plantillas de correo electrónico», «Ver plantillas de webhook», «Editar plantillas de webhook», «Archivar plantillas de webhook», «Ver plantillas de enlaces», «Editar plantillas de enlaces», «Ver activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias», «Editar informes», «Ver plantillas de banners», «Ver configuración multilingüe», «Usar operador», «Ver agentes de Decisioning Studio», «Ver evento de conversión de Decisioning Studio».|
|Gestión de usuarios|«Ver usuarios del panel de control», «Editar usuarios del panel de control», «Ver equipos», «Editar equipos», «Archivar equipos».|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Crear un rol

Las funciones permiten una mayor estructuración al agrupar los permisos personalizados individuales con los controles de acceso al espacio de trabajo. Esto es especialmente útil si tiene muchas marcas o espacios de trabajo regionales en un mismo cuadro de mandos. Con las funciones, puede añadir usuarios del cuadro de mandos a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol | Espacio de trabajo | Permisos  
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda |{::nomarkdown} [DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda{:/}  | «Ver campañas», «Editar campañas», «Archivar campañas», «Ver lienzos», «Editar lienzos», «Archivar lienzos», «Ver bloques de contenido», «Editar bloques de contenido», «Archivar bloques de contenido», «Lanzar bloques de contenido», «Ver indicadores de características», «Editar indicadores de características», «Archivar indicadores de características», «Ver segmentos», «Editar segmentos», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias». |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de{:/} la piel  |«Ver campañas», «Editar campañas», «Archivar campañas», «Ver lienzos», «Editar lienzos», «Archivar lienzos», «Ver bloques de contenido», «Editar bloques de contenido», «Archivar bloques de contenido», «Lanzar bloques de contenido», «Ver indicadores de características», «Editar indicadores de características», «Archivar indicadores de características», «Ver segmentos», «Editar segmentos», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias».|
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda, [DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de{:/} la piel  | «Ver usuarios del panel», «Editar usuarios del panel», «Ver equipos», «Editar equipos», «Archivar equipos»|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y las funciones de equipos?

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para agregar permisos de usuario a Teams

Es posible que encuentres dificultades al intentar guardar los permisos en el panel de Braze, especialmente al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tienes en el espacio de trabajo. Esta restricción existe porque no tiene sentido tener un equipo si todos los usuarios tienen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel del espacio de trabajo. En su lugar, asigna permisos exclusivamente a nivel de equipo.

## Usuarios limitados

Los usuarios limitados tienen permisos específicos que les permiten ser administradores de determinados aspectos del panel de Braze, pero con restricciones en comparación con los administradores de la empresa y los administradores del espacio de trabajo.

| Ámbito de aplicación | Descripción |
| --- | --- |
| Permisos | Los usuarios con permisos limitados pueden editar los permisos de otros usuarios con permisos limitados si tienen los permisos «Ver usuarios del panel» y «Editar usuarios del panel». También pueden crear nuevos usuarios limitados y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni gestionar cuentas de administrador de la empresa. |
| Limitaciones de funciones | Si un usuario con permisos limitados tiene todos los permisos excepto «Administrador del espacio de trabajo», seguirá teniendo acceso a todos los demás permisos que normalmente se conceden a un administrador del espacio de trabajo. |
| Visibilidad de los permisos | Si un usuario con permisos limitados tiene permisos para «Ver usuarios del panel» y «Editar usuarios del panel» para un espacio de trabajo (como Dev), pero no para otro (como Prod), no verán los permisos del espacio de trabajo Prod en la página de detalles de los usuarios del panel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparación de usuarios limitados

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador del espacio de trabajo | Los administradores del espacio de trabajo tienen permisos específicos para gestionar los espacios de trabajo, pero no tienen la misma autoridad que los administradores de la empresa. Los usuarios con permisos limitados pueden heredar permisos similares a los de los administradores del espacio de trabajo si tienen marcados los permisos necesarios. |
| Administrador (administrador de la empresa) | Los administradores de la empresa tienen permisos más amplios, incluida la posibilidad de eliminar usuarios del panel. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de la empresa para realizar esa acción. |
| Acceso solo para lectura | Para acceder a algunas partes del panel, como la página Campañas, los usuarios deben tener asignados permisos de visualización.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Error de acceso limitado

Los usuarios pueden encontrar mensajes como «Necesitas permisos para «Ver páginas de destino» para acceder a esta página». En tales casos, el usuario y el administrador de la cuenta deben verificar que se hayan concedido los permisos necesarios. Si es así, intenta resolver el problema desactivando y volviendo a habilitar los permisos del usuario. 

{% alert note %}
No es posible fusionar o importar permisos de usuario de un usuario del panel de control a otro.
{% endalert %}

## Editar los permisos de un usuario

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Usuarios de la empresa** y selecciona su nombre.

![La página «Usuarios de la empresa» en Braze muestra una tabla con los usuarios del panel de Braze.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador

Los administradores tienen acceso a todas las funciones y la posibilidad de modificar cualquier configuración de la empresa. Pueden:

- Cambiar [la configuración de aprobación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Añadir, editar, eliminar, suspender o anular la suspensión de otros [usuarios de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuarios Braze como CSV

Para conceder o eliminar privilegios de administrador, seleccione **Este usuario es un administrador** y, a continuación, seleccione **Actualizar usuario**.

![Los detalles del usuario seleccionado con la casilla de verificación de administrador activada.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, este no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o de espacio de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marque o desmarque la casilla situada junto a ese permiso. Cuando haya terminado, seleccione **Actualizar usuario**.

|Nombre del permiso|Descripción|
|----------|-----------|
|Administrar configuración de empresa|Permite a los usuarios modificar la configuración de permisos y la verificación del remitente. .|
|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espacio de trabajo

Puede dar a un usuario permisos diferentes para cada espacio de trabajo al que pertenezca en Braze. Para gestionar los permisos a nivel del espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y, a continuación, elige los permisos manualmente o asigna un [conjunto de permisos o una función]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que hayas creado previamente. Si necesitas dar a un usuario permisos diferentes para distintos espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

En **Espacios de trabajo**, seleccione uno o varios espacios de trabajo en el menú desplegable. A continuación, en **Permisos**, selecciona uno o varios permisos. Se les asignarán estos permisos sólo para los espacios de trabajo que hayas seleccionado. Si lo deseas, puedes seleccionar **Asignar acceso de administrador al espacio de trabajo** si prefieres concederles permisos completos para este espacio de trabajo.

Cuando haya terminado, seleccione **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo seleccionados manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

En **Espacios de trabajo**, seleccione uno o varios espacios de trabajo en el menú desplegable. A continuación, en **Conjuntos de permisos**, seleccione un conjunto de permisos. Se les asignarán estos permisos sólo para los espacios de trabajo que hayas seleccionado.

Cuando haya terminado, seleccione **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

En **Espacios de trabajo**, seleccione uno o varios espacios de trabajo en el menú desplegable. A continuación, en **Función**, elige una función. Se les asignarán estos permisos sólo para los espacios de trabajo que hayas seleccionado.

Cuando haya terminado, seleccione **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de una función en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportación de permisos de usuario

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Usuarios de la empresa** y selecciona **Exportar usuarios**. En breve le enviaremos un archivo CSV a su dirección de correo electrónico.

![La página «Usuarios de la empresa» en Braze con la opción «Exportar usuarios» resaltada.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permisos

| Permiso | Definición |
|-------------------------------------------------|---------------------|
| Ver datos de facturación                            | Ver detalles de facturación |
| Ver atributos personalizados marcados como Información personal identificable (PII)            | Ver atributos personalizados marcados como PII |
| Ver PII                                        | Ver PII |
| Ver perfiles de usuarios que cumplen las reglas de PII                | Accede a la búsqueda de usuarios y visualiza los perfiles de usuario con la PII censurada. |
| Ver datos de consumo                                 | Ver datos de uso |
| Fusionar usuarios duplicados                           | Combinar usuarios duplicados en un solo usuario. Los duplicados se eliminan después de la fusión. |
| Vista previa de usuarios duplicados                         | Realiza una vista previa de qué perfiles de usuario son duplicados. |
| Ver plantillas de Canvas                           | Ver plantillas Canvas |
| Archivar plantillas de Canvas                        | Mover plantillas de Canvas al archivo |
| Lanzar bloques de contenido                           | Lanzar bloques de contenido |
| Lanzar centros de preferencias                       | Iniciar centros de preferencias |
| Exportar datos de usuario                                | Descargar usuarios desde el panel |
| Editar integraciones de Currents                      | Crear, actualizar y eliminar integraciones de Currents |
| Ver la integración de las corrientes                       | Ver integraciones de Currents |
| Ver campañas                                  | Ver campañas |
| Editar campañas                                  | Crear y actualizar campañas |
| Archivar campañas                               | Mover campañas al archivo |
| Enviar campañas                                  | Iniciar, detener, pausar o reanudar campañas | 
| Enviar lienzos                         		  | Iniciar, detener, pausar o reanudar lienzos |
| Ver las reglas de limitación de frecuencia                    | Ver las reglas de limitación de frecuencia |
| Editar reglas de limitación de frecuencia                    | Crear y actualizar reglas de limitación de frecuencia |
| Ver Canvas                                   | Ver Canvas |
| Editar Canvas                                   | Crear y actualizar lienzos |
| Archivar Canvas                                | Mover lienzos al archivo |
| Ver bloques de contenido                             | Ver bloques de contenido |
| Editar bloque de contenido                             | Crear y actualizar bloques de contenido |
| Archivar bloques de contenido                          | Mover bloques de contenido al archivo |
| Ver las feature flags                              | Ver indicadores de características |
| Editar conmutador de características                              | Crear y actualizar indicadores de características |
| Archiva feature flags                           | Mover características al archivo |
|  Ver plantillas de mensajes de WhatsApp                | Permite a los usuarios ver [las plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Editar plantillas de mensajes de WhatsApp | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el generador de plantillas. Esta característica está actualmente en acceso anticipado. |
| Ver segmentos                                   | Ver segmentos . Los usuarios deben tener el permiso «Ver segmentos» para tener el permiso «Editar segmentos» o «Archivar segmentos». |
| Archivar segmentos                                | Archivar y desarchivar segmentos. A los usuarios con el permiso «Archivar segmentos» también se les debe conceder el permiso «Ver segmentos». |
| Editar segmentos                                   | Crear y actualizar segmentos. A los usuarios con permiso para «Editar segmentos» también se les debe conceder el permiso para «Ver segmentos». |
| Ver grupo de control global                       | Ver la página de configuración del grupo de control global |
| Editar grupo de control global                       | Crea y guarda los cambios en el grupo de control global. Los usuarios con el permiso «Editar grupo de control global» también deben tener permisos para «Editar campañas» y «Editar lienzos». A los usuarios con el permiso «Editar grupo de control global» también se les concede el permiso «Ver grupo de control global». |
| Ver plantillas de banners                           | Ver plantillas de banners |
| Editar plantillas de banners                           | Crear y actualizar plantillas de banners |
| Plantillas de banners de archivo                   	  | Mover plantillas de banners al archivo |
| Ver plantillas de correo electrónico                            | Ver plantillas de correo electrónico |
| Editar plantilla de correo electrónico                            | Crear y actualizar plantillas de correo electrónico |
| Archivar plantillas de correo electrónico                         | Mover plantillas de correo electrónico al archivo |
| Ver plantillas de enlaces   	                      | Ver plantillas de enlaces |
| Editar plantillas de enlaces	                          | Crear y actualizar plantillas de enlaces |
| Publicar páginas de inicio                           | Activar un borrador de página de destino |
| Editar borradores de páginas de destino                        | Crear y guardar borradores de páginas de destino |
| Ver páginas de inicio			                  | Ver páginas de destino |
| Editar plantillas de páginas de destino	                  |  Crear y actualizar plantillas de páginas de destino. |
| Ver plantillas de páginas de inicio	                  | Ver plantillas de páginas de destino |
| Plantilla de página de destino del archivo 	              | Mover las plantillas de la página de destino al archivo |
| Ver activos de la biblioteca de medios                       | Ver activos de la biblioteca multimedia |
| Editar activos de la biblioteca de medios                       | Crear y actualizar los activos de la biblioteca multimedia. |
| Eliminar activos de la biblioteca de medios                     | Eliminar definitivamente los activos de la biblioteca multimedia |
| Ver ubicaciones                                  | Ver ubicaciones |
| Editar ubicaciones                                  | Crear y editar ubicaciones |
| Ubicación de los archivos                               | Mover ubicaciones al archivo |
| Ver códigos promocionales                            | Ver códigos promocionales |
| Editar códigos promocionales                            | Crear y actualizar códigos promocionales |
| Códigos promocionales de las exportaciones                          | Descarga una lista de códigos promocionales desde el panel. |
| Ver centros de preferencia                         | Ver centros de preferencias  |
| Editar centros de preferencia                         | Crear y actualizar centros de preferencias |
| Lanzar centros de preferencias	                      | Activa un borrador del Centro de preferencias o actualiza uno ya existente. |
| Ver las claves de API                                   | Ver claves de API |
| Editar claves de API                                   | Crear y actualizar claves de API |
| Ver grupos internos                            | Ver grupos internos |
| Editar grupos internos                            | Crear y actualizar grupos internos |
| Ver registro de actividad de mensajes                       | Ver registros de actividad de mensajes |
| Ver registro de usuarios del evento                             | Ver registros de usuarios del evento |
| Ver identificadores API                            | Ver identificadores API y otros identificadores |
| Ver panel de uso de la API                        | Ver el panel de control de uso de la API |
| Ver límites de la API                                 | Ver límites de velocidad de la API |
| Ver alertas de uso de la API                           | Ver alertas de uso de la API |
| Editar alertas de uso de la API                           | Crear y actualizar alertas de uso de API |
| Editar depurador de SDK                               | Crear y descargar sesiones del depurador SDK |
| Ver depurador de SDK                               | Ver el depurador SDK  o las sesiones de depuración |
| Ver configuración de la aplicación                               | Ver la página de configuración de la aplicación |
| Editar configuración de la aplicación                               | Crear, editar y actualizar aplicaciones dentro de la configuración de las aplicaciones. |
| Ver catálogos                                   | Ver catálogos y selecciones |
| Editar catálogos                                   | Crear y actualizar catálogos y selecciones. |
| Exportar catálogos                                 | Descargar catálogos desde el panel |
| Eliminar catálogos                                 | Eliminar catálogos de forma permanente |
| Ver usuarios del panel de control                            | Ver usuarios de la empresa |
| Editar usuarios del panel                            | Crear y actualizar usuarios de la empresa 
| Ver configuración del correo electrónico                             | Ver preferencias de correo electrónico |
| Editar configuración de correo electrónico                             | Habilitar y actualizar las preferencias de correo electrónico | 
| Editar identificador Cifrado a nivel de campo            | Habilita y actualiza la configuración del cifrado a nivel de campo. |
| Ver atributos personalizados                          | Ver atributos personalizados e informe de uso |
| Editar atributos personalizados                          | Crear y actualizar atributos personalizados |
| Atributos personalizados de la lista de bloqueo                     | Añade atributos personalizados a una lista de bloqueados que restringe el uso en el panel. |
| Eliminar atributos personalizados                        | Eliminar permanentemente los atributos personalizados |
| Exportar atributos personalizados                        | Descargar atributos personalizados desde el panel de control |
| Ver eventos personalizados                              | Ver eventos personalizados e informes de uso, y añadir eventos personalizados al informe de análisis diario que se envía por correo electrónico. |
| Editar eventos personalizados                              | Crear y actualizar eventos personalizados |
| Eventos personalizados de la lista de bloqueo                         | Añade eventos personalizados a una lista de bloqueados que restringe el uso en el panel. |
| Eliminar eventos personalizados                            | Eliminar eventos personalizados de forma permanente |
| Exportar eventos personalizados                            | Descargar eventos personalizados desde el panel |
| Editar segmentación de propiedades de eventos personalizados         | Habilitar y deshabilitar la segmentación para propiedades del evento personalizado |
| Ver productos                                   | Ver productos |
| Editar productos                                   | Crear y actualizar productos |
| Productos de la lista de bloqueo                              | Añade productos a una lista de bloqueo que restringe su uso en el panel. |
| Editar segmentación de propiedades de compra             | Habilitar y deshabilitar la segmentación para las propiedades del evento de compra |
| Editar socios tecnológicos                        | Crear y actualizar socios tecnológicos |
| Editar la ingesta de datos en la nube                       | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Ver configuración multilingüe                    | Ver configuración multilingüe |
| Crear configuración regional multilingüe de localización           | Crear y actualizar la configuración regional multilingüe de localización |
| Eliminar configuración regional multilingüe           | Eliminar permanentemente la configuración regional multilingüe de la localización |
| Editar suscripciones                              | Crear y actualizar grupos de suscripción |
| Ver etiquetas                                       | Ver etiquetas |
| Editar etiquetas                                       | Crear y actualizar etiquetas |
| Borrar etiquetas                                     | Eliminar etiquetas de forma permanente |
| Ver equipos                                      | Ver equipos |
| Modificar equipos                                      | Crear y actualizar equipos |
| Archivar equipos                                   | Mover equipos al archivo |
| Ver transformación de datos                        | Ver transformaciones de datos |
| Editar transformación de datos                        | Crear y actualizar transformaciones de datos |
| Lanzar campañas                                | Iniciar, detener, pausar o reanudar campañas existentes. |
| Lanzar Canvas                                 | Iniciar, detener, pausar o reanudar lienzos existentes. |
| Editar plantillas de Canvas                           | Crear y actualizar plantillas de Canvas |
| Aprobar campañas                               | Aprobar o rechazar campañas. El [flujo de trabajo de aprobación de campañas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Si estás interesado en participar en el acceso anticipado, ponte en contacto con tu director de cuentas. |
| Aprobar Canvas                                | Aprobar o rechazar lienzos. El [flujo de trabajo de aprobación de Lienzos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Si estás interesado en participar en el acceso anticipado, ponte en contacto con tu director de cuentas. |
| Ver Colocaciones                                 | Ver ubicación del banner |
| Editar ubicaciones                                 | Ver la ubicación de los banners sin realizar cambios |
| Archivar colocaciones                              | Mover las ubicaciones de los banners al archivo |
| Ver configuración push                              | Ver configuración de push |
| Editar configuración push                              | Crear y actualizar la configuración de push |
| Editar informes                                    | Crear y actualizar informes |
| Ver Importar usuarios                               | Ver importaciones de usuarios en CSV |
| Importar usuarios                                    | Subir usuarios al panel |
| Editar datos de usuario                                  | Crear y actualizar datos de usuario |
| Ver fusionar usuarios                                | Ver una lista de registros de fusión de usuarios |
| Ver los registros de eliminación de usuarios	            	  | Ver los registros de eliminación de usuarios |
| Borrar usuarios del panel	                  | Eliminar usuarios de forma permanente del panel, ya sea de forma individual o masiva. |      
| Ver agentes de IA personalizados                           | Permite a los usuarios ver agentes de IA personalizados. |
| Editar agentes de IA personalizados                           | Permite a los usuarios crear y actualizar agentes de IA personalizados. |
| Archivo Agentes de IA personalizados                        | Permite a los usuarios archivar agentes de IA personalizados. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }