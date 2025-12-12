---
nav_title: Puntuación de clientes potenciales
article_title: Crear un flujo de trabajo de puntuación de clientes potenciales
page_order: 1
page_type: reference
description: "Aprende a utilizar Braze para realizar la puntuación simple de clientes potenciales, la puntuación externa de clientes potenciales y el traspaso de clientes potenciales."
---

# Crear un flujo de trabajo de puntuación de clientes potenciales

> Este caso de uso demuestra cómo puedes utilizar Braze para actualizar las puntuaciones de los usuarios potenciales en tiempo real y entregar automáticamente las oportunidades a tus equipos de Ventas.

Hay dos pasos clave para crear un flujo de trabajo de puntuación de clientes potenciales en Braze:

1. Crea un Canvas de puntuación de clientes potenciales en Braze o integra una herramienta externa de puntuación de clientes potenciales:
- [Puntuación sencilla de clientes potenciales](#simple-lead-scoring)
- [Puntuación externa de clientes potenciales](#external-lead-scoring)

2. Crea una campaña webhook para enviar clientes potenciales cualificados a tu equipo de Ventas:
- [Entrega del mando: De cliente potencial cualificado para marketing (MQL) a ventas](#lead-handoff)

## Puntuación sencilla de clientes potenciales

### Paso 1: Crea un Canvas

1. Ve a **Mensajería** > **Canvas** y selecciona **Crear Canvas**, y luego rellena los datos básicos de tu Canvas.

2. Dale a tu Canvas un nombre relevante, como "Lead Scoring Canvas" y, para facilitar su localización, etiquétalo con algo como "Lead Management".<br><br>Paso 1 de la creación de un Canvas con el nombre "Lead Scoring Canvas" y la etiqueta "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Paso 2: Configura tus criterios de entrada

1. Continúa con el paso **Programa de entrada** y selecciona un programa de entrada **basado en acciones**. Esto introducirá a los usuarios en el Canvas cuando realicen acciones específicas.

2. En **Opciones basadas en acciones**, añade estas dos acciones:
    - **Cambia el valor del atributo personalizado** por el nombre de tu atributo de puntuación de clientes potenciales (como `lead score`). Si aún no has creado un atributo de puntuación de clientes potenciales, sigue los pasos de [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). Esto introducirá a los usuarios en el Canvas siempre que cambie su puntuación de cliente potencial.
    - **Añadir una dirección de correo electrónico**

\![Paso 2 de la creación de un Canvas con el horario de entrada de "Basado en la acción" y las opciones basadas en la acción de cambiar un atributo personalizado "puntuación de clientes potenciales" y añadir una dirección de correo electrónico.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Paso 3: Identifica tu audiencia objetivo

#### Paso 3a: Seleccionar segmentos

Todos los usuarios son elegibles para la puntuación de clientes potenciales, así que puedes añadir reglas específicas de la empresa sobre a quién puntuar seleccionando a qué [segmentos de]({{site.baseurl}}/user_guide/engagement_tools/segments/) usuarios dirigirte y aplicando [filtros adicionales]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Por ejemplo, puedes excluir a empleados, usuarios que ya son clientes y similares. 

\![Paso 3 de la creación de un Canvas con opciones para seleccionar segmentos y filtros para acotar la audiencia de entrada.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Paso 3b: Configurar la reelegibilidad de Canvas

Un usuario pasará por este Canvas muchas veces a lo largo de su ciclo de vida contigo, así que asegúrate de que pueda volver a entrar tan rápido como salió la vez anterior. Esto puede conseguirse mediante la configuración de la re-elegibilidad. 

En **Controles de entrada**, haz lo siguiente:
- Selecciona **Permitir a los usuarios volver a entrar en este Canvas**.
- Selecciona **Ventana Especificada**.
- Establece la reelegibilidad en "0" **segundos**.

\!["Controles de entrada" sección que tiene selecciones para "Permitir a los usuarios volver a entrar en este Canvas" en una "Ventana especificada" de 0 segundos.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Paso 3c: Actualizar configuración de envío

Dada la naturaleza operativa de este Canvas y el hecho de que no se enviarán mensajes a estos usuarios, no es necesario que te atengas a los estados de suscripción.

En **Configuración de la suscripción**, para **Enviar a estos usuarios:** selecciona **todos los usuarios, incluidos los usuarios dados de baja**. 

\![Paso 4 de la creación de un Canvas para configurar las opciones de envío de mensajes.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Paso 4: Construye tu Canvas

#### Paso 4a: Añadir una ruta de acción

Bajo tu variante, selecciona el icono más y, a continuación, selecciona **Rutas de acción**.

\![Canvas con "Rutas de acción" en el menú que se abre con el icono más.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Paso 4b: Crear Grupos de Acción

Cada Grupo de Acciones representará todas las acciones que conduzcan al mismo incremento o decremento de puntos. Puedes configurar hasta ocho Grupos de Acción. En este escenario, configuraremos cuatro grupos.

Añade los siguientes grupos a tu Ruta de acción:

- **Grupo 1:** Todos los eventos que cuentan para un incremento de 1 punto.
- **Grupo 2:** Todos los eventos que cuentan para un incremento de 5 puntos.
- **Grupo 3:** Todos los eventos que cuentan para un decremento de 1 punto.
- **Todos los demás:** Las rutas de acción te permiten definir la ventana para esperar a ver si un usuario realiza una acción, antes de soltarlo en un grupo de "todos los demás". Para la puntuación de clientes potenciales, esta es una oportunidad para disminuir la puntuación por "inactividad".

\![Ruta de acción que contiene Grupos de Acción para sumar un punto, cinco puntos y diez puntos; restar un punto y diez puntos; y "Todos los demás".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Paso 4c: Configura cada grupo para incluir los eventos relevantes

En cada Grupo de Acciones, selecciona **Seleccionar desencadenante** y elige el evento que añadirá el número de puntos para ese Grupo de Acciones en concreto. Añade más desencadenantes para incluir todos los eventos que incrementarán en uno la puntuación de clientes potenciales. Por ejemplo, un usuario podría incrementar su puntuación en uno cuando inicie una sesión en cualquier aplicación o realice un evento personalizado (como registrarse o unirse a un seminario web). 

\![Grupo de acciones para añadir un punto con los desencadenantes de "Iniciar sesión en cualquier aplicación" y "Realizar evento personalizado".]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Paso 4d: Añadir usuario Pasos de actualización

Añade un paso de Actualización de usuario a cada ruta en Canvas creada debajo de tu Ruta de acción. 

\![Canvas que muestra la ruta de acción con rutas de actualización de usuario ramificadas para cada grupo de acción.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
En la pestaña **Componer** de cada paso de Actualización de Usuario, haz lo siguiente para los campos respectivos:

| Campo | Acción |
| --- | --- |
| **Nombre del atributo** | Selecciona el atributo de puntuación de clientes potenciales que seleccionaste en el paso 2 (`lead score`).|
| **Acción** | Cambia la acción a **Aumentar por** si la ruta aumenta la puntuación o **Disminuir por** si la ruta disminuye la puntuación |
| **Incrementar por** o **Disminuir por** | Introduce el número de puntos que se aumentarán o disminuirán de la puntuación principal.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Lanza tu Canvas

Eso es. Tu Canvas de puntuación de clientes potenciales está listo para lanzarse.

## Puntuación externa de clientes potenciales

Tanto si utilizas uno de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/), tu propio modelo interno de puntuación de clientes potenciales, aprendizaje automático u otra herramienta de puntuación de clientes potenciales, tenemos múltiples opciones para ti.

### Socios externos

Consulta [Socios tecnológicos]({{site.baseurl}}/partners/home) para conocer a nuestros socios B2B que ofrecen funciones de puntuación de clientes potenciales. ¿No ves ahí tu herramienta? Puedes realizar la integración llamando a nuestro punto final de la API [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API. 

### Modelos de datos internos de puntuación de clientes potenciales

Puedes integrar Braze con tus modelos de datos internos, incluidos los modelos de puntuación de clientes potenciales, de varias formas. Consulta a continuación algunos ejemplos comunes de cómo nuestros clientes se han integrado con Braze.

#### Almacén de datos en la nube integrado

{% tabs %}
{% tab Braze as a data source %}

Como herramienta de marketing, Braze contiene datos extremadamente relevantes que podrían complementar el modelo interno de puntuación de clientes potenciales de tu equipo. 

Por ejemplo, los datos de interacción de la mensajería (como aperturas y clics en el correo electrónico, participación en la página de destino y otros) pueden determinar el nivel de participación de un cliente potencial. Puedes devolver estos datos a tu almacén de datos en la nube y hacer que estén disponibles como entrada para tus modelos de puntuación de clientes potenciales utilizando las soluciones Braze de exportación de datos en streaming:

- [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Intercambio seguro de datos Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

Después de que tus equipos internos hayan creado y ejecutado tu modelo de puntuación de clientes potenciales, puedes volver a introducir esos datos en Braze para segmentar mejor y dirigirte a los clientes potenciales para enviarles mensajes relevantes. Puedes hacerlo con [la Ingesta de datos en la nube Braze]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

Con la ingesta de datos en la nube, tus equipos internos crearán una nueva tabla o vista con tus identificadores de usuario, las últimas puntuaciones de clientes potenciales y las marcas de tiempo en que se actualizaron las puntuaciones. Braze recogerá la tabla o vista y añadirá las puntuaciones de clientes potenciales a los perfiles de usuario.

{% endtab %}
{% endtabs %}

## Entrega del mando: De cliente potencial cualificado para marketing (MQL) a ventas {#lead-handoff}

Nuestro enfoque recomendado para los traspasos de clientes potenciales es tener un cliente potencial o contacto correspondiente vinculado a cada usuario en Braze. Estos clientes potenciales entrarían en la cola de tus equipos de ventas cuando sus estados de cliente potencial cambien a una etapa MQL, momento en el que Salesforce pondría en marcha un flujo de trabajo de enrutamiento o asignación de clientes potenciales. 

Para actualizar el registro de clientes potenciales en Salesforce con el estado del cliente potencial de Braze, te recomendamos que utilices una plantilla de webhook desencadenado.

### Paso 1: Crear una campaña webhook

### Paso 2: Configura tu webhook

#### Paso 2a: Componer webhook

1. Dale un nombre a tu campaña webhook, como "Salesforce > Actualizar cliente potencial a MQL".

2. Introduce la URL de tu webhook en el formato {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. El ID de usuario de Braze de {% raw %}`{{$user_id}}}`{% endraw %} debe coincidir con tu ID de contacto de Salesforce. Si no, utiliza un alias en lugar de {% raw %}`{{$user_id}}}`{% endraw %}.

3. Actualiza el **Método HTTP** a **PATCH**.

4. Configura tu carga útil para que sólo actualice el registro de clientes potenciales en Salesforce si la puntuación de ese cliente potencial supera tu umbral predefinido. Consulta el ejemplo de cuerpo de solicitud que aparece a continuación para obtener una puntuación de cliente potencial superior a 100.

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
5\. Incluye las siguientes cabeceras:

| Cabecera | Contenido |
| --- | --- |
| Autorización | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Para recuperar un token, [configura una aplicación conectada](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) para el flujo de credenciales de cliente OAuth 2.0 y, a continuación, utiliza Contenido conectado para recuperar el portador de Salesforce: <br><br>{% raw %}<code>{% connected_content https://[instancia].my.salesforce.com/servicios/oauth2/token <br>:method post <br> :cuerpo client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:guardar resultado %}{% endraw %} <br> Portador {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | aplicación/json |
{: .reset-td-br-1 reset-td-br-2}

\![Webhook que se compone con una URL de webhook de Salesforce, método HTTP PATCH, cuerpo de solicitud de texto sin procesar y encabezados de solicitud.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Paso 2b: Programar envíos de webhooks

La campaña debe desencadenarse cada vez que cambie la puntuación del usuario. Esta campaña se desencadenará para cualquier usuario cuya puntuación cambie, pero sólo afectará a los usuarios que no sean actualmente un MQL y hayan superado el umbral que estableciste en el paso anterior.

En el paso **Programar entrega**, selecciona lo siguiente:
- Un tipo de entrega **basada en acciones** 
- Una acción desencadenante de **Cambiar valor de atributo personalizado** con el nombre de tu atributo de puntuación de clientes potenciales y una acción de **cualquier nuevo valor**

#### Paso 2c: Identificar la audiencia objetivo

En el paso **Audiencias objetivo**, incluye un filtro que excluya a los usuarios cuyo estado de cliente potencial ya esté en MQL o más allá, como "`lead_status` `is none of` `MQL`".

\![Las opciones de orientación del webhook con el filtro de “lead_status” no es ninguna de "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Paso 3: Campaña de lanzamiento

Selecciona **Lanzar** y observa cómo cambia el estado de tus clientes potenciales en Salesforce a medida que cruzan el umbral de puntuación de clientes potenciales MQL.

