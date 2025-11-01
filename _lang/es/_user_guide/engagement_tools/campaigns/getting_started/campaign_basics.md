---
nav_title: Conceptos básicos de la campaña
article_title: Conceptos básicos de la campaña
page_order: 1
page_type: reference
description: "Este artículo de referencia trata de los aspectos básicos de las campañas, y aborda varias preguntas que debes plantearte al configurar tus primeras campañas."
tool: Campaigns

---

# Conceptos básicos de las campañas

> Este artículo de referencia trata de los aspectos básicos de las campañas, y aborda varias preguntas que debes plantearte al configurar tus primeras campañas.

## Comprender la estructura de la campaña

Antes de empezar con los detalles más sutiles de la configuración de campañas, vamos a identificar los detalles clave para comprender cómo funcionan las campañas en los distintos canales de mensajería.

Las campañas son un paso de mensaje único para conectar con tus usuarios en canales, o más comúnmente denominados canales de mensajería. Estos canales de mensajería incluyen tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push, SMS y MMS, y webhooks. Al comprender dónde residen tus clientes, puedes aprovechar los canales de mensajería adecuados para comunicarte.

## Construir el recorrido del cliente

Dado que las campañas pueden construirse de forma única en función del canal de mensajería, puedes utilizar estas cinco W de visualización para ayudarte a identificar y conceptualizar tus estrategias de interacción con los clientes y tus objetivos.

### El "qué": Ponle nombre a tu campaña

> ¿Qué intentas ayudar al usuario a hacer o entender?

Nunca subestimes el poder del nombre. Braze está hecho para la colaboración, así que éste es un momento excelente para poner los cimientos de cómo comunicarás los objetivos a tu equipo. Para saber más sobre los recorridos del cliente, ¡consulta nuestro curso de Braze Learning [sobre Mapeado del ciclo de vida del usuario](https://learning.braze.com/mapping-customer-lifecycles)!

### El "cuándo": Crear condiciones de partida

> ¿Cuándo se encontrará un cliente con esta campaña? 

Los usuarios pueden entrar en tu campaña de tres formas: en una fecha y hora determinadas (programada), cuando realizan una acción específica (basada en la acción) o cuando hacen algo que desencadena una llamada a la API (desencadenada por la API). 

La entrega programada consiste en ajustar tus campañas para que se envíen a una hora concreta y, opcionalmente, con una cadencia determinada. Las campañas basadas en la acción responden a comportamientos específicos del cliente en tiempo real. Esto puede incluir realizar una compra o interactuar con otra campaña. Las campañas desencadenadas por API pueden configurarse para determinar acciones clave de los clientes en tu plataforma que, cuando se consigan, desencadenarán una llamada de API a Braze y enviarán tus campañas.

### El "quién": Selecciona una audiencia de entrada

> ¿A quién quieres llegar? 

Puedes utilizar [segmentos prede]({{site.baseurl}}/user_guide/engagement_tools/segments) finidos para dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento o técnicas. Añade más filtros al crear tu campaña para adaptar aún más tu segmento. Sólo los usuarios que coincidan con estos criterios de audiencia objetivo pueden entrar en el viaje. Consulta esta tabla para obtener un resumen rápido de los tipos de filtros disponibles.

| Filtrar | Descripción |
|---|---|
| Datos personalizados | Segmenta a los usuarios en función de los eventos y atributos que definas. Puedes utilizar características específicas de tu producto. |
| Actividad del usuario | Segmenta a los clientes en función de sus acciones y compras. |
| Reorientación | Segmenta a los clientes que hayan enviado, recibido o interactuado con campañas anteriores. |
| Actividad de marketing | Segmenta a los clientes en función de comportamientos universales como la última interacción o las campañas recibidas. |
| Atributos del usuario | Segmenta a los clientes por sus atributos y características constantes. |
| Atribución de instalación | Segmenta a los clientes por su primera fuente, grupo de anuncios, campaña o anuncio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### El "por qué": Identificar eventos de conversión

> ¿Por qué haces esta campaña? 

Siempre es importante tener un objetivo definido en mente, y las campañas te ayudan a comprender tu rendimiento en relación con los KPI, como la interacción con las sesiones, las compras y los eventos personalizados. Seleccionar al menos un [evento de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) te permitirá comprender el rendimiento de tu campaña.

### El "dónde": Encontrar mi audiencia

> ¿Dónde puedo llegar mejor a mi audiencia?

Aquí es donde determinamos qué canales de mensajería tienen más sentido para el recorrido de tu usuario. Lo ideal sería llegar a tus usuarios allí donde son más activos.

### El "cómo": Construye la experiencia

> ¿Cómo construyo mi campaña después de identificar las cinco W?

Considera la posibilidad de configurar variantes y pruebas A/B a medida que te familiarices con la creación de campañas. Ten en cuenta que las campañas admiten hasta ocho variantes con un grupo de control. Utiliza los análisis de tu campaña para tomar decisiones informadas a medida que construyes tu campaña, ajustando cualquier cosa, desde tu audiencia segmentada hasta el contenido real de tu mensajería.

