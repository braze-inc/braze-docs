---
nav_title: Nexla
article_title: Nexla
description: "Este artículo de referencia describe la asociación entre Braze y Nexla, una plataforma unificada de operaciones de datos que permite a los usuarios de Braze Currents extraer, transformar, y cargar datos de «data lakes» a otras ubicaciones en un formato personalizado."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) es líder en operaciones unificadas de datos y un Gartner Cool Vendor 2021. La plataforma Nexla facilita a cualquiera la creación de flujos de datos escalables, entregando operaciones de datos gobernadas y sin fricciones, mejor colaboración y agilidad para los equipos empresariales y de datos. Los equipos que trabajan con datos obtienen una experiencia unificada sin código/con código bajo para integrar, transformar, aprovisionar y supervisar datos para cualquier caso de uso. 

La integración de Braze y Nexla permite a los clientes que utilizan [Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) aprovechar Nexla para extraer, transformar, y cargar datos de «data lakes» a otras ubicaciones en un formato personalizado, haciendo que los datos sean fácilmente accesibles en todo su ecosistema.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Nexla | Se necesita una [cuenta Nexla](https://www.nexla.com/get-demo) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Los datos como producto de Nexla, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), facilitan el trabajo con datos de cualquier formato sin preocuparse de los metadatos. Cuando configures tus flujos de datos hacia o desde Braze con Nexla, las herramientas sin código te lo ponen fácil y disponible en cuestión de minutos. Una vez establecido el flujo de datos a un destino, Nexla supervisará tu flujo y se adaptará a cualquier cantidad de datos.

## Integración

### Paso 1: Crear una cuenta Nexla

Si aún no tienes una cuenta Nexla, visita el [sitio web](https://www.nexla.com) de Nexla para solicitar una demostración y una prueba gratuitas. A continuación, conéctate a [www.dataops.nexla.io](https://www.dataops.nexla.io) e inicia sesión con tus nuevas credenciales.

### Paso 2: Añade tu fuente

#### Si Braze es tu origen de datos
1. En la plataforma Nexla, ve a **Flujos > Crear un nuevo flujo** en la barra de herramientas de la izquierda.
2. Haz clic en **Crear nueva fuente**, selecciona el conector Braze y haz clic en **Siguiente**. 
3. Selecciona **Añadir una nueva credencial**, asigna un nombre a la credencial, añade tu clave de API Braze y el punto final REST, y **Guardar**.
4. Por último, selecciona tus datos y haz clic en **Guardar**. 

Ahora Nexla buscará en el origen cualquier dato que encuentre y generará un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) para transformarlo o enviarlo al destino.

#### Si Braze es tu destino

Visita la documentación de Nexla sobre la [conexión de fuentes a Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Paso 3: Transformar (opcional)

Si quieres realizar [transformaciones](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personalizadas en tus datos o utilizar los conectores prediseñados de Nexla, haz clic en el botón **Transformar** del conjunto de datos para acceder al Generador de transformaciones. En la [documentación de Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data) encontrarás orientación sobre el uso del Constructor de Transformaciones.

### Paso 4: Enviar a destino

Para enviar datos a un destino, haz clic en la flecha **Enviar a destino** del conjunto de datos y selecciona cualquiera de los conectores de destino de Nexla o Braze si tenías un origen diferente. Introduce tus credenciales, configura las opciones de destino y haz clic en **Guardar**. Los datos empezarán a fluir instantáneamente en el formato que hayas especificado hacia el destino que elijas.

## Uso de esta integración

Una vez configurado el flujo, no hace falta nada más. Nexla gestionará cualquier cambio en los datos de origen, escalará a cualquier dato nuevo y te notificará cualquier cambio de esquema o error para su triaje. Si quieres hacer cambios en las transformaciones, el origen o el destino, puedes hacer clic en estas opciones y realizar el cambio, y Nexla actualizará el flujo al instante.

