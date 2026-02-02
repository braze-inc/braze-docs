---
nav_title: Swym
article_title: Swym
description: "Este artículo de referencia describe la asociación entre Braze y Swym, que permite a los compradores guardar productos y continuar fácilmente su viaje a través de sitios web, aplicaciones móviles y tiendas minoristas."
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# Swym

> [Swym](https://getswym.com/) ayuda a las marcas de comercio electrónico a captar la intención de compra con listas de deseos, guardar para más tarde, registro de regalos y alertas de reposición de existencias. Utilizando datos ricos y basados en permisos, puedes crear campañas hiperdirigidas y entregar experiencias de compra personalizadas que impulsen la interacción, aumenten las conversiones e incrementen la fidelización.

*Esta integración está mantenida por Swym.*

## Sobre la integración

La integración de Swym y Braze te permite entregar campañas de marketing personalizadas y basadas en eventos que convierten la intención del comprador en ventas. Utiliza la integración para que los compradores puedan continuar donde lo dejaron, colaborar con otros a lo largo de su recorrido de compra y recibir campañas de reorientación de alto rendimiento.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym  | Las aplicaciones Swym Wishlist Plus, Back in Stock, o ambas, deben estar instaladas en tu plataforma de comercio electrónico (Shopify o BigCommerce), y debes tener el plan Enterprise.       |
| Una clave de API REST Braze  | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Ejemplos

Al conectar las aplicaciones Wishlist Plus y Back in Stock Alerts de Swym con Braze, puedes enviar automáticamente a Braze eventos de actividad de los compradores, como adiciones a la lista de deseos, suscripciones a Back in Stock, alertas de bajada de precios y recordatorios, como eventos personalizados. Estos eventos pueden utilizarse para desencadenar mensajes automatizados en Braze, facilitando una comunicación oportuna, relevante y atractiva que haga que los compradores vuelvan a realizar una compra.

## Integración de Swym

### Paso 1: Conecta tu aplicación Swym a Braze

Actualmente, la integración de Braze con Swym es una integración gestionada y no es autoservicio. Para empezar, ponte en contacto con el equipo de soporte de Swym en [support@getswym.com](mailto:support@getswym.com) y proporciona la siguiente información para que Swym pueda configurar la integración en tu nombre:

1. Genera una [clave de API REST]({{site.baseurl}}/api/basics/#about-rest-api-keys) en tu panel Braze con el permiso `users.track`.

![Generar una clave de API en Braze.]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
Para proteger tus claves de API, Swym recomienda que compartas las credenciales de forma segura utilizando una herramienta de enlace única y autodestructiva (por ejemplo, [OneTimeSecret](https://onetimesecret.com/)).
{% endalert %}

{: start="2"}
2\. Braze gestiona varias instancias para su panel y sus puntos finales REST. Proporciona el [punto final REST]({{site.baseurl}}/api/basics/#endpoints) de la instancia que estás aprovisionando.

3. Después de compartir la clave de API y la URL de instancia con el equipo de soporte de Swym, ellos configurarán la integración por ti y te responderán con una confirmación.

4. Una vez completada la configuración, los eventos personalizados de Swym se registrarán automáticamente en Braze. Puedes ver la lista de eventos Swym registrados en el panel de Braze yendo a **Configuración de datos** > Eventos personalizados. 

5. Visualiza las propiedades de cada evento Swym seleccionando **Gestionar propiedades** del evento personalizado correspondiente. Estas propiedades contienen los valores del evento que pueden utilizarse para personalizar tus mensajes.

![Propiedades personalizadas en Braze.]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### Paso 2: Suscríbete a los eventos que quieras enviar a Braze

Desde tu aplicación Wishlist Plus, ve a la pestaña **Marketing** y busca la sección **Automatizaciones**. Aquí puedes seleccionar los eventos a los que quieres suscribirte. 

![Eventos a suscribir.]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Eventos de la aplicación Swym Wishlist Plus

| Nombre de evento | Cuando se desencadena este evento |  
|------------|------------------------------|  
| Compartir lista de deseos | Cuando un comprador comparte una lista de deseos con otra persona |  
| Añadir a la lista de deseos | Cuando un comprador añade un artículo a su lista de deseos |  
| Recordatorio de la lista de deseos | Recordatorio sobre los artículos de la lista de deseos de un comprador|   
| Recordatorio de guardado para más tarde | Recordatorio sobre los artículos guardados para más tarde de un comprador |  
| Alerta de bajada de precios | El producto de una lista de deseos se pone a la venta |  
| Alerta de existencias bajas | El producto de una lista de deseos se está agotando |  
| Alerta de nuevo en stock | Se repone el producto de una lista de deseos |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Eventos de la aplicación Swym Back in Stock Alerts

| Nombre de evento | Cuando se desencadena este evento |  
|------------|------------------------------|  
| Confirmación de disponibilidad | El comprador se suscribe para recibir una notificación cuando un producto vuelva a estar en stock |  
| Alerta de reabastecimiento | Se repone el producto para el que un comprador solicitó una alerta de agotado |  
| Recordatorio de reabastecimiento | Alerta de seguimiento (normalmente unas 24 horas después de la primera alerta de reabastecimiento, configurable)|   
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Paso 3: Crea una campaña o Canvas de Braze

Para automatizar la entrega de mensajes personalizados para tus compradores, debes crear una campaña o Canvas independiente en Braze para cada evento al que te hayas suscrito. Cada campaña o Canvas debe configurarse para desencadenarse en función del evento específico y utilizar las propiedades del evento correspondientes para rellenar de contenido dinámico tus mensajes. Para una guía paso a paso, puedes consultar [Primeros pasos: Campañas y lonas]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

![Un evento basado en la acción.]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

Para más información, consulta el [centro de ayuda de Swym](https://help.getswym.com/en/articles/12344153-braze-integration) o ponte en contacto con el equipo de soporte de Swym en [support@getswym.com](mailto:support@getswym.com). 