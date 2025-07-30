---
nav_title: Campañas de usuarios activos
article_title: Campañas de usuarios activos
page_order: 0.5
page_type: tutorial
description: "Este artículo describe las ventajas de las campañas de usuarios activos en el panel de control de Braze y los pasos para crear y configurar una."
tool: 
  - Campaigns

---

# Campañas de usuarios activos

> Identifique a sus usuarios activos para ayudarle a realizar campañas a medida y recompensar a los que frecuentan su plataforma. 

Llegar a los usuarios ya activos de su aplicación puede ser una herramienta poderosa para ayudar a crear un grupo de usuarios constantes. Un poco de reconocimiento personalizado de sus usuarios avanzados puede convertirlos en evangelizadores de su aplicación.

También puede consultar nuestro [curso Braze Learning](https://learning.braze.com/quick-overview-segment-and-campaign-setup) sobre estrategia de marketing por correo electrónico y campañas de ciclo de vida recomendadas.

## Comprender a los usuarios activos

Braze define un "usuario activo" para un periodo de tiempo determinado como cualquier usuario que tenga una sesión en ese periodo de tiempo.

Si un usuario pierde la conectividad, almacenaremos en caché los datos de la sesión localmente y los cargaremos cuando el usuario recupere la conexión a la red. Estas sesiones también se aplicarán al recuento de usuarios activos. Además, si su aplicación tiene un proceso de registro, Braze contará a todos los usuarios como activos, registrados o no registrados.

Si establece ID de usuario para identificar a los usuarios, cuando un nuevo usuario inicie sesión se contará como un usuario activo independiente. Los usuarios que se actualicen a través de la API también se contabilizarán como usuarios activos en el periodo de tiempo en que se actualicen.

## Paso 1: Identificar a los principales usuarios

Utilizando nuestra selección de filtros, cree un segmento de usuarios que considere que engloba a su base de usuarios más fieles y constantes. El siguiente segmento de muestra define a los principales usuarios.

![]({% image_buster /assets/img_archive/define_top_users.png %} "Define tus principales usuarios")

Además, no tendrá que seguir actualizando este segmento, ya que los usuarios que pasen dentro o fuera de las restricciones de la campaña serán correspondientemente apuntados o descartados.

{% alert note %}
El ejemplo anterior segmenta a los usuarios según el uso general de la aplicación. En la mayoría de los casos, la colección total de filtros necesarios para definir su segmento de usuarios principales vendrá definida en gran medida por las características específicas de su aplicación.
{% endalert %}

## Paso 2: Llega a tus mejores usuarios

### Haz que tus usuarios se sientan apreciados

Haz que tus usuarios se sientan apreciados agradeciéndoles su fidelidad y dedicación a tu aplicación. Ofrezca a sus usuarios más razones para volver a su aplicación y fomentar su actividad. Esto puede adoptar la forma de ofertas especiales o bonificaciones exclusivas para sus mejores usuarios. 

Las recompensas inesperadas pueden ser más efectivas para animar a los usuarios a seguir actuando que si se las hubieras prometido desde el principio.

![Una campaña en el paso Redactar con una notificación enriquecida de iOS que dice: "¡Gracias de nuevo por comprar con nosotros! Para mostrarte nuestro agradecimiento, te regalamos los gastos de envío en tu próxima compra".]({% image_buster /assets/img/congratulations_push.jpg %})

### Haz un seguimiento de tus resultados

Realice un seguimiento de las aperturas para asegurarse de que se dirige a la colección adecuada de usuarios con el tipo de mensaje óptimo. Además, lleve un registro de las cancelaciones push y tenga cuidado de no perder a estos usuarios cruciales.

