---
nav_title: Distribuciones con atributos personalizados
article_title: Distribuciones con atributos personalizados con Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Este artículo de referencia describe la integración de Braze con Voucherify. La integración con Braze te habilita para enviar códigos de Voucherify en tus mensajes de Braze."
page_type: partner
search_tag: Partner
---

# Distribuciones con atributos personalizados

> La integración con Braze te habilita para enviar códigos de Voucherify en tus mensajes de Braze. Este artículo de referencia explica cómo utilizar los atributos personalizados de Braze con las distribuciones de Voucherify.

_Esta integración es mantenida por Voucherify._

{% alert tip %}
Antes de utilizar los atributos personalizados Braze en las distribuciones de Voucherify, tienes que añadir tus usuarios Braze al panel de Voucherify. Puedes utilizar Braze Connected Content para sincronizar usuarios o importar tus clientes a través de CSV o API. Visita [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) para obtener más información.
{% endalert %}

Los atributos personalizados de Braze te habilitan para asignar códigos de Voucherify a atributos personalizados en perfiles de usuario en Braze. Puedes utilizar cupones únicos, tarjetas regalo, tarjetas de fidelización y códigos de referidos. Primero, conecta Voucherify con Braze, crea una distribución en Voucherify y, por último, crea una campaña en Braze con el fragmento de atributo personalizado en tu plantilla de mensajes.

## Paso 1: Conecta tu cuenta de Voucherify a Braze

Primero, conecta tu cuenta de Voucherify con Braze.

1. Copia la clave de API REST de tu cuenta Braze.
2. Ve al directorio **Integraciones** en tu panel de Voucherify, busca Braze y elige **Conectar.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Pega la clave de API de Braze y elige **Conectar**:  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Paso 2: Distribución del código

Cuando estés conectado, puedes iniciar una nueva [distribución](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) de Voucherify que asigne un código al atributo personalizado en el perfil de usuario en Braze. Más adelante, podrás utilizar los atributos recibidos con códigos en tus campañas Braze.

Antes de configurar la distribución, tienes que añadir tus usuarios Braze al panel de Voucherify. Visita [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) para obtener más información.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Puedes distribuir códigos a Braze utilizando dos modos:

- **Modo manual**
- Define un **flujo de trabajo automatizado** que desencadene la entrega de código en respuesta a una acción realizada por tus usuarios.

Tanto en modo manual como automático, Voucherify envía códigos únicos con sus atributos y los asigna a los atributos personalizados de Braze en los perfiles de usuario.

![Mapea campos a atributos personalizados]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Distribución manual %}

El modo manual es una acción única que asigna códigos a una audiencia elegida. Ve a **Distribuciones** en tu panel de control, ejecuta el administrador de distribuciones con el signo más y elige **Mensaje manual**.

1.  Ponle nombre a tu distribución.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Elige una campaña que sea fuente de códigos únicos **(1)** y selecciona un segmento de usuarios o un cliente único como receptores **(2)**. Visita [Voucherify](https://support.voucherify.io/article/51-customer-segments) para saber más sobre los segmentos de clientes.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  A continuación, añade permisos de marketing. Si no recopilas permisos de tu audiencia, desactiva la verificación de consentimiento.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Elige Braze como canal y mapea los campos personalizados que se añadirán al perfil de usuario en Braze. Debes añadir el campo que representa el código del vale publicado; el resto de campos son opcionales.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Cuando hayas terminado, podrás ver un resumen de la distribución. Haz clic en **Guardar y enviar** para entregar códigos a los perfiles de usuario en Braze.  

_Recuerda que todas las distribuciones manuales se envían con un retraso de 10 minutos._

{% endtab %}
{% tab Flujo de trabajo automático %}

Voucherify puede enviar códigos a Braze automáticamente en respuesta a los siguientes desencadenantes:

- **Segmento específico de Voucherify introducido/dejado por el cliente**
- **Publicación correcta del código**: el mensaje se envía cuando el código de una campaña se publica (asigna) a un cliente en Voucherify.
- **El estado del pedido ha cambiado** (pedido creado, pedido actualizado, pedido pagado, pedido cancelado)
- **Créditos de regalo añadidos**: el mensaje se envía cuando se añaden créditos de tarjeta regalo a la tarjeta del cliente.
- **Puntos de fidelización añadidos**: el mensaje se envía cuando se añaden puntos de fidelización al perfil del cliente.
- **Vales canjeados**: el mensaje se envía a los clientes que canjearon vales con éxito.
- **Devolución de canje de cupón**: el mensaje se envía al cliente cuyo canje se ha devuelto correctamente.
- **Canje de recompensas**: el mensaje se envía cuando un cliente canjea una recompensa por fidelización o referidos.
- **Se ha registrado un evento personalizado para un cliente**: el mensaje se desencadena cuando Voucherify registra un evento personalizado concreto.

Para configurar un flujo de trabajo automático con Braze y Voucherify, [visita el tutorial de distribuciones](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Paso 3: Utiliza atributos personalizados de Voucherify en tu campaña Braze

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Una vez añadido el atributo personalizado con el código a los atributos personalizados del cliente en Braze, puedes utilizarlo en tus campañas.

Edita el cuerpo del mensaje y añade el atributo personalizado definido en la distribución de Voucherify. Coloca {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} para mostrar el código único.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Cuando esté listo, podrás ver el código en la vista previa de tu mensaje.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

