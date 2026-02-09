---
nav_title: Estudio de decisión Go
article_title: BrazeAI Estudio de Decisiones Go
page_order: 0
description: "Aprende a configurar e integrar BrazeAI Decisioning <sup>StudioTM</sup> Go en Braze."
---

# BrazeAI Decisioning Studio™ Go

> Localiza la información clave en Braze para comenzar la integración con BrazeAI Decisioning Studio™ Go.

## Esenciales

### Crear una clave de API REST en Braze

Para crear una nueva clave de API REST:

1. En el panel de Braze, ve a **Configuración** > **API e identificadores** > **Claves de API**.
2. Selecciona **Crear clave de API**.
3. Introduce un nombre para tu clave de API. Un ejemplo es "DecisioningStudioGoEmail".
4. Selecciona los permisos en función de las siguientes categorías:
    - **Datos de usuario:** selecciona `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Mensajes:** seleccionar `messages.send`
    - **Campañas:** selecciona todos los permisos de la lista
    - **Canvas:** selecciona todos los permisos de la lista
    - **Segmentos:** selecciona todos los permisos de la lista
    - **Plantillas:** selecciona todos los permisos de la lista

{: start="5"}
5\. Selecciona **Crear clave de API**.
6\. A continuación, copia la clave de API y pégala en tu portal BrazeAI Decisioning Studio™ Go.

### Localización de tu nombre para mostrar correo electrónico Braze

Para encontrar el nombre para mostrar de tu correo electrónico Braze:

1. En el panel de Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Localiza el nombre de pantalla que se utilizará con BrazeAI Decisioning Studio™ Go.
3. Copia y pega el **Nombre para** **mostrar** **de** en el portal BrazeAI Decisioning Studio™ Go como **Nombre para mostrar de correo electrónico**.
4. Copia y pega la dirección de correo electrónico asociada en tu portal BrazeAI Decisioning Studio™ Go como **dirección de correo electrónico De**, que combina la parte local y el dominio.

### Localización de tu ID de usuario

Para encontrar tu ID de usuario:

1. En el panel de Braze, ve a **Audiencia** > **Buscar usuarios**.
2. Busca al usuario por su ID externo, alias de usuario, correo electrónico, número de teléfono o token de notificaciones push.
3. Copia el ID de usuario como referencia en tu configuración.

![Ejemplo de perfil de usuario a partir de la ubicación de un usuario con su ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Encontrar tu URL Braze

Para identificar tu URL Braze:

1. Ve al panel de Braze.
2. En la ventana de tu navegador, tu URL de Braze empieza por `https://` y termina por `braze.com`. Un ejemplo de URL de Braze es `https://dashboard-01.braze.com`.

### Encontrar tu clave de API Braze

{% alert note %}
Braze ofrece ID de aplicaciones (denominadas claves de API en el panel de Braze) que puedes utilizar con fines de seguimiento, como asociar la actividad a una aplicación específica de tu espacio de trabajo. Si utilizas ID de aplicación, BrazeAI Decisioning Studio™ Go permite asociar un ID de aplicación a cada experimentador.<br><br>Si no utilizas ID de aplicación, puedes introducir cualquier cadena de caracteres como marcador de posición.
{% endalert %}

1. En el panel de Braze, ve a **Configuración** > Configuración de la aplicación **.**
2. Ve a la aplicación que quieras seguir.
3. Copia y pega la **clave de API** en tu portal BrazeAI Decisioning Studio™ Go.

### Configuración de las claves de API de Klaviyo

Debes configurar una clave de API para utilizar Klaviyo para BrazeAI Decisioning Studio™ Go.

1. En Klaviyo, ve a **Configuración** > **Claves de API**.
2. Selecciona **Crear clave de API privada**. 
3. Introduce un nombre para la clave de API. Un ejemplo es "Experimentadores del Estudio de Decisiones".
4. Selecciona los siguientes permisos para la clave de API:
    - Campañas: Leer Acceso
    - Privacidad de datos: Acceso total
    - Eventos: Acceso total
    - Flujos: Acceso total
    - Imágenes: Leer Acceso
    - Lista: Acceso total
    - Métricas: Acceso total
    - Perfiles: Acceso total
    - Segmentos: Leer Acceso
    - Plantillas: Acceso total
    - Webhooks: Leer Acceso

![Una clave de API de Klaviyo con permisos seleccionados.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Seleccione **Crear**.
6\. Copia esta clave de API y pégala en el portal BrazeAI Decisioning Studio™ Go donde se te pida.

### Configuración de un paquete de aplicaciones SFMC

Para utilizar Salesforce Marketing Cloud para BrazeAI Decisioning Studio™ Go, debes configurar un paquete de aplicaciones en Salesforce Marketing Cloud. 

1. Ve a tu página de inicio de Marketing Cloud. 
2. Abre el menú de la cabecera global y selecciona **Configuración**.
3. Ve a **Aplicaciones** en **Herramientas de la plataforma** en el panel lateral de navegación y, a continuación, selecciona **Paquetes instalados**.
4. Selecciona **Nuevo** para crear un paquete de aplicación.
5. Dale un nombre y una descripción al paquete de la aplicación.

![Un paquete de aplicación con el nombre "Experimentador 1 - Prueba 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecciona **Añadir componente**.
7\. Para el **Tipo de componente**, selecciona **Integración API**. A continuación, selecciona **Siguiente**.
8\. Para el **Tipo de integración**, selecciona **Servidor a servidor**. A continuación, selecciona **Siguiente**.
9\. A continuación, selecciona los siguientes ámbitos recomendados sólo para el paquete de tu aplicación:
    \- Canales > Correo electrónico > Leer, Escribir, Enviar
    \- Canales > OTT > Leer
    \- Canales > Push > Leer
    \- Canales > SMS > Leer
    \- Canales > Social > Leer
    \- Canales > Web > Leer
    \- Activos > Documentos e imágenes > Leer, Escribir
    \- Activos > Contenido guardado > Leer, Escribir
    \- Automatización > Automatizaciones > Leer, Escribir, Ejecutar
    \- Automatización > Viajes > Leer, Escribir, Ejecutar, Activar/Parar/Pausar/Enviar/Programar
    \- Contactos > Audiencias > Leer
    \- Contactos > Lista y suscriptores > Leer, Escribir
    \- Cross Cloud Platform > Audiencia de mercado > Ver
    \- Cross Cloud Platform > Miembro de la audiencia de marketing > Ver
    \- Cross Cloud Platform > Marketing Cloud Connect > Leer
    \- Datos > Extensiones de datos > Lectura, Escritura
    \- Datos > Ubicación de los archivos > Leer
    \- Datos > Seguimiento de Eventos > Lectura, Escritura
    \- Notificaciones de eventos > Devoluciones de llamada > Leer
    \- Notificaciones de eventos > Suscripciones > Leer

{% details Show image of recommended scopes %}

![Los ámbitos recomendados para el paquete de aplicaciones de Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Seleccione **Guardar**.
11\. Copia y pega los siguientes campos en el portal BrazeAI Decisioning Studio™ Go: **ID de cliente**, **Secreto de cliente**, **URI base de autenticación**, **URI base REST**, **URI base SOAP**.