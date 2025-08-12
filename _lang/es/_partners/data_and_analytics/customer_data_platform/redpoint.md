---
nav_title: Redpoint
article_title: Redpoint 
description: "La integración de Redpoint con Braze le permite incorporar y enriquecer los perfiles de usuario de Braze con sus datos de origen."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) es una plataforma tecnológica que ofrece a los profesionales del marketing una plataforma de orquestación de campañas totalmente integrada. Aproveche las funciones de segmentación, programación y automatización de Redpoint para controlar cómo y cuándo se importan los datos CDP a Braze.

_Esta integración está mantenida por Redpoint._

## Sobre la integración

La integración de Braze y Redpoint le permite crear segmentos Braze basados en sus datos CDP de Redpoint. Redpoint proporciona dos modos para pasar datos a Braze: 

1. Modo **Braze de incorporación y Upsert**: "Upserts" un perfil de usuario de Redpoint en Braze. Se utiliza para dar de alta o actualizar registros de usuarios cuando los datos han cambiado. 
2. Modo **Añadir Braze**: Actualiza el perfil de un usuario si ese usuario ya existe en Braze. 

Configurará una plantilla de exportación y un canal de salida para cada modo.

{% alert note %}
"Upsert" es una combinación de las palabras "update" (actualizar) e "insert" (insertar). Se utiliza cuando se desea insertar un nuevo registro en una tabla de la base de datos si aún no existe o actualizar el registro si ya existe. Básicamente, upsert comprueba si un registro concreto está presente en la base de datos. Si el registro está presente, se actualiza, y si no lo está, se inserta un nuevo registro.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Artefactos de gestión de datos de Redpoint | La integración de Braze se apoya en un conjunto de artefactos de gestión de datos de Redpoint. Póngase en contacto con [el servicio de asistencia de Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) para solicitar los artefactos correspondientes a su versión de Redpoint Data Management. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Atributos personalizados de Redpoint CDP

Los siguientes atributos personalizados de Redpoint pueden añadirse a un perfil de usuario Braze.

| Campo               | Descripción                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | El objeto de atributo de perfil CDP de Redpoint                                                                                  |
| `rpi_audience_outputs`| Conjunto de etiquetas de salida de audiencia a las que se dirige el usuario en una ejecución del canal Redpoint Outbound Delivery Braze         |
| `rpi_offers`         | Conjunto de etiquetas de oferta a las que se dirige el usuario en una ejecución del canal Redpoint Outbound Delivery Braze                   |
| `rpi_contact_ids`    | Conjunto de identificadores de contactos del historial de ofertas a los que se dirige el usuario en una ejecución del canal Redpoint Outbound Delivery Braze.     |
| `rpi_channel_exec_ids`| Matriz de ID de ejecución de canal donde el usuario es el objetivo en una ejecución de canal Redpoint Outbound Delivery Braze.       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integración

### Paso 1: Configurar plantillas

#### Paso 1a: Crear la plantilla Braze Onboarding and Upsert

En Redpoint Interaction (RPI), cree una nueva plantilla de exportación y nómbrela **Braze Onboarding and Upsert**. Esta plantilla define las asignaciones básicas entre el CDP de Redpoint y el perfil de usuario de Braze, junto con cualquier atributo personalizado adicional que desee añadir a sus perfiles de usuario en Braze.

Arrastre los atributos de Redpoint CDP a la columna **Atributos**. Establece cada **Valor de Fila de Encabezado** en el [atributo de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) Braze correspondiente. 

La siguiente tabla enumera los atributos CDP de Redpoint y sus correspondientes atributos Braze:

| Atributo Redpoint | Valor de la fila de cabecera |
|--------------------|------------------|
| PID                | `external_id`    |
| Nombre          | `first_name`     |
| Apellido          | `last_name`      |
| Correo electrónico principal      | `email`          |
| País principal    | `country`        |
| FECHA DE NACIMIENTO                | `dob`            |
| Género             | `gender`         |
| Ciudad principal       | `home_city`      |
| Teléfono principal      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Añada el atributo **Nombre de salida** de la tabla **Historial de ofertas**. Por último, añade cualquier atributo personalizado adicional de Redpoint que quieras fusionar en Braze. Por ejemplo, la siguiente es una plantilla de incorporación y actualización con educación, ingresos y estado civil como atributos adicionales.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Paso 1b: Crear la plantilla Braze Append

Cree una segunda plantilla de exportación para operaciones de append-only llamada **Braze Append**.

En esta plantilla sólo se establecen dos atributos. Para **PID**, establezca el **valor de la fila de cabecera** como `external_id`. Para **Nombre de salida**, establezca la **Fila de cabecera** como `output_name`.

![Una plantilla de exportación de muestra con los atributos `external_id` y nombre de salida.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Paso 1c: Establecer formato de fecha

Para ambas plantillas de exportación, vaya a la pestaña **Opciones** y establezca el **Formato de fecha** en el valor **Formato personalizado**. Establezca el formato como **aaaa-MM-dd**.

![La pestaña de opciones muestra el formato de fecha establecido en aaaa-MM-dd.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Paso 2: Crear canales de salida

En RPI, cree dos nuevos canales. Establezca ambos canales en **Entrega de salida**. Nombre un canal **Braze Onboarding y Upsert**, y el otro **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Tras la incorporación inicial de sus registros de CDP a Braze, compruebe si los flujos de trabajo posteriores de Redpoint Interaction que utilizan el canal Braze Onboarding and Upsert están diseñados para seleccionar únicamente los registros que han cambiado desde la sincronización inicial de incorporación.
{% endalert %}

### Paso 3: Configurar los canales

#### Paso 3a: Establecer plantilla y formato de ruta de exportación

Vaya a la pestaña **General** de la pantalla de **Configuración de** canales. Establezca la plantilla de exportación para cada canal respectivo. 

A continuación, defina un **formato de ruta de exportación** en ambos canales que apunte a una red compartida, un protocolo de transferencia de archivos o una ubicación de proveedor de contenidos externo que sea accesible tanto para Redpoint Interaction como para Redpoint Data Management. 

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

El formato del directorio de exportación en ambos canales será idéntico y deberá terminar en `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Paso 3b: Configurar la ejecución posterior

Vaya a la pestaña **Post Ejecución** en la pantalla de **Configuración de** Canales. 

Marque la casilla de verificación **Post-ejecución** para llamar a una URL de servicio después de la ejecución del canal. Introduce la URL de tu servicio Web de Gestión de Datos de Redpoint. Esta entrada será idéntica tanto en tu canal de Incorporación como en el de Adhesión.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Paso 4: Configura los componentes Braze en Redpoint Data Management 

El archivo que contiene los artefactos de Redpoint Data Management (RPDM) para soportar la integración Braze contiene un README con instrucciones detalladas para configurar los componentes necesarios. Tenga en cuenta los siguientes detalles al configurar su integración. 

#### Paso 4a: Actualiza la automatización RPI a Braze con tu punto final REST Braze y el directorio de salida RPI base 

Después de importar los artefactos relacionados con Braze en Redpoint Data Management, abra la automatización denominada **AUTO_Process_RPI_to_Braze** y actualice las dos variables de automatización siguientes con los valores de su entorno:

* **BRAZE_API_URL**: El punto final REST Braze
* **BASE_OUTPUT_DIRECTORY**: El directorio de salida compartido entre Redpoint Interaction y Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Paso 4b: Actualizar el proyecto de anexión de RPI a Braze 

El proyecto de gestión de datos de Redpoint denominado **PROJ_RPI_to_Braze_Append** contiene el esquema del archivo de exportación de entrega saliente y las asignaciones para el objeto de atributo personalizado `rpi_cdp_attributes` en Braze. 

Actualice el esquema de entrada de archivos y la herramienta de inyección de documentos denominada **RPI a Braze Document Injector** con cualquier atributo CDP personalizado adicional definido en su plantilla de archivo de exportación. Este ejemplo muestra la asignación adicional de educación, ingresos y estado civil:

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Utilizar la integración

El canal Braze de entrega saliente puede aprovecharse ahora dentro de los flujos de trabajo de Redpoint Interaction. Siga las prácticas estándar para crear reglas de selección y audiencias en RPI, así como para crear programas de flujo de trabajo y desencadenantes asociados. 

Para habilitar la sincronización de una salida de RPI Audience con Braze, cree una oferta de entrega saliente y asóciela al canal **Braze Onboarding and Upsert** o **Braze Append**. Esto depende de si la intención es crear o fusionar nuevos registros en Braze, o sólo añadir datos de campaña si el registro ya existe en Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Una vez que el flujo de trabajo se ha ejecutado correctamente en RPI, los datos de orquestación y CDP procedentes de RPI pueden utilizarse ahora para crear segmentos en Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Puede ver las propiedades asociadas a Redpoint en el perfil del usuario.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}


