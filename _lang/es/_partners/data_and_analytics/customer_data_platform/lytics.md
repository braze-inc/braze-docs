---
nav_title: Lytics
article_title: Lytics
description: "Este artículo de referencia cubre la integración de Braze y Lytics. Lytics es una plataforma empresarial de datos de los clientes para profesionales del marketing, analistas y tecnólogos. Esta integración permite a las marcas sincronizar y mapear sus datos de Lytics directamente con Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) es la plataforma de datos de los clientes (CDP) elegida por la próxima generación de empresas centradas en el cliente. Las soluciones Lytics Decision Engine, Conductor y Cloud Connect ofrecen a los especialistas en marketing y a los equipos de datos la oportunidad de llevar a cabo la resolución de identidades, la orquestación y la optimización de campañas en tiempo real y respetando la privacidad.

_Esta integración está mantenida por Lytics._

## Sobre la integración

La integración de Braze y Lytics proporciona una visión unificada de tus clientes para habilitar una potente personalización e impulsar campañas optimizadas utilizando la mejor orquestación de acciones y decisiones.

La integración permite a las marcas:

- Exporta audiencias a Braze directamente desde Lytics
- Enviar eventos de campañas Braze o Canvases a Lytics en tiempo real para campañas personalizadas y para construir perfiles de usuario enriquecidos.

## Casos prácticos

Conecta Braze a Lytics para [importar](#importing-data-from-braze-to-lytics) correo electrónico, SMS y actividad push para enriquecer los perfiles de usuario de Lytics. Si utilizas Braze y Lytics juntos, también puedes [exportar](#integration) las audiencias de Lytics basadas en comportamientos y multicanal para crear recorridos del cliente Braze altamente personalizados utilizando datos propios.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Lytics | Se necesita una cuenta de Lytics para aprovechar esta integración. |
| Número de cuenta Lytics | Es necesario un número de cuenta de Lytics para configurar la URL del punto final del webhook. |
| Token de la API de Lytics | Un token de API REST de Lytics con permisos de administrador de datos. <br><br> Se puede crear dentro del panel de Lytics desde **Consola de configuración de la cuenta** > **Tokens de acceso** > **Crear nuevo token**. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permiso de `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| instancia de Braze | Tu [instancia de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Ponte en contacto con tu administrador de incorporación de Braze para obtener esta información si no estás seguro. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Esta sección describe cómo exportar datos de Lytics a Braze.

### Paso 1: Crear una autorización

En Lytics, navega hasta el panel **Autorización** dentro de la consola **Datos** en la barra de navegación. Selecciona **Crear nueva autorización** y busca y selecciona **Braze**.

En el mensaje **Configurar autorización** que aparece, proporciona una etiqueta y una descripción e introduce tu clave de API REST y tu instancia de Braze. Selecciona **Completar** cuando hayas terminado.

![]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Paso 2: Crear un nuevo trabajo

En Lytics, navega hasta el panel **Trabajos** dentro de la consola **Datos** en la barra de navegación. Selecciona **Crear nuevo trabajo** y busca y selecciona **Braze**.  En la ventana **Seleccionar tipo de tarea** que aparece, selecciona **Exportar audiencia**.

![]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

A continuación, elige una autorización dentro de las opciones de **Seleccionar autorización**.

![]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Paso 3: Configurar el trabajo

Dentro de la pregunta **Configurar trabajo**, proporciona una etiqueta y una descripción opcional. A continuación, en la entrada **Campo ID externo de usuario de Braze**, selecciona el campo de Lytics que contiene el ID externo de usuario de Braze (`braze_id`). El siguiente paso es el más importante: selecciona las audiencias que vas a exportar a Braze.

![]({% image_buster /assets/img/lytics/braze_job.png %}){: style="max-width:80%;"}

Por último, elige la opción preferida para la casilla **Usuarios existentes**. Si dejas marcada esta casilla, se añadirán los usuarios que ya existan en la audiencia de Lytics seleccionada. Si no está marcada, los usuarios sólo se exportarán a Braze cuando entren o salgan de la audiencia una vez iniciado el flujo de trabajo.

{% alert note %}
Al marcar esta casilla, todos los usuarios existentes en la audiencia seleccionada serán enviados a Braze. Esto hará que se genere un punto de datos por usuario y por audiencia para la sincronización inicial.
{% endalert %}

Haz clic en **Completar** cuando hayas terminado para iniciar la exportación y guardar.

![]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Una vez configurada la tarea de exportación, Lytics enviará las audiencias seleccionadas a Braze a través de la integración nativa. A continuación se muestra un ejemplo de audiencia que muestra la estructura JSON de la audiencia enviada a Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Se creará un nuevo usuario en Braze para cualquier `external_id` incluido en la exportación de audiencia que aún no exista en Braze. 

## Importar datos de Braze a Lytics

Puedes importar datos de audiencia de Braze a Lytics utilizando los siguientes métodos:

- [Utilizando webhooks](#using-webhooks)
- [Desde un archivo CSV](#from-a-csv-file)

### Utilizando webhooks

#### Paso 1: Crear un token de API de Lytics

Navega hasta el Menú de Cuenta de Lytics en la esquina inferior izquierda seleccionando tu nombre de cuenta, y selecciona **Tokens de Acceso** en el menú desplegable. A continuación, selecciona **Crear token de API**

![]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Introduce un nombre, una descripción opcional y un periodo de caducidad del token. A continuación, alterna el ámbito **del administrador de datos** para los permisos de API y haz clic en **Generar token**. Copia el token y guárdalo en un lugar seguro.

![]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Paso 2: Configurar la URL del webhook de Lytics

La URL del webhook de Lytics la utiliza Braze para enviar un mensaje a la API de Lytics desde Braze. Este mensaje puede utilizarse para personalizar tus campañas en Lytics o para enriquecer tu perfil de cliente de Lytics. Es necesario añadir los dos parámetros siguientes en la URL del webhook de Lytics:

- Número de cuenta Lytics
- Token de la API de Lytics

Configura la URL de tu webhook como se indica a continuación:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Sustituye `<ACCOUNT-NUMBER>` por tu número de cuenta y `<LYTICS-API-TOKEN>` por tu token de la API de Lytics.

#### Paso 3: Crear un Webhook en Braze 

En Braze, crea una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). Añade la URL del webhook de Lytics en el campo **URL del webhook**.

Tras definir el tipo de solicitud (método HTTP `POST` ) y configurar el resto de detalles del webhook, tu webhook está listo para ser probado y desplegado. Aquí tienes un cuerpo de muestra de la petición POST después de configurar el webhook en Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### Desde un archivo CSV

Esta sección describe cómo importar datos de usuario Braze de un segmento a Lytics.

#### Paso 1: Crear una autorización

En Lytics, navega hasta el panel **Autorización** dentro de la consola **Datos** en la barra de navegación. Selecciona **Crear nueva autorización** y busca y selecciona **Integraciones personalizadas**.

Selecciona el tipo preferido de autorización SFTP en función de tus requisitos empresariales y de seguridad. Se admiten los siguientes tipos de autorización para importar archivos a Lytics mediante SFTP:

- Autorización del servidor SFTP cliente
- Autorización del servidor SFTP cliente con clave privada PGP
- Autorización del servidor SFTP administrado por Lytics

Las autorizaciones SFTP de clave pública son sólo para exportación SFTP.

![]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

En el aviso **Configurar autorización** que aparece, proporciona una etiqueta y una descripción y completa el resto de requisitos de configuración. Haz clic en **Completar** cuando hayas terminado.

#### Paso 2: Exportar los datos de tus segmentos a CSV

En Braze, ve a **Audiencia** > **Segmentos**. Localiza el segmento que deseas exportar y, a continuación, selecciona <i class="fas fa-gear" aria-label="Configuración"></i> y luego **Exportar datos de usuario CSV**. Puedes exportar hasta 500.000 usuarios en un segmento. Para más detalles, consulta [Exportar datos de segmentos a CSV]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/).

#### Paso 3: Configurar un trabajo de importación CSV

En Lytics, navega hasta el panel **Trabajos** dentro de la consola **Datos** en la barra de navegación. Selecciona **Crear nuevo trabajo** y busca y selecciona **Integraciones personalizadas**.

A continuación, selecciona el tipo de trabajo. Para importar archivos CSV de Braze a Lytics, selecciona **Importar CSV** como tipo de trabajo.

![]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Por último, introduce una etiqueta y una descripción opcional para el trabajo y configura cualquier otro detalle necesario. Haz clic en **Completar** para iniciar y guardar el trabajo.







