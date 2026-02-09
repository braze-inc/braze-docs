---
nav_title: Amplitude
article_title: Importación de cohortes de Amplitude
description: "Este artículo de referencia describe las funciones de importación de cohortes de Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
search_tag: Partner
---

# Importación de cohortes de Amplitude

> Este artículo explica cómo importar cohortes de usuarios de [Amplitude](https://amplitude.com/) a Braze. Para más información sobre la integración de Amplitude y sus otras funcionalidades, consulta el [artículo principal de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integración de importación de datos

Cualquier integración que establezca contará para el volumen de puntos de datos de su cuenta.

### Paso 1: Obtener la clave de importación de datos Braze

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Amplitude**. Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. 

Una vez generada, puede crear una nueva clave o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso al configurar un postback en el dashboard de Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Paso 2: Configurar la integración Braze en Amplitude

En Amplitude, ve a **Fuentes & Destinos** > **[nombre del proyecto]** > **Destinos** > Braze. En el mensaje que aparece, proporciona la clave de importación de datos Braze y el punto final REST, y haz clic en **Guardar**.

![]({% image_buster /assets/img/amplitude.png %})

### Paso 3: Exportar una cohorte de amplitud a Braze

En primer lugar, para exportar usuarios de Amplitude a Braze, crea una [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) de usuarios que desees exportar. Amplitude puede sincronizar cohortes con Braze utilizando los siguientes identificadores:
- Alias de usuario
- ID del dispositivo
- ID de usuario (ID externo)

Amplitude admite varias propiedades de mapeado de identificadores por orden de prioridad. Puedes configurar un mapeado de identificador primario, secundario y terciario. Durante la sincronización, si a un usuario le falta el primario, Amplitude utiliza el siguiente disponible. Esto mejora la cobertura de la sincronización, reduce los usuarios descartados e incluye más usuarios anónimos y parcialmente identificados en tu sincronización. 

Una vez que hayas creado una cohorte, haz clic en **Sincronizar con...** para exportar estos usuarios a Braze.

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

#### Definir la cadencia de sincronización

Las sincronizaciones de cohortes pueden configurarse para que se realicen una sola vez, programarse como diarias o cada hora, o incluso en tiempo real, que se actualiza cada minuto. 

Cualquier integración que configures registrará puntos de datos. Si tienes alguna pregunta sobre los matices de los puntos de datos Braze, tu administrador de cuentas Braze puede responderte.

### Paso 4: Segmentar usuarios en Braze

En Braze, para crear un segmento de estos usuarios, navega a **Segmentos** en **Interacción**, asigna un nombre a tu segmento y selecciona **Cohortes de Amplitude** como filtro. A continuación, utiliza la opción "includes" y elige la cohorte que creaste en Amplitude. 

![En el constructor de segmentos Braze, el filtro "amplitude_cohorts" está configurado en "includes_value" y "Prueba de cohorte de Amplitude".]({% image_buster /assets/img/amplitude2.png %})

Después de guardarlo, puede hacer referencia a este segmento durante la creación de Canvas o campañas en el paso de segmentación de usuarios.

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.
