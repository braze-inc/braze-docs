---
nav_title: Buenas prácticas
article_title: Buenas prácticas para el suministro de noticias
page_order: 20
page_type: reference
description: "En este artículo se describen las mejores prácticas para diseñar y personalizar las tarjetas de noticias."
channel: news feed
hidden: true

---

# Mejores prácticas de noticias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> La fuente de noticias Braze es un flujo dinámico y específico de contenido enriquecido. Ofrece una potente forma de llegar a los usuarios con contenidos continuamente actualizados que no requieren trabajo de desarrollo adicional. Este contenido puede dirigirse a varios segmentos y programarse del mismo modo que otros mensajes Braze. Cada tarjeta consta de un título, un resumen, una imagen y, opcionalmente, una URL. La fuente también incluye la posibilidad de establecer vínculos profundos dentro de la aplicación, enlazar directamente con App Store, Google Play, etc. o dirigir a los usuarios a una vista Web. Este elemento exclusivo de la interfaz de usuario de Braze debe activarse durante [la integración][1]. Asegúrese de comentarlo con sus desarrolladores.

Para conocer los distintos tipos de tarjetas de noticias, cómo crearlas, casos de uso, así como las especificaciones de las tarjetas y las imágenes, lee nuestra página sobre [creación de elementos de noticias][4].

> Braze mejora los tiempos de carga utilizando una CDN global para alojar todas las imágenes de la fuente de noticias.

## Buenas prácticas {#news-feed-best-practices}

En Braze, valoramos la personalización que aporta News Feed. Estas son algunas de nuestras mejores prácticas y consejos para ayudarle a sacar el máximo partido de Braze.

### Que llame la atención

Cuanto más llamativas, relevantes e interesantes sean tus noticias, más probabilidades tendrás de que las vean los demás.  

- Utiliza las noticias para que tu aplicación parezca dinámica y se actualice con regularidad mostrando nuevos contenidos.
- Diversificar el tipo de anuncios de tarjetas con plantillas para mantener interesante el News Feed
- Aproveche el espacio visual incorporando imágenes y gráficos que destaquen.

### Hágalo personal

Las empresas y sus usuarios adoran y valoran la personalización.

- Personaliza la sección de noticias para reflejar la identidad de tu marca y crear una experiencia de aplicación perfecta.
- Tenga en cuenta que los módulos orientados pueden inspirar acciones inmediatas dentro de la aplicación, y las URL de protocolo pueden dirigir la atención a diferentes secciones de la aplicación, fomentando comportamientos específicos como reseñas, compras y mucho más.
- Segmente a los usuarios y adapte determinados anuncios para inspirar acciones específicas.

### Haz que sea útil

El contenido que decidas mostrar a través de la sección de noticias puede ser muy variado y funcionar en tándem con las campañas.  

- Ofrezca anuncios que fomenten la interacción, destaquen las novedades y promuevan las ventas.
- Elabore un calendario para campañas como las de incorporación, etc., y determine la cadencia y frecuencia adecuadas de los mensajes.
- Fortalecer y reforzar las campañas integrando otros mensajes multicanal en el News Feed.

## Ejemplo de integración

1-800-Flowers.com utiliza las noticias para ofrecer información relevante a sus usuarios. La integración del SDK sigue siendo totalmente transparente: no se menciona Braze en la propia aplicación y el módulo News Feed tiene una estética de diseño coherente con el resto de la aplicación.

![shapefeed][2]{: style="max-width:50%;"}

Puede ver más ejemplos de News Feeds en nuestros [Estudios de casos][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
[3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
