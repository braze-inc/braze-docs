---
nav_title: Octolis
article_title: Octolis
description: "Este artículo de referencia describe la asociación entre Braze y Octolis, una plataforma de activación de datos, que te permite integrar tus datos en Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com) es una potente plataforma de activación de datos (o CDP sin cabeza). Situándose sobre una base de datos de tu propiedad, Octolis es una forma sencilla de unificar, preparar, puntuar y sincronizar datos en tus herramientas empresariales.

_Esta integración está mantenida por Octolis._

## Sobre la integración

La integración de Braze y Octolis actúa como middleware entre tus fuentes de datos brutos y Braze, lo que te permite recuperar y unificar datos de diversas fuentes, online y offline:
1. Unifica y combina datos de fuentes como Eshop, CRM, sistema TPV, etc.
2. Normalizar y puntuar
3. Sincronización en tiempo real de campos y eventos computados con Braze

![]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Octolis | Se necesita una cuenta Octolis para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST Braze con permisos [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Clave de la aplicación Braze | La clave del identificador de tu aplicación. Se encuentra en el **panel de Braze > Administrar configuración > Clave de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Antes de comenzar la integración, consulta las secciones siguientes sobre conexiones, fuentes, audiencias y sincronizaciones.

Para más información, consulta la sección [Primeros pasos](https://help.octolis.com/) de Octolis.

### Paso 1: Conecta Octolis a tus orígenes de datos

Para enviar datos a Braze, debes asegurarte de que has creado al menos una [audiencia](https://help.octolis.com/audiences/create-a-no-code-audience). Una audiencia combina varios orígenes de datos, los aplica a los pasos de la preparación y añade campos computados.

Estas audiencias deben construirse a partir de varios orígenes de datos. Una fuente puede ser cualquiera de las siguientes:
- Un objeto de Salesforce (contactos, cuentas, etc.)
- Un objeto Zendesk (tickets)
- Un archivo dentro de un SFTP (archivo CSV que contenga algunos contactos, archivo JSON que contenga eventos...)
- Una tabla/vista de una base de datos.
- Uno de tus sistemas nos envía registros a través de webhooks o llamadas a la API.

### Paso 2: Añadir Braze como destino

A continuación, para establecer Braze como nuevo destino, selecciona **\+ Añadir más** en la parte superior de tu destino actual dentro de la pantalla principal y selecciona **Braze** entre las herramientas empresariales disponibles.

![]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Una vez seleccionado, proporciona lo siguiente:

- Tu clave de API de Braze: Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**.
- Ventana temporal: Octolis aplicará el límite de velocidad en el periodo dado.
- Volumen de solicitudes: Número de solicitudes que puedes hacer dentro de este plazo.
- Atributos personalizados: Especifica aquí los nuevos campos que enviarás a Braze, su formato (cadena, entero, flotante), y marca la casilla **Obligatorio para sincronizaciones** si quieres que alguno de ellos sea obligatorio para una sincronización.

![]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Una vez configurado, Braze aparecerá como un nuevo destino en la pantalla de inicio.

### Paso 3: Crear una nueva sincronización

En el menú, haz clic en **Sincronizaciones** y selecciona **Añadir sincronización** en la parte superior derecha. Selecciona la audiencia que quieres seleccionar de la audiencia que has creado previamente.
A continuación, selecciona **Braze** como destino y la entidad a la que enviarás los datos.

![]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Paso 4: Establece la configuración de salida

Por defecto, Braze crea todos los atributos que enviarías, pero debes documentar la lista de campos que se sincronizarán.

![]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Aquí tienes una definición específica de los campos de configuración.

| Campo | Descripción |
| --- | --- |
| ¿Hacia dónde quieres sincronizar a la audiencia? | La entidad Braze en la que crearás o actualizarás registros. |
| ¿Qué campo se utiliza para identificar un registro? | El campo utilizará Octolis para identificar un registro si ya existe en Braze. |
| ¿Con qué frecuencia quieres enviar cada registro? | Por predeterminado, la sincronización será incremental para todas las integraciones (API, base de datos, FTP). Esto significa que sólo se actualizarán los valores nuevos desde la última actualización. Si es necesario, también puedes enviar tablas enteras a intervalos regulares. Al iniciarse, Octolis enviará la tabla completa. |
| ¿Qué campos deben sincronizarse? | Mapeado de campos Octolis a Braze. La lista de todos los campos disponibles aparece en el menú desplegable. Para enviar un campo calculado a Braze, primero debes asegurarte de haber creado la columna correspondiente dentro de tu entidad Braze. |
| ¿Cuándo quieres sincronizar la audiencia? | Cómo se enviarán los datos a Braze: manualmente, en tiempo real o programado.  |
| Sincronizar al grabar... | Crear: Para las adhesiones voluntarias, es importante que la tabla Braze siga siendo maestra. No quieres que Octolis desencadene una sincronización cuando se actualice el campo.<br><br>Actualizar: En cambio, para un campo de nombre de pila, por ejemplo, quieres poder actualizar el campo en tu tabla Braze cada vez que un cliente te dé una nueva entrada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Deduplicación multiclave

La deduplicación es un reto importante cuando se concilian datos de múltiples fuentes, especialmente online y offline. Gracias al avanzado módulo sin código de Octolis, puedes utilizar varias claves para [la deduplicación](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work). Este módulo está disponible para cada tabla maestra, lo que significa que puedes adaptar la lógica a cada entidad.


