---
nav_title: Justuno
article_title: Justuno
description: "Aprende a integrar Justuno con Braze para aprovechar los datos de clientes en ambas plataformas y crear experiencias más personalizadas para todas las audiencias."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) te permite crear experiencias de visita totalmente optimizadas para todas tus audiencias con segmentos dinámicos, ofreciendo la segmentación más avanzada disponible, todo ello sin afectar a la velocidad del sitio ni aumentar el trabajo de desarrollo. Analiza las tasas de conversión consultando análisis personalizados como el número de perfiles creados, la tasa de retorno de visitantes influenciados y las páginas por sesión para mantener una ventaja de marketing en tu sector. Justuno te habilita para aumentar los ingresos por visitante, establecer interacciones significativas con los clientes y hacer crecer tu negocio. Optimiza todo el recorrido de la audiencia de extremo a extremo con una plataforma conectada.

## Ejemplos

Braze permite a cualquier especialista en marketing recopilar cualquier cantidad de datos de cualquier fuente y actuar sobre ellos, para que puedas interactuar de forma creativa con los clientes en tiempo real, en todos los canales y desde una sola plataforma.

La integración de Justuno y Braze te ofrece lo mejor de ambos mundos. Puedes combinar los datos de clientes guardados en Braze con los datos de visitantes y clientes guardados en Justuno y crear experiencias más personalizadas para todas las audiencias. Esto aumenta la eficacia de tus campañas de marketing y la interacción con los clientes.

## Requisitos previos

| Clave de API REST de Braze | Una clave de API REST de Braze con los permisos `users.track` y `custom_attributes.get`.<br><br>Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto final REST de Braze | URL de tu punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de Justuno con Braze

### Paso 1: Crear atributos personalizados en Braze

Para sincronizar los atributos de usuario de Justuno con Braze, tendrás que crear esos atributos en Braze si aún no lo has hecho. Para ello, ve a **Configuración de datos** > **Atributos personalizados** y, a continuación, crea tus atributos personalizados. Para una guía completa, consulta [Gestionar atributos personalizados en Braze]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

### Paso 2: Añade la aplicación Braze a Justuno

#### Paso 2.1: Añádelo a tu cuenta

Para añadir la aplicación Braze a tu cuenta de Justuno, ve a **Configuración de la cuenta** > **Aplicaciones** y, a continuación, busca y selecciona la aplicación Braze.

![La página "Conectar aplicaciones" en Justuno con la aplicación Braze mostrada en la lista de resultados de búsqueda.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Introduce la clave de API y la URL base [que creaste anteriormente](#prerequisites) y, a continuación, selecciona **Conectar**.

![La ventana emergente de Autenticación Braze que solicita una clave de API Braze y una URL base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Paso 2.2: Añádelo a tu flujo de trabajo

Para añadir la aplicación Braze a tu [flujo de trabajo de Justuno](https://hub.justuno.com/knowledge/workflows-overview), arrastra y suelta la acción **Sincronizar con aplicación** en tu flujo de trabajo, y luego elige **Seleccionar aplicación** > **Braze**.

![La opción "Seleccionar aplicación" situada en la acción "Sincronizar con la aplicación".]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Paso 3: Conecta tus grupos de suscripción Braze

Para enviar datos de perfil desde Justuno a un correo electrónico Braze específico o a un grupo de suscripción SMS, tendrás que añadir su ID a la aplicación Braze en tu flujo de trabajo Justuno.

| Tipo de ID                          | ¿Es necesario? | Descripción                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS ID de grupo de suscripción  | Sí       | Este ID se utiliza para recoger el consentimiento de SMS de los perfiles de usuario. Si no se introduce ningún ID en Justuno, los perfiles no tendrán consentimiento cuando Justuno empuje ese perfil a Braze. |
| ID del grupo de suscripción al correo electrónico Braze | No        | Si no se introduce este ID en Justuno, Justuno enviará los datos de perfil a Braze como usuario sin grupos de suscripción asociados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Paso 3.1: Localizar los ID en Braze

Para localizar estos ID en el panel de Braze:

1. Vaya a **Audiencia** > **Suscripciones**.
2. Para cada grupo de suscripción, anota el ID situado en la columna ID.

#### Paso 3.2: Añade los ID a la aplicación Braze

En tu flujo de trabajo Justuno, abre la aplicación Braze e introduce los ID de cada grupo de suscripción.

![La aplicación Braze abierta en un flujo de trabajo Justuno con la opción de añadir ID de grupo de suscripción por correo electrónico y SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Paso 4: Configura tus atributos

Los siguientes atributos se sincronizan automáticamente desde Justuno a Braze:

- Correo electrónico  
- Teléfono  
- Nombre  
- Apellido  
- Idioma  
- Género  
- País

Para sincronizar atributos adicionales:

1. En la aplicación Braze dentro de tu flujo de trabajo, selecciona **Sincronizar otra propiedad**.
    ![La aplicación Braze abierta en un flujo de trabajo de Justuno mostrando la opción "Sincronizar otra propiedad".]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Elige qué atributos Braze quieres sincronizar.
3. Haz coincidir las propiedades en Justuno con sus equivalentes en Braze (como los contactos sociales, cumpleaños, preferencias de compra, respuestas a cuestionarios y similares). Ten en cuenta que estas propiedades se consideran datos de 0 o datos de 1a parte. Para saber más, consulta [Justuno: Recopilación de datos de visitantes](https://www.justuno.com/guides/zero-first-party-data/).
4. En el constructor de flujos de trabajo, elige **Guardar**, **Vista previa** o **Publicar** tu flujo de trabajo.
    ![Se abrió el menú "Publicar" con las opciones de guardar, vista previa o mostrar el historial de versiones.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Lo que hay que saber

- Debes introducir manualmente el ID del grupo de suscripción en la configuración de la aplicación.  
- Los siguientes tipos de datos Braze **no** son **compatibles**: Objeto, matriz de objetos.  
- El consentimiento implícito por SMS se proporciona cuando no se utiliza el campo de consentimiento por SMS de Justuno.  
- El consentimiento explícito por SMS se respeta si el diseño de Justuno incluye el campo de consentimiento.
