---
nav_title: SimonAI
article_title: SimonAI
description: "Utiliza la integración de Braze y SimonAI para crear y sincronizar audiencias sofisticadas con Braze para su orquestación, en tiempo real y sin código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> La Plataforma [Simon AI][1] Agentic Marketing ayuda a los equipos de marketing a lograr una verdadera personalización uno a uno. Combina un CDP componible con agentes de IA que operan directamente en la Nube de Datos de IA Snowflake para actuar como equipo de datos y ejecución de un especialista en marketing.

Utiliza la integración de Braze y Simon AI para crear y sincronizar audiencias avanzadas con Braze para una orquestación en tiempo real y sin código. Con esta integración, puedes aprovechar la resolución de identidades, la unificación de datos de clientes y la segmentación basada en IA de Simon AI para impulsar campañas Braze más personalizadas e impactantes.

## Requisitos previos

Para empezar, tienes que autenticar tu cuenta Braze dentro de tu cuenta Simon AI.

| Requisito         | Descripción                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI          | Debes tener una cuenta de Simon AI para aprovechar la integración de Braze desde Simon AI.                                                                    |
| Clave de API REST de Braze  | Una clave de API REST Braze con permisos `users.track`, `campaigns.trigger.schedule.create`, y `campaigns.trigger.send`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| URL del panel de Braze | [La URL de tu punto final REST][3]. Tu punto final dependerá de la URL Braze de tu instancia.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

- Desencadenar un Braze Canvas o un correo electrónico  
- Pasar y actualizar propiedades de Segment
- Sincronizar rasgos y propiedades de contacto

{% alert note %}  
Al utilizar la integración de Simon y Braze, Simon solo envía deltas en cada sincronización a Braze, evitando costes por datos irrelevantes. Para más información, consulta [Rasgos de sincronización y propiedades de contacto](#sync-traits-and-contact-properties).
{% endalert %}

## Integración

### Autentica tu cuenta Braze en Simon AI

Para utilizar la integración Braze, primero autentica tu cuenta Braze en Simon:

1. En la barra de navegación de la izquierda, haz clic en **Integraciones** y desplázate hasta Braze.
2. Introduce tu [clave de API REST][2] de Braze y [la URL de tu panel][3].
3. Haz clic en **Guardar cambios**.

Una conexión correcta muestra **Conectado** en la ventana.

![Pantalla de integración en Simon AI][8]{: style="max-width:70%"}

### Añadir acciones Braze a Flujos o Viajes en Simon AI

Después de autenticar tu cuenta Braze en Simon AI, puedes añadir acciones Braze a [Flows][4] y [Journeys][5].

Hay tres acciones disponibles:

- **Sincroniza el atributo del segmento Simon**: sincroniza los detalles de tu segmento con un atributo personalizado nuevo o existente en Braze.
- **Desencadena un Canvas de Braze**: desencadena un Canvas de Braze que aproveche los datos de tu segmento Simon.
- **Envía una campaña Braze**: lanza una campaña Braze completa desde Simon.

![Desplegable que muestra la lista de acciones Braze disponibles en Simon AI.][9]{: style="max-width:60%"}

Algunas acciones solo están disponibles para determinados tipos de Flow o Journeys. Más información en [docs.simondata.com][6].

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

![Selección de rasgos de sincronización en Simón AI][10].

[1]: https://www.simondata.com




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}

