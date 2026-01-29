---
nav_title: Autenticación del correo electrónico
article_title: Autenticación del correo electrónico
page_order: 2
page_type: reference
description: "Este artículo de referencia trata sobre la autenticación del correo electrónico, un conjunto de técnicas destinadas a dotar a su correo electrónico de información verificable sobre su origen."
channel: email

---

# Autenticación del correo electrónico

> La autenticación del correo electrónico es un conjunto de técnicas que dotan a sus mensajes de información verificable sobre su origen.<br><br>Una autenticación adecuada es crucial para que los proveedores de servicios de Internet (ISP) le reconozcan como remitente de correos electrónicos deseables y le entreguen su correo inmediatamente. Sin autenticación, se presume que tu alcance es fraudulento. 

## Métodos de autenticación

### Marco de la Política de Remitentes (SPF)

Este método confirma que su dirección IP de envío de correo electrónico Braze está autorizada a enviar correo en su nombre. SPF es su autenticación básica y se consigue publicando los registros de texto en la configuración DNS. El servidor receptor comprobará los registros de DNS y determinará si son auténticos. Este método está diseñado para validar el remitente del correo electrónico.

Braze configura tu registro SPF cuando configuramos tus IP y dominios. Aparte de añadir los registros de DNS que te proporcionamos, no tienes que hacer nada más.

### Correo identificado por claves de dominio (DKIM)

Este método confirma que su dominio de envío de correo electrónico Braze está autorizado a enviar correo en su nombre. Este método está diseñado para validar la autenticidad del remitente y valida que se preserve la integridad del mensaje. También utiliza firmas digitales criptográficas individuales para que los ISP puedan estar seguros de que el correo que entregan es el mismo que usted envió.

Braze firma el correo con tu clave privada secreta. Los ISP verifican la firma con su clave pública, que está almacenada en su registro DNS personalizado. No hay dos firmas exactamente iguales, y sólo tu clave pública puede verificar con éxito la firma de tu clave privada.

Braze configura tu registro DKIM cuando configuramos tus IP y dominios. Aparte de añadir los registros de DNS que te proporcionamos, no tienes que hacer nada más.

### Autenticación, notificación y conformidad de mensajes basada en dominios (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) es un protocolo de autenticación de correo electrónico para que los remitentes de correo electrónico demuestren la legitimidad de su correo, lo que habilita la confianza del receptor del buzón y fomenta la aceptación del correo. DMARC permite a los remitentes de correo electrónico especificar cómo tratar los correos electrónicos que no se autenticaron mediante Sender Policy Framework (SPF) o Domain Keys Identified Mail (DKIM). Esto se consigue verificando que se superan las comprobaciones SPF y DKIM. 

Los remitentes dan instrucciones a los proveedores de buzones sobre cómo tratar el correo que no supera las comprobaciones de firma o autenticación. Los fallos pueden indicar suplantación de identidad. Puedes indicar a los proveedores que rechacen o pongan en cuarentena el correo defectuoso y que envíen informes automatizados. Esto ayuda a los proveedores a identificar a los emisores de correo electrónico no deseado, bloquear el correo electrónico malicioso, minimizar los falsos positivos y mejorar la transparencia de los informes de autenticación.

#### Cómo funciona

Para implementar DMARC, debe publicar un registro DMARC en el sistema de nombres de dominio (DNS). Se trata de un registro TXT que expresa públicamente la política de su dominio de correo electrónico tras comprobar el estado de SPF y DKIM. DMARC autentica si SPF o DKIM, o ambos, pasan. A esto se le llama Alineación DMARC.

Un registro DMARC también indica a los servidores de correo electrónico que envíen informes XML a la dirección de correo electrónico de notificación que figura en el registro DMARC. Estos informes proporcionan información sobre cómo se mueve su correo electrónico por el ecosistema y le permiten identificar todo lo que intenta utilizar su dominio de correo electrónico para enviar comunicaciones por correo electrónico.

Establece una política DMARC en el dominio raíz para que se aplique a todos los subdominios. Esto evita una configuración adicional en los subdominios actuales y futuros. Puedes establecer una de las siguientes políticas:

| Política | Impacto |
| --- | --- |
| Ninguno | Indica al proveedor de buzones que no realice ninguna acción contra los mensajes que fallen. |
| Cuarentena | Indica al proveedor del buzón que envíe los mensajes que fallen a la carpeta de correo no deseado. |
| Rechazar | Indique al proveedor del buzón que los mensajes que fallen irán a la carpeta de correo no deseado y deben bloquearse. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Cómo comprobar la autenticación DMARC de su dominio

Hay dos opciones para comprobar la autenticación DMARC de su dominio:

- **Opción 1:** Puede introducir su dominio o subdominio principal en cualquier comprobador DMARC de terceros, como [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para comprobar si tiene una política DMARC y cuál es su configuración.
    - **MXToolbox**: Si configura su DMARC como dominio raíz, introdúzcalo en MXToolbox. Si configura el DMARC en el subdominio, introduzca el subdominio en MXToolbox. Tenga en cuenta que MXToolbox no "mira hacia arriba o hacia abajo" cuando realiza búsquedas. Esto significa que si configura el DMARC en el dominio raíz e introduce el subdominio, MXToolbox mostrará un fallo ya que no sabe que el DMARC se ha configurado en el dominio raíz.
- **Opción 2:** Abra un correo electrónico de su dominio o subdominio en su buzón y busque el mensaje original para comprobar si DMARC está pasando la autenticación en este correo electrónico.

Por ejemplo, si utilizas Gmail, sigue estos pasos:

1. Haga clic en **Más** <i class="fa-solid fa-ellipsis"></i> en un mensaje de correo electrónico.
2. Seleccione **Mostrar original**.
3. Comprueba si tienes un estado "PASS" para **DMARC**.

![Un correo electrónico que tiene "PASS" como valor DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

