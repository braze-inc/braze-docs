---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Este artículo de referencia describe la asociación entre Braze y Certona, una solución de personalización omnicanal en tiempo real que ofrece personalización en todo el ciclo de vida del cliente. Utiliza Certona con el socio de contenido conectado Braze para insertar fácilmente recomendaciones de contenido en campañas multicanal."
page_type: partner
search_tag: Partner

---

# Certona

> La plataforma de Certona aporta personalización a todo el ciclo de vida del cliente. Desde campañas de correo electrónico altamente individualizadas hasta recomendaciones de productos basadas en aprendizaje automático, Certona le garantiza que está aprovechando el poder de la personalización.

_Esta integración está mantenida por Certona._

## Sobre la integración

La integración de Braze y Certona aprovecha las recomendaciones de productos de aprendizaje automático de Certona en las campañas Braze y Canvases a través de Connected Content.

## Requisitos previos

| Requisito| Descripción|
| ---| ---|
| [Cuenta Certona](https://manage.certona.com/) | Se necesita una cuenta Certona para beneficiarse de esta asociación. |
| [Punto final de la API REST de Certona](https://manage.certona.com/) | Este endpoint se utiliza directamente en su mensaje de campaña Braze para extraer contenido recomendado basado en el ID de usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Utilice la API REST de Certona para insertar contenido personalizado en sus mensajes. Para ello, añada la siguiente plantilla de contenido conectado al compositor de mensajes Braze junto con el punto final de la API REST de Certona.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

A continuación, define el contenido que deseas llamar, como texto o imágenes relevantes. Por ejemplo, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Una imagen de una campaña push con Contenido Conectado relacionado con Certona incluido en el cuerpo del mensaje.]({% image_buster /assets/img/certona.png %})

Una vez que hayas puesto este mensaje en el cuerpo del compositor, previsualiza tu llamada a Contenido Conectado para asegurarte de que has mostrado la información correcta.

![Una imagen que muestra la pestaña "Prueba", animando a los usuarios a probar a fondo su mensaje antes de enviarlo.]({% image_buster /assets/img/certona2.png %})


