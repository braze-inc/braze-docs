---
nav_title: Jebbit
article_title: Jebbit
description: "Este artículo de referencia describe la asociación entre Braze y Jebbit, un PaaS que te permite pasar correos electrónicos y atributos de usuario de tus campañas de Jebbit como datos de usuario a Braze en tiempo real."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) es un PaaS que te permite crear experiencias atractivas para que los usuarios capturen datos propios.

_Esta integración está mantenida por Jebbit._

## Sobre la integración

La integración de Braze y Jebbit te permite pasar correos electrónicos de usuarios y atributos de tus campañas de Jebbit como datos de usuario a Braze en tiempo real. Estos datos pueden utilizarse para impulsar iniciativas de marketing, como campañas de correo electrónico personalizadas y activadores. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
|Cuenta Jebbit | Se necesita una cuenta Jebbit para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST Braze con todos los permisos de datos de usuario. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
|Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Cuando solicites la integración con Jebbit, comunica si hay que cumplir algún plazo estricto. Además, asegúrate de que tienes mapeados los atributos de tu(s) experiencia(s) Jebbit que te gustaría pasar a Braze.

### Paso 1: Proporcionar credenciales de API

Proporciona tus credenciales API a Jebbit en un archivo de texto a través de una solicitud de archivo de Dropbox.
Envía tu archivo utilizando la siguiente [URL de Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Paso 2: Confirmar el envío de la prueba

Un ingeniero de Jebbit asignado a tu integración enviará un envío de prueba de Jebbit a Braze, para que puedas ver cómo se verán los datos en tu entorno Braze. Este es el último paso para activar la integración. Ahora que tus datos Jebbit están configurados, utilízalos para impulsar tus iniciativas de marketing.

{% alert note %}
El ID de atributo que ha establecido en Jebbit es como se mostrará el nombre del campo de atributo en Braze.
{% endalert %}

## Personalización

Actualmente admitimos específicamente los puntos finales de [datos de usuario]({{site.baseurl}}/api/endpoints/user_data/), pero se pueden admitir solicitudes de puntos finales diferentes.

Los nombres de los campos de atributos también pueden personalizarse según sus preferencias.

Si quieres atributos adicionales de Jebbit en Braze, mapea el nuevo atributo en tu cuenta de Jebbit. El atributo se mostrará automáticamente en Braze a medida que recopiles datos para ese atributo.

