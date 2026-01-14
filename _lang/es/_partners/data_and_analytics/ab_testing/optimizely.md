---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Este artículo de referencia describe la asociación entre Braze y Optimizely que te permite sincronizar tus segmentos de clientes, eventos y eventos Currents de Braze con la plataforma de datos de Optimizely."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) es una plataforma líder de experiencia digital que ofrece herramientas de experimentación y gestión de contenidos para productos digitales y campañas de marketing.

La integración de Braze y Optimizely es una integración bidireccional que te permite:

- Sincroniza tus segmentos y eventos de clientes Braze con la plataforma de datos Optimizely (ODP) cada noche para enriquecer los perfiles, informes y segmentación de clientes Optimizely.
- Envía eventos de Braze Currents desde Braze a la herramienta de informes de Optimizely.
- Sincroniza datos de clientes y eventos ODP con Braze para enriquecer tus datos de clientes Braze y desencadenar mensajería Braze basada en eventos de clientes en ODP.

## Requisitos previos

| Requisito                     | Descripción |
|----------------------------------|-------------|
| Cuenta de la Plataforma de Datos Optimizely | Se necesita una cuenta de la Plataforma de Datos Optimizely (ODP) para aprovechar esta asociación. |
| Clave de API REST de Braze               | Una clave de API REST Braze con los siguientes permisos: `users.track`,`users.export.segments`,`segments.list`,`campaigns.trigger.send`, y `canvas.trigger.send`. |
| Currents                         | Para volver a exportar datos a Optimizely, necesitas tener configurado Braze Currents en tu cuenta. |
| URL y token de Optimizely         | Esto se puede obtener navegando a tu panel de Optimizely y copiando la URL de ingestión y el token. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Configura la integración

1. En el **Directorio de Aplicaciones** de Optimizely Data Platform (ODP), selecciona la aplicación **Braze** y luego selecciona **Instalar aplicación**.
2. Ve a la pestaña **Configuración**. En la sección **Autorización**, haz lo siguiente:
    1. Introduce **la clave de API REST** de Braze.
    2. Selecciona la **URL de** tu **instancia de** Braze.
    2. Selecciona **Verificar clave de API**.
3. En Braze, ve a **[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**.
4. Selecciona **Crear nueva corriente** > **Exportar Currents personalizados**.
5. Configura las Corrientes utilizando el endpoint y el token proporcionados en ODP. Esto es necesario para sincronizar los eventos de Braze con ODP. 

![Autorización optimizada.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6\. En ODP, expande la sección **Segmentos** y selecciona segmentos específicos de la lista **Segmentos a sincronizar**, o selecciona **Importar todos los clientes** para sincronizar todos los segmentos.
7\. Añade los [mapeados de campo adicionales](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que quieras entre Braze y ODP.
8\. Seleccione **Guardar**.

![Optimizely Braze sincronización de segmentos.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Debes seleccionar segmentos para importar perfiles de clientes Braze. Si no seleccionas ningún segmento, la integración no importará ningún perfil de cliente.
{% endalert %}

### Paso 2: Campos de datos mapeados

La integración tiene mapeados predeterminados de campos de datos entre Braze y ODP. Por ejemplo, el campo **Correo electrónico** en Braze está mapeado al campo **Correo electrónico visto por última vez** en ODP.

![Campos de mapeado de segmentos Optimizely y Braze.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Mapear campos adicionales (opcional)

Si hay campos de datos adicionales en Braze que quieras mapear en ODP, haz lo siguiente en ODP:

1. En la sección **Segmentos** de la aplicación, selecciona el campo Braze de la lista desplegable **Campos de datos de usuario Braze**.
2. Selecciona el campo ODP de la lista desplegable **Campos de cliente ODP**.
3. Selecciona **Guardar mapa de campo**.

![Optimizely Braze Segmento Guardar Mapas de Campo]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Borrar mapeados de campos no obligatorios (opcional)

También puedes eliminar los mapeados de campos de datos que no sean necesarios. Haz lo siguiente en ODP:

1. En la sección **Segmentos** de la aplicación, selecciona el mapeado de campos que quieras eliminar de la lista desplegable **Mapa de campos**.
2. Selecciona **Eliminar mapa de campos**.

![Optimizely Braze Segmento Eliminar Mapas de Campo]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Paso 3: Sincronizar datos de la Plataforma de Datos Optimizely (ODP) con Braze

Después de configurar la integración, puedes establecer una activación en ODP para sincronizar tus datos de clientes de ODP con Braze.

1. Ve a **Activación** > **Interacción** y selecciona **Crear nueva campaña**.
2. Selecciona **Comportamiento** para configurar una sincronización automatizada y recurrente.
3. Selecciona **Crear desde cero** y, a continuación, introduce un nombre para tu activación que represente los datos que vas a sincronizar con Braze (como **Sincronización de datos Braze**).
4. En la sección **Inscripción**, puedes sincronizar los datos de los clientes que coincidan con un segmento o sincronizar los datos de los clientes que desencadenen un evento (como cuando ODP registra que un cliente abre un correo electrónico):
   - **Clientes que coinciden con un segmento:** Selecciona el segmento que desees y, a continuación, selecciona **Siguiente**.<br><br>![Optimizely Selecciona Segmento]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Clientes que desencadenan un evento:** Despliega la lista desplegable **Filtrar** y selecciona el evento ODP que se va a utilizar como desencadenante de esta sincronización de datos con Braze. A continuación, expande **Reglas de automatización** y ajústalas como desees. <br><br>![Evento desencadenante Optimizely]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Despliega **Puntos de intervención**, selecciona para editar **el Punto de intervención 1** y, a continuación, selecciona **Braze**.
6. Despliega la sección **Destino** y, a continuación, selecciona el **Identificador de destino**.
7. Selecciona una de las siguientes opciones para **Añadir usuarios a** en la sección **Configurar**:
    - **Campaña:** Añade clientes a una campaña específica en Braze. Después de elegir esta opción, debes seleccionar la campaña Braze.
    - **Canvas:** Añade clientes a un Canvas específico en Braze. Tras elegir esta opción, debes seleccionar el lienzo Braze.
    - **Sólo actualización de perfil:** Actualiza sólo el perfil de cliente Braze.
8. (Opcional) Selecciona el **Número de campos adicionales** que quieres sincronizar con Braze (hasta 20).  
    A continuación, selecciona lo siguiente para cada lista desplegable de campo adicional y campo de entrada que:
    - En cada lista desplegable **Campo #**, selecciona el campo Braze que quieras rellenar. 
    - En cada **Valor # de campo** correspondiente, introduce el campo ODP que quieres enviar al campo Braze seleccionado. Por ejemplo, si seleccionaste **Nombre de la empresa** en la lista desplegable **Campo nº**, introduce `{{customer.company_name}}` para el correspondiente **Valor de campo nº**.
9. Selecciona **Guardar** y, a continuación, selecciona tu nombre de activación en la ruta de migas de pan.
10. Selecciona **Seleccionar hora de inicio y horario** en la sección **Puntos de contacto** si has seleccionado **Clientes que coinciden con un segmento** para la inscripción.
11. Completa la siguiente configuración:
    - **Recurrente o Continuo:** Selecciona **Recurrente**.
    - **Fecha de inicio:** Introduce la fecha en la que quieres enviar los datos a Braze.
    - **De extremo a extremo:** Predeterminado a **Nunca**. Si quieres finalizar la sincronización de datos Braze en una fecha concreta, establécelo aquí.
    - **Repite:** Ajústalo a **Diario**.
    - **Repetir cada** \- Fijar en **1 día**.
    - **Horario:** Introduce la hora a la que quieres enviar los datos a Braze.
    - **Zona horaria:** Selecciona la zona horaria en la que quieres enviar estos datos.
12. Selecciona **Aplicar**, **Guardar** y, a continuación, **Ir en vivo**. Tu sincronización comienza en la fecha y hora de inicio que designes (o cuando se produzca el evento desencadenante).

## Solución de problemas

### Inspecciona los eventos

Para verificar que los datos se sincronizan correctamente desde ODP a Braze, puedes inspeccionar los eventos en ODP.

1. En ODP, ve a **Configuración de la cuenta** > **Inspector de Eventos**.
2. Selecciona **Iniciar Inspector**.
3. Cuando hay datos disponibles en el inspector, aparece un número junto a **Actualizar**. Selecciona para ver los datos.
4. Se muestran los datos en bruto que ODP y Braze envían de un lado a otro. Selecciona **Ver detalles** para ver la versión formateada de esos datos brutos.
5. Los campos de datos enviados desde Braze a ODP empiezan por `_braze`.

### Comprueba los registros de actividad

Cada sincronización de datos también se registra en el [registro de actividad de ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Ve a **Configuración de la cuenta** > **Registro de actividad**.
2. Filtra las categorías por **Braze**.
3. Selecciona **Ver detalles** para obtener una vista formateada de los detalles del registro, incluido el número de coincidencias.

