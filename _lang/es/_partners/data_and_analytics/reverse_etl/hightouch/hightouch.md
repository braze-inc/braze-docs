---
nav_title: Hightouch
article_title: Hightouch
description: "Este artículo de referencia describe la asociación entre Braze y Hightouch, una plataforma para sincronizar los datos de sus clientes desde su almacén a las herramientas empresariales."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) es una moderna plataforma de integración de datos que le permite sincronizar datos de clientes, productos o propietarios desde su almacén o lago de datos a cualquier aplicación de su elección, todo ello sin ayuda de sus equipos de TI o ingeniería.

La integración de Braze y Hightouch le permite crear mejores campañas en Braze con datos de clientes actualizados procedentes de su almacén de datos. Al sincronizar automáticamente los datos de los clientes en Braze, ya no tendrá que preocuparse por la coherencia de los datos y podrá centrarse en crear experiencias de cliente de primera clase. 

Esta integración también le permite [importar cohortes de usuarios a Braze]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/), enviando campañas específicas basadas en datos que sólo pueden existir en su almacén.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Hightouch | Se necesita una cuenta Hightouch para beneficiarse de esta asociación.
| Clave REST API de Braze | Una clave de API REST Braze con permisos `users.track` y `users.export.ids`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).<br><br>Hightouch necesita el nombre del clúster en el que se encuentra su instancia de Braze. Por ejemplo, si tu punto final Braze es `https://rest.iad-01.braze.com`, sólo necesitas `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

* Sincronice datos sobre usuarios y cuentas en Braze para crear campañas hiperpersonalizadas.
* Actualice automáticamente sus segmentos Braze con datos frescos de su almacén.
* Ofrezca mejores experiencias incorporando a Braze datos de otros puntos de contacto con el cliente.
* Importe cohortes de usuarios a Braze, lo que le permitirá enviar campañas dirigidas y Canvases. 

## Integración

### Paso 1: Crea tu destino Hightouch Braze

1. En la plataforma Hightouch, en la sección **Destinos**, haz clic en **Añadir destino**.
2. Seleccione **Braze** en la lista de destinos disponibles.
3. Proporciona tu punto final REST Braze (excluyendo "https://rest.") y tu clave de API REST Braze.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### Paso 2: Sincronización de objetos y eventos

Hightouch permite sincronizar tanto objetos de usuario como eventos.

| Destino | Descripción | Modos admitidos |
|---|---|---|
| Objeto | Sincroniza los registros con objetos como usuarios u organizaciones en el destino.| Volver a insertar o actualizar |
| Eventos | Sincroniza los registros como eventos con tu destino; esto suele hacerse en forma de llamada de seguimiento. | Seguimiento de eventos o seguimiento de compras |

{% alert note %}
Consulte [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) para obtener más información sobre cómo afectan las sincronizaciones al consumo de puntos de datos Braze.
{% endalert %}

#### Sincronización de objetos Braze

Puede sincronizar objetos Hightouch (campos de usuario) con los campos predeterminados o personalizados equivalentes de Braze. También puede realizar la correspondencia de registros para ayudar a unificar los datos en las dos plataformas.

#### Sincronización de eventos Braze

Hightouch permite realizar un seguimiento de los datos de eventos y compras y sincronizarlos con Braze. En Hightouch se pueden configurar varias opciones que afectarán al comportamiento de la sincronización, como la configuración de los datos de seguimiento y la definición de un comportamiento de usuario inexistente.

{% alert important %}
Encontrará más instrucciones sobre la sincronización de objetos y eventos en [la documentación de Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demostración de integración

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


