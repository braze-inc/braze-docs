---
nav_title: Fidelización abierta
article_title: Fidelización abierta
description: "La integración de Braze y Open Loyalty te permite sincronizar datos de fidelización -como saldo de puntos, cambios de nivel y advertencias de caducidad- directamente en Braze en tiempo real."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Fidelización abierta

> [Open Loyalty](https://www.openloyalty.io/) es una plataforma de programas de fidelización basada en la nube que te permite crear y gestionar programas de recompensa y fidelización de clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización -como el saldo de puntos, los cambios de nivel y las advertencias de caducidad- directamente en Braze en tiempo real. Te permite desencadenar mensajes personalizados (correo electrónico, push, SMS) cuando cambia el estado de fidelización de un usuario.

_Esta integración la mantiene Open Loyalty_

## Sobre la integración

Esta integración utiliza transformaciones de datos Braze para capturar webhooks de Open Loyalty y mapearlos en perfiles de usuario Braze.

* **Actualizaciones en tiempo real**: Push eventos de fidelización (puntos ganados, subidas de nivel) a Braze.
* **Personalización**: Utiliza atributos de fidelización (saldo actual, nombre del siguiente nivel) en tus plantillas Braze.
* **Bidireccional**: Actualiza los atributos personalizados de los clientes de Open Loyalty basándote en los datos de interacción de Braze.

## Ejemplos

Esta integración abarca los siguientes flujos de datos:

1. **Sincronizar eventos con Braze (Entrada)**: Sigue los cambios de puntos, las subidas de nivel o los canjes de recompensas enviando datos de Open Loyalty a Braze. La Transformación de Datos convierte estos datos en un Evento de Usuario.
2. **Modificación de los Miembros Abiertos de Fidelización (Salientes)**: Actualiza automáticamente los datos de los miembros en Open Loyalty en función del comportamiento del usuario en Braze, como añadir etiquetas "VIP" o actualizar atributos personalizados.

## Requisitos previos

Antes de empezar, necesitas lo siguiente:

| Requisito | Descripción |
| :--- | :--- |
| Abrir cuenta de fidelización | Necesitas una cuenta de Administrador en un Inquilino Abierto de Fidelización para beneficiarte de esta asociación. |
| Clave de API REST de Fidelización Abierta | Una clave de API REST de Open Loyalty (para integraciones que envían datos de Braze a Open Loyalty). <br><br> Créala en **Configuración > Administradores > Claves de API**. |
| Clave de API REST Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Crea esta clave en el panel de Braze desde **Configuración** > **Claves de API**. |
| Transformación de datos Braze | Necesitas acceder a la pestaña "Configuración de datos" en Braze para configurar los escuchadores de webhook. |
| Coincidencia de ID | El `external_id` del usuario en Braze debe coincidir con su `loyaltyCardNumber` (u otro identificador predeterminado) en Open Loyalty. |
| ID de inquilino | Tu ID de inquilino de fidelización abierta (necesario para las actualizaciones salientes). |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integración

La integración principal sincroniza los eventos webhook de Open Loyalty con Braze mediante la Transformación de Datos.

### Paso 1: Generar la URL del Webhook en Braze

Primero, crea una transformación de datos en Braze para generar una URL única para recibir datos.

1.  En Braze, abre **Configuración de Datos > Transformación de Datos**.
2.  Haz clic en **Crear transformación**.
3.  Rellena los siguientes campos:
     * **Nombre de la transformación**: Proporciona un nombre descriptivo (por ejemplo, "Eventos de actualización de puntos de fidelización abiertos").
     * **Selecciona el destino**: Elige **POST: Seguimiento de usuarios**.
4.  Haz clic en **Crear transformación**.
5.  Localiza la **URL del webhook** en la parte derecha y haz clic en **Copiar**.

{% alert important %}
Guarda bien esta URL; la necesitas para el siguiente paso.
{% endalert %}

### Paso 2: Crear la suscripción al webhook en Open Loyalty

Dile a Open Loyalty que envíe eventos específicos a la URL que acabas de generar.

1.  Accede a tu Panel de Administración de Open Fidelización.
2.  Ve a **General > Webhooks**.
3.  Haz clic en **Añadir nuevo webhook** y configura la suscripción:
    * **eventName**: Selecciona el evento del que quieres hacer un seguimiento (por ejemplo, `AvailablePointsAmountChanged`, `CustomerLevelChanged`, o `CampaignEffectWasApplied`).
    * **url**: Pega la URL del Webhook Braze del Paso 1.
    * Añade las siguientes cabeceras:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Guarda la suscripción al webhook.

### Paso 3: Configurar la transformación de datos

Escribe la lógica JavaScript en Braze para mapear la carga útil entrante de Open Loyalty a propiedades Braze.

1.  En Braze, abre la transformación de datos que creaste en el Paso 1.
2.  Desencadena el evento en Open Loyalty (por ejemplo, cambia los puntos de un miembro o asigna un nivel) para generar una carga útil de muestra en el panel de **detalles del webhook**.
3.  En el editor de **código de Transformación**, escribe un script para mapear los datos entrantes. Utiliza el siguiente ejemplo como guía:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,
     
      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",
     
      // timestamp
      "time": new Date().toISOString(),
     
      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4\. Haz clic en **Validar** para asegurarte de que el código se ejecuta con tu carga útil de muestra y, a continuación, haz clic en **Activar**.


## Utilizar la fidelización abierta con Braze

Una vez completada la integración de entrada, configura **las Actualizaciones de salida** para modificar los miembros de Open Loyalty en función del comportamiento de Braze.

### Paso 1: Configurar campaña Webhook Braze

Este proceso utiliza Webhooks Braze para enviar una solicitud `PATCH` a la API de miembros de Fidelización Abierta (por ejemplo, para añadir una etiqueta "VIP").

1.  En Braze, crea una nueva **campaña Webhook** (o utiliza un Webhook dentro de un Canvas).
2.  Haz clic en **Componer webhook**.
3.  **URL del webhook**: Construye la URL utilizando tu instancia de Open Loyalty, el ID de inquilino y la variable Braze Liquid para el ID de usuario.
    * Formato:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Rellena los siguientes campos:   
    * **Método de solicitud**: `PATCH`
    * **Encabezados de solicitud**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Cuerpo de la solicitud**: Selecciona `Raw text` y pega la carga útil:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Paso 2: Configura el desencadenador

1.  Navega hasta la pestaña **Programa de** **entrega** o de **entrada**.
2.  Rellena los siguientes campos:
    * **Método de entrega**: Basado en la acción.
    * **Desencadenar**: Define el desencadenante correspondiente (por ejemplo, un usuario entra en un segmento concreto en Braze).
    * **Lanzamiento**: Activa la campaña.

## Solución de problemas

### Verificar Eventos Entrantes
Cuando la Transformación de datos está activa, los datos aparecen en Braze como un evento personalizado. Compruébalo creando una campaña con un desencadenante **Realizar evento personalizado** y comprobando si el evento que has definido (por ejemplo, `Loyalty Event Triggered`) está disponible.

### Verificar los webhooks salientes
Comprueba el registro de actividad de mensajes en Braze para asegurarte de que el webhook devolvió un estado `200 OK`.
* **Error 401**: Comprueba tu token de la API de fidelización abierta.
* **Error 404**: El ID de usuario en Braze no existe en Open Fidelización.