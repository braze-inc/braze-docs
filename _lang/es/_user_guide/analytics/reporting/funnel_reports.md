---
nav_title: Informes de embudo
article_title: Informes de embudo para campañas y lonas
page_order: 6
page_type: reference
description: "Esta página explica las ventajas de los informes de embudo, cómo configurarlos y cómo interpretar tu informe."
tool: Reports
---

# Informes de embudo

> El informe de embudo ofrece un informe visual que te permite analizar los recorridos que realizan tus clientes tras recibir una campaña o Canvas. Informe de embudo 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si tu campaña o Canvas utiliza un grupo de control o múltiples variantes, puedes comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar basándote en estos datos.

\![Informe de embudo 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Configuración de los informes de embudo

\![Informe de embudo 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Puedes ejecutar informes de embudo para campañas activas existentes y Lienzos. Estos informes muestran una serie de eventos por los que progresa el destinatario de una campaña a lo largo de 1-30 días desde la fecha en que entra en el Canvas o en la campaña. Un usuario se considera convertido a través de un paso del embudo si realiza el evento en el orden especificado.

Los informes de embudo están disponibles en las siguientes ubicaciones del panel:

- La página de **análisis de campaña** de una campaña concreta
- La página **Detalles del** Canvas de un Canvas concreto, seleccionando el botón **Analizar variantes**. 

{% alert important %}
Los informes de embudo no están disponibles para las [campañas API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Paso 1: Selecciona un intervalo de fechas

Puedes seleccionar un marco temporal para tu informe (dentro de los últimos seis meses), y refinar los datos para ver los usuarios que, al entrar en la campaña o Canvas, completaron los eventos del embudo dentro de una ventana establecida (máximo de 30 días). En el siguiente ejemplo, tu embudo buscaría usuarios que recibieron esta campaña o Canvas en los últimos siete días y completaron el embudo en tres días.

{% alert note %}
Si estableces la ventana para completar el embudo en un día, entonces el evento del embudo debe producirse en las 24 horas siguientes a la recepción del mensaje. Sin embargo, si seleccionas varios días, la ventana de tiempo se cuenta como días naturales en la zona horaria de la empresa.
{% endalert %}

\![Informe de embudo para un Canvas con "Últimos 7 días" seleccionado en el desplegable de marco temporal.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Paso 2: Selecciona eventos para los pasos del embudo

Para cada informe de embudo, el primer evento es cuando el usuario recibe tu mensaje. A partir de ahí, los eventos posteriores que elijas embuten el número de usuarios que realizaron esos eventos, así como los eventos anteriores. 

#### Eventos disponibles del informe de embudo

| Campaña | Sesión Iniciada, Compra Realizada, Evento Personalizado Realizado, Evento de Interacción con Mensaje | Campaña | Sesión Iniciada, Compra Realizada, Evento Personalizado Realizado, Evento de Interacción con Mensaje | Campaña | Sesión Iniciada, Compra Realizada, Evento Personalizado Realizado, Evento de Interacción con Mensaje
| Canvas | Sesión Iniciada, Compra Realizada, Evento Personalizado Realizado, Paso en Canvas Recibido, Interacción con el Paso | Canvas
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
El evento de informe **Interactuado con Paso** sólo puede utilizarse con pasos en Canvas que utilicen los canales de mensajería correo electrónico o push.
{% endalert %}

\![Informe de embudo para un Canvas con un desplegable de los eventos de informe disponibles.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Los informes de embudo te permiten comparar el éxito de tus mensajes más allá de los eventos de conversión o de interacción de mensajes que configuraste inicialmente. Así que si hay un evento de conversión que no añadiste inicialmente, puedes seguir las conversiones de ese evento utilizando un embudo.

Por ejemplo, si seleccionas una ventana temporal de informe de 14 días, seguida de los eventos `Added to cart` y `Made purchase`, verás tanto el número de usuarios que añadieron a la cesta en los 14 días siguientes a la recepción del mensaje como el número de usuarios que añadieron a la cesta y luego realizaron una compra en los 14 días siguientes a la recepción de la campaña.

Como otro ejemplo, puede que quieras ver el porcentaje de usuarios que convirtieron un correo electrónico después de hacer clic en él. Para calcularlo, podrías crear un informe en el que el segundo evento sea hacer clic en tu correo electrónico y el tercero realizar tu evento de conversión.

Tras seleccionar **Crear informe**, el informe de embudo puede tardar varios minutos en generarse. Durante este tiempo, puedes navegar desde el informe a otras páginas del panel. Recibirás una notificación en el panel cuando tu informe esté listo.

## Interpretar tu informe de embudo

En tu informe de embudo, puedes comparar directamente el grupo de control con las variantes que hayas configurado. Cada evento consecutivo mostrará qué porcentaje de los usuarios anteriores completaron esa acción y se convirtieron a través del embudo.

### Componentes del informe de embudo

- **Eje horizontal**: Muestra el porcentaje de destinatarios de mensajes que realizaron esas acciones. 
- **Gráfico**: Muestra el número de mensajes recibidos, el número de usuarios que realizaron las acciones anteriores, así como la acción que elegiste, la tasa de conversión y el porcentaje de cambio respecto al control.
- **Opción Regenerar**: Te permite regenerar tu informe e indica cuándo se generó por última vez el informe actual. 
- **Variantes**: Denotado por columnas de colores, el informe de embudo permite hasta 8 variantes y un grupo de control. Por defecto, el **gráfico** sólo mostrará tres variantes. Para ver más, puedes seleccionar manualmente el resto de variantes.

Gráfico del informe de embudo.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para campañas con múltiples variantes**: Braze mostrará una tabla con las métricas de cada suceso y variante y el porcentaje de cambio respecto al control. La tasa de conversión es el número de usuarios que realizaron el evento (y los posteriores) por destinatario del mensaje.

**Para las campañas con reelegibilidad**: Si un usuario recibe la campaña más de una vez en la ventana de tiempo del informe, Braze determinará si el usuario debe incluirse en el embudo basándose en las acciones que este usuario realizó después de la primera vez que recibió la campaña dentro de la ventana de tiempo.
- Ten en cuenta que puede haber una discrepancia entre los valores del embudo y los de la conversión estándar, ya que los usuarios pueden convertir más de una vez si vuelven a ser elegibles, pero los informes de embudo convertirán un máximo de una vez aunque un usuario realice el evento más de una vez. 

**Para campañas multivariantes con reelegibilidad**: Si un usuario recibe múltiples variantes de la campaña durante la ventana de tiempo del informe, Braze determinará si deben incluirse en el embudo de variantes basándose en las acciones que este usuario realizó después de la primera vez que recibió la variante de campaña. Esto significa que el mismo usuario podría contar para múltiples variantes diferentes si recibiera múltiples variantes durante la ventana de tiempo del embudo.

{% alert important %}
Los usuarios huérfanos no son objeto de seguimiento en los informes de embudo. Cuando un usuario anónimo entra en un Canvas o en una campaña y más tarde se identifica a través del método `changeUser()`, su ID de Braze cambia. Los informes de embudo sólo registran los eventos de seguimiento que coinciden con el ID del usuario en el momento de la entrada y no tienen en cuenta los eventos realizados por el usuario después de cambiar su ID. Esto significa que los eventos de conversión realizados por el usuario después de identificarse no se incluirán en el informe de embudo.
{% endalert %}

