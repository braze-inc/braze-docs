---
nav_title: Permisos
article_title: Permisos Braze
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo funcionan los permisos de usuario en Braze. Aquí puedes aprender a editar y establecer permisos de usuario, eligiendo quién puede acceder a tus aplicaciones en el panel de control."
tool: Dashboard

---

# Permisos Braze

> Aprenda a crear conjuntos de permisos, crear funciones, editar permisos de usuario y exportar permisos de usuario, para que pueda asegurarse de que sus usuarios sólo acceden a los espacios de trabajo y las funciones que más necesitan.

## Creación de un conjunto de permisos

Utilice conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Pueden aplicarse a usuarios de cuadros de mando que necesiten el mismo acceso en distintos espacios de trabajo. Para crear un conjunto de permisos, vaya a **Configuración** > **Configuración de permisos** y, a continuación, seleccione **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nombre|Permisos
\|-----------|----------------|
|Desarrolladores: Acceso a la consola de desarrollo.
|Especialistas en marketing|"Campañas de acceso, lonas, tarjetas, feature flags, segmentos, biblioteca multimedia y centros de preferencias" <br> "Gestionar activos de la mediateca"|
|Gestión de usuarios|"Gestionar usuarios del panel" <br> "Gestionar equipos"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Crear un rol

Las funciones permiten una mayor estructuración al agrupar los permisos personalizados individuales con los controles de acceso al espacio de trabajo. Esto es especialmente útil si tiene muchas marcas o espacios de trabajo regionales en un mismo cuadro de mandos. Con las funciones, puede añadir usuarios del cuadro de mandos a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol | Espacio de trabajo | Permisos  
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda {:/} | "Campañas de acceso, lienzos, tarjetas, banderas de características, segmentos, mediateca y centro de preferencias"<br>"Gestionar activos de la mediateca" |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de la piel {:/} | "Campañas de acceso, lienzos, tarjetas, banderas de características, segmentos, biblioteca de medios y centros de preferencias" <br>"Gestionar activos de la mediateca" |
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda, [DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de la piel {:/} | "Gestionar usuarios del panel"<br>"Gestionar equipos" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y funciones de los Equipos?

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para añadir permisos de usuario a Equipos

Puedes encontrar dificultades al intentar guardar permisos en el panel de Braze, sobre todo al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un Equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tiene a nivel de espacio de trabajo. Esta restricción existe porque no hay ninguna ventaja en tener un Equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir con éxito un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel de espacio de trabajo. En su lugar, asigna permisos exclusivamente a nivel de equipo.

## Usuarios limitados

Los usuarios limitados tienen permisos específicos que les permiten gestionar determinados aspectos del panel Braze, aunque tienen restricciones en comparación con los administradores de empresa y los administradores de espacios de trabajo.

| Permisos | Los usuarios limitados pueden editar los permisos de otros usuarios limitados si tienen marcado el permiso "Gestionar usuarios del panel". También pueden crear nuevos usuarios limitados y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni administrar cuentas de administrador de empresa. |
| Limitaciones de rol | Si un usuario limitado tiene todos los permisos excepto el de "Administrador de grupo de aplicaciones", seguirá teniendo acceso a todos los demás permisos que suelen concederse a un administrador de espacio de trabajo. |
| Visibilidad de los permisos | Si un usuario limitado tiene marcada la opción "Gestionar usuarios del panel" para un grupo de aplicaciones (como Dev) pero no para otro (como Prod), no verá los permisos del grupo de aplicaciones Prod en su perfil "Gestionar usuarios". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparación de usuarios limitados

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador del grupo de aplicaciones | Los administradores de grupos de aplicaciones tienen permisos específicos para gestionar grupos de aplicaciones, pero no tienen la misma autoridad que los administradores de empresa. Los usuarios limitados pueden heredar permisos similares a los de los administradores de grupos de aplicaciones si tienen marcados los permisos necesarios. |
| Administrador de la empresa | Los administradores de empresa tienen permisos más amplios, incluida la capacidad de eliminar usuarios del panel. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de la empresa para realizar esa acción. |
| Permiso básico de sólo lectura | Para acceder a determinadas partes del panel, como la página de socios tecnológicos, los usuarios deben tener un permiso básico de sólo lectura. Esto incluye tener habilitada la opción "Gestionar integraciones externas", junto con permisos para Acceder a campañas, lienzos, tarjetas, segmentos y biblioteca multimedia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Error de acceso limitado

Los usuarios pueden encontrarse con mensajes como "Acceso limitado. No tienes permisos para acceder a esta Página". En estos casos, el administrador de la cuenta debe comprobar si puede resolver el problema deshabilitando y volviendo a habilitar los permisos del usuario.

{% alert note %}
No es posible fusionar o importar permisos de usuario de un usuario del panel a otro.
{% endalert %}

## Editar los permisos de un usuario

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Usuarios de empresa** y, a continuación, selecciona su nombre.

![La página "Usuarios de la empresa" en Braze con un usuario listado en los resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Administrador

Los administradores tienen acceso a todas las funciones y la posibilidad de modificar cualquier configuración de la empresa. Pueden hacerlo:

- Cambiar [la configuración de aprobación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Añadir, editar, eliminar, suspender o anular la suspensión de otros [usuarios de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- Exportar usuarios Braze como CSV

Para conceder o eliminar privilegios de administrador, seleccione **Este usuario es un administrador** y, a continuación, seleccione **Actualizar usuario**.

![Los detalles del usuario seleccionado con la casilla de verificación admin en foco.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Si elimina los privilegios de administrador de un usuario, éste no podrá acceder a Braze hasta que le asigne al menos un permiso [a nivel de empresa](#company) o [de espacio de trabajo](#workspace).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marque o desmarque la casilla situada junto a ese permiso. Cuando haya terminado, seleccione **Actualizar usuario**.

|Nombre del permiso|Descripción|
|----------|-----------|
|Administrar configuración de empresa|Permite a los usuarios modificar cualquier configuración de la empresa.|
|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espacio de trabajo

Puede dar a un usuario permisos diferentes para cada espacio de trabajo al que pertenezca en Braze. Para gestionar sus permisos a nivel de espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y, a continuación, elige sus permisos manualmente para seleccionar o asignar un conjunto de permisos [que hayas creado previamente](#creating-a-permission-set).

Si necesitas dar a un usuario permisos diferentes para distintos espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

En **Espacios de trabajo**, seleccione uno o varios espacios de trabajo en el menú desplegable. A continuación, en **Permisos**, elige uno o varios permisos del desplegable. Braze asigna estos permisos sólo para los espacios de trabajo que hayas seleccionado. Opcionalmente, puede seleccionar **Activar acceso de administrador** si desea darles permisos completos para este espacio de trabajo.

Cuando haya terminado, seleccione **Actualizar usuario**.

![Los permisos a nivel de espacio de trabajo se seleccionan manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

En **Espacios de trabajo**, seleccione uno o varios espacios de trabajo en el menú desplegable. A continuación, en **Conjuntos de permisos**, seleccione un conjunto de permisos. Braze asigna estos permisos sólo para los espacios de trabajo que hayas seleccionado.

Cuando haya terminado, seleccione **Actualizar usuario**.

![Los permisos a nivel de espacio de trabajo se asignan mediante un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportación de permisos de usuario

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Usuarios de la empresa** y, a continuación, selecciona **Exportar usuarios**. En breve le enviaremos un archivo CSV a su dirección de correo electrónico.

![La página "Usuarios de la empresa" en Braze con la opción "Exportar usuarios" en primer plano.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permisos

{% alert important %}
A partir de abril de 2024, para crear o actualizar listas de códigos promocionales, los usuarios de Braze necesitan el permiso "Acceder a campañas, lienzos, tarjetas, segmentos, biblioteca multimedia".
{% endalert %}

|Nivel|Apellidos|Definición|
|---|---|---|
|Administrador|Administrador|Permite a los usuarios acceder a todas las funciones disponibles. Esta es la configuración por defecto para todos los nuevos usuarios. Puede actualizar la configuración de la empresa (nombre de la empresa y zona horaria), cosa que no pueden hacer los usuarios limitados.|
|Empresa|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
|Empresa|Administrar configuración de empresa|Permite a los usuarios modificar cualquier configuración de la empresa.|
|Espacio de trabajo|Acceda a Campañas, Lienzos, Tarjetas, Bloques de contenido, Banderas de características, Segmentos, Mediateca, Ubicaciones, Códigos de promoción y Centros de preferencias.|Permite a los usuarios ver las métricas de rendimiento de campañas y Canvas, crear y duplicar borradores de campañas y Lienzos, editar borradores y plantillas de campañas y Canvas, ver borradores de segmentos, plantillas y medios, crear plantillas, cargar medios, crear o actualizar listas de códigos promocionales, ver informes de interacción y ver la configuración de mensajes globales en el panel. Sin embargo, los usuarios con este permiso no pueden pausar ni editar los contenidos en directo existentes.|
|Espacio de trabajo|Acceso a la consola para desarrolladores|Permite el acceso completo a los siguientes ajustes y registros:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Claves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de actividad de mensajes</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de eventos de usuario</a></li></ul>{:/}|
|Espacio de trabajo|Aprobar y denegar campañas|Permite a los usuarios aprobar o denegar campañas. El [flujo de trabajo de aprobación de campañas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Póngase en contacto con su gestor de cuenta si está interesado en participar en el acceso anticipado.|
|Espacio de trabajo|Aprobar y denegar Canvas|Permite a los usuarios aprobar o denegar lienzos. El [flujo de trabajo de aprobación de Lienzos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso.|
|Espacio de trabajo|Editar integraciones de Currents|Permite a los usuarios modificar una conexión Currents, incluidas las credenciales. Por defecto, a los usuarios que tienen asignado el permiso "Integraciones externas" también se les asigna este permiso.|
|Espacio de trabajo|Editar segmentos|Permite a los usuarios crear y editar segmentos. Puede seguir creando campañas con segmentos y filtros existentes sin este permiso. Necesita este permiso para generar un segmento a partir de los usuarios de un CSV o para volver a segmentar el grupo de usuarios del CSV.|
|Espacio de trabajo|Exportar datos de usuario|Permite a los usuarios exportar sus datos de usuario desde segmentos, campañas y Canvases. Este permiso incluye información sensible del usuario como nombres, direcciones de correo electrónico y otra información personal identificable (PII) recopilada. Para exportar CSV desde el panel, debes tener este permiso y el permiso "Ver PII".|
|Espacio de trabajo|Importar y actualizar datos de usuario|Permite a los usuarios importar archivos CSV y de actualización de usuarios de aplicaciones, así como ver la página de importación de usuarios. Esto también le permite editar el estado de suscripción de un usuario y las reglas de inclusión/exclusión de su grupo de suscripción.|
|Espacio de trabajo|Lanzar y administrar bloques de contenido|Permite a los usuarios lanzar y administrar [bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espacio de trabajo|Lanzar centros de preferencias|Permite a los usuarios lanzar [centros de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espacio de trabajo|Administrar aplicaciones|Permite a los usuarios editar **la configuración de la aplicación**.|
|Espacio de trabajo|Administrar permisos para el dashboard de catálogos|Permite a los usuarios crear y gestionar catálogos.|
|Espacio de trabajo|Administrar usuarios del dashboard| Permite a los no administradores ver, editar y gestionar la página **Usuarios de la empresa**, y gestionar los usuarios del panel en su espacio de trabajo modificando los permisos de cualquier usuario, incluidos los suyos propios. Los usuarios con este permiso no pueden eliminar usuarios (sólo los administradores pueden eliminar usuarios).<br><br>Esto corresponde al permiso heredado `MANAGE_DEVELOPERS_AND_PERMISSIONS`.|
|Espacio de trabajo|Administrar configuración del correo electrónico|Permite a los usuarios guardar los cambios de configuración del correo electrónico**(Configuración** > **Preferencias de correo electrónico**).|
|Espacio de trabajo|Administrar eventos, atributos, compras|Permite a los usuarios editar atributos personalizados (los usuarios sin esta capacidad pueden seguir viendo atributos personalizados), editar y ver propiedades de eventos personalizados, y editar y ver propiedades de productos en **Configuración de datos**.|
|Espacio de trabajo|Administrar integraciones externas|Permite acceder a todas las pestañas de **los socios tecnológicos**, sincronizar Braze con otras plataformas y gestionar [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espacio de trabajo|Administrar conmutadores de características|Permite a los usuarios crear o editar [banderas de características]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espacio de trabajo|Administrar activos de biblioteca de medios|Permite a los usuarios añadir, editar y eliminar activos de la mediateca.|
|Espacio de trabajo|Administrar grupos de suscripción|Permite a los usuarios crear y gestionar grupos de suscripción.|
|Espacio de trabajo|Gestionar etiquetas|Permite a los usuarios editar o eliminar etiquetas (en **Gestión de etiquetas**). No necesita este permiso para añadir etiquetas a campañas o segmentos.|
|Espacio de trabajo|Gestionar equipos|Permite a los usuarios gestionar **Equipos Internos**. La posibilidad de seleccionar este permiso depende de su contrato con Braze.<br><br>Esto corresponde al permiso heredado `MANAGE_TERRITORIES`.|
|Espacio de trabajo|Administrar transformaciones|Permite a los usuarios crear y gestionar Transformaciones de Datos.|
|Espacio de trabajo|Enviar campañas, Canvas|Permite a los usuarios editar, archivar y detener campañas y lienzos, crear campañas y lanzar lienzos. |
|Espacio de trabajo|Ver datos de facturación|Permite a los usuarios ver las suscripciones y la facturación.|
|Espacio de trabajo|Ver la integración de las corrientes|Permite a los usuarios ver toda la información sobre una conexión Currents, excluyendo las credenciales. Por defecto, a los usuarios que tienen asignado el permiso "Acceder a campañas, lienzos, tarjetas, bloques de contenido, indicadores de características, segmentos, biblioteca multimedia, ubicaciones, códigos de promoción y centros de preferencias" también se les asigna este permiso.|
|Espacio de trabajo|Ver atributos personalizados marcados como Información personal identificable (PII)|Permite a los usuarios que no son administradores ver atributos personalizados que contienen información sensible y están marcados como información de identificación personal (PII).|
|Espacio de trabajo|Ver PII|Permite a los usuarios ver los campos de información de identificación personal (PII) definidos por tu empresa dentro del panel. Los usuarios también pueden ver los campos PII en la pestaña **Vista previa como usuario** de las vistas previas de los mensajes.<br><br>Necesitas este permiso para utilizar [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), porque permite acceder directamente a algunos datos de clientes. Para exportar archivos CSV desde el panel, los usuarios necesitan tanto este permiso como el permiso "Exportar datos de usuario".|
|Espacio de trabajo|Ver perfiles de usuarios que cumplen las reglas de PII|Permite a los usuarios ver los perfiles de usuario que contienen campos que tu empresa ha definido como información de identificación personal (PII), pero redacta los campos PII.<br><br>Necesitas este permiso para utilizar la herramienta de búsqueda de usuarios. |
|Espacio de trabajo|Ver transformaciones|Permite a los usuarios ver [las transformaciones de datos Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espacio de trabajo|Ver datos de consumo|Permite a los usuarios ver el uso de la aplicación, incluidos los paneles de rendimiento del canal.|
|Espacio de trabajo|Fusionar usuarios duplicados|Permite a los usuarios fusionar perfiles de usuario duplicados.|
|Espacio de trabajo|Vista previa de usuarios duplicados|Permite previsualizar qué perfiles de usuario están duplicados.|
|Espacio de trabajo|Crear y editar plantillas de Canvas|Permite a los usuarios crear y editar plantillas Canvas.|
|Espacio de trabajo|Ver plantillas de Canvas|Permite a los usuarios ver plantillas Canvas.|
|Espacio de trabajo|Archivar plantillas de Canvas|Permite a los usuarios archivar plantillas de Canvas.|
|Espacio de trabajo|Gestionar la segmentación de propiedades de eventos personalizados|Permite a los usuarios crear segmentos en función de la frecuencia y la recurrencia de las propiedades del evento.|
|Espacio de trabajo|Publicar páginas de inicio|Permite a los usuarios publicar [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espacio de trabajo|Crear borradores de página de inicio|Permite a los usuarios crear y guardar borradores de páginas de destino.|
|Espacio de trabajo|Acceder a páginas de inicio|Permite a los usuarios acceder a la página **Páginas de destino**.|
|Espacio de trabajo|Crea y edita plantillas de páginas de inicio|Permite a los usuarios crear y editar plantillas de páginas de destino.|
|Espacio de trabajo|Ver plantillas de páginas de inicio|Permite a los usuarios ver plantillas de páginas de destino.|
|Espacio de trabajo|Archiva plantillas de páginas de inicio|Permite a los usuarios archivar plantillas de páginas de destino.|
|Espacio de trabajo|Ver agentes de IA personalizados|Permite a los usuarios ver [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esta característica está actualmente en fase beta.|
|Espacio de trabajo|Crear agentes de IA personalizados|Permite a los usuarios crear agentes de IA personalizados. Esta característica está actualmente en fase beta.|
|Espacio de trabajo|Editar agentes de IA personalizados|Permite a los usuarios editar agentes de IA personalizados. Esta característica está actualmente en fase beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
