---
nav_title: API de personalización de Hightouch
article_title: API de personalización de Hightouch
description: "Este artículo de referencia describe la integración entre Braze y la API de personalización de Hightouch, un servicio gestionado para alojar una API de datos de baja latencia basada en cualquier conjunto de datos de su almacén de datos en la nube. Este artículo de referencia repasa los casos de uso que resuelve la API de personalización de Hightouch, los datos con los que trabaja, cómo configurarla y cómo integrarla con Braze."
page_type: partner
search_tag: Partner
---

# API de personalización de Hightouch

> [La API de personalización](https://hightouch.com/docs/destinations/personalization-api) de Hightouch es un servicio gestionado que le permite alojar una API de datos de baja latencia basada en cualquier conjunto de datos de su almacén de datos en la nube.

![]({% image_buster /assets/img/hightouch/cohort7.png %})

La integración de Braze y Hightouch le permite utilizar la API con [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para extraer datos actualizados de clientes u objetos en sus campañas o Canvases en el momento del envío.

La API de personalización de Hightouch proporciona un punto final REST para utilizar en la configuración de Braze. En concreto, puedes utilizar la oferta de contenido conectado Braze para realizar una solicitud GET a la API de personalización para recuperar toda la información relacionada con un identificador concreto. Los datos expuestos por esta API pueden representar datos de clientes, productos o cualquier otro objeto. 

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## Requisitos previos

| Requisito| Descripción|
| ---| ---| 
| [Cuenta Hightouch](https://app.hightouch.com/login) con la API de personalización activada | Se necesita una [cuenta de nivel empresarial](https://hightouch.com/pricing) de Hightouch para beneficiarse de esta asociación.|
| Casos de uso definidos | Antes de configurar la API, debes determinar tu caso de uso para esta integración. Consulte la siguiente lista de casos de uso comunes. |
| Datos almacenados en un almacén de datos en la nube u otra fuente | Hightouch se integra con [más de 25 fuentes de datos](https://hightouch.com/integrations) |
| Clave API de Hightouch | Puede crearse en **Hightouch > Configuración > Claves API > Añadir clave API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab casos de uso %}

### Ejemplos

Antes de empezar, es útil planificar exactamente cómo quieres utilizar la API de personalización.

Los casos de uso más comunes son:
- **Recomendaciones** de productos para agilizar la incorporación de recomendaciones de productos personalizadas en plantillas de correo electrónico, campañas o experiencias dentro de la aplicación.
- **Impulse campañas de marketing personalizadas** enriqueciendo los puntos de contacto de marketing con recomendaciones dinámicas de productos.
- **Ofrecer personalización en la aplicación o en la web**, por ejemplo, resultados de búsqueda personalizados, precios basados en cohortes y mensajería, recomendaciones de artículos o ubicaciones de las tiendas más cercanas.
- **Recomendaciones basadas en datos financieros o médicos: los**datos financieros tienen requisitos estrictos que Hightouch cumple mediante sus [estrictas políticas de seguridad de datos](https://hightouch.com/docs/security/overview#compliance). Con Hightouch, puede crear segmentos de clientes basados en datos financieros o médicos sin exponer los atributos subyacentes utilizados en sus criterios de segmentación.

{% endtab %}
{% tab Conjuntos de datos %}

### Conjuntos de datos

La Personalization API actúa como una caché para los datos seleccionados en su almacén, por lo que ya debería tener los datos de recomendación almacenados allí. Si es necesario, puedes utilizar Hightouch para transformarlo según una plantilla. Este tipo de datos incluye:
- metadatos del usuario, como región geográfica, edad u otra información demográfica
- Acciones o eventos del usuario, incluidas compras anteriores, páginas vistas, clics, etc.

{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Conectar fuente de datos a Hightouch

[Las fuentes](https://hightouch.com/docs/getting-started/concepts#sources) Hightouch son el lugar donde residen los datos empresariales de su organización. En este caso, es dondequiera que se almacenen los datos de sus usuarios.
1. En Hightouch, vaya a **Visión General de Fuentes > Añadir Fuente**. Seleccione su almacén de datos como fuente.<br><br>
2. Introduzca las credenciales pertinentes, que variarán en función de la fuente. 

Para más detalles, consulta la [documentación de](https://hightouch.com/docs) origen correspondiente.

### Paso 2: Datos del modelo

Los modelos Hightouch definen qué datos extraer de su fuente. Para configurar un nuevo modelo, sigue estos pasos:

1. En Hightouch, vaya a [**Resumen de modelos**](https://app.hightouch.com/models) > **Añadir modelo** y selecciona la fuente que acabas de conectar. <br><br>
2. A continuación, elija un [método de modelización](https://hightouch.com/docs/models/creating-models). Como toda la información debe estar unida en una tabla, puede utilizar el selector visual de tablas para definirla. Como alternativa, puede escribir SQL para incluir sólo las columnas que desee o basarse en sus modelos dbt, Looker Looks o libros de trabajo Sigma existentes.<br><br>
3. Antes de continuar, previsualiza tu modelo para asegurarte de que consulta los datos que te interesan. Por defecto, Braze limita la vista previa a los 100 primeros registros. Una vez validados los datos, haz clic en **Continuar**.<br><br>
4. Nombre su modelo, por ejemplo, "Recomendaciones de usuarios".<br><br>
5. Por último, seleccione una clave primaria y haga clic en **Finalizar**. Una clave primaria debe ser una columna con identificadores únicos. Este es también el campo que utilizará para llamar a la API de personalización para recuperar las recomendaciones de un usuario en particular.

### Paso 3: Configurar la API de personalización

Preparar la API para recibir peticiones tiene dos pasos:
- Habilitación de la API de personalización en las regiones más cercanas a su infraestructura
- Creación de sincronizaciones para definir qué modelos deben materializarse en la caché gestionada por Hightouch.

Siga estas instrucciones para completar ambos:

1. En Hightouch, vaya a [**Destinos**](https://app.hightouch.com/destinations) y seleccione la API de personalización de Hightouch creada para usted. Si no tiene habilitado este destino, póngase en contacto con [el servicio de asistencia de Hightouch](mailto:friends@hightouch.com).<br><br>
2. A continuación, seleccione la región adecuada. Seleccionar la región más cercana a su infraestructura reducirá sus tiempos de respuesta. Si no ve una región cercana a su infraestructura, póngase en contacto con [el servicio de asistencia de Hightouch](mailto:friends@hightouch.com).<br><br>
3. Vaya a la [página de resumen de**sincronizaciones**](https://app.hightouch.com/syncs) y haga clic en el botón **Añadir sincronización**. A continuación, seleccione el modelo correspondiente y el destino que haya configurado previamente.<br><br> 
4. Introduzca un nombre alfanumérico para la colección. Las colecciones son conceptualmente similares a las tablas de las bases de datos. Cada uno debe representar un tipo de datos concreto, como clientes o facturas. Los nombres de las colecciones deben ser alfanuméricos y formarán parte de su punto final de la API de personalización.<br><br>
5. A continuación, especifique qué columna de su modelo debe servir como índice primario para las búsquedas de registros. Este campo debe identificar de forma exclusiva cada registro de la colección y suele coincidir con la clave primaria de su modelo. La API de personalización admite búsquedas en varios índices. Por ejemplo, puede que quieras recuperar perfiles de clientes utilizando `user_id`, `anonymous_id`, o `email_address`. Para activar varios índices, póngase en contacto con [el servicio de asistencia de Hightouch](mailto:friends@hightouch.com).<br><br>
6. Utilice el mapeador de campos para especificar qué columnas de su modelo deben incluirse en la carga útil de la respuesta de la API. Puede cambiar el nombre de estos campos y utilizar el mapeador avanzado para aplicar transformaciones utilizando el lenguaje de plantillas Liquid.<br><br>
7. Seleccione el [comportamiento de eliminación](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) adecuado para su caso de uso.<br><br>
8. Por último, haz clic en **Continuar** y selecciona un [calendario de sincronización](https://hightouch.com/docs/syncs/schedule-sync-ui).

Hightouch sincronizará ahora los datos de su almacén con una base de datos gestionada y los expondrá a través de la API de personalización.

### Paso 4: Llama a la API de personalización a través del contenido conectado Braze

Una vez que haya configurado su instancia de API de personalización, puede utilizarla como un punto final de contenido conectado Braze. 

Se puede acceder a la API en `https://personalization.{region}.hightouch.com`, por ejemplo, `https://personalization.us-west-2.hightouch.com`. 

La información está disponible utilizando este punto final `/v1/collections/:collection_name/records/:index_key/:index_value`.

Por ejemplo, puede incluir este fragmento en una campaña o Canvas:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Puede utilizar la plantilla Liquid para hacer referencia a las propiedades devueltas en la carga JSON y utilizarlas en su mensajería.

Para el siguiente ejemplo de carga útil:

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

Las siguientes referencias de Liquid devolverían estos datos de ejemplo:

| Plantilla líquida | Ejemplo devuelto |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Lenguaje universal |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solución de problemas

Si tiene alguna pregunta, póngase en contacto con [el servicio de asistencia de Hightouch](mailto:friends@hightouch.com).

