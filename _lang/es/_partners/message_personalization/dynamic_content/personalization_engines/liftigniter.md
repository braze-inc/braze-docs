---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "Este artículo de referencia describe la asociación entre Braze y LiftIgniter, una plataforma de personalización líder, que ayuda a las empresas a transformar la experiencia del cliente."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter es una plataforma de personalización líder que ayuda a las empresas a transformar la experiencia de sus clientes mediante la personalización en tiempo real en todos los puntos de intervención.

_Esta integración está mantenida por Liftigniter._

## Sobre la integración

La integración de LiftIgniter y Braze aprovecha el contenido conectado para permitirte recomendar temas interesantes como artículos de noticias, ropa y otros artículos y videos de comercio minorista.

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
| Cuenta LiftIgniter | Se requiere una [cuenta de LiftIgniter](https://console.liftigniter.com/login) para beneficiarse de esta asociación. |
| Integración API Liftigniter | Debes [integrar](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter en tu sitio o aplicación para poder extraer recomendaciones de allí. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

Utiliza [la API REST de LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) para insertar contenido personalizado en tus mensajes. Cuando tengas tu cuenta de LiftIgniter y LiftIgniter esté integrado en tu aplicación, añade la siguiente plantilla a tu creador de mensajes para llamar al contenido de tus mensajes, sustituyendo la información según sea necesario (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

A continuación, escribe tu mensaje, definiendo el contenido que deseas llamar con JSON. Por ejemplo, `{{json.items[0].title}}`.

{% endraw %}

![Una imagen que muestra una campaña push que incluye llamadas a contenido conectado específicas de LiftIgniter. También se ha añadido lógica de Contenido conectado al campo de imagen.]({% image_buster /assets/img/liftigniter.png %})

Una vez que hayas colocado este mensaje en el cuerpo del compositor, podrás previsualizar tu mensaje. Incluso puedes introducir imágenes, como se muestra en el siguiente ejemplo:

![Una vista previa del aspecto que tendrá el mensaje una vez enviado.]({% image_buster /assets/img/liftigniter2.png %})


