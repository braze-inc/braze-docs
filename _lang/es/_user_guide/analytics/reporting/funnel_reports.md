---
nav_title: Informes de embudo
article_title: Informes de embudo para campañas y lienzos
page_order: 6
page_type: reference
description: "Esta página explica las ventajas de los informes de embudo, cómo configurarlos y cómo interpretar tu informe."
tool: Reports
---

# Informes de embudo

> Los informes de embudo ofrecen un informe visual que le permite analizar los recorridos que realizan sus clientes tras recibir una campaña o Canvas. ![Informe de embudo 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Si su campaña o Canvas utiliza un grupo de control o múltiples variantes, puede comprender cómo las diferentes variantes han impactado en el embudo de conversión a un nivel más granular y optimizar en base a estos datos.

![Informe de embudo 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Configuración de los informes de embudo

![Informe de embudo 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Puede ejecutar informes de embudo para campañas activas existentes y Canvases. Estos informes muestran una serie de eventos por los que pasa el destinatario de una campaña a lo largo de 1-30 días desde la fecha en que entra en el Canvas o en la campaña. Un usuario se considera convertido a través de un paso del embudo si realiza el evento en el orden especificado.

Los informes de embudo están disponibles en las siguientes ubicaciones del panel:

- La página de **Análisis de Campaña** para una campaña específica
- La página **Detalles del Canvas** de un Canvas concreto, seleccionando el botón **Analizar variantes**. 

{% alert important %}
Los informes de embudo no están disponibles para [las campañas API]({{site.baseurl}}/api/api_campaigns/).
{% endalert %}

### Paso 1: Seleccione un intervalo de fechas

Puedes seleccionar un marco temporal para tu informe (dentro de los últimos seis meses), y refinar los datos para ver los usuarios que, al entrar en la campaña o Canvas, completaron los eventos del embudo dentro de una ventana establecida (máximo de 30 días). En el siguiente ejemplo, tu embudo buscaría usuarios que recibieron esta campaña o Canvas en los últimos siete días y completaron el embudo en tres días.

{% alert note %}
Si estableces la ventana para completar el embudo en un día, entonces el evento del embudo debe producirse en las 24 horas siguientes a la recepción del mensaje. Sin embargo, si selecciona varios días, la ventana de tiempo se cuenta como días naturales en la zona horaria de la empresa.
{% endalert %}

![Informe de embudo 5]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Paso 2: Seleccionar eventos para los pasos del embudo

Para cada informe de embudo, el primer evento es cuando el usuario recibe su mensaje. A partir de ahí, los eventos posteriores que elijas canalizan el número de usuarios que realizaron esos eventos, así como los eventos anteriores. Los eventos del informe de embudo tanto para los embudos de campaña como para los de Canvases permiten iniciar sesión, realizar una compra y eventos personalizados, mientras que sólo los embudos de campaña incluyen eventos de participación en el mensaje.

![Informe de embudo 3]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Los informes de embudo le permiten comparar el éxito de sus mensajes más allá de los eventos de conversión o de participación en el mensaje que configuró inicialmente. Por lo tanto, si hay un evento de conversión que no añadió inicialmente, todavía puede realizar un seguimiento de las conversiones para ese evento utilizando un embudo.

Por ejemplo, si selecciona una ventana temporal de informe de 14 días, seguida de los eventos `Added to cart` y `Made purchase`, verá tanto el número de usuarios que añadieron al carro en los 14 días siguientes a la recepción del mensaje como el número de usuarios que añadieron al carro y luego realizaron una compra en los 14 días siguientes a la recepción de la campaña.

Como otro ejemplo, es posible que desee ver el porcentaje de usuarios que convirtieron en un correo electrónico después de hacer clic en él. Para calcular esto, podría crear un informe en el que el segundo evento sea hacer clic en su correo electrónico y el tercer evento sea realizar su evento de conversión.

Tras seleccionar **Crear informe**, el informe de embudo puede tardar varios minutos en generarse. Durante este tiempo, puedes navegar desde el informe a otras páginas del panel. Recibirás una notificación en el salpicadero cuando tu informe esté listo.

## Interpretar el informe del embudo

En su informe de embudo, puede comparar directamente el grupo de control con las variantes que haya establecido. Cada evento consecutivo mostrará qué porcentaje de los usuarios anteriores completaron esa acción y convirtieron a través del embudo.

### Componentes del informe embudo

- **Eje horizontal**: Muestra el porcentaje de destinatarios de mensajes que realizaron esas acciones. 
- **Gráfico**: Muestra el número de mensajes recibidos, el número de usuarios que han realizado las acciones previas, así como la acción elegida, la tasa de conversión y el porcentaje de cambio con respecto al control.
- **Opción Regenerar**: Permite regenerar el informe e indica cuándo se generó por última vez el informe actual. 
- **Variantes**: Denotado por columnas de color, el informe de embudo permite hasta 8 variantes y un grupo de control. Por defecto, el **gráfico** sólo mostrará tres variantes. Para ver más, puede seleccionar manualmente el resto de variantes.

![Informe de embudo 4]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Para campañas con múltiples variantes**: Braze mostrará una tabla con las métricas de cada evento y variante y el porcentaje de cambio con respecto al control. La tasa de conversión es el número de usuarios que han realizado el evento (y los siguientes) por destinatario del mensaje.

**Para las campañas con reelegibilidad**: Si un usuario recibe la campaña más de una vez en la ventana de tiempo del informe, Braze determinará si el usuario debe incluirse en el embudo en función de las acciones que este usuario realizó después de la primera vez que recibió la campaña dentro de la ventana de tiempo.
- Tenga en cuenta que puede haber una discrepancia entre el embudo y los valores de conversión estándar, ya que los usuarios pueden convertir más de una vez con la re-elegibilidad, pero los informes de embudo convertirán un máximo de una vez, incluso si un usuario realiza el evento más de una vez. 

**Para campañas multivariantes con reelegibilidad**: Si un usuario recibe múltiples variantes de la campaña durante la ventana de tiempo del informe, Braze determinará si deben incluirse en el embudo de variantes en función de las acciones que este usuario realizó después de la primera vez que recibió la variante de la campaña. Esto significa que el mismo usuario podría contar para múltiples variantes diferentes si recibiera múltiples variantes durante la ventana de tiempo del embudo.

