---
nav_title: Scuba
article_title: Análisis de buceo
description: "Esta referencia técnica de Scuba y Braze describe cómo activar la información de datos en tiempo real de Scuba mediante Segmentos Braze."
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Análisis de buceo

>[Scuba Analytics](https://scuba.io) es una plataforma de colaboración de datos completa, impulsada por el aprendizaje automático y diseñada para datos de series temporales de alta velocidad. Scuba le permite exportar selectivamente usuarios (también llamados actores) y cargarlos en su plataforma Braze. En Scuba, las propiedades de actor personalizadas se utilizan para analizar tendencias de comportamiento, activar sus datos en varias plataformas y realizar modelos predictivos mediante aprendizaje automático.

_Esta integración es mantenida por Scuba Analytics._

## Requisitos previos

Para utilizar Scuba Analytics con Braze, necesitarás lo siguiente:

| Requisito | Descripción |
|---|---|
|Token API de Scuba | Un token de la API de Scuba que puedes recuperar del punto final `https://{scuba_hostname}/api/create_token`. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia](https://scuba.io). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Carga de datos de buceo en Braze

{% alert important %}
La siguiente petición utiliza curl. Para gestionar mejor las solicitudes de API, te recomendamos que utilices un cliente de API, como Postman.
{% endalert %}

Para cargar tus datos de Scuba en Braze, haz una petición POST a `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` utilizando el tipo de contenido `application/json`:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

Sustituye lo siguiente:

| Marcador de posición             | Descripción                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | La URL del punto final REST de Braze de tu instancia de Braze actual. Para más información, consulta [Claves de API REST]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Tu clave de API REST Braze con el permiso `users.track`.                                                                                                                                      |
| `HOSTNAME`              | El nombre de host de su instancia actual de Scuba.                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Su token de la API de Scuba.                                                                                                                                                                           |
| `TABLE_NAME`            | La tabla a la que pertenece su conjunto de datos. Para más información, consulta [Glosario: Tabla de conjuntos de datos](https://docs.scuba.io/glossary/dataset-table).                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | La propiedad de actor a la que pertenece su conjunto de datos. Sólo se devolverán los datos que coincidan con este nombre. Para más información, consulta [Glosario: Propiedad del actor](https://docs.scuba.io/glossary/actor-property).                                             |
| `ACTOR_PROPERTY_FILTER` | El filtro de búsqueda de audiencia para su propiedad de actor.                                                                                                                                             |
| `ACTOR_ID`              | El ID de la propiedad de actor a la que pertenece su conjunto de datos. Esta identificación coincide con tu `external_id` en Braze. Para más información, consulta [Glosario: Actor](https://docs.scuba.io/glossary/actor).                                              |
| `PERIOD_START`          | El periodo de inicio como fecha compatible con BQL. Para más información, consulta [Sintaxis y uso de BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                 |
| `PERIOD_END`            | El periodo final como fecha compatible con BQL. Para más información, consulta [Sintaxis y uso de BQL](https://docs.scuba.io/guides/bql-syntax-and-usage).                                                                                                   |
| `RECORD_LIMIT`          | **Opcional**: El número máximo de registros a devolver. Si se omite `scuba_record_limit`, Scuba devolverá un máximo de 100 registros. Para cambiar esto, asigna cualquier número no negativo a `scuba_record_limit`.    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comportamiento por defecto

Por defecto, `update_existing_only` está configurado en `false`, lo que actualizará sus registros existentes en Braze, así como creará nuevos registros para aquellos que no existan. Para evitar que Scuba cree nuevos registros, configura `update_existing_only` en `true`.

### Límite de velocidad

Scuba aplica un límite de velocidad de 50.000 peticiones por minuto a este punto final.

## Creación de segmentos utilizando los datos de comportamiento de Scuba

Después de [cargar sus datos](#uploading-your-scuba-data-to-braze), puede crear segmentos de usuarios en Braze utilizando los datos de comportamiento de Scuba.

### Paso 1: Crear un nuevo segmento

En Braze, vaya a **Audiencia** > **Segmentos**, seleccione **Crear segmento** e introduzca un nombre para su segmento.

![Creación de un nuevo segmento en Braze.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### Paso 2: Busque y seleccione el atributo Scuba

En **Detalles del segmento** > **Filtros**, seleccione **Atributos personalizados**.

![Seleccionando el filtro "Atributo personalizado" en "Detalles del segmento".]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

Seleccione **Buscar atributos personalizados** y, a continuación, elija el nombre de la propiedad del actor que utilizó en su solicitud POST anterior.

![Selección de la propiedad del actor como atributo personalizado.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### Paso 3: Configurar el atributo

Junto al nombre de la propiedad del actor, elija un operador y un valor (si procede). Estos valores están determinados por las propiedades del actor que ha definido en Scuba. Cuando haya terminado, seleccione **Guardar**.

![Elegir un funcionamiento y un valor para el ] seleccionado ({% image_buster /assets/img/scuba/analytics/operator_end.png %})


