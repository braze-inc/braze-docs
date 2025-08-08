---
nav_title: Identificador Cifrado a nivel de campo
article_title: Identificador Cifrado a nivel de campo
page_order: 101
alias: "/field_level_encryption/"
description: "Este artículo de referencia explica cómo encriptar direcciones de correo electrónico para minimizar la información de identificación personal (PII) compartida en Braze."
page_type: reference
---

# Cifrado a nivel de campo del identificador

> Mediante el cifrado a nivel de campo identificador, puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.

{% alert important %}
La encriptación a nivel de campo identificador está disponible como característica adicional. Para empezar con el cifrado a nivel de campo identificador, ponte en contacto con tu director de cuentas Braze.
{% endalert %}

## Cómo funciona

Las direcciones de correo electrónico se deben codificar y cifrar antes de añadirlas a Braze. Cuando se envíe un mensaje, se realizará una llamada a AWS KMS para obtener la dirección de correo electrónico descifrada. A continuación, la dirección de correo electrónico con hash se insertará en los metadatos para que los eventos de entrega e interacción se vinculen al usuario original. Así es como Braze puede hacer un seguimiento del análisis del correo electrónico. Braze redactará cualquier dirección de correo electrónico en texto plano que se incluya y no almacenará la dirección de correo electrónico en texto plano del usuario.

## Requisitos previos

Para utilizar el cifrado a nivel de campo de identificador, debes tener acceso a AWS KMS para [cifrar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) y [aplicar hash a](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) las direcciones de correo electrónico **antes de** enviarlas a Braze. 

Sigue estos pasos para configurar tu método de autenticación con clave secreta de AWS.

1. Para recuperar tu ID de clave de acceso y tu clave de acceso secreta, [crea un usuario IAM y un grupo de administradores](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) en AWS con una política de permisos para el servicio de administración de claves de AWS. El usuario IAM debe tener los permisos [kms:Descifrar](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) y [kms:GenerarMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html). Para más detalles, consulta los [permisos de AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Selecciona **Mostrar credenciales de seguridad de usuario** para revelar tu ID de clave de acceso y tu clave de acceso secreta. Anota estas credenciales en algún sitio o selecciona el botón **Descargar credenciales**, ya que tendrás que introducirlas cuando conectes tus claves AWS KMS.
3. Debes configurar KMS en las siguientes regiones de AWS:
    - **Clústeres Braze US:** `us-east-1`
    - **Clústeres Braze UE:** `eu-central-1`
4. En el servicio de administración de claves de AWS, crea dos claves y asegúrate de que el usuario IAM está añadido en los permisos de uso de claves:
    - **[Cifrar/descifrar](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Selecciona el tipo de clave **Simétrica** y el uso de las claves **Cifrar y Descifrar**.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Selecciona Tipo de clave **simétrica** y **Generar y verificar el uso de la clave MAC**. La especificación de la clave debe ser **HMAC_256**. Después de crear la clave, anota en algún sitio el ID de la clave HMAC, ya que tendrás que introducirlo en Braze.

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Paso 1: Conecta tus claves AWS KMS

En el panel de Braze, ve a **Configuración de datos** > **Cifrado a nivel de campo**. Para tu configuración de AWS KMS, introduce lo siguiente:

- ID de la clave de acceso
- Clave de acceso secreta
- ID de la clave HMAC (no se puede actualizar después de guardarla)

## Paso 2: Selecciona tus campos encriptados

A continuación, selecciona **Dirección de correo electrónico** para codificar el campo. 

Cuando se activa la encriptación de un campo, no se puede revertir a un campo desencriptado. Esto significa que la encriptación es una configuración permanente. Cuando configures la encriptación de la dirección de correo electrónico, confirma que ningún usuario tiene direcciones de correo electrónico en el espacio de trabajo. Esto garantiza que no se almacenen direcciones de correo electrónico en texto plano en Braze al activar la característica para el espacio de trabajo.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Paso 3: Importar y actualizar usuarios

Cuando la encriptación a nivel de campo de identificador está activada, debes hacer hash y encriptar la dirección de correo electrónico antes de añadirla a Braze. Asegúrate de minusvalorar la dirección de correo electrónico antes de enviarla. Consulta el [objeto de atributos del usuario](#user-attributes-object) para más detalles.

Al actualizar la dirección de correo electrónico en Braze, debes utilizar el valor de correo electrónico hash siempre que se incluya `email`. Esto incluye lo siguiente:

- Puntos finales REST:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Añadir o actualizar usuarios mediante CSV

{% alert note %}
Al crear un nuevo usuario con una dirección de correo electrónico, debes añadir `email_encrypted` con el valor del correo electrónico encriptado del usuario. De lo contrario, no se creará el usuario. Del mismo modo, si vas a añadir una dirección de correo electrónico a un usuario existente que no tiene correo electrónico, debes añadir `email_encrypted`. De lo contrario, el usuario no será actualizado.
{% endalert %}

## Consideraciones

Estas características no son compatibles con el cifrado a nivel de campo identificador:

- Identificar y capturar la dirección de correo electrónico mediante SDK
- Formularios de captura de mensajes dentro de la aplicación por correo electrónico
- Informes sobre el dominio del destinatario, incluyendo gráficos del proveedor de buzón de correo Email Insights
- Filtrar direcciones de correo electrónico por expresión regular
- Sincronización de la audiencia
- Integración con Shopify

### Objeto de atributos del usuario

Cuando utilices el cifrado a nivel de campo del identificador con el punto final `/users/track`, toma nota de estos detalles de campo para el [objeto de atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- El campo `email` debe ser el valor hash del correo electrónico.
- El campo `email_encrypted` debe ser el valor encriptado del correo electrónico.

## Preguntas más frecuentes

### ¿Cuál es la diferencia entre cifrar y hashing?

La encriptación es una función bidireccional en la que es posible encriptar y desencriptar datos. Si el mismo valor de texto plano se cifra varias veces, el algoritmo de cifrado de AWS (AES-256-GCM) producirá valores cifrados diferentes. El hashing es una función unidireccional en la que el texto plano se codifica de forma que no se pueda descifrar. El hashing produce siempre el mismo valor. Esto nos permite mantener los estados de suscripción de varios usuarios que comparten la misma dirección de correo electrónico.

### ¿Qué dirección de correo electrónico debo utilizar en mi envío de prueba?

Las direcciones de correo electrónico en texto plano son compatibles con los envíos de prueba. Para ver el aspecto de un correo electrónico de un usuario concreto, haz lo siguiente:

1. Selecciona **Vista previa del mensaje como usuario**.
2. En **Envío de prueba**, selecciona **Anular atributos del destinatario con los atributos del usuario de la vista previa actual**.

{%raw%}
### ¿Qué ocurre si añado esta dirección de correo electrónico Liquid `{{${email_address}}}` en Braze?

Braze mostrará la dirección de correo electrónico en texto plano al enviar el correo electrónico. En la vista previa, mostraremos la versión encriptada del correo electrónico. Te recomendamos que utilices el ID externo del usuario si haces referencia a un usuario en una URL personalizada de un clic.

`{{${email_address}}}` no se admite actualmente en el centro de preferencias ni en las páginas de cancelar suscripción.
{%endraw%}

### ¿Qué dirección de correo electrónico debo esperar ver en Currents?

La dirección de correo electrónico con hash se incluye en los eventos de entrega e interacción por correo electrónico.

### ¿Qué dirección de correo electrónico debo esperar ver en el archivo de mensajes?

La dirección de correo electrónico en texto plano se incluye en el archivo de mensajería. Se envían directamente al proveedor de almacenamiento en la nube del cliente y puede haber otros datos personales incluidos en los cuerpos del correo electrónico.

### ¿Puedo utilizar mail-to list- cancelar suscripción para la gestión de suscripciones con codificación a nivel de campo identificador?

No. Si utilizas "mail-to list-unsubscribe", enviarás la dirección de correo electrónico descifrada en texto plano a Braze. Con el cifrado a nivel de campo identificador activado, admitimos el método HTTP: basado en URL, incluido el de un clic. También te recomendamos que incluyas un enlace para cancelar suscripción con un solo clic en el cuerpo de tu correo electrónico.

### ¿El cifrado a nivel de campo del identificador admite otros identificadores como el teléfono?

No. Actualmente, el cifrado a nivel de campo identificador sólo es compatible con las direcciones de correo electrónico.
