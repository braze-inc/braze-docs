---
nav_title: Nift
article_title: Nift
description: "Este artículo de referencia describe la asociación entre Braze y Nift, una plataforma bilateral que ayuda a las empresas a adquirir, captar y retener clientes."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) ayuda a las empresas a captar, fidelizar y retener clientes. La plataforma de dos caras ayuda a los socios a dar las gracias a sus clientes con tarjetas regalo Nift. Dar las gracias a los clientes aumenta su valor de duración del ciclo de vida y genera ingresos incrementales.

_Esta integración está mantenida por Nift._

## Sobre la integración

La integración de Braze y Nift te permite desencadenar automáticamente "agradecimientos" con regalos de Nift en momentos clave del ciclo de vida del cliente e identificar qué clientes utilizaron su regalo. Las tarjetas regalo de Nift pueden utilizarse para acceder a productos y servicios suministrados por marcas que confían en la tecnología de emparejamiento de Nift para captar nuevos clientes de forma rentable a escala.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Nift | Se necesita una cuenta Nift para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST Braze con todos los permisos de datos de usuario. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conecta con Braze en Nift

Visita tu [panel de Nift](https://www.gonift.com/users/sign_in), ve a **Cuentas** > **Integraciones** > **Braze** y haz clic en **Conectar**.

### Paso 2: Añadir credenciales Braze

En la página **Vincula tu cuenta Braze**, proporciona tu clave de API REST Braze y selecciona tu punto final Braze, que dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints).

Puedes cambiar el nombre del parámetro ID de cliente en el enlace de referidos enviado a tus clientes. Nift lo utilizará para marcar a tus clientes como procesados en Braze cuando hayan seleccionado un regalo de una de nuestras marcas.

Haz clic en **Vincular cuenta**.

!["Página de integración del servicio Nift que solicita al usuario la clave de API de Braze y la URL del panel de Braze.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Utilizar la integración

Para utilizar la integración, distribuye el enlace de referidos en tu mensajería. Cuando tu cliente utilice el enlace de referidos y seleccione un regalo de una de nuestras marcas, Nift lo marcará como procesado en Braze.

Tras la integración con Braze, Nift empujará automáticamente los eventos al registro Braze existente del cliente con los siguientes datos:

- Nombre del evento: `nift_processed`
- Hora: La hora en que el cliente seleccionó/utilizó el regalo



