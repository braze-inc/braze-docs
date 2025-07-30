---
nav_title: Ejemplos
article_title: Casos de uso de la transformación de datos Braze
page_order: 2
page_type: reference
description: "Este artículo de referencia proporciona algunos casos de uso de la transformación de datos Braze."
---

# Casos prácticos de transformación de datos

> Considere los siguientes casos de uso posibles con Braze Data Transformation y una combinación de webhooks de las plataformas externas de ejemplo.

## Generación de clientes potenciales

Usted aloja un formulario Typeform de generación de clientes potenciales en su sitio web. Cuando los nuevos usuarios rellenan este formulario, usted puede:
- Crear nuevos usuarios en Braze.
- Añádelos a una de tus listas de correo electrónico Braze.
- Sincroniza algunas de sus respuestas como atributos personalizados en Braze, ya que sus respuestas son valiosos datos de primera mano que pueden impulsar experiencias de mensajería personalizada para su uso futuro.

## Abrir tickets de servicio

Cuando los clientes abren tickets de servicio al cliente en una plataforma como Zendesk, puedes:
- Escribe un evento personalizado en Braze cuando se crea un ticket de Zendesk.
- Escriba un evento personalizado con propiedades de evento en Braze cuando se proporcione una calificación CSAT negativa a Zendesk.

## Integración con Braze

Braze tiene una integración con [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/), una plataforma de información y cuestionarios para clientes. Con Transformación de datos, puede guardar varias respuestas de encuesta en un atributo personalizado anidado, en lugar de en la integración existente que guarda varios atributos personalizados.

## Ejemplo de código de transformación

Considere esta carga útil de muestra de Typeform, una plataforma de encuestas, que se envía cada vez que se recibe una respuesta a una encuesta.

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformación básica %}

Este ejemplo toma las respuestas del cuestionario como atributos y escribe un evento para indicar que se ha completado el cuestionario:

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Transformación avanzada %}

Desarrollemos aún más el ejemplo básico de transformación e introduzcamos una declaración `if` para clasificar al usuario en una de las respuestas.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}