---
nav_title: "Datos de interacción de mensajería"
article_title: "Datos de interacción de mensajería"
permalink: "/messaging_interaction_data/"
hidden: true
---

# Acerca de la disponibilidad de los datos de la interacción de mensajería

> Este artículo contiene información sobre los datos de interacción de campañas y Canvas y su disponibilidad.

### ¿Qué son los datos de interacción de la mensajería?

Los datos de interacción de mensajería se refieren a cómo interactúa un usuario con una campaña o Canvas que ha recibido (por ejemplo, cuando un usuario abre la campaña A o un usuario recibe la variante A). Estos datos se utilizan para reorientar.

{% alert important %}
A partir de principios de 2024, los datos de interacción de mensajería estarán disponibles según el proceso aquí descrito.
{% endalert %}

### ¿Cuándo están disponibles los datos de interacción de la mensajería?

Los datos de interacción están siempre disponibles. Para las campañas activas y los Lienzos, los datos de interacción están siempre disponibles en tiempo real. 

Para las campañas paradas y los Lienzos, sus datos de interacción caducan a los tres meses, a menos que se utilicen en filtros de reorientación por campañas activas o Lienzos. Los datos de interacción caducados se trasladan al almacenamiento a largo plazo y no están disponibles para su uso a menos que se restauren mediante el proceso descrito a continuación.

Los datos de interacción caducados nunca se borran y se pueden recuperar en cualquier momento.

#### Características que utilizan datos de interacción

Las siguientes características utilizan datos de interacción de mensajería:

- Filtros de reorientación que reorientan a una campaña o Canvas específico
    - Alias al que se hizo clic en la campaña
    - Alias en que se hizo clic en paso en Canvas
    - Campaña que se abrió o a la que se hizo clic
    - Paso que se abrió o en el que se hizo clic
    - Convertido desde campaña
    - Convertido desde Canvas
    - Variación de Canvas ingresada
    - Grupo de control en campaña
    - Grupo de control en Canvas
    - Último mensaje recibido de una campaña concreta
    - Último mensaje recibido de un paso de Canvas concreto
    - Variante de campaña recibida
    - Mensaje recibido de una campaña
    - Mensaje recibido de un paso en Canvas
- Filtros de reorientación que reorientan en campañas o Canvas de una etiqueta determinada
    - Mensaje recibido de una campaña o Canvas con etiqueta
    - Campaña o Canvas que se abrió o en la que se hizo clic con etiqueta
    - Último mensaje recibido de una campaña o de Canvas con una etiqueta concreta
- Listas de **campañas recibidas** y **mensajes recibidos de** Canvas en el perfil de usuario
- punto final `/users/export`
- Exportación CSV de **datos de usuario** en las páginas de resumen de campaña y Canvas

Estas características no incluirán datos de interacciones caducadas en sus resultados. Para incluir datos de interacción caducados en los resultados de estas características, restaura la campaña o el Canvas con datos caducados.

#### Características que no utilizan datos de interacción

Las siguientes características **no** utilizan datos de interacción de mensajería, lo que significa que estas características no se ven afectadas por la expiración de los datos de interacción de mensajería:

- Configuración de la campaña y Canvas
- Análisis de campañas y Canvas
- Informes de análisis (como el generador de informes, el generador de consultas y los informes de interacción)
- Currents
- Compartir datos Snowflake
- Extensiones de segmento
- Puntos de datos
- Los siguientes filtros de reorientación:
    - Alias con clic en cualquier campaña o paso en Canvas
    - Conmutador de características
    - Rebote duro
    - Te marcó como correo no deseado
    - Jamás recibió un mensaje de campaña o de paso en Canvas
    - Número de teléfono no válido
    - Última interacción con un mensaje
    - Últimos inscritos en cualquier grupo de control
    - Última impresión de un mensaje dentro de la aplicación
    - Último mensaje recibido
    - Último correo electrónico recibido 
    - Última notificación emergente recibida
    - Último SMS recibido
    - Último webhook recibido
    - Último WhatsApp recibido
    - Última categoría enviada de palabras clave entrantes de SMS específicas
    - Última fuente de noticias vista
    - Recuento de visualizaciones del canal de noticias

### ¿Cómo restauro los datos de interacción de la mensajería?

Para restaurar tus datos de interacción, sigue estos pasos:

1. Ve a la campaña caducada o a Canvas.
2. En la parte superior de la página de destino de la campaña o de Canvas, haz clic en **Restaurar datos de interacción** en el banner.

![][1]

También puedes restaurar los datos de interacción de varias campañas desde la página Campañas, seleccionando las campañas y haciendo clic en el botón Restaurar datos de interacción.

El tiempo que se tarda en restaurar los datos de interacción varía, pero en la mayoría de los casos, este proceso puede durar entre 5 y 15 minutos. Recibirás un correo electrónico una vez finalizado el restablecimiento.

#### Restaurar por etiqueta

También puedes restaurar los datos de interacción de campañas caducadas o Lienzos con una etiqueta determinada.

1. Ve a la página de **Campañas** o **Canvas** y busca por la etiqueta correspondiente.
2. Selecciona tus campañas o Lienzos.
3. Selecciona **Restaurar datos de interacción** para restaurar los datos de esas campañas o Lienzos.

Tras otros tres meses de inactividad, estas campañas o Lienzos volverán a caducar.

#### Reorientación por etiqueta

Las campañas que utilizan filtros de reorientación por etiqueta no están exentas de caducidad. Los filtros de reorientación que reorientan por etiqueta incluyen:

- Mensaje recibido de una campaña o Canvas con etiqueta
- Campaña o Canvas que se abrió o en la que se hizo clic con etiqueta
- Último mensaje recibido de una campaña o de Canvas con una etiqueta concreta

### ¿Cuándo estuvieron disponibles los datos de interacción de mensajería en el pasado?

Antes, los datos de interacción de los mensajes se borraban cuando una campaña o Canvas:
- No había enviado mensajes en 25 meses de calendario, Y
- No se utilizó para reorientar en ninguna campaña activa, Lienzos o Tarjetas de contenido.

Las campañas y los lienzos con datos de interacción de mensajería previamente eliminados no pueden utilizarse en filtros de reorientación para campañas, lienzos y segmentos.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
