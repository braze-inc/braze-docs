---
nav_title: Informes de embudo
article_title: Informes de embudo para campañas y Canvas
page_order: 6
page_type: reference
description: "Esta página explica las ventajas de los informes de embudo, cómo configurarlos y cómo interpretar tu informe."
tool: Reports
---

# Informes de embudo

> Los informes de embudo ofrecen un informe visual que te permite analizar los recorridos que realizan tus clientes tras recibir una campaña o Canvas. ![Informe de embudo 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si tu campaña o Canvas utiliza un grupo de control o múltiples variantes, puedes comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar en base a estos datos.

![Informe de embudo 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Configuración de los informes de embudo

![Informe de embudo 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Puedes ejecutar informes de embudo para campañas activas existentes y Canvas. Estos informes muestran una serie de eventos por los que pasa el destinatario de una campaña a lo largo de 1-30 días desde la fecha en que entra en el Canvas o en la campaña. Un usuario se considera convertido a través de un paso del embudo si realiza el evento en el orden especificado.

Los informes de embudo están disponibles en las siguientes ubicaciones del dashboard:

- La página de **Análisis de campaña** para una campaña específica
- La página **Detalles del Canvas** de un Canvas concreto, seleccionando el botón **Analizar variantes**

{% alert important %}
Los informes de embudo no están disponibles para [las campañas API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Paso 1: Selecciona un intervalo de fechas

Puedes seleccionar un marco temporal para tu informe (dentro de los últimos seis meses) y refinar los datos para ver los usuarios que, al entrar en la campaña o Canvas, completaron los eventos del embudo dentro de una ventana establecida (máximo de 30 días). En el siguiente ejemplo, tu embudo buscaría usuarios que recibieron esta campaña o Canvas en los últimos siete días y completaron el embudo en tres días.

{% alert note %}
Si estableces la ventana para completar el embudo en un día, entonces el evento del embudo debe producirse en las 24 horas siguientes a la recepción del mensaje. Sin embargo, si seleccionas varios días, la ventana de tiempo se cuenta como días naturales en la zona horaria de la empresa.
{% endalert %}

![Informe de embudo para un Canvas con "Últimos 7 días" seleccionado en el desplegable de marco temporal.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Paso 2: Selecciona eventos para los pasos del embudo

Para cada informe de embudo, el primer evento es cuando el usuario recibe tu mensaje. A partir de ahí, los eventos posteriores que elijas canalizan el número de usuarios que realizaron esos eventos, así como los eventos anteriores.

#### Eventos disponibles del informe de embudo

| Campaña | Sesión iniciada, Compra realizada, Evento personalizado realizado, Evento de interacción con mensaje |
| Canvas | Sesión iniciada, Compra realizada, Evento personalizado realizado, Paso en Canvas recibido, Interacción con el paso |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
El evento de informe **Interacción con el paso** solo puede utilizarse con pasos en Canvas que utilicen los canales de mensajería correo electrónico o push.
{% endalert %}

![Informe de embudo para un Canvas con un desplegable de los eventos de informe disponibles.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Los informes de embudo te permiten comparar el éxito de tus mensajes más allá de los eventos de conversión o de interacción con el mensaje que configuraste inicialmente. Por lo tanto, si hay un evento de conversión que no añadiste inicialmente, todavía puedes realizar un seguimiento de las conversiones para ese evento utilizando un embudo.

Por ejemplo, si seleccionas una ventana temporal de informe de 14 días, seguida de los eventos `Added to cart` y `Made purchase`, verás tanto el número de usuarios que añadieron al carrito en los 14 días siguientes a la recepción del mensaje como el número de usuarios que añadieron al carrito y luego realizaron una compra en los 14 días siguientes a la recepción de la campaña.

Como otro ejemplo, es posible que quieras ver el porcentaje de usuarios que convirtieron en un correo electrónico después de hacer clic en él. Para calcular esto, podrías crear un informe en el que el segundo evento sea hacer clic en tu correo electrónico y el tercer evento sea realizar tu evento de conversión.

Tras seleccionar **Crear informe**, el informe de embudo puede tardar varios minutos en generarse. Durante este tiempo, puedes navegar desde el informe a otras páginas del dashboard. Recibirás una notificación en el dashboard cuando tu informe esté listo.

## Interpretar tu informe de embudo

En tu informe de embudo, puedes comparar directamente el grupo de control con las variantes que hayas establecido. Cada evento consecutivo mostrará qué porcentaje de los usuarios anteriores completaron esa acción y convirtieron a través del embudo.

### Componentes del informe de embudo

- **Eje horizontal**: Muestra el porcentaje de destinatarios de mensajes que realizaron esas acciones. 
- **Gráfico**: Muestra el número de mensajes recibidos, el número de usuarios que realizaron las acciones previas, así como la acción elegida, la tasa de conversión y el porcentaje de cambio con respecto al control.
- **Opción de regenerar**: Permite regenerar el informe e indica cuándo se generó por última vez el informe actual. 
- **Variantes**: Representadas por columnas de color, el informe de embudo permite hasta 8 variantes y un grupo de control. Por defecto, el **gráfico** solo mostrará tres variantes. Para ver más, puedes seleccionar manualmente el resto de variantes.

![Gráfico del informe de embudo.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para campañas con múltiples variantes**: Braze mostrará una tabla con las métricas de cada evento y variante y el porcentaje de cambio con respecto al control. La tasa de conversión es el número de usuarios que realizaron el evento (y los siguientes) por destinatario del mensaje.

**Para campañas con reelegibilidad**: Si un usuario recibe la campaña más de una vez en la ventana de tiempo del informe, Braze determinará si el usuario debe incluirse en el embudo en función de las acciones que este usuario realizó después de la primera vez que recibió la campaña dentro de la ventana de tiempo.
- Ten en cuenta que puede haber una discrepancia entre el embudo y los valores de conversión estándar, ya que los usuarios pueden convertir más de una vez con la reelegibilidad, pero los informes de embudo convertirán un máximo de una vez, incluso si un usuario realiza el evento más de una vez. 

**Para campañas multivariantes con reelegibilidad**: Si un usuario recibe múltiples variantes de la campaña durante la ventana de tiempo del informe, Braze determinará si deben incluirse en el embudo de variantes en función de las acciones que este usuario realizó después de la primera vez que recibió la variante de campaña. Esto significa que el mismo usuario podría contar para múltiples variantes diferentes si recibió múltiples variantes durante la ventana de tiempo del embudo.

{% alert important %}
Los usuarios huérfanos no son objeto de seguimiento en los informes de embudo. Cuando un usuario anónimo entra en un Canvas o en una campaña y más tarde se identifica a través del método `changeUser()`, su ID de Braze cambia. Los informes de embudo solo registran los eventos de seguimiento que coinciden con el ID de usuario en el momento de la entrada y no tienen en cuenta los eventos realizados por el usuario después de cambiar su ID. Esto significa que los eventos de conversión realizados por el usuario después de identificarse no se incluirán en el informe de embudo.
{% endalert %}

## Preguntas frecuentes

### ¿Por qué los análisis del Canvas son diferentes a los del informe de embudo?

Los análisis a nivel de paso en Canvas y los informes de embudo utilizan reglas de alcance diferentes para el mismo intervalo de fechas, por lo que no se espera que coincidan. Las diferencias se reducen a cómo cada informe define "qué eventos cuentan".

**Análisis de Canvas (Analizar variantes):** El intervalo de fechas filtra los eventos por **cuándo ocurrieron**. Si seleccionas del 1 al 7 de enero, verás todas las entradas y eventos de conversión que ocurrieron durante esa ventana, independientemente de cuándo el usuario entró en el Canvas. Un usuario que entró el 1 de enero pero convirtió el 8 de enero mostraría una entrada y cero conversiones, porque la conversión quedó fuera de las fechas seleccionadas. La ventana de conversión configurada en el paso del Canvas también puede extenderse mucho más allá de 14 días, por lo que los análisis a nivel de paso pueden capturar conversiones en un horizonte más largo.

**Informes de embudo:** El intervalo de fechas filtra a los usuarios por **cuándo entraron** en el Canvas. Si seleccionas del 1 al 7 de enero, el informe incluye a todos los usuarios que entraron durante esa ventana y luego rastrea sus acciones durante hasta 14 días después de la entrada (o la ventana que configures en el embudo). El mismo usuario que entró el 1 de enero y convirtió el 8 de enero mostraría una entrada y una conversión, porque la conversión ocurrió dentro de la ventana posterior a la entrada.

Además, los informes de embudo requieren que los eventos ocurran en el orden especificado y cuentan a cada usuario como máximo una vez, mientras que los análisis de Canvas cuentan todas las conversiones e interacciones sin una restricción de orden.