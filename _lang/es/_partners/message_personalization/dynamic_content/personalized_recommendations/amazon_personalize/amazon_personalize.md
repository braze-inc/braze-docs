---
nav_title: Amazon Personalizar
article_title: Amazon Personalizar
alias: "/partners/amazon_personalize_overview/"
description: "Este artículo de referencia describe una arquitectura de referencia para la integración entre Braze y Amazon Personalize. Este artículo de referencia le ayudará a comprender los casos de uso que ofrece Amazon Personalize, los datos con los que trabaja, cómo configurar el servicio y cómo integrarlo con Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalizar
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize es como tener tu propio sistema de recomendación de aprendizaje automático de Amazon durante todo el día. Basado en más de 20 años de experiencia en recomendaciones, Amazon Personalize le permite mejorar la interacción con el cliente mediante recomendaciones personalizadas de productos y contenidos en tiempo real y promociones de marketing específicas.

_Esta integración es mantenida por Amazon Personalize._

## Sobre la integración

Mediante el aprendizaje automático y un algoritmo que usted ayuda a definir, Amazon Personalize puede ayudarle a entrenar un modelo que produzca recomendaciones de alta calidad para sus sitios web y aplicaciones. Estos modelos le permitirán crear listas de recomendaciones basadas en los comportamientos anteriores de los usuarios, ordenar los elementos por relevancia y recomendar otros elementos en función de la similitud. Las listas obtenidas de Amazon Personalize API pueden utilizarse en Braze Connected Content para ejecutar campañas de recomendación personalizadas de Braze. Al integrarse con Amazon Personalize, los clientes tienen libertad para controlar los parámetros utilizados para entrenar los modelos y definir objetivos empresariales opcionales que optimicen el resultado del algoritmo. 

Este artículo de referencia le ayudará a comprender los casos de uso que ofrece Amazon Personalize, los datos con los que trabaja, cómo configurar el servicio y cómo integrarlo con Braze.

## Requisitos previos

| Requisito| Descripción|
| ---| ---| 
| Cuenta de Amazon Web Service | Se necesita una cuenta de AWS para beneficiarse de esta asociación. Después de tener una cuenta de AWS, puede acceder a Amazon Personalize a través de la consola de Amazon Personalize, la interfaz de línea de comandos de AWS (CLI de AWS) o los SDK de AWS. |
| Casos de uso definidos | Antes de crear un modelo, debe determinar su caso de uso para esta integración. Consulte la siguiente lista de casos de uso comunes. |
| Conjuntos de datos | Los modelos de recomendación de Amazon Personalize requieren tres tipos diferentes de conjuntos de datos: interacciones, usuarios y artículos. Consulte los siguientes detalles para ver los requisitos de cada conjunto de datos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab casos de uso %}

**Ejemplos**

Antes de crear un modelo, debe determinar su caso de uso para esta integración. Algunos casos de uso habituales son:
- Recomiende artículos a los usuarios basándose en sus interacciones anteriores, creando una experiencia verdaderamente personalizada para sus usuarios.
- Proporcionar una lista de artículos o resultados de búsqueda adaptados a cada usuario, aumentando el compromiso al mostrar artículos por relevancia para el usuario.
- Encuentra recomendaciones de artículos similares, ayudando a los usuarios a descubrir cosas nuevas.

En la siguiente guía, nos centraremos en la receta de recomendaciones personalizadas para el usuario.

{% endtab %}
{% tab Conjuntos de datos %}

**Conjuntos de datos**

Para comenzar a utilizar los modelos de recomendación de Amazon Personalize, necesita tres tipos de conjuntos de datos:

- Interacciones
  - Almacena el historial de interacciones entre usuarios y artículos
  - Requiere los valores `USER_ID`, `ITEM_ID`, `EVENT_TYPE` y `TIMESTAMP` y opcionalmente acepta metadatos sobre el evento
- Usuarios
  - Almacena metadatos sobre los usuarios
  - Requiere un valor `USER_ID` y al menos un campo de metadatos (cadena o numérico) como sexo, edad, fidelización
- Elementos
  - Almacena metadatos sobre los artículos
  - Requiere un `ITEM_ID` y al menos un campo de metadatos (textual, categórico o numérico) que describa el artículo

Para una receta de recomendaciones de usuario, debe proporcionar un conjunto de datos de interacciones que contenga al menos 1000 puntos de datos de interacción de al menos 25 usuarios únicos con al menos dos interacciones cada uno. Estos conjuntos de datos pueden cargarse en bloque utilizando archivos CSV almacenados en S3 o de forma incremental a través de la API.

{% endtab %}
{% endtabs %}

## Creación de modelos

### Paso 1: Entrenando

Una vez importados los conjuntos de datos, puede crear una solución. Una solución utiliza una de las [recetas](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (algoritmos) de Amazon Personalize para entrenar un modelo. En nuestro caso, utilizaremos la receta `USER_PERSONALIZATION`. El entrenamiento de la solución crea una versión de la solución (modelo entrenado) que puede evaluar en función de las métricas de rendimiento del modelo.

Amazon Personalize te permite ajustar los hiperparámetros que el modelo utiliza para entrenarse. Por ejemplo:
- El parámetro "Percentil de longitud del historial de usuario" que se encuentra en la consola de Amazon Personalize permite ajustar el percentil del historial de usuario que se incluirá en el entrenamiento:<br><br>![Configuración mínima máxima del perfil de usuario]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: excluye un porcentaje de usuarios con historiales muy cortos, lo que puede ser útil para eliminar artículos populares y elaborar recomendaciones basadas en patrones subyacentes más profundos.
  - `max_user_history_length_percentile`: ajusta el porcentaje de usuarios a tener en cuenta cuando se entrena con longitudes de historial muy largas.

El número de dimensiones ocultas ayuda a detectar patrones más complicados para conjuntos de datos complejos, mientras que la técnica de retropropagación a través del tiempo (BPTT) ajusta las recompensas para un evento temprano después de que se produjera una cadena de eventos que dio lugar a una acción de alto valor.

Además, Amazon Personalize ofrece un ajuste automático de hiperparámetros mediante la ejecución simultánea de varias versiones de la solución con diferentes valores. Para utilizar el ajuste, active **Realizar HPO** al crear una solución.

### Paso 2: Evaluar y comparar

Una vez finalizada la formación de una solución, estás preparado para evaluarla y comparar diferentes versiones. Cada versión de la solución muestra las métricas calculadas. Algunas de las métricas disponibles son:

- **Normalizar la ganancia acumulada descontada:** compara el orden recomendado de los elementos con la lista real de elementos y asigna a cada elemento un peso correspondiente a su posición en la lista.
- **Precisión @k:** la cantidad de artículos recomendados correctamente dividida por la cantidad de todos los artículos recomendados, donde `k` es el número de artículos.
- **Rango recíproco medio:** se centra en la primera recomendación mejor clasificada y calcula cuántos artículos recomendados se ven antes de que aparezca la primera recomendación emparejada.
- **Cobertura:** proporción de elementos únicos recomendados con respecto al número total de elementos únicos del conjunto de datos.

## Obtener recomendaciones

Una vez que haya creado una versión de la solución con la que esté satisfecho, es hora de poner en práctica las recomendaciones. Hay dos formas de acceder a las recomendaciones:

1. Campaña en tiempo real<br>Una campaña es una versión de la solución desplegada con un rendimiento mínimo de transacciones definido. Una transacción es una única llamada a la API para obtener la salida de la recomendación, y se define como TPS, o transacciones por segundo, con un valor mínimo de uno. La campaña escalará recursos en caso de un aumento de la carga, pero no caerá por debajo de su valor mínimo. Puedes consultar las recomendaciones en la consola, en la CLI de AWS o a través de los SDK de AWS en tu código.<br><br>
2. Trabajo por lotes<br>Un trabajo por lotes exporta las recomendaciones a un bucket de S3. La tarea toma como entrada un archivo JSON con una lista de ID de usuario para los que desea exportar las recomendaciones. A continuación, tras especificar los permisos correctos y el destino de salida, estarás listo para ejecutar el trabajo. El tiempo de ejecución depende del tamaño de los conjuntos de datos y de la longitud de la lista de recomendaciones.

### Filtros

Los filtros permiten ajustar el resultado de la recomendación excluyendo elementos en función del ID del elemento, el tipo de evento o los metadatos. También puede filtrar a los usuarios en función de sus metadatos, como la edad o el estado de fidelización. Los filtros pueden resultar útiles para evitar que se recomienden artículos con los que el usuario ya ha interactuado.

## Integración de resultados con Braze

Con el modelo creado y la campaña de recomendaciones, está listo para ejecutar una campaña Braze para sus usuarios utilizando Tarjetas de contenido y Contenido conectado.
Antes de ejecutar una campaña Braze, debe crear un servicio que pueda servir estas recomendaciones a través de una API. Puedes seguir [el paso 3 del artículo del taller]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze) para desplegar el servicio utilizando los servicios de AWS. También puede desplegar su propio servicio backend independiente que proporcione las recomendaciones.

### Caso de uso de la campaña de tarjeta de contenido

Realicemos una campaña de tarjetas de contenido con el primer elemento recomendado de la lista.<br><br>
En los siguientes ejemplos, vamos a consultar
`GET http://<service-endpoint.com>/recommendations?user_id=user123` con un parámetro `user_id` que devolverá una lista de elementos recomendados:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

En el panel de control de Braze, cree una nueva [campaña de tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). En el campo de texto del mensaje, cree un bloque Connected Content Liquid para consultar la API y guardar la respuesta en la variable `recommendations`:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

A continuación, puede hacer referencia al primer elemento de la matriz resultante y mostrar el contenido al usuario:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Incluyendo el título, la imagen y enlazando la URL, así es como quedaría la Tarjeta de Contenido completa:

![Una imagen de una campaña con Contenido Conectado añadida al cuerpo del mensaje y al campo "Añadir imagen". Esta imagen también muestra la lógica de Contenido conectado añadida al campo "Redirigir a URL Web", que vincula a los usuarios a una URL de recomendación.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})


