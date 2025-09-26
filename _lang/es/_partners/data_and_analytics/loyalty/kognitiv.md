---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire es un sistema tecnológico de fidelización que le permite implementar y evaluar su estrategia de fidelización, ofreciendo capacidades innovadoras y comunicaciones personalizadas con los miembros para mejorar la eficacia del programa."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) es un sistema tecnológico de fidelización que ayuda a desbloquear experiencias de cliente inigualables a través de programas de fidelización basados en resultados que amplifican el compromiso del cliente, aumentan el gasto y celebran el comportamiento leal.

_Esta integración está mantenida por Kognitiv Inspire._

## Sobre la integración

La integración de Braze y Kognitiv le permite implementar y evaluar su estrategia de fidelización, ofreciendo capacidades innovadoras y comunicaciones personalizadas a los miembros para mejorar la eficacia del programa.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Kognitiv | Para beneficiarse de esta asociación es necesario disponer de una cuenta [Kognitiv](http://kognitiv.com). |
| Clave API de Kognitiv | Una clave REST API de Kognitiv. Puedes crearlo en la página de **tokens de seguridad de la API**. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

- **Inscripción personalizada en programas de fidelización**: Impulsa a tus miembros en su recorrido de fidelización con una inscripción al programa sin complicaciones y una notificación de bienvenida personalizada entregada a través de su canal preferido.
- **Emisión de recompensas y notificación de interacción**: Mantén viva la chispa de la fidelización emitiendo recompensas y notificaciones que celebren los hitos de cada miembro.
- **Categorización y segmentación estratégica de los miembros**: Permita un compromiso más personalizado clasificando y segmentando a los miembros en función del gasto, el compromiso y reglas empresariales simples o complejas adaptadas a las necesidades específicas de su marca.
- **Notificación en tiempo real de los requisitos para la promoción**: Haz que cada miembro se sienta especial con notificaciones instantáneas de su elegibilidad para promociones exclusivas.

## Integración

Utilice los webhooks de Kognitiv para enviar solicitudes a Braze cuando se produzcan eventos de fidelización. Los siguientes ejemplos ilustran cómo utilizar Kognitiv y Braze para emitir una recompensa, registrar a un usuario de Kognitiv en Braze y enviarle un correo electrónico de bienvenida.

{% raw %}
### Braze: emisión de recompensas

El siguiente ejemplo de Kognitiv emite una recompensa para los miembros. Kognitiv Inspire comunicará ese evento de emisión de recompensas a Braze como un evento personalizado a través de webhooks. Para enviar un correo electrónico de seguimiento para comunicar la recompensa, cree una campaña o Canvas que se active a partir de ese evento personalizado.

**URL del webhook**: `<braze-api-rest-endpoint>`
**Cuerpo de la solicitud**: `Raw Text`

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: Portador `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Cuerpo de la solicitud

```json
{ 
  "events" : [ 
    { 
    "external_id" : "{{memberId}}", 
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38", 
    "name" : "rewards_issued", 
    "time" : "{{issuedDate}}", 
    "issued_date" : "{{issuedDate}}", 
    "issued_location_name" : "{{issuedLocationName}}", 
    "reward_type" : "{{rewardType}}" 
    } 
  ] 
}
```

### Crear un usuario y enviar un correo electrónico de bienvenida

El siguiente ejemplo de Kognitiv crea un nuevo usuario en Braze cuando se inscribe en KLS. Para programar un correo electrónico de bienvenida para este usuario, cree una campaña o un lienzo en Braze que se active en función de atributos personalizados específicos.

**URL del webhook**: `<braze-api-rest-endpoint>` <br>
**Cuerpo de la solicitud**: `Raw Text`

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: Portador `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Cuerpo de la solicitud

```json
{ 
  "attributes": [ 
    { 
      "app_id": "93ec5a59-3752-4a45-855b6109ba38", 
      "bio": "Software Architect", 
      "country": "{{memberAddressCO}}", 
      "email": "{{memberEmail}}", 
      "email_subscribe": "opted_in", 
      "external_id": "{{memberId}}", 
      "first_name": "{{memberFirstName}}", 
      "home_city": "{{memberAddressCity}}", 
      "time_zone": "America/Chicago", 
      "total_points_balance": "{{memberPointsAvailable}}", 
      "CreatedKLS": "{{issuedTimestamp}}", 
      "email_contact_allowed" : "{{memberEmailContactAllowed}}", 
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}", 
      "date_joined": "{{issuedDate}}" 
    } 
  ] 
}
```
{% endraw %}

## Documentación y características de integración de Kognitiv Inspire

Una vez que integre Braze con Kognitiv Inspire, Kognitiv le permite acceder a su amplia cartera de API, a las funciones de webhook de vanguardia y a las sólidas capacidades de importación y exportación de datos para una transferencia masiva sin problemas. Para obtener más información sobre las funciones y capacidades de integración de Kognitiv Inspire, consulte la [guía de recursos](https://info.kognitivloyalty.com) de Kognitiv o póngase en contacto con ellos para una demostración guiada.

### Puntos finales

**Autorización de la API REST**
- Región de EEUU: `https://app.kognitivloyalty.com/Auth/connect/token`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/Auth/connect/token`
- Región APAC: `https://aus.kognitivloyalty.com/Auth/connect/token`

**API REST (URL base)**
- Región de EEUU: `https://app.kognitivloyalty.com/api`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/api`
- Región APAC: `https://aus.kognitivloyalty.com/api`

**Puntos finales de servicios Web (URL base)**
- Región de EEUU: `https://app.kognitivloyalty.com/WS`
- Región CA/EMEA: `https://ca.kognitivloyalty.com/WS`
- Región APAC: `https://aus.kognitivloyalty.com/WS`

Para obtener más información sobre la configuración de tokens de acceso y puntos finales SFTP, ponte en contacto con Kognitiv para una demostración.


