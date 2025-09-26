---
nav_title: Resumen arquitectónico
article_title: Resumen arquitectónico
page_order: 3
description: "Este artículo trata de las diferentes partes y piezas del stack tecnológico de Braze, con enlaces a artículos relevantes."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# Para empezar: Resumen arquitectónico

> Este artículo trata de las diferentes partes y piezas del stack tecnológico de Braze, con enlaces a artículos relevantes. 

A un alto nivel, Braze se ocupa de datos. La plataforma Braze, impulsada por el SDK, la API REST y las integraciones de socios, te permite agregar tus datos y actuar sobre ellos. 

![Braze tiene diferentes capas. En total, consta del SDK, la API, el panel y las integraciones de socios. Cada una de ellas aporta partes de una capa de ingesta de datos, una capa de clasificación, una capa de orquestación, una capa de personalización y una capa de acción. La capa de acción tiene varios canales, como push, mensajes dentro de la aplicación, Catálogo Conectado, webhook, SMS y correo electrónico.]({% image_buster /assets/img/getting-started/braze_listen_understand_act.png %}){: style="display:block;margin:auto;" }

* [Ingesta de datos](#ingestion): Braze extrae datos de diversas fuentes.
* [Clasificación](#classification): Tu equipo de marketing segmenta dinámicamente tu base de usuarios utilizando estas métricas. 
* [Orquestación](#orchestration): Braze coordina de forma inteligente los mensajes a diferentes segmentos de audiencia en el momento ideal.
* [Acción](#action): Tu equipo de marketing actúa a partir de los datos, creando contenidos a través de diversos canales de mensajería, como los SMS y el correo electrónico.
* [Personalización](#personalization): Los datos se transforman en tiempo real con información personalizada sobre tu audiencia. 
* [Exportación](#exporting-data): Después, Braze hace un seguimiento de la interacción de tus usuarios con esta mensajería y la vuelve a introducir en la plataforma, creando un bucle. Obtendrás información sobre estos datos mediante informes y análisis en tiempo real.

Todo esto funciona conjuntamente para crear interacciones satisfactorias entre tu base de usuarios y tu marca, de modo que puedas alcanzar tus objetivos. Braze hace todo esto en el contexto de lo que llamamos nuestra pila integrada verticalmente. Profundicemos en cada capa, de una en una.

## Ingesta de datos {#ingestion}

Braze se basa en una arquitectura de datos de transmisión que aprovecha Snowflake, Kafka, MongoDB y Redis. Los datos de muchas fuentes pueden cargarse en Braze mediante SDK y API. La plataforma puede manejar cualquier dato en tiempo real, independientemente de cómo esté anidado o estructurado. Los datos en Braze se almacenan en el perfil de usuario. 

{% alert tip %}
Braze puede hacer un seguimiento de los datos de un usuario a lo largo de su trayecto contigo, desde que es anónimo hasta que inicia sesión en tu aplicación y es conocido. Los ID de usuario, llamados `external_id`s en Braze, deben establecerse para cada uno de tus usuarios. Deben ser inmutables y accesibles cuando un usuario abra la aplicación, permitiéndote hacer un seguimiento de tus usuarios en todos los dispositivos y plataformas. Consulta [el artículo Ciclo de vida del usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) para conocer las mejores prácticas.
{% endalert %}

![Braze importa fuentes de datos backend desde la API, fuentes de datos frontend desde el SDK, datos de almacén de datos desde la ingesta de datos en la nube de Braze y desde las integraciones de los socios. Estos datos se exportan a través de la API de Braze ]({% image_buster /assets/img/getting-started/import-export.png %}){: style="display:block;margin:auto;" }

{% alert note %}
Esta base de datos de perfiles de usuario centrada en la persona permite una velocidad interactiva en tiempo real. Braze precalcula los valores cuando llegan los datos y almacena los resultados en nuestro formato de documento ligero para una rápida recuperación. Y como la plataforma se diseñó así desde el principio, es ideal para la mayoría de los casos de uso de la mensajería, especialmente combinada con otros conceptos de datos como el contenido conectado, los catálogos de productos y los atributos anidados.
{% endalert %}

### Fuentes de datos backend a través de la API Braze
Braze puede extraer datos de bases de datos de usuarios, transacciones offline y almacenes de datos a través de nuestra [API REST]({{site.baseurl}}/api/endpoints/user_data). 

### Orígenes de datos frontend a través de Braze SDK
Braze captura automáticamente datos propios de fuentes de datos frontend, como los dispositivos de los usuarios, mediante el [SDK de Braze]({{site.baseurl}}/user_guide/getting_started/web_sdk/). El SDK gestiona los usuarios nuevos (anónimos) y administra los datos de su perfil de usuario a lo largo de su ciclo de vida. 

### Integraciones del socio
Braze tiene más de 150 socios tecnológicos, a los que llamamos "Alloys". Puedes complementar tus fuentes de datos mediante una red significativamente sólida de [tecnologías interoperables y API de datos.]({{site.baseurl}}/partners/home) 

### Conexión directa al almacén mediante la ingesta de datos en la nube de Braze
Puedes transmitir datos de clientes desde tu almacén de datos a la plataforma a través de [la ingesta de datos en la nube Braze]({{site.baseurl}}/user_guide/data/cloud_ingestion/) en sólo unos minutos, lo que te permitirá sincronizar los atributos, eventos y compras relevantes de los usuarios. La integración de la ingesta de datos en la nube admite estructuras de datos complejas, como JSON anidado y matrices de objetos.

La ingesta de datos en la nube puede sincronizar datos de Snowflake, Amazon Redshift, Databricks y Google BigQuery.

## Clasificación {#classification}
La capa de clasificación habilita a tu equipo para clasificar y construir dinámicamente audiencias, llamadas [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments), basándose en los datos que pasan por Braze. 

{% alert note %}
En las capas de clasificación, orquestación y personalización es donde tu equipo de marketing realizará gran parte de su trabajo. La mayoría de las veces interactúan con estas capas a través del panel de Braze, nuestra interfaz Web. Los desarrolladores tienen un papel en la configuración y personalización de estas capas.
{% endalert %}

Muchos tipos comunes de atributos de usuario, como el nombre, el correo electrónico, la fecha de nacimiento, el país y otros, son seguidos automáticamente por el SDK de forma predeterminada. Como desarrollador, trabajarás con tu equipo para definir qué datos adicionales y personalizados tiene sentido seguir para tu caso de uso. Tus datos personalizados influirán en cómo se clasificará y segmentará tu base de usuarios. Configurarás este modelo de datos durante el proceso de implementación. 

Más información sobre [datos recopilados automáticamente y datos personalizados]({{site.baseurl}}/developer_guide/analytics/).

## Orquestación {#orchestration}
La capa de orquestación permite a tu equipo de marketing diseñar recorridos de usuario basados en los datos de usuario y la interacción previa. Este trabajo se realiza principalmente a través de la interfaz de nuestro panel, pero también tienes la opción de lanzar [campañas a través de la API]({{site.baseurl}}/api/api_campaigns#api-campaigns). Por ejemplo, puedes hacer que tu backend le diga a Braze cuándo enviar los mensajes y campañas que tus especialistas en marketing diseñaron en el panel, y desencadenarlos según la lógica de tu backend. Un ejemplo de mensaje desencadenado por la API podrían ser los restablecimientos de contraseña o las confirmaciones de envío. 

{% alert note %}
Las campañas desencadenadas por la API son ideales para casos de uso transaccional más avanzados. Permiten a los especialistas en marketing gestionar la copia de la campaña, las pruebas multivariantes y las reglas de reelegibilidad dentro del panel Braze, a la vez que desencadenan la entrega de ese contenido desde tus servidores y sistemas. La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán al mensaje en tiempo real.
{% endalert %}


### Banderas de características
Braze te permite habilitar o deshabilitar a distancia la funcionalidad de una selección de usuarios mediante [banderas de características]({{site.baseurl}}/developer_guide/feature_flags/). Esto permite a tus especialistas en marketing dirigirse al segmento correcto de tu base de usuarios con mensajería para características que aún no has desplegado a toda tu audiencia. Pero, además, los indicadores de características pueden utilizarse para activar y desactivar una característica en producción sin necesidad de desplegar código adicional ni actualizar la tienda de aplicaciones. Esto te permite desplegar nuevas características con seguridad y confianza.

## Personalización {#personalization}
La capa de personalización representa la capacidad de entregar contenido dinámico en tus mensajes. Utilizando Liquid, un lenguaje de personalización muy extendido, tu equipo puede extraer dinámicamente los datos existentes para mostrar el mensaje adaptado a cada destinatario. Además, puedes insertar cualquier información accesible en tu servidor web o mediante API directamente en los mensajes que envíes, como notificaciones push o correos electrónicos, utilizando [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). El Contenido Conectado se basa en Liquid y utiliza una sintaxis familiar.

Y como este contenido dinámico es programable, los especialistas en marketing pueden incluir valores calculados, respuestas de otras llamadas o elementos del catálogo de productos. Una vez que hayas configurado estos sistemas durante la implementación, tu equipo de marketing podrá hacerlo sin apenas ayuda de los equipos técnicos. 

## Acción {#action}
La capa de acción habilita la mensajería real a tus usuarios. El objetivo de la capa de acción es enviar el mensaje adecuado al usuario adecuado en el momento adecuado, basándose en los datos disponibles a través de todas las capas comentadas anteriormente. La mensajería se realiza dentro de tu aplicación o sitio web (como el envío de mensajes dentro de la aplicación o a través de elementos gráficos como carruseles de tarjetas de contenido y pancartas) o fuera de tu experiencia de la aplicación (como el envío de notificaciones push o correos electrónicos).

### Canales de mensajería
Braze se diseñó para gestionar un panorama tecnológico en evolución con su modelo de datos centrado en el usuario e independiente del canal. El panel de control desencadena la entrega de mensajes y transacciones. Por ejemplo, tus especialistas en marketing pueden desencadenar un mensaje SMS ofreciendo un cupón para uno de tus escaparates recién abiertos cuando un usuario entre en la geovalla establecida cerca de esta ubicación, o enviar a un usuario un correo electrónico para informarle de que su programa favorito tiene una nueva temporada.

El [SDK de Braze]({{site.baseurl}}/user_guide/getting_started/web_sdk/) potencia canales de mensajería adicionales: push, mensajes dentro de la aplicación y tarjetas de contenido. Integras el SDK con tu aplicación o sitio web para permitir que tu equipo de marketing utilice el panel Braze para coordinar sus campañas en todos los canales de mensajería admitidos.

![]({% image_buster /assets/img/getting_started/channels.png %})

## Exportar datos
Fundamentalmente, todas las interacciones del usuario final con Braze son objeto de seguimiento para que puedas medir tu interacción y alcance. Después de que Braze haya agregado tus datos de todas estas fuentes, se pueden exportar de nuevo a tu pila tecnológica utilizando una variedad de herramientas, cerrando el bucle.

### Currents
[Currents]({{site.baseurl}}/user_guide/data/braze_currents/) es un complemento opcional de Braze que proporciona una exportación de streaming granular que alimenta continuamente otros destinos de tu pila. Currents es una fuente de datos brutos por usuario y evento que exporta datos cada cinco minutos o cada 15.000 eventos, lo que ocurra primero. Ejemplos de algunos destinos descendentes para Currents serían Segment, S3, Redshift y Mixpanel, entre otros. 

### Intercambio de datos Snowflake
La funcionalidad de [Compartición Segura de Datos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) de Snowflake permite a Braze darte acceso seguro a los datos de nuestro portal Snowflake sin preocuparte de las fricciones del flujo de trabajo, los puntos de fallo y los costes innecesarios que conllevan las típicas relaciones con los proveedores de datos. Todo el intercambio se realiza a través de la capa de servicios y el almacén de metadatos únicos de Snowflake: en realidad, no se copia ni se transfiere ningún dato entre cuentas. Se trata de un concepto importante porque los datos compartidos no ocupan almacenamiento en una cuenta de consumidor y, por tanto, no contribuyen a tus gastos mensuales de almacenamiento de datos. Lo único que se cobra a los consumidores son los recursos informáticos (es decir, los almacenes virtuales) utilizados para consultar los datos compartidos.

### API de exportación Braze
La API de Braze proporciona [puntos finales]({{site.baseurl}}/api/endpoints/export) que te permiten exportar mediante programación análisis agregados, así como exportar datos de usuario individuales. Estos datos pueden exportarse para audiencias y segmentos de cualquier tamaño. 

### CSVs
Por último, existe una opción para descargar tus datos a nivel agregado directamente desde el panel como [CSV]({{site.baseurl}}/user_guide/data/export_braze_data/). La opción CSV permite fácilmente a los miembros de tu equipo exportar datos desde Braze.

{% alert tip %}
Mientras que la exportación CSV tiene un límite base de 500.000 filas, las API no tienen límite en este sentido.
{% endalert %}

## Todo a la vez 
Uno de tus usuarios, llamémosle Mel, acaba de recibir el anuncio de tu producto. Entre bastidores, todas las capas de la plataforma Braze trabajaron juntas para garantizar que este proceso se desarrollara sin problemas. 

La información de Mel se introdujo en Braze desde tu plataforma heredada de interacción con los clientes mediante una importación CSV. Cada vez que Mel interactuaba con tu aplicación tras la integración, se añadían más datos a su perfil de cliente. 

El anuncio de tu producto se envió a todos los clientes a los que les gustó un artículo similar en tu aplicación. Has definido estos datos como un evento personalizado. El SDK hizo un seguimiento de este evento y segmentó tu base de usuarios en consecuencia. Braze orquestó la mejor hora del día para enviar este anuncio, y personalizó el anuncio llamando a Mel por su nombre preferido. 

Cuando Mel abre el anuncio, añade tu nuevo producto a su lista de deseos. Braze hace un seguimiento de que hizo clic en el correo electrónico automáticamente. El SDK hace un seguimiento de que ha incluido tu nuevo producto en la lista de deseos. Cada vez que interactúan con tu marca, tú y tus usuarios aprendéis más el uno del otro.

![]({% image_buster /assets/img/getting-started/putting-it-all-together.png %})



