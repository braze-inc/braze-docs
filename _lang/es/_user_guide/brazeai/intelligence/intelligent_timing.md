---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "Este artículo ofrece un resumen de Intelligent Timing (antes Entrega Inteligente) y de cómo puedes aprovechar esta característica en tus campañas y Lienzos."

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Utiliza Intelligent Timing para entregar tu mensaje a cada usuario cuando Braze determine que es más probable que ese usuario interactúe (abra o haga clic), lo que se conoce como su hora óptima de envío. Esto te facilita comprobar que estás enviando mensajes a tus usuarios a su hora preferida, lo que puede conducir a una mayor interacción.

## 

Braze calcula la hora óptima de envío basándose en un análisis estadístico de las interacciones anteriores de tus usuarios con tu aplicación, y de sus interacciones con cada canal de mensajería. Se utilizan los siguientes datos de interacción: 

- Horario de las sesiones
- Push Direct Opens
- Push Influenced Opens
- Clics en correos electrónicos
- 

Por ejemplo, Sam puede abrir tus correos electrónicos por la mañana con regularidad, pero abre tu aplicación e interactúa con las notificaciones por la tarde. Eso significa que Sam recibiría una campaña por correo electrónico con Intelligent Timing por la mañana, mientras que recibiría campañas con notificaciones push por la tarde, cuando es más probable que interactúe.



## Casos prácticos

- Envía campañas recurrentes sin límite de tiempo
- Automatización de campañas con usuarios de múltiples zonas horarias
- Cuando envíes mensajes a tus usuarios más interactivos (ellos tendrán la mayor cantidad de datos de interacción)

## Utilizar Intelligent Timing

Esta sección describe cómo configurar Intelligent Timing para tus campañas y Lienzos.



###  

1. Crea una campaña y redacta tu mensaje.
2. 
3. En **Opciones de programación temporal**, selecciona **Temporización inteligente**.
4.    
5. 
6.  En este momento se enviará el mensaje si el perfil de un usuario no tiene suficientes datos para calcular un tiempo óptimo.



#### 

 


  


1. 
2. 



 



#### Vista previa de los plazos de entrega

Para ver una estimación de cuántos usuarios recibirán el mensaje en cada hora del día, utiliza el gráfico de vista previa (sólo campañas).

1. Añade segmentos o filtros en el paso Audiencias objetivo.
2. En la sección **Vista previa de horas de entrega para** (que aparece tanto en los pasos Audiencias objetivo como en Programar entrega), selecciona tu canal.
3. Haz clic en **Actualizar datos**.



###  

 

#### 

Lanza tu campaña al menos 48 horas antes de la fecha de envío programada. Esto se debe a las variaciones en las zonas horarias. Braze calcula la hora óptima a medianoche en la hora de Samoa (UTC+13), uno de los primeros husos horarios del mundo. Un solo día abarca unas 48 horas en todo el mundo, lo que significa que si lanzas una campaña dentro de ese margen de 48 horas, es posible que la hora óptima de un usuario ya haya pasado en su zona horaria, y el mensaje no se envíe.

{% alert important %}
Si se lanza una campaña y el tiempo óptimo de un usuario es inferior a una hora en el pasado, el mensaje se envía inmediatamente. Si la hora óptima ha pasado más de una hora, el mensaje no se envía.
{% endalert %}

#### 

Si te diriges a una audiencia que ha realizado una acción en un periodo de tiempo determinado, deja al menos un margen de 3 días en tus filtros de segmento. 



Esto también se debe a las zonas horarias: seleccionar un periodo inferior a 3 días puede hacer que algunos usuarios salgan del segmento antes de alcanzar su hora óptima de envío.

 

#### 



  



###  

  

 



1. Al configurar Intelligent Timing, selecciona **Sólo enviar mensajes en horas concretas**.
2. Introduce la hora de inicio y fin de la ventana de entrega.



###  







###  Vista previa de los plazos de entrega



1. Añade segmentos o filtros en el paso Audiencias objetivo.
2. En la sección **Vista previa de horas de entrega para** (que aparece tanto en los pasos Audiencias objetivo como en Programar entrega), selecciona tu canal.
3. 



Siempre que cambies cualquier configuración sobre Intelligent Timing o la audiencia de tu campaña, actualiza de nuevo los datos para ver un gráfico actualizado.

El gráfico muestra en azul a los usuarios que tenían datos suficientes para calcular una hora óptima y en rojo a los usuarios que utilizarán la hora alternativa. Utiliza los filtros de cálculo para ajustar la vista previa y obtener una visión más granular de cualquiera de los grupos de usuarios.
{% endtab %}



 


###  



  Los pasos de mensajes que se dirigen a varios canales pueden enviar o intentar enviar mensajes en momentos diferentes para canales diferentes. Cuando se intenta enviar el primer mensaje en un paso de Mensajería, se avanza automáticamente a todos los usuarios.

###  



###  





####  

 

- **Días:** 1 día son 24 horas, calculadas desde que el usuario entra en el paso Retraso.
- **Días del calendario:** 1 día es el periodo que transcurre desde que el usuario introduce el paso Retraso hasta medianoche en su zona horaria. Esto significa que 1 día natural puede ser tan corto como unos minutos.

Cuando utilices Intelligent Timing, te recomendamos que utilices días naturales para tus retrasos en lugar de días de 24 horas. Esto se debe a que con los días del calendario, el mensaje se enviará el último día del retraso, a la hora óptima. Con un día de 24 horas, existe la posibilidad de que la hora óptima del usuario sea antes de entrar en el paso, lo que significa que se añadirá un día más a su retraso.

Por ejemplo, supongamos que la hora óptima de Luka son las 14:00 h. Entra en el paso Retraso a las 14:01 del 1 de marzo, y el retraso se establece en 2 días.

- El día 1 termina el 2 de marzo a las 14:01 h
- El día 2 termina el 3 de marzo a las 14:01 horas

Sin embargo, Intelligent Timing está configurado para entregar a las 14 h, que ya ha pasado. Así que Luka no recibirá el mensaje hasta el día siguiente: 4 de marzo a las 14:00 h.

![Gráfico que muestra la diferencia entre días y días de calendario, en el que si la hora óptima de un usuario son las 14:00, pero entra en el paso de retraso a las 14:01 y el retraso se establece en 2 días. Días entrega el mensaje 3 días más tarde porque el usuario entró en el paso después de su hora óptima, mientras que días calendario entrega el mensaje 2 días más tarde, en el último día de retraso.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}



## Limitaciones

- Los mensajes dentro de la aplicación, las tarjetas de contenido y los webhooks se entregan inmediatamente y no se les da un tiempo óptimo.
- Intelligent Timing no está disponible para campañas basadas en acciones o desencadenadas por API.
- Intelligent Timing no debe utilizarse en los siguientes casos:
    - **Límite de velocidad:** Si se utilizan tanto el límite de tasa como el Intelligent Timing, no hay garantías sobre cuándo se entregará el mensaje. Las campañas recurrentes diarias con Intelligent Timing no admiten con precisión un tope total de envío de mensajes.
    - **Campañas de calentamiento de IP:** Algunos comportamientos de Intelligent Timing pueden causar dificultades para alcanzar los volúmenes diarios necesarios cuando estás calentando tu IP por primera vez. Esto se debe a que Intelligent Timing evalúa los segmentos dos veces: una vez cuando se crea por primera vez la campaña o el Canvas, y otra vez antes de enviarlos a los usuarios para verificar que deben seguir estando en ese segmento. Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. Estos usuarios no se reemplazan, lo que afecta a lo cerca del tope máximo de usuarios que puedes llegar.

## Solución de problemas

### Gráfico de vista previa que muestra pocos usuarios con tiempos óptimos

Braze necesita una cierta cantidad de datos de interacción para hacer una buena estimación. Si no hay suficientes datos de sesión o los usuarios objetivo tienen pocos o ningún clic o apertura (como los nuevos usuarios), Braze predeterminará el tiempo de espera. Dependiendo de tu configuración, podría ser la hora de la aplicación más popular o una hora alternativa personalizada.

### Envío fuera de plazo

Tu campaña de Intelligent Timing podría estar enviándose más allá de la fecha programada si estás aprovechando las [pruebas A/B con una optimización]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/). Las campañas que utilizan optimizaciones de pruebas A/B pueden enviar automáticamente la variante ganadora una vez finalizada la prueba inicial, lo que aumenta la duración de la campaña. Por defecto, las campañas con una optimización enviarán la variante ganadora a los usuarios restantes al día siguiente de la prueba inicial, pero puedes cambiar esta fecha de envío.

Si utilizas Intelligent Timing, te recomendamos dejar más tiempo para que finalice la prueba A/B y programar el envío de la Variante Ganadora para 2 días después de la prueba inicial en lugar de 1 día.

## 

### 

#### 



#### 

  

### 

#### 



1.  
  - Horario de las sesiones
  - 
  - 
  - 
  - 
2. 

#### 

 

#### 

   

#### 

 

### Campañas

#### 

   

#### 

   

#### 

  

 

### 

#### 



1.  
2.  

  

#### 

  

####  

 

#### 

  



#### 

  

Esto puede hacer que los segmentos se desplacen y cambien, lo que a menudo hace que algunos usuarios salgan del segmento en la segunda evaluación. 

#### 

 

#### 



#### 

   



