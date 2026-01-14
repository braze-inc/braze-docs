---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Este artículo de referencia describe la asociación entre Braze y Amplitude, una plataforma de análisis de productos e inteligencia empresarial."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/) es una plataforma de análisis de productos e inteligencia empresarial.

La integración bidireccional de Braze y Amplitude te permite [importar tus Cohortes de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), rasgos de usuario y eventos a Braze, así como crear segmentos que pueden dirigirse a los usuarios en futuras campañas o Canvases. También puedes aprovechar Braze Currents para [exportar tus eventos Braze a Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) y realizar análisis más profundos de tus datos de producto y marketing.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta de amplitud | Se necesita una [cuenta de Amplitude](https://amplitude.com/) para beneficiarse de esta asociación. |
| Currents | Para poder exportar los datos a Amplitude, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Elige una integración 

Amplitude y Braze ofrecen dos métodos de integración diferentes. Lee la documentación siguiente para decidir qué métodos se ajustan a tus necesidades:

- Retransmisión en streaming del evento Braze: Una integración que te permite enviar datos de eventos de Amplitude sin procesar directamente a Braze.
- [Importación de cohortes]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/): Una integración que permite reenviar cohortes de Amplitude a Braze.

## Retransmisión en streaming de eventos Braze

### Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Clave de API REST de Braze | Una clave Braze REST API con todos los permisos.<br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [Tu URL del punto final REST][1]. Tu punto final dependerá de la URL Braze de tu instancia. |
| Identificador de la aplicación Braze | El identificador de la aplicación que recibirá los eventos de Amplitude. Esto se puede encontrar en el **panel de Braze > consola para desarrolladores > configuración.** |

### Configuración de Amplitude

1. En Amplitude, ve a **Destinos de datos** y busca "Braze - Flujo de eventos".
2. Introduce un nombre para la sincronización y haz clic en **Crear sincronización**.
3. Haz clic en **Editar** e indica tu punto final de la API REST de Braze, la clave de API REST y el identificador de la aplicación Braze.
4. Utiliza el filtro de envío de eventos para seleccionar los eventos que deseas enviar. Puedes enviar todos los eventos, pero Amplitude recomienda elegir los más importantes. 
5. Cuando hayas terminado, habilita el destino y guárdalo. 

Consulta [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) para obtener más información sobre esta integración.

## Sincronizar rasgos de usuario y cómputos

Utiliza Audiences para enviar propiedades de usuario y cálculos a Braze como atributos personalizados. Podrás sincronizar las propiedades de los usuarios o las propiedades computadas de los usuarios que hayan estado activos en los últimos 90 días.

Cuando se actualice una propiedad de usuario o un cálculo, Amplitude actualizará un atributo personalizado en Braze con el mismo nombre que esa propiedad de usuario o cálculo.

Las sincronizaciones de rasgos de usuario y computación crearán nuevos usuarios para identificadores de usuario que aún no existen en Braze. Las computadoras y los rasgos de usuario sólo pueden sincronizarse utilizando identificadores de usuario. Un identificador de usuario puede ser cualquiera de los siguientes:
- ID externo
- ID de Braze
- Alias de usuario
- Dirección de correo electrónico

Consulta la documentación de Amplitude para obtener más información sobre la [sincronización de propiedades, recomendaciones y cohortes con destinos de terceros](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Cómo sincronizar las propiedades y los cálculos de los usuarios

En Amplitude Audiences, selecciona **Sincronizaciones > Crear sincronización**.

![]({% image_buster /assets/img/amplitude11.png %})

A continuación, elige sincronizar una propiedad de usuario, una computación, una cohorte o una recomendación. 

{% tabs %}
{% tab Sincronización de las propiedades de los usuarios %}

Selecciona **Propiedad de usuario** y, a continuación, la propiedad de usuario que desees sincronizar.

![]({% image_buster /assets/img/amplitude7.png %})

A continuación, selecciona un destino con el que sincronizar tu propiedad de usuario.

![]({% image_buster /assets/img/amplitude8.png %})

Por último, define la frecuencia de tu sincronización.

![Define tu cadencia como sincronización única o sincronización programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Cálculo de sincronización %}

Selecciona **Cálculo** y, a continuación, el cálculo que desees sincronizar

![]({% image_buster /assets/img/amplitude10.png %})

A continuación, selecciona un destino para sincronizar tu cálculo.

![]({% image_buster /assets/img/amplitude8.png %})

Por último, define la frecuencia de tu sincronización.

![Define tu cadencia como sincronización única o sincronización programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Puntos finales de la API del perfil de usuario de Amplitude

Para comprobar algunos de los puntos finales comunes de la API de Amplitude que se pueden utilizar con el Contenido Conectado, consulta la [documentación sobre la API de Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).
