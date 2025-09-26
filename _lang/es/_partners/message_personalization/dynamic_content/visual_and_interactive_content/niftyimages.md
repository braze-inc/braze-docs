---
nav_title: NiftyImages
article_title: NiftyImages
description: "Aprende a integrar NiftyImages con Braze."
alias: /partners/niftyimages/
page_type: partner
search_tag: Partner
---

# NiftyImages

> [NiftyImages](https://niftyimages.com) es un software de personalización de correo electrónico en tiempo real que permite a los profesionales del marketing enviar comunicaciones por correo electrónico relevantes y actualizadas de forma más eficaz, al tiempo que aumenta la participación y los ingresos. Es una herramienta fácil de usar y de autoservicio que permite a los profesionales del marketing añadir contenido dinámico a sus correos electrónicos de forma fácil y rápida.

_Esta integración está mantenida por NiftyImages._

## Requisitos previos

NiftyImages funciona con la plataforma Braze por defecto sin necesidad de integración. Para empezar, todo lo que necesitas es una [cuenta NiftyImages](https://niftyimages.com/Signup).

## Características compatibles

Al aprovechar NiftyImages en Braze, puede crear imágenes dinámicas y personalizadas para sus campañas de correo electrónico asignando sus etiquetas de personalización Braze existentes a sus URL de NiftyImages.

- **Privacidad:** Todos tus datos se almacenan en Braze, no en NiftyImages.
- **Imágenes personalizadas:** Utiliza cualquier etiqueta «merge» Braze para personalizar una imagen.
- **Tablas y gráficos:** Muestre los niveles, el estado de los clientes, el dinero gastado, los puntos, etc. mediante tablas y gráficos personalizables.
- **Mapas:** Mostrar una imagen de un mapa con la ubicación más cercana al lugar donde un usuario abre su correo electrónico.
- **Temporizadores de cuenta atrás personalizados:** Muestre temporizadores únicos con variables de fecha de base de datos para cumpleaños, vencimientos de pruebas, fecha de la última compra, facturas vencidas o fecha del último inicio de sesión.
- **Contenidos en tiempo real:** Muestre imágenes en tiempo real para recomendaciones de productos, carritos abandonados, bajadas de precios, niveles de inventario, meteorología, etc.
- **Encuestas en directo:** Muestre encuestas en directo para fomentar la participación y conocer los niveles de interés.
- **Lógica basada en reglas:** Muestra imágenes dinámicas basadas en datos de usuario, demográficos, de comportamiento, ubicación, hora del día, día de la semana, dispositivo de apertura, sistema operativo, etc.

Por ejemplo, he aquí una imagen personalizada generada por NiftyImages utilizando el nombre de pila de un cliente.

![ALT_TEXT.]({% image_buster /assets/img/niftyimages/1.png %}){: style="max-width:70%;"}

## Creación de una NiftyImage

### Paso 1: Crear una etiqueta merge

En NiftyImages, elige una etiqueta de fusión y, a continuación, rellena los valores predeterminados. Cuando haya terminado, seleccione **Siguiente**.

![texto alternativo]({% image_buster /assets/img/niftyimages/2.png %}){: style="max-width:70%;"}

Si lo desea, introduzca los tipos de datos y seleccione **Siguiente**.

![texto alternativo]({% image_buster /assets/img/niftyimages/3.png %})
{: style="max-width:70%;"}

Opcionalmente, puedes elegir guardar tu etiqueta para utilizarla en el futuro. Cuando hayas terminado, selecciona **Guardar** para crear tu etiqueta merge.

![texto alternativo]({% image_buster /assets/img/niftyimages/4.png %}){: style="max-width:70%;"}

### Paso 2: Personaliza tu imagen

Personaliza la fuente, el tamaño, la posición, el color, las capas y mucho más de tu imagen. Cuando hayas terminado, copia la URL de tu imagen.

![texto alternativo]({% image_buster /assets/img/niftyimages/5.png %})

### Paso 3: Añade la URL de la imagen a Braze

En Braze, abre una campaña o un lienzo y pega la URL de tu NiftyImage. Opcionalmente, puedes obtener una vista previa de tus cambios para verificar tus etiquetas de Liquid.


![texto alternativo]({% image_buster /assets/img/niftyimages/6.png %})
