---
nav_title: Crear campañas
article_title: Creación de campañas de tarjetas Banner
alias: "/create_banner_card/"
description: "Este artículo de referencia explica cómo crear y enviar tarjetas de visita utilizando campañas Braze."
page_type: reference
---

# Creación de campañas de tarjetas Banner

> Aprende a crear tarjetas de presentación cuando crees una campaña en Braze. Para más información general, consulta [Acerca de las tarjetas Banner]({{site.baseurl}}/developer_guide/banners/).

{% alert important %}
Las tarjetas de estandarte están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Requisitos previos {#prerequisite-determine-placement}

Estas son las versiones mínimas del SDK para empezar a utilizar las tarjetas Banner:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Crear una campaña de Tarjeta Banner

{% multi_lang_include banners/creating_placements.md %}

### Paso 2: Crear una campaña

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **Tarjeta Banner**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade equipos y etiquetas según sea necesario. Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el generador de informes, puedes filtrar por las etiquetas correspondientes.
5. Selecciona el emplazamiento que creaste previamente para asociarlo a tu campaña.
6. Añade variantes si es necesario. Puedes elegir un tipo de mensaje y un diseño diferentes para cada uno. Para obtener más información sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Paso 2: Redacta un mensaje

Para componer tu tarjeta de presentación, selecciona **Editar mensaje**. Aquí puedes dar estilo a la tarjeta y definir el comportamiento al hacer clic.

#### Paso 2.1: Estiliza la tarjeta {#styles}

Puedes arrastrar y soltar bloques y filas en el área del lienzo para empezar a construir tu mensaje. Para personalizar las propiedades del fondo de tu mensaje, la configuración de los bordes y mucho más, selecciona **Estilos**. Si sólo quieres personalizar el estilo de un bloque o fila concretos, selecciónalo para realizar los cambios.

![Panel de estilo del compositor de la tarjeta Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Paso 2.2: Definir el comportamiento al hacer clic

Cuando un cliente hace clic en un enlace de la tarjeta de presentación, puedes elegir que navegue más profundamente en tu aplicación o redirigirlo a otra página web. Además, puedes elegir [registrar un atributo o evento personalizado]({{site.baseurl}}/developer_guide/analytics/), que actualizará el perfil de tu cliente con datos personalizados cuando haga clic en la tarjeta de presentación.

### Paso 3: Configurar la prioridad de la tarjeta {#set-card-priority}

Cuando varias campañas hacen referencia al mismo ID de colocación, las tarjetas se muestran por orden de nivel de prioridad. Por predeterminado, las tarjetas de presentación recién creadas se establecen en media, pero puedes establecer manualmente la prioridad en alta, media o baja. Si varias tarjetas comparten el mismo nivel de prioridad, se mostrará primero la tarjeta más reciente.

Para configurar la prioridad de una tarjeta:

1. Selecciona **Clasificador de prioridades**.
2. Arrastra y suelta las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Aplicar clasificación**.

### Paso 3: Termina de construir la campaña

Termina de construir tu campaña completando lo siguiente:

| Opción                    | Descripción |
|---------------------------|-------------|
| **Duración de la campaña** | Elige una fecha y hora de inicio para tu campaña con la tarjeta Banner. Por predeterminado, las tarjetas Estandarte duran indefinidamente. Puedes cambiarlo seleccionando **Hora de finalización** y especificando una fecha y hora de finalización. |
| **Usuarios objetivo** | Dirígete a los usuarios eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una instantánea de la población aproximada del segmento. La pertenencia exacta a un segmento se calcula justo antes de enviar el mensaje. |
| **Eventos de conversión** | Haz un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas después de recibir una campaña. Puedes definir eventos de conversión con una ventana de hasta 30 días para contar la acción como conversión. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Paso 4: Prueba y lanzamiento

Después de crear tu campaña, pruébala y revísala para asegurarte de que funciona como esperabas. Cuando estés listo, ¡lanza tu campaña con la tarjeta Banner!
