---
nav_title: Puntuación de clientes potenciales
article_title: Creación de un flujo de trabajo de puntuación de clientes potenciales
page_order: 1
page_type: reference
description: "Aprenda a utilizar Braze para realizar la puntuación simple de clientes potenciales, la puntuación externa de clientes potenciales y el traspaso de clientes potenciales."
---

# Creación de un flujo de trabajo de puntuación de clientes potenciales

> Este caso de uso demuestra cómo puede utilizar Braze para actualizar las puntuaciones de clientes potenciales de los usuarios en tiempo real y entregar automáticamente los clientes potenciales a sus equipos de ventas.

Hay dos pasos clave para crear un flujo de trabajo de puntuación de clientes potenciales en Braze:

1. Cree un lienzo de puntuación de clientes potenciales en Braze o integre una herramienta externa de puntuación de clientes potenciales:
- [Puntuación sencilla de clientes potenciales](#simple-lead-scoring)
- [Calificación externa de clientes potenciales](#external-lead-scoring)

2. Cree una campaña webhook para enviar clientes potenciales cualificados a su equipo de ventas:
- [Transición de clientes potenciales: De cliente potencial calificado por el equipo de marketing (MQL) a las ventas](#lead-handoff)

## Puntuación sencilla de clientes potenciales

### Paso 1: Crear un lienzo

1. Ve a **Mensajería** > **Canvas** y selecciona **Crear Canvas**, y luego rellena los datos básicos de tu Canvas.

2. Dele a su Canvas un nombre relevante como "Lead Scoring Canvas" y, para una mejor localización, etiquételo con algo como "Lead Management".<br><br>![Paso 1 de la creación de un Canvas con el nombre "Lead Scoring Canvas" y la etiqueta "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Paso 2: Configura tus criterios de entrada

1. Vaya al paso **Programa de entrada** y seleccione un programa de entrada **basado en acciones**. Esto introducirá a los usuarios en el Canvas cuando realicen acciones específicas.

2. En **Opciones basadas en acciones**, añada estas dos acciones:
    - **Cambia el valor del atributo personalizado** por el nombre de tu atributo de puntuación de clientes potenciales (como `lead score`). Si aún no ha creado un atributo de puntuación de clientes potenciales, siga los pasos de [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). Esto introducirá a los usuarios en el Canvas cada vez que cambie su puntuación de cliente potencial.
    - **Agregar una dirección de correo electrónico**

![Paso 2 de la creación de un Canvas con el horario de entrada de "Basado en la acción" y las opciones basadas en la acción de cambiar un atributo personalizado "puntuación de clientes potenciales" y añadir una dirección de correo electrónico.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Paso 3: Identificar tu audiencia objetivo

#### Paso 3a: Seleccionar segmentos

Todos los usuarios son elegibles para la puntuación de clientes potenciales, por lo que puede añadir reglas específicas de la empresa sobre a quién puntuar seleccionando a qué [segmentos de]({{site.baseurl}}/user_guide/engagement_tools/segments/) usuarios dirigirse y aplicando [filtros adicionales]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Por ejemplo, puede excluir a empleados, usuarios que ya son clientes y similares. 

![Paso 3 de la creación de un Canvas con opciones para seleccionar segmentos y filtros para acotar la audiencia de entrada.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Paso 3b: Configurar la reelegibilidad de Canvas

Un usuario pasará por este lienzo muchas veces a lo largo de su ciclo de vida con usted, así que asegúrese de que pueda volver a entrar tan rápido como salió la vez anterior. Esto puede conseguirse mediante la configuración de la reelegibilidad. 

En **Controles de entrada**, haga lo siguiente:
- Seleccione **Permitir a los usuarios volver a entrar en este lienzo**.
- Selecciona **Ventana especificada**.
- Establezca la reelegibilidad en "0" **segundos**.

![Sección "Controles de entrada" que tiene selecciones para "Permitir a los usuarios volver a entrar en este Canvas" en una "Ventana especificada" de 0 segundos.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Paso 3c: Actualizar la configuración de envío

Dada la naturaleza operativa de este Canvas y el hecho de que no se enviarán mensajes a estos usuarios, no es necesario atenerse a los estados de suscripción.

En **Configuración de la suscripción**, en **Enviar a estos usuarios:** seleccione **todos los usuarios, incluidos los usuarios dados de baja**. 

![Paso 4 de la creación de un Canvas para configurar las opciones de envío de mensajes.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Paso 4: Construye tu Canvas

#### Paso 4a: Añadir una ruta de acción

Bajo tu variante, selecciona el ícono más y, a continuación, selecciona **Rutas de acción**.

![Canvas con "Rutas de acción" mostradas en el menú abierto por el icono más.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Paso 4b: Crear grupos de acción

Cada Grupo de Acciones representará todas las acciones que conducen al mismo incremento o decremento de puntos. Puede configurar hasta ocho Grupos de Acción. En este escenario, crearemos cuatro grupos.

Añada los siguientes grupos a su ruta de acción:

- **Grupo 1:** Todos los eventos que cuentan para un incremento de 1 punto.
- **Grupo 2:** Todos los eventos que cuentan para un incremento de 5 puntos.
- **Grupo 3:** Todos los eventos que cuentan para un decremento de 1 punto.
- **Todos los demás:** Las rutas de acción permiten definir la ventana para esperar a ver si un usuario realiza una acción, antes de incluirlo en un grupo de "todos los demás". Para la puntuación de clientes potenciales, esta es una oportunidad para disminuir la puntuación por "inactividad".

![Ruta de acción que contiene Grupos de Acción para sumar un punto, cinco puntos y diez puntos; restar un punto y diez puntos; y "Todos los demás".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %})

#### Paso 4c: Configure cada grupo para incluir los eventos pertinentes

En cada Grupo de Acciones, seleccione **Seleccionar activador** y elija el evento que sumará el número de puntos para ese Grupo de Acciones en particular. Añada más disparadores para incluir todos los eventos que incrementarán en uno la puntuación de clientes potenciales. Por ejemplo, un usuario podría incrementar su puntuación en uno cuando inicia una sesión en cualquier aplicación o realiza un evento personalizado (como registrarse o unirse a un seminario web). 

![Grupo de acciones para añadir un punto con los desencadenantes de "Iniciar sesión en cualquier aplicación" y "Realizar evento personalizado".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Paso 4d: Paso de actualización de usuario

Añada un paso de Actualización de Usuario a cada ruta Canvas creada debajo de su Ruta de Acción. 

![Canvas que muestra la ruta de acción con rutas de actualización de usuario ramificadas para cada grupo de acción.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
En la pestaña **Redactar** de cada paso de Actualización de usuario, haga lo siguiente para los campos respectivos:

| Campo | Acción |
| --- | --- |
| **Nombre del atributo** | Seleccione el atributo de puntuación de clientes potenciales que seleccionó en el paso 2 (`lead score`).|
| **Acción** | Cambia la acción a **Aumentar por** si el camino aumenta la puntuación o **Disminuir por** si el camino disminuye la puntuación. |
| **Incrementar por** o **Disminuir por** | Introduzca el número de puntos que se aumentarán o disminuirán de la puntuación principal.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Lanza tu Canvas

Eso es todo. Su lienzo de puntuación de clientes potenciales está listo para lanzarse.

## Calificación externa de clientes potenciales

Ya sea utilizando uno de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/), su propio modelo interno de puntuación de clientes potenciales, aprendizaje automático u otra herramienta de puntuación de clientes potenciales, tenemos múltiples opciones para usted.

### Socios externos

Consulta [Socios tecnológicos]({{site.baseurl}}/partners/home) para conocer a nuestros socios B2B que ofrecen funciones de puntuación de clientes potenciales. ¿No ves tu herramienta? Puedes realizar la integración llamando a nuestro punto final de la API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users). 

### Modelos de datos internos de puntuación de clientes potenciales

Puede integrar Braze con sus modelos de datos internos, incluidos los modelos de puntuación de clientes potenciales, de varias maneras. Vea a continuación algunos ejemplos comunes de cómo nuestros clientes se han integrado con Braze.

#### Almacén de datos en la nube integrado

{% tabs %}
{% tab Braze como fuente de datos %}

Como herramienta de marketing, Braze contiene datos extremadamente relevantes que podrían complementar el modelo interno de puntuación de clientes potenciales de su equipo. 

Por ejemplo, los datos de participación en la mensajería (como aperturas y clics de correos electrónicos, participación en la página de destino y otros) pueden determinar el nivel de participación de un cliente potencial. Puede devolver estos datos a su almacén de datos en la nube y hacer que estén disponibles como entrada para sus modelos de puntuación de clientes potenciales utilizando las soluciones de exportación de datos en flujo Braze:

- [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Intercambio seguro de datos Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze como destino %}

Después de que sus equipos internos hayan creado y ejecutado su modelo de puntuación de clientes potenciales, puede volver a introducir esos datos en Braze para poder segmentar y dirigir mejor a los clientes potenciales los mensajes pertinentes. Puedes hacerlo con [la Ingesta de datos en la nube Braze]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

Con Cloud Data Ingestion, sus equipos internos crearán una nueva tabla o vista con sus identificadores de usuario, las últimas puntuaciones de clientes potenciales y las marcas de tiempo en las que se actualizaron las puntuaciones. Braze recogerá la tabla o vista y añadirá las puntuaciones de los clientes potenciales a los perfiles de usuario.

{% endtab %}
{% endtabs %}

## Transición de clientes potenciales: De cliente potencial calificado por el equipo de marketing (MQL) a las ventas{#lead-handoff}

Nuestro enfoque recomendado para los traspasos de clientes potenciales es tener un cliente potencial o contacto correspondiente vinculado a cada usuario en Braze. Estos prospectos entrarían en la cola de sus equipos de ventas cuando sus estados de prospectos cambien a una etapa MQL, momento en el que Salesforce iniciaría un flujo de trabajo de asignación o enrutamiento de prospectos. 

Para actualizar el registro de clientes potenciales en Salesforce con el estado del cliente potencial desde Braze, recomendamos utilizar una plantilla de webhook activada.

### Paso 1: Crear una campaña webhook

### Paso 2: Configure su webhook

#### Paso 2a: Componer webhook

1. Asigne un nombre a su campaña webhook, como "Salesforce > Actualizar cliente potencial a MQL".

2. Introduzca la URL de su webhook en el formato {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. El ID de usuario de Braze de {% raw %}`{{$user_id}}}`{% endraw %} debe coincidir con su ID de contacto de Salesforce. Si no, utilice un alias en lugar de {% raw %}`{{$user_id}}}`{% endraw %}.

3. Actualice el **método HTTP** a **PATCH**.

4. Configure la carga útil para que sólo actualice el registro de clientes potenciales en Salesforce si la puntuación del cliente potencial supera el umbral predefinido. Consulte el ejemplo de cuerpo de solicitud a continuación para obtener una puntuación de cliente potencial superior a 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Incluya las siguientes cabeceras:

| Encabezado | Contenido |
| --- | --- |
| Autorización | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Para recuperar un token, [configura una aplicación conectada](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) para el flujo de credenciales de cliente OAuth 2.0 y, a continuación, utiliza Contenido conectado para recuperar el portador de Salesforce: <br><br>{% raw %}<code>{% connected_content <mem_d664afea-b595-417b-accb-0a485396cb13/>[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]_mem_amp_client_secret=[client_secret]_mem_amp_grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Webhook que se compone con una URL de webhook de Salesforce, método HTTP PATCH, cuerpo de solicitud de texto sin procesar y encabezados de solicitud.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Paso 2b: Programar envíos de webhooks

La campaña debe activarse cada vez que cambie la puntuación del usuario. Esta campaña se activará para cualquier usuario cuya puntuación cambie, pero sólo afectará a los usuarios que no sean actualmente un MQL y que hayan superado el umbral establecido en el paso anterior.

En el paso **Programar entrega**, seleccione lo siguiente:
- Un tipo de entrega **basado en la acción** 
- Una acción desencadenante de **Cambiar valor de atributo personalizado** con el nombre de su atributo de lead scoring y una acción de **cualquier nuevo valor**

#### Paso 2c: Identificar la audiencia objetivo

En el paso **Públicos objetivo**, incluya un filtro que excluya a los usuarios cuyo estado de cliente potencial ya esté en MQL o más allá, como "`lead_status` `is none of` `MQL`".

![Las opciones de orientación del webhook con el filtro de "lead_status" no es ninguna de "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Paso 3: Lanzar campaña

Seleccione **Lanzar** y observe cómo cambia el estado de sus clientes potenciales en Salesforce a medida que sus clientes cruzan el umbral de puntuación de clientes potenciales MQL.

