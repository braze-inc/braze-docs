---
nav_title: Clarisights
article_title: Clarisights
description: "Este artículo de referencia describe la asociación entre Braze y Clarisights, una plataforma de informes de marketing de rendimiento de autoservicio, que permite importar datos de campañas Braze y Canvases para ayudar a conseguir una interfaz de informes unificada de marketing de rendimiento y CRM/retención."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com) es una plataforma autoservicio de informes de marketing del rendimiento para organizaciones basadas en datos. Integra, procesa y visualiza automáticamente todos sus datos procedentes de fuentes de marketing, analíticas y de atribución.

_Esta integración está mantenida por Clarisights._

## Sobre la integración

La integración de Braze y Clarisights le permite importar datos de campañas Braze y Canvases para ayudarle a conseguir una interfaz de informes unificada de marketing de rendimiento y CRM/retención.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Clarisights | Se requiere un espacio de trabajo Clarisights para aprovechar esta asociación |
| Clave REST API de Braze | Una clave Braze REST API con los siguientes permisos:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Nombre del espacio de trabajo Braze | El nombre del espacio de trabajo asociado a la clave Braze API. Este nombre se utilizará para identificar la integración del espacio de trabajo en Clarisights. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Con la integración de Braze y Clarisights, los usuarios pueden crear diferentes visualizaciones y tablas para obtener información de las campañas que han creado. Algunos de los casos de uso más frecuentes son:

{% tabs %}
{% tab Mejor visibilidad %}
Mejor visibilidad del rendimiento global de las campañas y los lienzos.

![Un gráfico que muestra un ejemplo de mejor viabilidad en la plataforma Clarisights. Este gráfico incluye estadísticas de aperturas de campañas y Canvas, clics, envíos, conversiones, etc.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Informes detallados %}
Informes detallados para campañas y lienzos.

![Un gráfico que muestra informes granulares, como "total enviado por canal de envío" y "tasa de conversión".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Cuadros de mando unificados %}
Paneles unificados para CMO y CXO.

![Un gráfico que muestra un ejemplo de paneles unificados.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integración

Para sincronizar datos Braze con Clarisights, debes crear un conector Braze y conectar espacios de trabajo Braze.

1. En Clarisights, vaya a la página **Integraciones**, localice el conector **Braze** y seleccione **\+ Conectar**.<br>![Una lista de los conectores disponibles en el mercado de integraciones de Clarisights.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. A continuación, mediante el flujo de integración, conecta tu cuenta de Clarisights a Braze. Para ello, proporciona tu clave de API REST Braze, el nombre del espacio de trabajo Braze y el punto final REST Braze.<br>![Conector del espacio de trabajo Braze en la plataforma Clarisights. Esta página tiene campos para el nombre del espacio de trabajo Braze, la clave de API REST Braze y el punto final REST Braze.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Antes de que la integración se realice correctamente, los usuarios verán los espacios de trabajo conectados en la misma página.<br>![En "Cuentas Braze" encontrarás una lista de los espacios de trabajo conectados.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Mediante esta integración

Para incluir Braze como fuente de datos en sus informes Clarisights, vaya a **Crear nuevo informe**. Asigne un nombre a su informe y seleccione **Braze** como fuente de datos en el mensaje que aparece. También puede elegir las métricas y dimensiones que desea incluir en el informe. Cuando haya terminado, seleccione **Crear informe**. 

Los datos de Braze empezarán a fluir a partir de la siguiente importación de datos programada. Ponte en contacto con tu administrador del éxito del cliente de Clarisights para solicitar recambios de mayor duración. 

![La configuración del informe Clarisight muestra los campos de nombre y origen de datos. Para este ejemplo, se selecciona "Braze" como origen de datos.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Visite Clarisights para obtener más información sobre las [métricas y dimensiones](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) disponibles o la [creación de informes](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).


