---
nav_title: Segmentación de ubicación
article_title: Segmentación de ubicación
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Location
description: "En este artículo se explica cómo configurar la segmentación por ubicación, que permite segmentar a los usuarios por ubicación."

---

# Segmentación de ubicación

> Este artículo le mostrará cómo configurar la orientación por ubicación, lo que le permitirá segmentar a los usuarios según su ubicación más reciente. Es perfecto para las campañas y estrategias basadas en la localización.

## Paso 1: Cree su segmento

Vaya a la página **Segmentos**, en **Audiencia**, para ver todos sus segmentos de usuarios actuales. En esta página puede crear y nombrar nuevos segmentos. Para empezar, haga clic en **Crear segmento** y asigne un nombre a su segmento.

![][1]{: style="max-width:70%;"}

## Paso 2: Personaliza tu ubicación

Una vez que haya creado su segmento, añada un filtro de **Ubicación más reciente** para dirigirse a los usuarios por el último lugar en el que utilizaron su aplicación. Tiene la opción de destacar a los usuarios en una región circular estándar o en una región poligonal personalizable.

![][2]

### Regiones circulares

Para las regiones circulares, puede mover el origen y ajustar el radio de ubicación para su segmentación.

![Un contorno circular de ciudades entre Nueva Jersey y Nueva York.][3]{: style="max-width:70%;"}

### Regiones poligonales

Para las regiones poligonales, puede designar más específicamente qué áreas desea incluir en su segmento.

![Un contorno del estado de Nueva York como región poligonal seleccionada.][4]{: style="max-width:70%;"}

## Apoyo a la asociación para beacon y geovallas

La combinación de la beacon o geovalla existente con nuestras características de segmentación y mensajería te proporciona más información sobre las acciones físicas de tus usuarios para que puedas enviarles mensajes en consecuencia. Puedes aprovechar el seguimiento de ubicación con algunos de nuestros socios: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
