---
nav_title: Campañas de usuarios activos
article_title: Campañas de usuarios activos
page_order: 0.5
page_type: tutorial
description: "Este artículo describe las ventajas de las campañas de usuario activo en el panel de Braze y los pasos para crear y configurar una."
tool: 
  - Campaigns

---

# Campañas de usuarios activos

> Identifica a tus usuarios activos para ayudarte a hacer campañas a medida y recompensa a los que frecuentan tu plataforma. 

Llegar a los usuarios ya activos de tu aplicación puede ser una herramienta poderosa para ayudar a crear un grupo de usuarios constantes. Un poco de reconocimiento personalizado de tus usuarios avanzados puede convertirlos en evangelizadores de tu aplicación.

También puedes consultar nuestro [curso de Braze](https://learning.braze.com/quick-overview-segment-and-campaign-setup) Learning sobre estrategia de correo electrónico y campañas según el ciclo de vida recomendadas.

## Comprender a los usuarios activos

Braze define un "usuario activo" para un periodo de tiempo determinado como cualquier usuario que tenga una sesión en ese periodo de tiempo.

Si un usuario pierde la conectividad, almacenaremos en caché los datos de la sesión localmente y los cargaremos cuando el usuario recupere la conexión a la red. Estas sesiones también se aplicarán al recuento de usuarios activos. Además, si tu aplicación tiene un proceso de registro, Braze contará a todos los usuarios como activos-registrados o no registrados.

Si configuras ID de usuario para identificar a los usuarios, cuando un nuevo usuario se conecte se contará como un usuario activo distinto. Los usuarios que se actualicen a través de la API también se contarán como usuarios activos en el periodo de tiempo en que se actualicen.

## Paso 1: Identificar a tus principales usuarios

Utilizando nuestra selección de filtros, crea un segmento de usuarios que consideres que engloba a tu base de usuarios más fieles y constantes. El siguiente segmento de muestra define a los principales usuarios.

\![]({% image_buster /assets/img_archive/define_top_users.png %} "Define your top users")

Además, no tendrás que seguir actualizando este segmento, ya que a los usuarios que entren o salgan de las restricciones de la campaña se les aplicará o descartará correspondientemente.

{% alert note %}
El ejemplo anterior segmenta a los usuarios según el uso general de la aplicación. En la mayoría de los casos, la colección total de filtros necesarios para definir tu segmento de usuarios principales vendrá definida en gran medida por las particularidades de tu aplicación.
{% endalert %}

## Paso 2: Llega a tus principales usuarios

### Haz que tus usuarios se sientan apreciados

Haz que tus usuarios se sientan apreciados agradeciéndoles su fidelización y dedicación a tu aplicación. Da a tus usuarios más razones para volver a tu aplicación y fomentar así su actividad. Esto puede adoptar la forma de ofertas especiales o bonificaciones exclusivas para tus principales usuarios. 

Las recompensas inesperadas pueden ser más eficaces para animar a los usuarios a seguir actuando que si se las hubieras prometido desde el principio.

Una campaña en el paso Redactar con una notificación enriquecida de iOS que dice: "¡Gracias de nuevo por comprar con nosotros! Para mostrarte nuestro agradecimiento, te regalamos los gastos de envío de tu próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Haz un seguimiento de tus resultados

Haz un seguimiento de las aperturas para asegurarte de que te diriges a la colección adecuada de usuarios con el tipo de mensaje óptimo. Además, haz un seguimiento de las adhesiones voluntarias push y ten cuidado de no perder a estos usuarios cruciales.

