---
nav_title: Sólo palabras
article_title: Sólo palabras
description: "Este artículo de referencia describe la asociación entre Braze y Just Words, una plataforma empresarial SaaS basada en IA que crea versiones personalizadas de las campañas existentes y optimiza las líneas del asunto, el contenido creativo y los diseños de correo electrónico HTML a lo largo del tiempo."
alias: /partners/just_words/
page_type: partner
---

# Guía de integración de Just Words

> [Just Words](https://www.justwords.ai/) hiperpersonaliza la mensajería a escala en los canales de marketing del ciclo de vida, permitiéndote probar dinámicamente cientos de variaciones y actualizar automáticamente el contenido de bajo rendimiento.

Cuando utilices Just Words con [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) Braze para personalizar tus campañas y lienzos Braze existentes, Just Words utilizará Braze Currents para optimizar el contenido dinámicamente, para que no tengas que hacerlo tú.

## ¿Cuáles son los beneficios?

Una vez completada tu integración, puedes aprovechar la plataforma de Just Works para:

- Ver los resultados del experimento en tiempo real
- Edita dinámicamente la copia
- Ver información sobre el rendimiento

{% alert note %}
¿Preguntas? Ponte en contacto con Just Words en su [página de reservas](https://www.justwords.ai/book-demo) o a través del canal compartido de Slack.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Sólo Palabras | Se necesita una cuenta [Just Words](https://www.justwords.ai/) para beneficiarse de esta asociación. Si no tienes una cuenta de Just Words, [programa una llamada de incorporación de 30 minutos](https://www.justwords.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de Just Words con Braze

### Paso 1: Crear una plantilla de Just Words

1. Ve a tu consola de Just Words y [crea una nueva plantilla](https://console.justwords.ai/new).
2. Elige un ID fácil de recordar que utilice sólo letras, números y guiones bajos.
3. Rellena los datos básicos de la campaña.
4. Utiliza la IA para generar variaciones personalizadas.

![La plataforma de creación de plantillas Just Words.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Paso 2: Crear una clave de API de Just Words

1. Ve a **Configuración de la organización** > **Claves de API** > **Generar clave de API**.
2. Copia y guarda la clave de API en una ubicación segura.

![El formulario de la clave de API de Just Words.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Paso 3: Utiliza Just Words en tu contenido Braze

Just Words trabaja con Lienzos y campañas utilizando Contenido conectado. Si estás creando un Canvas, cada paso en correo electrónico debe corresponder a una plantilla única de Just Words.

#### Paso 3.1: Configura tu prueba A/B

{% tabs %}
{% tab Canvas %}

1. En un Canvas, selecciona **Añadir variante** > **Añadir variante** hasta que tengas el número de variantes que desees, y añade pasos a cada variante (como un paso de Mensaje por correo electrónico).
2. Divide el tráfico de audiencia como desees. Por ejemplo, si tienes dos variantes, podrías dar a cada una el 50%. O podrías tener dos variantes con un 40% cada una y un grupo de control con un 20%. Para más información sobre las pruebas A/B para Canvas, consulta [Crear un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. En los creadores de mensajes que quieras utilizar con el contenido conectado, pega el fragmento de código de contenido conectado de la consola de Just Words, como el siguiente fragmento de código.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuración de la prueba A/B Canvas de Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaña %}

1. En el paso **Redactar mensajes** de tu campaña, crea dos variantes.
2. En el paso **Audiencia objetivo**, ve a la sección **Pruebas A/B** y modifica los porcentajes de usuarios que recibirán cada una de tus variantes (y tu grupo de control opcional). Puedes personalizar aún más tu prueba seleccionando una opción de optimización. Para obtener más información sobre las pruebas A/B para campañas, consulta [Crear pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. En el creador de mensajes, pega el fragmento de código Contenido conectado de la consola de Just Words, como el siguiente fragmento.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Paso 3.2:  Añade personalización con atributos personalizados (opcional)

Para personalizar tus mensajes con atributos personalizados (como `industry`), utiliza el siguiente formato de Liquid:

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Nota que el atributo personalizado de `industry` se indica con {% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %}. 

![Lógica Braze Liquid en un creador de mensajes HTML.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Paso 4: Vista previa del correo electrónico

Asegúrate de previsualizar el correo electrónico en Braze para confirmar que el contenido personalizado se muestra correctamente.

![Vista previa del mensaje Braze para un correo electrónico de Just Words.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Paso 5: Configurar Braze Currents

Braze Currents habilita el seguimiento y la optimización del rendimiento a lo largo del tiempo.

1. En Braze, ve a **Integraciones de socios** > **Exportación de datos**.
2. Selecciona **Crear nueva corriente de prueba** y, a continuación, **Exportación de datos de prueba de Amazon S3**.

!["Crear nueva corriente de prueba" desplegable con la opción de "Prueba de exportación de datos de Amazon S3".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\. Introduce el ID de acceso a AWS S3, la clave de acceso secreta de AWS, el nombre de contenedor y la carpeta que te proporcionó Just Words durante la incorporación.

![Sección "Credenciales" para la clave de acceso secreta de AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\. Selecciona los eventos de seguimiento, como envíos, aperturas, clics, cancelaciones de suscripción, conversiones y otros.

![Sección "Eventos de interacción con mensajes" con eventos para seleccionar.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\. Lanza la Corriente Braze.

¡Ya está todo listo! Ahora puedes utilizar Just Words con el contenido conectado Braze.