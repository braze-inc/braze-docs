---
nav_title: BlueConic
article_title: BlueConic
description: "Este artículo de referencia describe la asociación entre Braze y BlueConic, una plataforma líder de datos de clientes, que permite unificar datos en perfiles individuales persistentes y sincronizarlos en los dos sistemas para importar objetivos a través de un servidor S3 de Amazon Web Services."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/), la principal plataforma de datos de clientes, libera los datos de origen de las empresas de sistemas dispares y los hace accesibles donde y cuando se necesitan para transformar las relaciones con los clientes e impulsar el crecimiento del negocio. 

_Esta integración está mantenida por Blueconic._

## Sobre la integración

La integración de Braze y BlueConic permite a los usuarios unificar datos a través de perfiles individuales persistentes y luego sincronizarlos entre los dos sistemas para objetivos de importación a través de un servidor S3 de Amazon Web Services. Los objetivos potenciales incluyen iniciativas centradas en el crecimiento, orquestación del ciclo de vida del cliente, modelado y análisis, productos y experiencias digitales, monetización basada en la audiencia, etc. Esta integración permite tanto la importación como la exportación programadas por lotes. 

{% alert important %}
Al utilizar la integración, BlueConic enviará deltas (datos cambiantes) en cada sincronización. Esto incluye cualquier perfil que haya cambiado desde el último envío y todos los atributos de ese perfil. Controle el uso de los puntos de datos en consecuencia.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta BlueConic | Se requiere una [cuenta BlueConic](https://www.blueconic.com/) para beneficiarse de esta asociación. Necesitará acceso para [ver y editar conexiones](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles) dentro de su cuenta BlueConic para acceder a los plugins. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` y `segments.details`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia](https://portal.aws.amazon.com/billing/signup#/start). |
| Autenticación S3 | Necesitará acceso a un servidor de Amazon Web Services (S3) para exportar e importar los datos. |
| ID de la clave de acceso<br>Clave de acceso secreta | El ID de la clave de acceso y la clave de acceso secreta le permitirán autenticar su servidor S3 para importar y exportar. |
| Contenedor AWS | Usted tendrá que conectarse a S3 dentro del plugin. Tras la autenticación, los contenedores disponibles aparecerán en un menú desplegable. Aquí se almacenan los archivos que se van a importar o exportar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear una conexión Braze

En BlueConic, seleccione **Conexiones** en la barra de navegación y, a continuación, **Añadir conexión**. En la ventana que aparece, busca **Braze** y selecciona **Conexión Braze**. 

Despliegue o contraiga los campos de metadatos disponibles en la conexión haciendo clic en el icono del galón gris. En estos campos, puede marcar esta conexión como favorita, asignarle un nombre, añadir etiquetas, incluir una descripción y optar por recibir notificaciones por correo electrónico si la conexión [se ejecuta o no](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ). 

Guarda tu configuración.

### Paso 2: Configuración de una conexión Braze

Para configurar la conexión entre BlueConic y Braze, debe añadir las credenciales de su cuenta Braze y la información de la cuenta de Amazon Web Services (S3) para autenticar la conexión. 

1. En BlueConic, seleccione **Configurar y ejecutar** en la sección **Configuración** del panel izquierdo.<br><br>
2. En la página de autenticación Braze que se abre, introduce tu punto final de API REST Braze y tu clave de API Braze.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. En la sección de configuración y autenticación de S3, introduce estas credenciales: ID de la clave de acceso, clave de acceso secreta y contenedor de S3 de Amazon Web Services (S3). Deben ser las [mismas credenciales]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) que configuraste al configurar la integración de Braze y Amazon S3. Guarda tu configuración. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Paso 3: Creación de objetivos de importación o exportación (asignación de importaciones)

Una vez completada la autenticación, debe crear al menos un objetivo de importación o exportación, activar la conexión y programar o ejecutar la conexión.

{% tabs %}
{% tab Importar %}

1. Seleccione **Importar datos a BlueConic** en el panel izquierdo para abrir la página de configuración de datos Braze.<br><br>
2. Seleccione la ubicación de los datos en Braze. Aquí puede indicar a BlueConic dónde encontrar los datos a importar seleccionando su público Braze.<br>![La audiencia de BlueConic Braze configurada como "Usuarios de prueba de BlueConic".]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, mapea los identificadores entre Braze y BlueConic. <br>![El campo "ID externo" de Braze está mapeado con el campo "ID externo" de BlueConic.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Para vincular los datos del cliente entre los dos sistemas, introduzca uno o varios identificadores de cliente.<br>Utilice la casilla **Permitir creación...** para permitir que BlueConic cree nuevos perfiles para datos que no coincidan con un perfil BlueConic existente.<br><br>
4. A continuación, haga coincidir los campos de datos BlueConic que va a exportar con los campos Braze. Utilice los campos desplegables para seleccionar el identificador de perfil BlueConic o una propiedad de perfil a la izquierda y seleccione el identificador de perfil Braze correspondiente. A continuación, utilice el menú desplegable para especificar cómo debe añadirse el contenido importado a los valores existentes: añadido, sumado, establecido sólo si la propiedad del perfil está vacía o establecido a cero (si el campo Braze está vacío).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Utilice el botón **Añadir asignación** para crear líneas de asignación adicionales según sea necesario. Puede añadir varias líneas de asignación con la opción **Añadir campos restantes**. BlueConic detecta los campos Braze restantes y los empareja con las propiedades del perfil BlueConic. Puede establecer la estrategia de fusión para las importaciones (set, add, sum, set if empty o clear) y proporcionar un prefijo personalizado a los nombres de las propiedades del perfil BlueConic.<br><br>
5. Por último, seleccione **Ejecutar la conexión** para iniciar la conexión. Visite [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para obtener más información sobre la programación y ejecución de conexiones.
{% endtab %}
{% tab Exportar %}

1. Seleccione **Exportar datos a Braze** en el panel izquierdo para configurar su exportación de datos de BlueConic a Braze.<br><br>
2. Elija un segmento BlueConic para la exportación. Sólo se exportarán los perfiles de este segmento con identificadores coincidentes en Braze.<br>![Un segmento BlueConic de 20 000 perfiles.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. A continuación, vincule los identificadores entre los perfiles BlueConic y los campos Braze. Opcionalmente, puede dejar que BlueConic cree nuevos registros si no encuentra ninguna coincidencia.<br>![El campo "ID externo" de Braze está mapeado con el campo "ID externo" de BlueConic.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. A continuación, haga coincidir los campos de datos BlueConic que va a exportar con los campos Braze. Utilice el menú desplegable del icono de BlueConic para elegir el tipo de [información](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que desea exportar. La información disponible incluye las propiedades del perfil, los identificadores de perfil de BlueConic, los segmentos asociados, todas las interacciones vistas, los niveles de permiso y un valor de texto estático.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Por último, haga clic en **Ejecutar la conexión** para iniciar la conexión. Visite [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) para obtener más información sobre la programación y ejecución de conexiones.
{% endtab %}
{% endtabs %}

## Paso 4: Alternar conexión activada

Utilice el conmutador situado junto al título de la conexión Braze para activar o desactivar la conexión. Una conexión debe estar encendida para funcionar durante las horas programadas. 


