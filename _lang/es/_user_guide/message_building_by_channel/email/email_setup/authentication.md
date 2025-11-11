---
nav_title: Autenticación de correo electrónico
article_title: Autenticación de correo electrónico
page_order: 2
page_type: reference
description: "Este artículo de referencia trata de la autenticación del correo electrónico, un conjunto de técnicas destinadas a dotar a tu correo electrónico de información verificable sobre su origen."
channel: email

---

# Autenticación de correo electrónico

> La autenticación del correo electrónico es un conjunto de técnicas que dotan a tus correos electrónicos de información verificable sobre su origen.<br><br>Una autenticación adecuada es crucial para que los proveedores de servicios de Internet (ISP) te reconozcan como remitente de correos electrónicos deseables y entreguen tu correo inmediatamente. Sin autenticación, se presume que tu alcance es fraudulento. 

## Métodos de autenticación

### Marco de la Política de Remitentes (SPF)

Este método confirma que tu dirección IP de envío por correo electrónico Braze está autorizada a enviar correo en tu nombre. SPF es tu autenticación básica y se consigue publicando los registros de texto en la configuración de DNS. El servidor receptor comprobará los registros de DNS y determinará si son auténticos. Este método está diseñado para validar al remitente del correo electrónico.

Tu registro SPF se configurará cuando Braze configure tus IP y dominios: aparte de añadir los registros de DNS que te proporcionamos, no es necesaria ninguna otra acción.

### Correo identificado por claves de dominio (DKIM)

Este método confirma que tu dominio de envío de correo electrónico Braze está autorizado a enviar correo en tu nombre. Este método está diseñado para validar la autenticidad del remitente y valida que se preserve la integridad del mensaje. También utiliza firmas digitales criptográficas individuales para que los ISP puedan estar seguros de que el correo que entregan es el mismo que enviaste.

Braze firma el correo con tu clave privada secreta. Los ISP verifican la firma con tu clave pública, que está almacenada en tu registro de DNS personalizado. No hay dos firmas exactamente iguales, y sólo tu clave pública puede verificar con éxito la firma de tu clave privada.

Tu registro DKIM se configurará cuando Braze configure tus IP y dominios; más allá de añadir los registros de DNS que te proporcionamos, no es necesaria ninguna otra acción.

### Autenticación, notificación y conformidad de mensajes basados en dominios (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) es un protocolo de autenticación de correo electrónico para que los remitentes de correo electrónico demuestren la legitimidad de su correo, lo que habilita la confianza del receptor del buzón y fomenta la aceptación del correo. DMARC permite a los remitentes de correo electrónico especificar cómo gestionar los correos electrónicos que no se autenticaron mediante el Marco de Política del Remitente (SPF) o el Correo Identificado por Claves de Dominio (DKIM). Esto se consigue verificando que se superan las comprobaciones SPF y DKIM. 

Los remitentes pueden dar instrucciones a los proveedores de buzones sobre cómo deben tratar el correo que no ha superado sus comprobaciones de firma o autenticación. Los fallos podrían indicar que otros intentan imitarte a ti o a tu correo electrónico. Los remitentes pueden indicar a los proveedores de buzones que rechacen o pongan en cuarentena el correo, e incluso enviar informes automatizados sobre el correo que no supera las comprobaciones. Al hacerlo, los proveedores de correo electrónico pueden identificar mejor a los emisores de correo no deseado y evitar que el correo malicioso invada los buzones de entrada, al tiempo que minimizan los falsos positivos y proporcionan mejores informes de autenticación para una mayor transparencia en el mercado.

#### Cómo funciona

Para implantar DMARC, tienes que publicar un Registro DMARC en tu Sistema de Nombres de Dominio (DNS). Se trata de un registro TXT que expresa públicamente la política de tu dominio de correo electrónico tras comprobar el estado de SPF y DKIM. DMARC autentica si SPF o DKIM, o ambos, pasan. A esto se le llama Alineación DMARC.

Un registro DMARC también indica a los servidores de correo electrónico que envíen informes XML a la dirección de correo electrónico de notificación que figura en el registro DMARC. Estos informes proporcionan información sobre cómo se mueve tu correo electrónico por el ecosistema y te permiten identificar todo lo que intenta utilizar tu dominio de correo electrónico para enviar comunicaciones por correo electrónico.

La política que tengas en tu registro DMARC indicará al servidor de correo electrónico del destinatario participante qué hacer con el correo que no pase SPF y DKIM pero que afirme proceder de tu dominio. Braze recomienda establecer una política DMARC en el dominio raíz, que se aplicará a todos los subdominios. Esto significa que no será necesaria ninguna configuración adicional en los subdominios actuales ni en los nuevos en el futuro. Hay tres tipos de políticas que puedes establecer:

| Política | Impacto |
| --- | --- |
| Ninguno | Indica al proveedor de buzones que no realice ninguna acción contra los mensajes que fallen. |
| Cuarentena | Indica al proveedor del buzón que envíe los mensajes que fallen a la carpeta de correo no deseado. |
| Rechaza | Indica al proveedor del buzón que los mensajes que fallen irán a la carpeta de correo no deseado y deben bloquearse. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Cómo comprobar la autenticación DMARC de tu dominio

Hay dos opciones para comprobar la autenticación DMARC de tu dominio:

- **Opción 1:** Puedes introducir tu dominio o subdominio principal en cualquier comprobador de DMARC de terceros, como [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para comprobar si tienes una política DMARC y cuál es su configuración.
    - **MXToolbox**: Si configuras tu DMARC como dominio raíz, introdúcelo en MXToolbox. Si configuras el DMARC en el subdominio, introduce el subdominio en MXToolbox. Ten en cuenta que MXToolbox no "mira hacia arriba o hacia abajo" cuando realiza búsquedas. Esto significa que si configuras el DMARC en el dominio raíz e introduces el subdominio, MXToolbox mostrará un fallo, ya que no sabe que el DMARC se ha configurado en el dominio raíz.
- **Opción 2:** Abre un correo electrónico de tu dominio o subdominio en tu buzón, y busca el mensaje original para comprobar si DMARC está pasando la autenticación en este correo electrónico.

Por ejemplo, si utilizas Gmail, sigue estos pasos:

1. Haz clic en **Más** <i class="fa-solid fa-ellipsis"></i> en un mensaje de correo electrónico.
2. Selecciona **Mostrar original**.
3. Comprueba si tienes un estado "PASS" para **DMARC**.

\![Un correo electrónico que tiene "PASS" como valor DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

