---
nav_title: Amplitude y Connected Content
article_title: Amplitude y Connected Content
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "La API de perfiles de usuario de Amplitude sirve a los perfiles de usuario de Amplitude. Esto incluye propiedades de usuario, propiedades de usuario calculadas, una lista de ID de cohortes de cohortes que incluyen al usuario y recomendaciones."
search_tag: Partner

---

# Amplitude y Connected Content

> La API de perfiles de usuario de Amplitude sirve a los perfiles de usuario de Amplitude. Esto incluye propiedades de usuario, propiedades de usuario calculadas, una lista de ID de cohortes de cohortes que incluyen al usuario y recomendaciones. A continuación se enumeran los puntos finales comunes de la API de Amplitude que se pueden utilizar con el contenido conectado.

## Parámetros del punto final

La siguiente tabla muestra los parámetros que puede utilizar en sus llamadas a la API de perfil de usuario.

| Parámetro | Obligatorio | Descripción |
| --------- | -------- | ----------- |
| `user_id` | Opcional | Id. de usuario (id. de base de datos externa) que se va a consultar, obligatorio a menos que se establezca `device_id`. |
| `device_id` | Opcional | Id. del dispositivo (id. anónimo) que se va a consultar, obligatorio a menos que se establezca `user_id`. |
| `get_recs` | Opcional<br>(Falso por defecto) | Devuelve un resultado de recomendación para este usuario. |
| `rec_id` | Opcional | Recomendación(es) a recuperar, obligatorio si `get_recs` es true. Se pueden obtener varias recomendaciones separando `rec_ids` con comas. |
| `rec_type` | Opcional | Anula la configuración de control experimental por defecto y `rec_type=model` devolverá recomendaciones modeladas y `rec_type=random` devolverá recomendaciones aleatorias. Es posible que existan otras opciones en el futuro. |
| `get_amp_props` | Opcional<br>(Falso por defecto) | Devuelve un conjunto completo de propiedades de usuario para este usuario, sin incluir cálculos. |
| `get_cohort_ids` | Opcional<br>(Falso por defecto) | Devuelve una lista de todos los ID de cohorte de los que forma parte este usuario que se han configurado para ser rastreados. Por defecto, la pertenencia a una cohorte no se rastrea para los usuarios de ninguna cohorte. |
| `get_computations` | Opcional<br>(Falso por defecto) | Devuelve una lista de todos los cálculos habilitados para este usuario. |
| `comp_id` | Opcional | Devuelve un único cálculo que podría estar habilitado para este usuario. Devolverá un valor nulo si no existe. Si `get_computations` es verdadero, se obtendrán todos los valores, incluido éste (a menos que esté archivado o eliminado).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En la siguiente tabla se muestran los parámetros más habituales de las respuestas de Amplitude.

| Parámetro de respuesta | Descripción |
| ------------------ | ----------- |
| `rec_id` | El ID de recomendación solicitado. |
| `child_rec_id` | Un id de recomendación más detallado que Amplitude puede utilizar en el backend como parte de un experimento interno para mejorar el rendimiento del modelo. En la mayoría de los casos, será lo mismo que `rec_id`. |
| `items` | Lista de recomendaciones para este usuario. |
| `is_control` | true si este usuario forma parte del grupo de control. |
| `recommendation_source` | Nombre del modelo utilizado para generar esta recomendación |
| `last_updated` | Marca de tiempo de la última vez que se generó y sincronizó esta recomendación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Extremos comunes de amplitud

### Obtener una recomendación

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtener múltiples recomendaciones

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Obtener propiedades de usuario

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Obtener ID de cohorte

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Obtener un único cálculo

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Obtener todos los cálculos

#### Punto de conexión
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Ejemplo de respuesta
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

