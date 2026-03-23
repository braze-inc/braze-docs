---
nav_title: Guía de estilo para textos en imágenes
article_title: Guía de estilo para textos en imágenes
description: "Directrices para crear y dar estilo a imágenes en Braze Docs."
page_order: 1
noindex: true
---

# Guía de estilo para textos en imágenes

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## Optimiza la ubicación y el tamaño

Siempre que sea posible, coloca las imágenes cerca del texto relevante y ten en cuenta el uso de markdown de estilo de imagen para redimensionar las imágenes más grandes. Para algunos contenidos, esto debe hacerse [anclando el texto al lado izquierdo o derecho de la página]({{site.baseurl}}/home/styling_test_page/#image-test) dependiendo de la imagen y el espacio disponible.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="Ejemplo de optimización correcta de la ubicación de una imagen."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="Ejemplo de optimización incorrecta de la ubicación de una imagen."></td></tr>
</tbody>
</table>
{:/}

## Recorta las imágenes

Recorta las secciones relevantes de forma ajustada. A menos que sea necesario, no incluyas la barra de navegación lateral e incluye en su lugar las indicaciones de navegación en el artículo. Esto limita el número de imágenes que deben cambiarse cuando se producen cambios en la interfaz de usuario.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="Ejemplo de una imagen correctamente recortada."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="Ejemplo de una imagen incorrectamente recortada."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="Ejemplo de una imagen correctamente recortada."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="Ejemplo de una imagen incorrectamente recortada."></td></tr>
</tbody>
</table>
{:/}

Dado que Braze Docs ya añade un borde a cada imagen, omite los bordes en las capturas de pantalla de secciones. Buscamos un recorte limpio. El borde puede dejarse si hay componentes que se encuentran fuera o dentro del borde; consulta las siguientes imágenes como ejemplos.

**Correcto:**
![Ejemplo de recorte correcto de una imagen.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**Incorrecto:**  
![Ejemplo de recorte incorrecto de una imagen.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**Correcto:**  
![Ejemplo de recorte correcto de una imagen.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## Difumina la información sensible

Difumina cualquier información de identificación personal (PII) como nombres, correos electrónicos y claves de API.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="Ejemplo de difuminado correcto."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="Ejemplo de difuminado incorrecto."></td></tr>
</tbody>
</table>
{:/}

## No incrustes texto importante dentro de las imágenes

Evita incrustar texto dentro de las imágenes, ya que no todos los usuarios pueden leer texto en inglés (y las herramientas de traducción de páginas no traducen las imágenes). Este texto debe proporcionarse en el artículo. Proporciona texto alternativo en las imágenes para garantizar la máxima accesibilidad para los usuarios.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="Ejemplo correcto de no incrustar texto en una imagen."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="Ejemplo incorrecto de incrustar texto en una imagen."></td></tr>
</tbody>
</table>
{:/}

## No enfatices los componentes

No enfatices los componentes de las imágenes a menos que sea necesario. Usa cuadrados azules (la opción más accesible) con un grosor fino a medio para resaltar diferentes componentes de las imágenes. Asegúrate de que las "secciones resaltadas" no obstruyan la interfaz de usuario normal.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Correcto</th><th style="width: 50%;">Incorrecto</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="Ejemplo de énfasis correcto de componentes en una imagen."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="Ejemplo de énfasis incorrecto de componentes en una imagen."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="Ejemplo de énfasis correcto de componentes en una imagen."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="Ejemplo de énfasis incorrecto de componentes en una imagen."></td></tr>
</tbody>
</table>
{:/}