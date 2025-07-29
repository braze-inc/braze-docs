---
nav_title: Crear geovallas
article_title: Crear geovallas
page_order: 1
page_type: reference
toc_headers: h2
description: "En este artículo de referencia se explica qué son las geovallas y cómo crear y configurar eventos de geovalla."
tool: 
  - Location
search_rank: 9
---

# Geovallas

> El núcleo de la oferta de ubicación en tiempo real de Braze es el concepto de geovalla. Una geo-valla es un área geográfica virtual, representada como latitud y longitud combinadas con un radio, formando un círculo alrededor de una posición global específica. Las geocercas pueden tener desde el tamaño de un edificio hasta el de una ciudad entera.

## 

 Los usuarios que entran o salen de sus geocercas añaden una nueva capa de datos de usuario que puede utilizar para la segmentación y la reorientación.

Las geovallas se organizan en conjuntos de geovallas: un grupo de geovallas que pueden utilizarse para segmentar o interactuar con los usuarios en toda la plataforma. Cada conjunto de geovallas puede contener un máximo de 10 000 geovallas.



- Las aplicaciones de Android solo pueden almacenar localmente hasta 100 geovallas a la vez. Braze está configurado para almacenar solo hasta 20 geovallas localmente por aplicación.
- Los dispositivos iOS pueden controlar hasta 20 geovallas a la vez por aplicación. Braze supervisará hasta 20 ubicaciones si hay espacio disponible. 
- 
- Para que las geovallas funcionen correctamente, debes asegurarte de que tu aplicación no está utilizando todos los puntos de geovalla disponibles.



|  |  |
|---|---|
|  |  |
|  |   |
|  |    |


## 

###  



1. 
2. 
3. 
4. 

###  



1.  
2. 
3. 


Recomendamos crear geovallas con un radio de al menos 200 metros para una funcionalidad óptima. 




## 

Las geocercas pueden cargarse en bloque como un objeto GeoJSON de tipo `FeatureCollection`.   





- 
- 

### 



```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Usar eventos de geovallas



### 

Para utilizar datos de geocercas como parte de los activadores de campañas y Canvas, seleccione **Entrega basada en acciones** para el método de entrega. A continuación, añade una acción desencadenante de `Trigger a Geofence`. Por último, elige el conjunto de geovallas y los tipos de eventos de transición de geovalla para tu mensaje. También puede hacer avanzar a los usuarios a través de un lienzo mediante eventos de geovalla.



### 

Para utilizar datos de geofence para personalizar un mensaje, puede utilizar la siguiente sintaxis de personalización de Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Actualizar los conjuntos de geovallas

Para los usuarios activos, el SDK de Braze solo solicitará geovallas una vez al día al iniciar la sesión. Esto significa que, si se realizan cambios en los conjuntos de geovallas después de iniciar la sesión, tendrás que esperar 24 horas desde el momento en que los conjuntos se desplieguen por primera vez para recibir el conjunto actualizado.

{% alert note %}
Si las geovallas no se cargan en el dispositivo localmente, el usuario no puede desencadenar el geovallado aunque entre en la zona.
{% endalert %}

## 

### 

 

1. 
2. 
3. 


 








## Preguntas más frecuentes

### 

   

  

### 

 

  



### 



### 

  

 

### 

  

### 



