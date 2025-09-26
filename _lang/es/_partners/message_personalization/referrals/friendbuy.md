---
nav_title: Friendbuy
article_title: Friendbuy
description: "Aprende a integrar Friendbuy con Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Aprovecha la integración entre Friendbuy y Braze para ampliar tus capacidades de correo electrónico y SMS mientras automatizas sin esfuerzo las comunicaciones de tus programas de recomendación y fidelización. Braze generará perfiles de cliente para todos los números de teléfono de adhesión voluntaria recogidos a través de Friendbuy.

_Esta integración está mantenida por Friendbuy._

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta Friendbuy   | Es necesario tener una [cuenta Friendbuy](https://retailer.friendbuy.io/) para beneficiarse de esta asociación.                                                              |
| Una clave de API REST Braze  | Una clave de API REST de Braze con permisos `users.track`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**.        |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende de la URL de tu instancia de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de Friendbuy

En [Friendbuy](https://retailer.friendbuy.io/), ve a **Centro de desarrollo** > **Integraciones** y, en la tarjeta de integración Braze, selecciona **Añadir integración**.

![La tarjeta de integración Braze en Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

En el formulario, introduce tu punto final REST y tu clave de API y, a continuación, selecciona **Instalar integración**.

![El formulario de integración de Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Vuelve a tu [cuenta Friendbuy](https://retailer.friendbuy.io/) y actualiza la página. Si la integración se ha realizado correctamente, aparecerá un mensaje similar al siguiente:

![integración instalada]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Atributos personalizados

| Nombre de atributo personalizado            | Definición                                                                                                                                         | Tipo de datos |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Estado de los referidos Friendbuy**    | Los recomendantes se clasifican como *Defensor* y los recomendados como *Amigo recomendado*.                                                          | Cadena    |
| **Nombre del cliente Friendbuy**      | El nombre que el cliente introdujo al enviar su información a través de un widget de recomendación                                                                 | Cadena    |
| **Enlace de referidos Friendbuy**      | Un enlace personal de referidos (PURL) generado para un Defensor. Por ejemplo, https://fbuy.io/EzcW                                                       | Cadena    |
| **Fecha de la última acción de Friendbuy** | La fecha y hora en que el Defensor compartió por última vez con un Amigo a través de cualquier canal de compartición. Si el Defensor aún no ha compartido, la propiedad no será visible. | Tiempo      |
| **ID de campaña de Friendbuy**        | El identificador de campaña asociado al enlace de recomendación personal generado para un promotor.                                                               | Cadena    |
| **Nombre de la campaña Friendbuy**      | Nombre de la campaña asociada al enlace de recomendación personal generado para un promotor.                                                             | Cadena    |
| **Código promocional Friendbuy**        | El último código de cupón de referencia distribuido al cliente. Nota: sólo se mostrará un código                                            | Cadena    |
| **Valor del cupón Friendbuy**       | Valor monetario del último código de cupón distribuido al cliente.                                                                     | Número    |
| **Estado del cupón Friendbuy**      | Estado del último código de cupón distribuido al cliente. Nota: el estado será "distribuido" o "canjeado".                            | Cadena    |
| **Moneda de cupón Friendbuy**    | Código de moneda (USD, CAD, etc.) o porcentaje (%) asociado al último código de cupón distribuido al cliente.                             | Cadena    |
| **ID de campaña del cupón Friendbuy** | El ID de campaña asociado al código de cupón generado para un cliente.                                                                          | Cadena    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Comportamiento por defecto

Antes de que los datos de clientes puedan enviarse a Braze, los clientes deben adherirse voluntariamente a través del widget de referidos marcando una o más casillas de las siguientes:

![widget de referidos]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuy utiliza la norma internacional (E.164) para verificar los números de teléfono reales. Los números no válidos, como `555-555-5555`, no se enviarán a Braze.
{% endalert %}

### Comportamiento de las casillas de verificación

| Casilla seleccionada | Comportamiento                                                        |
|-------------------|-----------------------------------------------------------------|
| Sólo correo electrónico        | Sólo se envía a Braze la dirección de correo electrónico del cliente.             |
| Sólo por teléfono        | Sólo se envía a Braze el número de teléfono del cliente.              |
| Ninguno           | No se envía ningún dato del cliente a Braze.                              |
| Ambos              | La dirección de correo electrónico y el número de teléfono del cliente se envían a Braze. |


