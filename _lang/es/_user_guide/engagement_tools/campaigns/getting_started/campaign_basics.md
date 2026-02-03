---
nav_title: Conceptos básicos de la campaña
article_title: Conceptos básicos de la campaña
page_order: 1
page_type: reference
description: "Este artículo de referencia abarca los aspectos básicos de las campañas, cubriendo varias preguntas que deberías plantearte a la hora de configurar tus primeras campañas."
tool: Campaigns

---

# Conceptos básicos de las campañas

> Este artículo de referencia abarca los aspectos básicos de las campañas, cubriendo varias preguntas que deberías plantearte a la hora de configurar tus primeras campañas.

## Comprender la estructura de la campaña

Antes de empezar con los detalles más sutiles de la configuración de campañas, identifiquemos los detalles clave para entender cómo funcionan las campañas en los distintos canales de mensajería.

Las campañas son un paso de mensaje único para conectar con sus usuarios en canales, o más comúnmente denominados canales de mensajería. Estos canales de mensajería incluyen tarjetas de contenido, correo electrónico, mensajes dentro de la aplicación, push, SMS y MMS, y webhooks. Si sabe dónde residen sus clientes, podrá aprovechar los canales de mensajería adecuados para comunicarse.

## Construir el recorrido del cliente

Dado que las campañas pueden construirse de forma única en función del canal de mensajería, puede utilizar estas cinco W de visualización para ayudar a identificar y conceptualizar sus estrategias y objetivos de captación de clientes.

### El "qué": Ponle nombre a tu campaña

> ¿Qué intenta ayudar al usuario a hacer o entender?

Nunca subestimes el poder del nombre. Braze está concebido para la colaboración, por lo que es un momento excelente para poner los cimientos de cómo comunicarás los objetivos a tu equipo. Para obtener más información sobre los recorridos del cliente, consulte nuestro curso de Braze Learning [Mapping User Lifecycles](https://learning.braze.com/mapping-customer-lifecycles).

### El "cuándo": Crear condiciones de partida

> ¿Cuándo se encontrará un cliente con esta campaña? 

Los usuarios pueden entrar en su campaña de tres maneras: en una fecha y hora determinadas (programada), cuando realizan una acción específica (basada en acciones) o cuando hacen algo que activa una llamada a la API (activada por la API). 

La entrega programada consiste en ajustar sus campañas para que se envíen a una hora específica y, opcionalmente, durante una cadencia determinada. Las campañas basadas en acciones responden a comportamientos específicos de los clientes en tiempo real. Esto puede incluir realizar una compra o interactuar con otra campaña. Las campañas activadas por API pueden configurarse para determinar acciones clave de los clientes en su plataforma que, cuando se realicen, activarán una llamada de API a Braze y enviarán sus campañas.

### El "quién": Selecciona una audiencia de entrada

> ¿A quién quieres llegar? 

Puede utilizar [segmentos predefinidos]({{site.baseurl}}/user_guide/engagement_tools/segments) para dirigirse a los usuarios en función de sus características y acciones demográficas, de comportamiento o técnicas. Añada más filtros al crear su campaña para adaptar aún más su segmento. Solo los usuarios que coincidan con estos criterios de audiencia objetivo pueden entrar en el recorrido. Consulte esta tabla para obtener un resumen rápido de los tipos de filtro disponibles.

| Filtro | Descripción |
|---|---|
| Datos personalizados | Segmente a los usuarios en función de los eventos y atributos que defina. Puede utilizar características específicas de su producto. |
| Actividad del usuario | Segmente a los clientes en función de sus acciones y compras. |
| Reorientación | Segmente a los clientes que hayan enviado, recibido o interactuado con campañas anteriores. |
| Actividad de marketing | Segmente a los clientes en función de comportamientos universales como el último compromiso o las campañas recibidas. |
| Atributos del usuario | Segmentar a los clientes por sus atributos y características constantes. |
| Atribución de instalación | Segmente a los clientes por su primera fuente, grupo de anuncios, campaña o anuncio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### El "por qué": Identificar eventos de conversión

> ¿Por qué haces esta campaña? 

Siempre es importante tener un objetivo definido en mente, y las campañas le ayudan a comprender su rendimiento con respecto a KPI como la participación en la sesión, las compras y los eventos personalizados. La selección de al menos un [evento de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) le permitirá comprender el rendimiento de su campaña.

### El "dónde": Encontrar mi público

> ¿Dónde puedo llegar mejor a mi público?

Aquí es donde determinamos qué canales de mensajería tienen más sentido para el recorrido de tu usuario. Lo ideal es llegar a los usuarios allí donde son más activos.

### El "cómo": Construir la experiencia

> ¿Cómo construyo mi campaña después de identificar las cinco W?

Considere la posibilidad de establecer variantes y pruebas A/B a medida que vaya adquiriendo más experiencia en la creación de campañas. Tenga en cuenta que las campañas admiten hasta ocho variantes con un grupo de control. Utilice los análisis de su campaña para tomar decisiones con conocimiento de causa a medida que construye su campaña, ajustando cualquier cosa, desde su audiencia segmentada hasta el contenido real de su mensaje.

