---
nav_title: Tipos de mensajes
article_title: Tipos de mensajes LINE
page_order: 0
description: "Este artículo trata de los distintos tipos de mensajes de LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Tipos de mensajes LINE

> Este artículo cubre los tipos de mensajes de LINE que puedes componer, incluyendo aspectos y limitaciones.

Cuando redactas un mensaje de LINE, puedes arrastrar y soltar tipos de mensajes en el compositor y luego personalizarlos.

\![Panel de tipos de mensaje con tipos de mensaje para arrastrar al editor del compositor, incluyendo texto, imagen, mensaje enriquecido y mensaje basado en tarjeta.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texto

Un mensaje de texto de LINE puede contener hasta 5.000 caracteres e incluir emojis y personalización de Liquid.

Los casos de uso incluyen:
- Anuncia una promoción por tiempo limitado para las existencias en liquidación
- Envía felicitaciones de cumpleaños personalizadas con tarjetas de promoción únicas
- Comparte actualizaciones rápidas sobre próximos eventos

\![Un mensaje de texto que recuerda al usuario que no se olvide de la fiesta del Black Friday y de la posibilidad de ahorrar hasta un 80% antes de medianoche.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Imagen

Se puede añadir un mensaje de imagen LINE a través de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/), una URL o Liquid. Estas imágenes son independientes y no contienen enlaces clicables.

Los casos de uso incluyen:
- Mostrar un destino de vacaciones para inspirar a los usuarios a comprar billetes de avión
- Destaca las promociones de final de temporada para animar a los usuarios a abastecerse de la ropa de invierno del año que viene con grandes ofertas
- Inicia una cuenta atrás visual para una venta anual en toda la tienda

\![Un mensaje de imagen promocionando la venta de una tostadora.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Imagen URL

Utiliza imágenes de URL para casos de uso que incorporen:
- Imágenes dinámicas Liquid incluyendo Liquid en tu atributo de fuente de la imagen. Por ejemplo, puedes insertar {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como URL de la imagen para incluir el nombre de pila de un usuario en la imagen
- [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) extrayendo imágenes directamente de tu servidor Web o API de acceso público
- [Braze los catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) accediendo a las imágenes desde archivos CSV importados y puntos finales de API

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Longitud de la URL del archivo de imagen | 2.000 caracteres como máximo  |
| Formato de imagen          | PNG, JPEG             |
| Tamaño del archivo     |  10 MB máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mensajes enriquecidos (mapa de imágenes)

Un mensaje enriquecido con LINE es una imagen que contiene uno o varios enlaces que se abren seleccionando zonas concretas de la imagen. Selecciona una plantilla de mensajes enriquecidos para elegir cómo se mapean los enlaces en la imagen.

Los casos de uso incluyen:
- Mostrar una cuadrícula de los bolsos recién llegados con enlaces a la página de producto correspondiente a cada bolso
- Presenta un menú interactivo que inicie un pedido combinado seleccionando un artículo
- Presenta varias promociones para que los usuarios las elijan seleccionando un cuadrado de la cuadrícula

\![Un mensaje enriquecido de seis cuadrados con una foto de una cuadrícula en blanco y negro que los usuarios pueden tocar para recibir una oferta aleatoria.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mapa de imagen 

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Longitud de la URL del archivo de imagen | 2.000 caracteres como máximo  |
| Formato de imagen          | PNG (puede ser transparente), JPEG             |
| Relación de aspecto          | 1:1 (anchura:altura)
| Tamaño del archivo     |  10 MB máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace URI 

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Recuento de caracteres      | 1.000 máximo |
| Esquemas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Texto 

Un mensaje de texto enriquecido puede contener hasta 400 caracteres.

## Basado en tarjetas (carrusel)

Una mensajería basada en tarjetas de LINE permite a los usuarios desplazarse por varios mensajes, como en un carrusel, y actuar sobre los mensajes más relevantes para ellos seleccionando una tarjeta o los botones de una tarjeta.

Los casos de uso incluyen:
- Mostrar promociones para elementos de menú específicos
- Destaca las chaquetas más vendidas de esta temporada
- Presentar una muestra de los utensilios y aparatos de cocina que se incluyen en un kit

\![Un mensaje basado en tarjetas con al menos dos tarjetas que promueven bocadillos en el editor del compositor.]({% image_buster /assets/img/line/line_card_message.png %})

### Mensaje

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| Columnas                  | 10 máximo |
| Relación de aspecto             | Rectángulo: 1.51:1 <br> Cuadrado: 1:1  |
| Título                    | 40 caracteres máximo
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Imagen

| **Especificaciones** | **Propiedades recomendadas** |
|--------------------------|----------------------------|
| URL de la imagen                 | 2.000 caracteres como máximo |
| Formato de imagen              | JPEG o PNG |
| Anchura                     | 1.024 píxeles  |
| Tamaño del archivo                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Texto

| **Especificaciones** | **Propiedades recomendadas** |
|-------------------------|----------------------------|
| Personajes              | 120 como máximo (sin imagen ni título) <br> 60 como máximo (mensaje con imagen o título)  |
| Acciones                 | 3 máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


