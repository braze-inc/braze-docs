---
nav_title: Recomendaciones
article_title: Recomendaciones de artículos en Braze
page_order: 15
search_rank: 1
description: "Aprende todo sobre las herramientas de recomendaciones de artículos en Braze."
---

# Recomendaciones

> Intensifica tu juego de recomendaciones con Braze creando una herramienta de recomendaciones que pueda sugerir a tus usuarios artículos y contenidos que realmente desean. Desde personalizar experiencias con IA hasta construir tus propios motores con Liquid o Contenido conectado, encontrarás todo lo que necesitas para que cada recomendación cuente.

## Requisitos previos

Antes de que puedas crear o utilizar recomendaciones de artículos en Braze, tendrás que [crear al menos un catálogo; sólo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)los artículos de ese catálogo se recomendarán a los usuarios.

## Tipos y casos de uso

### AI Personalización {#ai}

Como parte de la característica [de recomendaciones de artículos de la]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) IA, las recomendaciones personalizadas de la IA aprovechan el aprendizaje profundo para predecir lo que más probablemente interesará a tus usuarios a continuación, basándose en lo que les ha interesado en el pasado. Este método proporciona un sistema de recomendación dinámico y a medida que se adapta al comportamiento del usuario.

Las recomendaciones personalizadas de IA utilizan los datos de los últimos 6 meses de interacción con los artículos, como compras o eventos personalizados, para construir el modelo de recomendación. Para los usuarios sin datos suficientes para una lista personalizada, los elementos más populares sirven como alternativa para que tus usuarios sigan recibiendo sugerencias relevantes.

Con las recomendaciones de artículos de IA, también puedes filtrar aún más los artículos disponibles con
[selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). Sin embargo, las selecciones con Liquid no pueden utilizarse en las recomendaciones de la IA, así que tenlo en cuenta cuando construyas las selecciones de tu catálogo.

{% alert tip %}
Las recomendaciones personalizadas con IA funcionan mejor con cientos o miles de artículos y, normalmente, al menos 30.000 usuarios con datos de compra o interacción. Esto es sólo una guía aproximada y puede variar. Los otros tipos de recomendación pueden funcionar con menos datos.
{% endalert %}

#### Casos de uso

Según los datos de interacción que se estén siguiendo, los casos de uso de este modelo podrían incluir:

{% tabs local %}
{% tab Most likely to purchase next %}
Predecir y recomendar los artículos que un usuario tiene más probabilidades de comprar a continuación, basándose en eventos de compra o eventos personalizados relacionados con las compras. Por ejemplo:

- Un sitio de viajes podría sugerir paquetes de vacaciones, vuelos o estancias en hoteles basándose en el historial de navegación y las reservas anteriores de un usuario, anticipándose a su próximo destino de viaje y facilitándole la planificación del mismo.
- Una plataforma de streaming puede analizar los hábitos de visionado para recomendar los programas o películas que un usuario tiene más probabilidades de ver a continuación, manteniéndolo enganchado y reduciendo las tasas de abandono.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Un método de seguimiento de compras, ya sea un objeto de compra o un evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** a **Personalizado AI**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige cómo realizas actualmente el seguimiento de los eventos de compra y la propiedad de evento correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Artículo más popular {#most-popular}

El modelo de recomendación "Más populares" presenta los elementos con los que los usuarios tienen más interacción.

#### Casos de uso

Basándose en los datos de interacción que se están siguiendo, los casos de uso de este modelo podrían incluir la recomendación:

{% tabs local %}
{% tab most popular %}
Anima a los usuarios a explorar los artículos más populares de tu catálogo en función de sus compras. Para asegurarte de que sólo aparece contenido relevante, te recomendamos filtrar con una selección. Por ejemplo, un servicio de entrega de comida podría destacar los platos o restaurantes mejor valorados dentro de la zona de un usuario, basándose en la popularidad de los pedidos en toda la plataforma, fomentando la prueba y el descubrimiento.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Un objeto de compra o cualquier evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Establece el **Tipo** en **Más populares**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes. Por ejemplo, el servicio de entrega de comida podría tener una selección para filtrar por ubicación del restaurante o tipo de plato.
5. Elige cómo realizas actualmente el seguimiento de los eventos y la propiedad de evento correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most liked %}
Anima a los usuarios a explorar artículos que les han gustado recientemente o artículos que son populares, basándote en un evento personalizado para los "Me gusta". Por ejemplo, una aplicación de streaming de música podría crear listas de reproducción personalizadas o sugerir el lanzamiento de nuevos álbumes basándose en los géneros o artistas que le han gustado a un usuario en el pasado, mejorando la interacción del usuario y el tiempo que pasa en la aplicación.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para likes
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** como **Más reciente**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona tu evento personalizado para gustos de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Destaca los artículos que han llamado la atención de tu base de usuarios a través de las visualizaciones para fomentar la interacción o las compras. Por ejemplo, un sitio web inmobiliario podría mostrar los anuncios más vistos en la zona de búsqueda de un usuario para destacar las propiedades que atraen mucha atención, lo que podría indicar buenas ofertas o ubicaciones deseables.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para vistas
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Establece el **Tipo** en **Más populares**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona tu evento personalizado para las vistas de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Muestra artículos añadidos a los carritos por muchos otros compradores, proporcionando a los usuarios una visión de las tendencias actuales entre tus ofertas.

Por ejemplo, un comercio minorista de moda podría promocionar ropa y accesorios que estén de moda basándose en las adiciones populares a los carritos por parte de otros clientes. A continuación, pueden crear una sección dinámica de "Tendencias actuales" en su página de inicio y aplicación móvil, que se actualiza en tiempo real para animar a los compradores a comprar antes de que se agoten los artículos.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para añadido a la cesta
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Establece el **Tipo** en **Más populares**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona de la lista tu evento personalizado para añadir al carrito.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Artículo más reciente {#most-recent}

El modelo de recomendación "Más reciente" presenta los elementos con los que más interactúan los usuarios. Utiliza este modelo para reducir el abandono animando a los usuarios que abandonan a volver a interactuar con contenidos relevantes.

#### Casos de uso

Basándose en los datos de interacción que se están siguiendo, los casos de uso de este modelo podrían incluir la recomendación:

{% tabs local %}
{% tab Recently clicked %}
Anima a los usuarios a volver a visitar los elementos en los que han hecho clic recientemente, basándote en un evento personalizado para los clics. Por ejemplo, un minorista de moda online podría crear una recomendación para enviar correos electrónicos de seguimiento o notificaciones push con prendas por las que un usuario ha mostrado interés al hacer clic en ellas, animándole a volver a visitar el artículo y realizar una compra.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para los clics
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** como **Más reciente**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona tu evento personalizado para clics de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Anima a los usuarios a explorar artículos que les han gustado recientemente o artículos que son populares, basándote en un evento personalizado para los "Me gusta". Por ejemplo, una aplicación de streaming de música podría crear listas de reproducción personalizadas o sugerir el lanzamiento de nuevos álbumes basándose en los géneros o artistas que le han gustado a un usuario en el pasado, mejorando la interacción del usuario y el tiempo que pasa en la aplicación.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para likes
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** como **Más reciente**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona tu evento personalizado para gustos de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Promociona artículos con los que los usuarios hayan interactuado recientemente, incluyendo visualizaciones, clics o compras. Este enfoque mantiene tus recomendaciones actualizadas y alineadas con los intereses más recientes del usuario.. Por ejemplo:

- **Educación:** Una plataforma de educación en línea podría animar a los usuarios que han visto recientemente un video educativo, pero no se han matriculado en un curso, a consultar cursos similares o temas de interés para mantener al usuario interactuando y motivado para empezar a aprender.
- **Fitness:** Una aplicación de fitness puede sugerir entrenamientos o retos similares a los que el usuario ha completado o con los que ha interactuado recientemente, manteniendo su rutina de ejercicios variada y atractiva.
- **Comercio minorista de mejoras para el hogar:** Después de que un cliente compre una herramienta eléctrica, un comercio minorista puede recomendarle accesorios relacionados o engranajes de seguridad basados en su compra reciente, mejorando la experiencia y la seguridad del usuario.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Un objeto de compra o cualquier evento personalizado para una interacción con los clientes
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** como **Más reciente**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona tu evento personalizado para clics de la lista.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Recuerda a los usuarios su interés por artículos que han añadido recientemente a su cesta, pero que aún no han comprado. Por ejemplo, un comercio minorista online podría enviar recordatorios u ofrecer descuentos por tiempo limitado en los artículos de su cesta, animando a los usuarios a completar sus compras antes de que caduquen las ofertas.
{% details Requirements %}

- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para añadido a la cesta
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Configura el **Tipo** como **Más reciente**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige **Evento personalizado** y selecciona de la lista tu evento personalizado para añadir al carrito.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Artículo de moda {#trending}

El modelo de recomendación "Tendencias" presenta los artículos que han mostrado el impulso más positivo en las interacciones recientes de los usuarios. Lo calculamos mediante un análisis ponderado de aproximadamente 10 semanas de historial de acontecimientos, aplicando la mayor ponderación a las 2 semanas aproximadas más recientes. Para evitar que las pequeñas fluctuaciones afecten a la calidad de la recomendación, aplicamos un umbral de actividad y técnicas de suavizado estadístico.

A diferencia del modelo "Más populares", que presenta artículos con una interacción alta y constante, este modelo presenta artículos que han experimentado un repunte en las interacciones. Puedes utilizarlo para recomendar productos prometedores y que actualmente están teniendo una mayor aceptación.

#### Casos de uso

Basándose en los datos de interacción que se están siguiendo, los casos de uso de este modelo podrían incluir la recomendación:

{% tabs local %}
{% tab Trending purchased %}
Destaca los artículos que tus usuarios han comprado recientemente con mayor frecuencia. Por ejemplo, una empresa de comercio electrónico podría recomendar artículos de temporada de los que los usuarios están empezando a abastecerse durante sus preparativos para la próxima temporada. 

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Un método de seguimiento de las compras (ya sea un objeto de compra o un evento personalizado)
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Ajusta el **Tipo** a **Tendencia**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige un evento de compra o un evento personalizado que realice un seguimiento de las compras, junto con la propiedad correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Destaca los elementos que han gustado recientemente a tus usuarios con mayor frecuencia. Por ejemplo, una aplicación de música podría presentar artistas prometedores que hayan experimentado un reciente aumento de los "me gusta" de los usuarios.

{% details Requirements %}
- Recomendaciones sobre el tema AI
- Catálogo de elementos relevantes
- Evento personalizado para el seguimiento de los Me gusta
{% enddetails %}

{% details Setting it up %}
1. Crea una [recomendación de artículo de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Ajusta el **Tipo** a **Tendencia**.
3. Selecciona tu catálogo.
4. (Opcional) Añade una selección para filtrar tu recomendación sólo a los elementos relevantes.
5. Elige tu evento personalizado para el seguimiento de los "Me gusta", junto con la propiedad correspondiente.
6. Entrena la recomendación.
7. [Utiliza la recomendación en mensajería.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basado en selecciones {#selections-based}

[Las selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) son grupos específicos de datos del catálogo. Cuando utilizas una selección, básicamente estás configurando filtros personalizados basados en columnas específicas de tu catálogo. Esto podría incluir filtros por marca, tamaño, ubicación, fecha de adición, etc. Te da el control sobre lo que recomiendas al permitirte definir los criterios que deben cumplir los elementos para mostrarse a los usuarios.

Los tres tipos anteriores implican la configuración y el entrenamiento de un modelo de recomendación en Braze. Aunque también puedes utilizar selecciones en esos modelos, también puedes llevar a cabo algunos casos de uso de recomendaciones sólo con selecciones de catálogo y personalización de Liquid.

#### Casos de uso

Basándose en los datos de interacción que se están siguiendo, los casos de uso de este modelo podrían incluir la recomendación:

{% tabs local %}
{% tab New items %}
Este escenario no se basa directamente en las acciones del usuario, sino en los datos de catálogo. Puedes filtrar los artículos nuevos en función de su fecha de incorporación al catálogo y promocionarlos mediante campañas dirigidas o Lienzos sin necesidad de entrenar un modelo de recomendación.

Por ejemplo, una plataforma de comercio electrónico de tecnología podría alertar a los entusiastas de la tecnología sobre los últimos gadgets o los próximos pedidos anticipados, utilizando filtros para dirigirse a los artículos que se han añadido recientemente al catálogo.

{% details Requirements %}
- Catálogo de elementos relevantes con un campo para la fecha añadida
{% enddetails %}

{% details Setting it up %}
1. Crea una selección basada en tu catálogo. Asegúrate de que tu catálogo tiene un campo de hora (campo con un **Tipo de datos** establecido en **Hora**) que corresponde a la fecha en que se añadió el artículo.
2. (Opcional) Añade filtros si lo deseas.
3. Asegúrate de que **Ordenar aleatoriamente** está desactivado.
4. En **Campo de ordenación**, selecciona tu campo de fecha añadida.
5. Establece **Orden de clasificación** descendente.
6. [Utiliza la selección en mensajería]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
Para una experiencia de usuario diversa, recomendar artículos al azar puede introducir variedad y despertar potencialmente el interés por las áreas menos visitadas del catálogo. Este método no requiere modelos o eventos específicos, sino que utiliza una selección de catálogo para garantizar que los artículos se muestren aleatoriamente.

Por ejemplo, una librería online podría ofrecer la característica "Sorpréndeme", que recomienda un libro al azar basándose en las compras anteriores del usuario o en sus hábitos de navegación, fomentando la exploración fuera de sus géneros de lectura habituales.

{% details Requirements %}
- Catálogo de elementos relevantes
- Selección con **Orden aleatorio** activado
{% enddetails %}

{% details Setting it up %}
1. [Crea una selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) basada en tu catálogo.
2. (Opcional) Añade filtros si lo deseas.
3. Activa **Ordenar aleatoriamente**.
4. [Utiliza la selección en mensajería]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basado en reglas {#rules-based}

Una herramienta de [recomendaciones basada en reglas]({{site.baseurl}}/rules_based_recommendations/) utiliza datos de usuario e información sobre productos para sugerir a los usuarios elementos relevantes dentro de los mensajes. Utiliza Liquid y los catálogos Braze o el Contenido conectado para personalizar dinámicamente el contenido en función del comportamiento y los atributos del usuario.

Las recomendaciones basadas en reglas se basan en una lógica fija que debes establecer manualmente. Esto significa que tus recomendaciones no se ajustarán al historial de compras y gustos individuales de un usuario a menos que actualices la lógica, por lo que este método es mejor para recomendaciones que no necesiten actualizaciones frecuentes.

#### Casos de uso

Según los datos de interacción que se estén siguiendo, los casos de uso de este modelo podrían incluir:

- **Recordatorios de reabastecimiento:** Enviar recordatorios de reposición de artículos con un ciclo de uso predecible, como las vitaminas mensuales o los comestibles semanales, basándose en su última fecha de compra.
- **Compradores por primera vez:** Recomienda kits de iniciación u ofertas introductorias a los primeros compradores para animarles a una segunda compra.
Programas de fidelización: Destaca los productos que maximizarían los puntos de fidelización o recompensas de un cliente en función de su saldo de puntos actual.
- **Contenido educativo:** Sugerir nuevos cursos o contenidos basados en los temas de materiales consumidos o adquiridos previamente.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Preguntas más frecuentes {#faq}

### ¿Qué hace que los artículos "Más populares" se mezclen con las recomendaciones de otros modelos?

Cuando nuestra herramienta de recomendaciones selecciona una lista para ti, primero da prioridad a las selecciones personalizadas basadas en el modelo específico que has elegido, como "Más reciente" o "Personalizado con IA". Si este modelo no puede llenar la lista completa de 30 recomendaciones por cualquier motivo, se añaden entonces algunos de tus artículos más populares entre todos los usuarios, para asegurarte de que cada usuario tenga siempre un conjunto completo de recomendaciones.

Esto ocurre en algunas condiciones específicas:

- El modelo encuentra menos de 30 artículos que coinciden con tus criterios.
- Los artículos relevantes ya no están disponibles o en stock.
- Los artículos no cumplen los criterios de selección actuales, quizás debido a un cambio en las existencias o a las preferencias del usuario.

### ¿Las recomendaciones existentes se entrenan semanalmente después de actualizar a Recomendaciones de Artículos Pro?

Sí, pero sólo después de su próxima actualización programada. Las recomendaciones existentes no cambian a entrenamiento semanal y predicción diaria inmediatamente después de actualizar a Recomendaciones de artículos Pro. Sin embargo, adoptarán el nuevo horario automáticamente en su próximo ciclo de reciclaje. Por ejemplo, si una recomendación se entrenó por última vez el 1 de febrero y está configurada para volver a entrenarse cada 30 días, adoptará el nuevo programa semanal tras su próxima actualización el 2 de marzo.