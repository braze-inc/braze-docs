---
nav_title: Simon Data
article_title: Simon Data
description: "Utiliza la integración de Braze y Simon Data para crear y sincronizar audiencias sofisticadas con Braze para su orquestación, en tiempo real y sin código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon Data

> [Simon Data](https://www.simondata.com) es una plataforma de datos de los clientes (CDP) fácil de usar para los especialistas en marketing y en la que confían los equipos de datos. Al transformar tu almacén de datos en una central de marketing, Simon impulsa los resultados empresariales y genera una experiencia del cliente superior.

Utiliza la integración de Braze y Simon Data para crear y sincronizar audiencias sofisticadas con Braze para su orquestación, en tiempo real y sin código. Con esta integración puedes aprovechar lo mejor de las capacidades de priorización de campañas y de correspondencia de identidades de Simon, la compatibilidad con agregados complejos y mucho más para elevar tus campañas Braze en sentido descendente.

## Requisitos previos

Para empezar, tienes que autenticar tu cuenta de Braze dentro de tu cuenta de Simon Data.

| Requisito         | Descripción                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon Data          | Debes tener una cuenta de Simon Data para aprovechar la integración de Braze desde Simon Data.                                                                    |
| Clave de API REST de Braze  | Una clave de API REST Braze con permisos `users.track`, `campaigns.trigger.schedule.create`, y `campaigns.trigger.send`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| URL del panel de Braze | [La URL de tu punto final REST]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Tu punto final dependerá de la URL Braze de tu instancia.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

- Desencadenar un Braze Canvas o un correo electrónico  
- Pasar y actualizar propiedades de Segment
- Sincronizar rasgos y propiedades de contacto

{% alert note %}  
Al utilizar la integración de Simon y Braze, Simon solo envía deltas en cada sincronización a Braze, evitando costes por datos irrelevantes. Para más información, consulta [Rasgos de sincronización y propiedades de contacto](#sync-traits-and-contact-properties).
{% endalert %}

## Integración

### Autentica tu cuenta Braze en Simon

Para utilizar la integración Braze, primero autentica tu cuenta Braze en Simon:

1. En la barra de navegación de la izquierda, haz clic en **Integraciones** y desplázate hasta Braze.
2. Introduce tu [clave de API REST]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys) de Braze y [la URL de tu panel]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints).
3. Haz clic en **Guardar cambios**.

Una conexión correcta muestra **Conectado** en la ventana.

![Pantalla de integración en Simon Data]({% image_buster /assets/img/simon_data/ConnecttoBraze.png %}){: style="max-width:70%"}

### Añadir acciones Braze a Flows o Journeys en Simon

Después de autenticar tu cuenta Braze en Simon, puedes añadir acciones Braze a [Flows](https://docs.simondata.com/docs/campaigns-flows) y [Journeys](https://docs.simondata.com/docs/campaigns-journeys-two).

Hay tres acciones disponibles:

- **Sincroniza el atributo del segmento Simon**: sincroniza los detalles de tu segmento con un atributo personalizado nuevo o existente en Braze.
- **Desencadena un Canvas de Braze**: desencadena un Canvas de Braze que aproveche los datos de tu segmento Simon.
- **Envía una campaña Braze**: lanza una campaña Braze completa desde Simon.

![Desplegable que muestra la lista de acciones Braze disponibles en Simon Data.]({% image_buster /assets/img/simon_data/BrazeActions.png %}){: style="max-width:60%"}

Algunas acciones solo están disponibles para determinados tipos de Flow o Journeys. Más información en [docs.simondata.com](https://docs.simondata.com).

### Sincronizar rasgos y propiedades de contacto

Para minimizar el consumo de datos, puedes elegir rasgos específicos para sincronizar de forma predeterminada, en lugar de actualizar cada campo para todos los clientes de un segmento.

{% alert note %}
Para empezar con la sincronización de rasgos, envía una solicitud al [Centro de soporte de Simon](https://docs.simondata.com/docs/support-center). Tu administrador de cuentas te avisará cuando puedas proceder con los siguientes pasos.
{% endalert %}

Después de que el director de cuentas active Contact Traits:

1. En Simon, expande **Centro de administración** en el navegador izquierdo y selecciona **Sincronizar rasgos de contacto**.
2. Elige **Braze**. Aquí se muestran las propiedades de los contactos, anidadas por conjunto de datos.
3. Selecciona los campos que quieras sincronizar cuando utilices la integración de Simon y Braze:
   1. **El número de rasgos** indica cuántos rasgos hay disponibles para elegir en ese conjunto de datos. Puedes elegir todo o ampliar la fila para seleccionar campos individuales.
   2. Edita el **Nombre descendente** si quieres que los nombres de los campos aparezcan de forma diferente cuando lleguen a Braze.
   3. Si es la primera vez que realizas la integración con Braze desde Simon, haz clic en **Rellenar todos los contactos**. El backfilling envía todos los puntos de datos a Braze la primera vez que utilizas una acción en un flujo o trayecto para asegurarte de que todos tus datos están totalmente sincronizados. Luego, en las siguientes sincronizaciones, solo se enviarán a Braze los rasgos que elijas en esta pantalla. Así te aseguras de que solo se te cobren los datos que necesitas.

![Selección de rasgos de sincronización en Simon Data.]({% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %})





