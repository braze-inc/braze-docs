---
nav_title: Permisos
article_title: Permisos Braze
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo funcionan los permisos de usuario en Braze. Aquí puedes aprender a editar y configurar los permisos de usuario, eligiendo quién puede acceder a tus aplicaciones en el panel."
tool: Dashboard

---

# Permisos Braze

> Aprende a crear conjuntos de permisos, crear roles, editar permisos de usuario y exportar permisos de usuario, para asegurarte de que tus usuarios sólo acceden a los espacios de trabajo y características que más necesitan.

## Crear un conjunto de permisos

Utiliza conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Pueden aplicarse a usuarios del panel que necesiten el mismo acceso en distintos espacios de trabajo. Para crear un **conjunto de permisos**, ve a **Configuración** > **Configuración de permisos** y, a continuación, selecciona **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nombre|Permisos|
\|-----------|----------------|
|Desarrolladores|"Access Dev Console"|Consola de desarrollo de acceso
|Especialistas en marketing|"Campañas de acceso, lonas, tarjetas, banderas de características, segmentos, biblioteca multimedia y centros de preferencias" <br> "Gestionar activos de la mediateca"|
|Gestión de usuarios|"Gestionar usuarios del panel" <br> "Administrar equipos"|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Crear un rol

Los roles permiten una mayor estructuración al agrupar tus permisos personalizados individuales con controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un mismo panel. Con los roles, puedes añadir usuarios del panel a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol | Espacio de trabajo | Permisos  
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda {:/} | "Campañas de acceso, lienzos, tarjetas, banderas de características, segmentos, mediateca y centro de preferencias"<br>"Gestionar activos de la mediateca" |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de la piel {:/} | "Campañas de acceso, lienzos, tarjetas, banderas de características, segmentos, biblioteca de medios y centros de preferencias" <br>"Gestionar activos de la mediateca" |
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Marca de moda, [QA] Marca de moda, [PROD] Marca de moda, [DEV] Marca de cuidado de la piel, [QA] Marca de cuidado de la piel, [PROD] Marca de cuidado de la piel {:/} | "Gestionar usuarios del panel"<br>"Administrar equipos" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y funciones de los Equipos?

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para añadir permisos de usuario a Equipos

Puedes encontrar dificultades al intentar guardar permisos en el panel de Braze, sobre todo al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un Equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tiene a nivel de espacio de trabajo. Esta restricción existe porque no hay ninguna ventaja en tener un Equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel de espacio de trabajo. En su lugar, asigna permisos exclusivamente a nivel de equipo.

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

\![La página "Usuarios de la empresa" en Braze con un usuario listado en los resultados.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Admin

Los administradores tienen acceso a todas las características y la posibilidad de modificar cualquier configuración de la empresa. Pueden hacerlo:

- Cambiar [configuración de aprobación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Añadir, editar, eliminar, suspender o cancelar la suspensión de otros [usuarios de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exportar usuarios de Braze como CSV

Para conceder o eliminar privilegios de administrador, selecciona **Este usuario es un administrador** y, a continuación, **Actualizar usuario**.

Detalles del usuario seleccionado con la casilla de verificación de administrador activada.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Si eliminas los privilegios de administrador a un usuario, no podrá acceder a Braze hasta que le asignes al menos un permiso [a nivel de](#workspace) [empresa](#company) o [de espacio de trabajo](#workspace).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marca o desmarca la casilla situada junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

|Nombre del permiso|Descripción|
|----------|-----------|
|Administrar configuración de la empresa|Permite a los usuarios modificar cualquier configuración de la empresa.|
|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espacio de trabajo

Puedes dar a un usuario permisos diferentes para cada espacio de trabajo al que pertenezca en Braze. Para gestionar sus permisos a nivel de espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y, a continuación, elige sus permisos manualmente para seleccionar o asignar un conjunto de permisos [que hayas creado previamente](#creating-a-permission-set).

Si necesitas dar a un usuario permisos diferentes para distintos espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver una descripción de cada permiso, consulta [Lista de permisos](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

En **Espacios de trabajo**, elige uno o varios espacios de trabajo del desplegable. A continuación, en **Permisos**, elige uno o varios permisos del desplegable. Se les asignarán estos permisos sólo para los espacios de trabajo que hayas seleccionado. Opcionalmente, puedes seleccionar **Habilitar acceso de administrador** si quieres darles permisos completos para este espacio de trabajo.

Cuando hayas terminado, selecciona **Actualizar usuario**.

Los permisos a nivel de espacio de trabajo se seleccionan manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

En **Espacios de trabajo**, elige uno o varios espacios de trabajo del desplegable. A continuación, en **Conjuntos de permisos**, elige un conjunto de permisos. Se les asignarán estos permisos sólo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

Se están asignando permisos a nivel de espacio de trabajo a través de un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportar permisos de usuario

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Usuarios de la empresa** y, a continuación, selecciona **Exportar usuarios**. En breve te enviaremos un archivo CSV a tu dirección de correo electrónico.

\![La página "Usuarios de la empresa" en Braze con la opción "Exportar usuarios" enfocada.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permisos

{% alert important %}
A partir de abril de 2024, para crear o actualizar listas de códigos promocionales, los usuarios de Braze necesitan el permiso "Acceder a campañas, lienzos, tarjetas, segmentos, biblioteca multimedia".
{% endalert %}

|Nivel|Nombre|Definición|
|---|---|---|
|Admin|Admin|Permite a los usuarios acceder a todas las características disponibles. Esta es la configuración predeterminada para todos los usuarios nuevos. Puede actualizar la configuración de la empresa (nombre de la empresa y zona horaria), cosa que los usuarios limitados no pueden hacer.|
|Empresa|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
|Empresa|Administrar configuración de la empresa|Permite a los usuarios modificar cualquier configuración de la empresa.|
|Espacio de trabajo|Campañas de acceso, lienzos, tarjetas, bloques de contenido, banderas de características, segmentos, mediatecas, ubicaciones, códigos promocionales y centros de preferencias.|Permite a los usuarios ver las métricas de rendimiento de campañas y Canvas, crear y duplicar borradores de campañas y Lienzos, editar borradores y plantillas de campañas y Canvas, ver borradores de segmentos, plantillas y medios, crear plantillas, cargar medios, crear o actualizar listas de códigos promocionales, ver informes de interacción y ver la configuración de mensajes globales en el panel. Sin embargo, los usuarios con este permiso no pueden pausar ni editar el contenido en vivo existente.|
|Espacio de trabajo|Acceder a la consola de desarrollo|Permite el acceso completo a las siguientes configuraciones y registros:{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Claves de API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Grupos internos</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Registro de actividad de mensajes</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Registro de usuarios del evento</a></li></ul>{:/}|
|Espacio de trabajo|Campañas de aprobación y denegación|Permite a los usuarios aprobar o denegar campañas. El [flujo de trabajo de aprobación de campañas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si estás interesado en participar en el acceso anticipado.|
|Espacio de trabajo|Aprobar y denegar lonas|Permite a los usuarios aprobar o denegar Lienzos. El [flujo de trabajo de aprobación de Lienzos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso.|
|Espacio de trabajo|Editar integraciones de Currents|Permite a los usuarios modificar una conexión Currents, incluidas las credenciales. Por defecto, a los usuarios a los que se les ha asignado el permiso "Integraciones externas" también se les asigna este permiso.|
|Espacio de trabajo|Editar segmentos|Permite a los usuarios crear y editar segmentos. Puedes seguir creando campañas con segmentos y filtros existentes sin este permiso. Necesitas este permiso para generar un segmento a partir de los usuarios de un CSV o reorientar el grupo de usuarios del CSV.|
|Espacio de trabajo|Exportar datos de usuario|Permite a los usuarios exportar sus datos de usuario de segmentos, campañas y Lienzos. Este permiso incluye información sensible del usuario como nombres, direcciones de correo electrónico y otra información personal identificable (PII) recopilada. |
|Espacio de trabajo|Importar y actualizar datos de usuario|Permite a los usuarios importar archivos CSV y de actualización de usuarios de la aplicación, así como ver la página de importación de usuarios. Esto también te permite editar el estado de suscripción de un usuario y sus reglas de adhesión/exclusión del grupo de suscripción.|
|Espacio de trabajo|Lanzar y gestionar bloques de contenido|Permite a los usuarios lanzar y administrar [bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espacio de trabajo|Poner en marcha Centros de Preferencia|Permite a los usuarios lanzar [centros de preferencias]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espacio de trabajo|Administrar aplicaciones|Permite a los usuarios editar **la configuración de la aplicación**.|
|Espacio de trabajo|Permiso para el panel de gestión de catálogos|Permite a los usuarios crear y administrar catálogos.|
|Espacio de trabajo|Administrar usuarios del panel de control| Permite a los no administradores ver, editar y gestionar la página **Usuarios de la empresa**, y gestionar los usuarios del panel en su espacio de trabajo modificando los permisos de cualquier usuario, incluidos los suyos propios. Los usuarios con este permiso no pueden eliminar usuarios (sólo los administradores pueden eliminar usuarios).|
|Espacio de trabajo|Administrar configuración de correo electrónico|Permite a los usuarios guardar los cambios de configuración del correo electrónico**(Configuración** > **Preferencias de correo electrónico**).|
|Espacio de trabajo|Gestionar Eventos, Atributos, Compras|Permite a los usuarios editar atributos personalizados (los usuarios sin esta capacidad pueden seguir viendo atributos personalizados), editar y ver propiedades de eventos personalizados, y editar y ver propiedades de productos en **Configuración de datos**.|
|Espacio de trabajo|Administrar integraciones externas|Permite acceder a todas las pestañas de **los socios tecnológicos**, sincronizar Braze con otras plataformas y gestionar [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espacio de trabajo|Administrar indicadores de características|Permite a los usuarios crear o editar [banderas de características]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espacio de trabajo|Administrar activos de la biblioteca multimedia|Permite a los usuarios añadir, editar y eliminar activos de la biblioteca multimedia.|
|Espacio de trabajo|Administrar grupos de suscripción|Permite a los usuarios crear y gestionar grupos de suscripción.|
|Espacio de trabajo|Administrar etiquetas|Permite a los usuarios editar o eliminar etiquetas (en **Gestión de etiquetas**). No necesitas este permiso para añadir etiquetas a campañas o segmentos.|
|Espacio de trabajo|Administrar equipos|Permite a los usuarios administrar **equipos internos**. La posibilidad de seleccionar este permiso depende de tu contrato con Braze.|
|Espacio de trabajo|Administrar transformaciones|Permite a los usuarios crear y gestionar Transformaciones de Datos.|
|Espacio de trabajo|Enviar Campañas, Lonas|Permite a los usuarios editar, archivar y detener campañas y Lienzos, crear campañas y lanzar Lienzos. |
|Espacio de trabajo|Ver detalles de facturación|Permite a los usuarios ver las suscripciones y la facturación.|
|Espacio de trabajo|Ver la integración de Currents|Permite a los usuarios ver toda la información sobre una conexión Currents, excluyendo las credenciales. Por predeterminado, también se asigna este permiso a los usuarios que tienen asignado el permiso "Acceder a campañas, lienzos, tarjetas, bloques de contenido, banderas de características, segmentos, mediatecas, ubicaciones, códigos promocionales y centros de preferencias".|
|Espacio de trabajo|Ver atributos personalizados marcados como PII|Permite a los usuarios que no son administradores ver atributos personalizados que contienen información sensible y están marcados como información de identificación personal (PII).|
|Espacio de trabajo|Ver PII|Permite a los usuarios ver los campos de información de identificación personal (PII) definidos por tu empresa dentro del panel. Los usuarios también pueden ver los campos PII en la pestaña **Vista previa como usuario** de las vistas previas de los mensajes.<br><br>Necesitas este permiso para utilizar [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), porque permite acceder directamente a algunos datos de clientes.|
|Espacio de trabajo|Ver perfiles de usuario Conformidad PII|Permite a los usuarios ver los perfiles de usuario que contienen campos que tu empresa ha definido como información de identificación personal (PII), pero redacta los campos PII.<br><br>Necesitas este permiso para utilizar la herramienta de búsqueda de usuarios. |
|Espacio de trabajo|Ver Transformaciones|Permite a los usuarios ver [las Transformaciones de Datos Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espacio de trabajo|Ver datos de uso|Permite a los usuarios ver el uso de la aplicación, incluidos los paneles de rendimiento del canal.|
|Espacio de trabajo|Fusionar usuarios duplicados|Permite a los usuarios fusionar perfiles de usuario duplicados.|
|Espacio de trabajo|Vista previa de usuarios duplicados|Permite a los usuarios ver previamente qué perfiles de usuario están duplicados.|
|Espacio de trabajo|Crear y editar plantillas de Canvas|Permite a los usuarios crear y editar plantillas Canvas.|
|Espacio de trabajo|Ver plantillas de Canvas|Permite a los usuarios ver plantillas Canvas.|
|Espacio de trabajo|Archivo Plantillas Canvas|Permite a los usuarios archivar plantillas de Canvas.|
|Espacio de trabajo|Gestionar la segmentación de propiedades de eventos personalizados|Permite a los usuarios crear segmentos en función de la frecuencia y la recurrencia de las propiedades del evento.|
|Espacio de trabajo|Publicar páginas de destino|Permite a los usuarios publicar [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espacio de trabajo|Crear borradores de página de destino|Permite a los usuarios crear y guardar borradores de páginas de destino.|
|Espacio de trabajo|Acceder a páginas de destino|Permite a los usuarios acceder a la página **Páginas de destino**.|
|Espacio de trabajo|Crea y edita plantillas de páginas de destino|Permite a los usuarios crear y editar plantillas de páginas de destino.|
|Espacio de trabajo|Ver plantillas de páginas de destino|Permite a los usuarios ver plantillas de páginas de destino.|
|Espacio de trabajo|Archivo Plantillas de páginas de destino|Permite a los usuarios archivar plantillas de páginas de destino.|
|Espacio de trabajo|Ver Agentes AI personalizados|Permite a los usuarios ver [agentes de IA personalizados]({{site.baseurl}}/user_guide/brazeai/agents/). Esta característica está actualmente en fase beta.|
|Espacio de trabajo|Crear agentes de IA personalizados|Permite a los usuarios crear agentes de IA personalizados. Esta característica está actualmente en fase beta.|
|Espacio de trabajo|Editar agentes AI personalizados|Permite a los usuarios editar agentes de IA personalizados. Esta característica está actualmente en fase beta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
