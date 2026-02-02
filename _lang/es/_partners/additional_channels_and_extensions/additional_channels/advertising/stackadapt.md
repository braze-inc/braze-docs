---
nav_title: StackAdapt
article_title: StackAdapt
description: "Este artículo de referencia describe la asociación entre Braze y StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) es la principal plataforma de marketing basada en IA utilizada por especialistas en marketing digital para entregar publicidad orientada al rendimiento.

_Esta integración está mantenida por StackAdapt._

La integración de Braze y StackAdapt te permite sincronizar los datos de perfil de usuario desde Braze al Data Hub de StackAdapt. Al conectar las dos plataformas, puedes crear una visión unificada de tus clientes y activar los datos propios para mejorar el rendimiento de los anuncios.

## Ejemplos

- **Reactivación de la interacción con los usuarios antiguos:** Identifica a los usuarios que se han dado de baja de las listas de correo electrónico de marketing en Braze y dirígete a ellos con anuncios programáticos en StackAdapt para reactivarlos a través de un canal diferente.
- **Crea experiencias multicanal:** Amplía el viaje del usuario más allá del correo electrónico. Por ejemplo, si un usuario hace clic en una campaña de correo electrónico en Braze, puedes utilizar StackAdapt para mostrarle un anuncio programático complementario, reforzando el mensaje e impulsando nuevas acciones.
- **Personalización a escala:** Aprovecha los puntos de datos granulares de Braze, como "Ciudad de origen" o "Idioma", para publicar anuncios y correos electrónicos muy relevantes, localizados y específicos de cada idioma.
- **Profundiza en el conocimiento de tu audiencia:** Al sincronizar los atributos de perfil, puedes crear segmentos de audiencia más ricos en StackAdapt, habilitando una orientación más precisa y experiencias publicitarias personalizadas.

## Requisitos previos

| Requisito | Descripción         |
| ----------- | ------------------- |
| **Cuenta StackAdapt**  | Necesitas una cuenta StackAdapt activa con permisos para gestionar las integraciones de Data Hub. |
| **Clave de API REST de Braze**  | Una clave Braze REST API con los siguientes permisos: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API.** |
| **Punto final REST Braze** | [La URL de tu punto final REST](https://www.braze.com/docs/api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cómo funciona

El concentrador de datos StackAdapt se conecta directamente a tu cuenta Braze para extraer los atributos del perfil de usuario. Esto te permite aprovechar tus datos de clientes de Braze directamente en StackAdapt para una segmentación y activación avanzadas de la audiencia.

### Flujo de datos

1. StackAdapt inicia una conexión segura con tu instancia de Braze utilizando las credenciales de API proporcionadas.
2. StackAdapt recupera los datos de perfil de usuario y, en concreto, las propiedades que has seleccionado y mapeado.
3. Los datos se normalizan e ingieren en tu Hub de Datos StackAdapt, quedando disponibles para su segmentación y uso en tus campañas.
4. La integración permite sincronizaciones de datos programadas (por ejemplo, diariamente) para mantener a tus audiencias de StackAdapt actualizadas con los datos de perfil más recientes de Braze.

## Campos sincronizados

StackAdapt puede sincronizar una variedad de campos del perfil Braze, incluyendo, pero no limitado a:

{% tabs local %}
{% tab Standard attributes %}
- Correo electrónico
- Fecha de nacimiento
- Nombre
- Apellido
- Teléfono
- Ciudad natal
- País
- Género
- Zona horaria
- Creado el
- ID externo
- Idioma 

{% endtab %}
{% tab Custom attributes %}
Atributos específicos de tu aplicación o negocio, definidos en función de tus necesidades empresariales concretas.

{% endtab %}
{% tab Attribution data %}
- Anuncio atribuido
- Grupo de anuncios atribuidos
- Campaña atribuida
- Fuente atribuida

{% endtab %}
{% tab Subscription status %}
- Estado de la suscripción del correo electrónico
- Estado de la suscripción a notificaciones push 

Es crucial mapear con precisión los campos en Braze que reflejan el consentimiento del usuario para las comunicaciones de marketing (por ejemplo, el estado de suscripción al correo electrónico) para que tus esfuerzos publicitarios sigan cumpliendo las preferencias del usuario y la normativa sobre privacidad.

{% endtab %}
{% endtabs %}

## Configuración de la integración

Sigue estos pasos para importar tus perfiles de usuario de Braze:

1. Accede a tu cuenta StackAdapt.
2. En el menú de navegación, selecciona **Centro de Datos**.
3. Selecciona **Importar perfiles** y, a continuación, selecciona **Braze** en la lista de integraciones disponibles.
4. Introduce tus credenciales de la API de Braze cuando se te solicite.
- **Clave de API REST Braze:** Se localiza en Braze yendo a **Configuración** > **Claves de API**. Como práctica recomendada de seguridad, recomendamos crear una clave de API dedicada para tu integración con StackAdapt.
- **Llave de la aplicación Braze:** Ubicado en Braze yendo a **Configuración** > **Claves de API** o **Gestionar aplicaciones**.
- **URL del punto final REST de Braze:** La URL base de tu instancia de Braze (por ejemplo, ```https://rest.iad-01.braze.com```).
5. Selecciona **Conectar** para verificar las credenciales.

![Conexión Braze en StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6\. Elige tu conexión y selecciona tu anunciante StackAdapt.
7\. Configura tus **mapeados de propiedad**. Revisa y confirma los mapeados predeterminados y las propiedades preseleccionadas que StackAdapt sugiere.
8\. (Opcional) Si quieres importar propiedades adicionales, selecciónalas marcando las casillas respectivas y especifica si contienen PII y su tipo de datos.

![Conexión Braze en StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\. Añade tus perfiles a una **Lista** o crea una nueva para poder agrupar y segmentar tus perfiles
10\. Selecciona **Activar integración** para iniciar la sincronización inicial de datos.

## Consideraciones

- **Importar eventos personalizados y propiedades:** Esta característica aún no es compatible.
- **Latencia de los datos:** La importación de todos los datos de perfil de usuario puede tardar hasta 24 horas.
- **Gestión del consentimiento:** Confirma que tus prácticas de recopilación de datos en Braze se ajustan a la normativa sobre privacidad y que tienes el consentimiento necesario para utilizar los datos de clientes con fines publicitarios. StackAdapt se basa en el estado de consentimiento transmitido desde tus sistemas fuente.
- **Coherencia de los atributos:** Para maximizar la eficacia de tus datos, mantén la coherencia en la forma de nombrar y rellenar los atributos en Braze antes de sincronizarlos con StackAdapt.
