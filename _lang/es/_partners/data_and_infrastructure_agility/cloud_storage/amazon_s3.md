---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Este artículo de referencia describe la asociación entre Braze y Amazon S3, un sistema de almacenamiento altamente escalable ofrecido por Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) es un sistema de almacenamiento altamente escalable ofrecido por Amazon Web Services.



- 
- 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Amazon S3 | Se necesita una cuenta de Amazon S3 para aprovechar esta asociación. |
| Contenedor de S3 dedicado | Antes de integrarte con Amazon S3, debes crear un contenedor de S3 para tu aplicación.<br><br>Si ya tienes un contenedor de S3, te recomendamos que crees un nuevo contenedor específico para Braze, de modo que puedas limitar los permisos. Consulta las siguientes instrucciones sobre cómo crear un nuevo contenedor. |
| Currents | Para volver a exportar datos a Amazon S3, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en tu cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 



1.  
2. Tras iniciar sesión, selecciona **S3** en la categoría **Almacenamiento y entrega de contenidos**. 
3. Selecciona **Crear contenedor** en la siguiente pantalla. 
4. Se te pedirá que crees tu contenedor y selecciones una región.

{% alert note %}

{% endalert %}

## Integración

 

- [Método de clave de acceso secreta de AWS](#aws-secret-key-auth-method)
- [Método ARN del rol de AWS](#aws-role-arn-auth-method)

## Método de autenticación de clave secreta de AWS

Este método de autenticación genera una clave secreta y un ID de clave de acceso que habilita a Braze a autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear usuario {#secret-key-1}

Para recuperar tu ID de clave de acceso y tu clave de acceso secreta, tendrás que [crear un usuario IAM y un grupo de administradores en AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Paso 2: Obtener credenciales {#secret-key-2}

 

![][11]

### Paso 3: Crear política {#secret-key-3}

 A continuación, selecciona **Crear tu propia política**. Esto dará permisos limitados, para que Braze sólo pueda acceder a los contenedores especificados. 

![][12]

{% alert note %}

{% endalert %}

Especifica un nombre de política de tu elección, e introduce el siguiente fragmento de código en la sección **Documento de Política**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. Sin estos permisos, la integración no superará la comprobación de credenciales y no se creará.

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Exportación de datos del panel %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Paso 4: Adjuntar política {#secret-key-4}

  

![][13]

### Paso 5: Vincular Braze a AWS {#secret-key-5}

{% tabs %}
{% tab Braze Currents %}

En Braze, ve a **Integraciones de socios** > **Exportación de datos**.



 

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Mantén actualizados tu ID de clave de acceso a AWS y tu clave de acceso secreta. Si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

También puedes añadir las siguientes personalizaciones en función de tus necesidades:

- **Ruta de la carpeta:** De forma predeterminada, `currents`. Si esta carpeta no existe, Braze te la creará automáticamente. 
- **Encriptación AES-256 del lado del servidor, en reposo:** Está predeterminado en OFF e incluye la cabecera `x-amz-server-side-encryption`.



Una notificación te informará de si tus credenciales se han validado correctamente. AWS S3 debería estar ahora configurado para Braze Currents.

{% endtab %}
{% tab Exportación de datos del panel %}



 

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}

{% endalert %}

Una notificación te informará de si tus credenciales se han validado correctamente. AWS S3 debería estar ahora integrado en tu cuenta Braze.

{% endtab %}
{% endtabs %}

## Método de autenticación ARN del rol de AWS



### Paso 1: Crear política {#role-arn-1}

Para empezar, inicia sesión en la consola de administración de AWS como administrador de cuentas. 

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}

{% endalert %}

Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Documento de Política**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. Seleccione **Revisar política** cuando haya terminado.

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Exportación de datos del panel %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}



![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Paso 2: Crear rol {#role-arn-2}



![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Recupera el ID de tu cuenta Braze y el ID externo de tu cuenta Braze:
- **Currents**: En Braze, ve a **Integraciones de socios** > **Exportación de datos**.  Aquí encontrarás los identificadores necesarios para crear tu rol.
- **Exportación de datos del panel**:  

De vuelta en la consola de AWS, selecciona **Otra cuenta de AWS** como tipo de selector de entidad de confianza. Proporciona el ID de tu cuenta Braze, marca la casilla **Requerir ID externo** e introduce el ID externo Braze. Seleccione **Siguiente** cuando haya terminado.

![La página S3 "Crear rol". Esta página tiene campos para el nombre del rol, la descripción del rol, las entidades de confianza, las políticas y el límite de permisos.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Paso 3: Adjuntar política {#role-arn-3}

A continuación, adjunta al rol la política que creaste anteriormente. Busca la póliza en la barra de búsqueda, y coloca una marca de verificación junto a la póliza para adjuntarla. Seleccione **Siguiente** cuando haya terminado.

![ARN del rol]({{site.baseurl}}/assets/img/create_role_3_attach.png)



![ARN del rol]({{site.baseurl}}/assets/img/create_role_4_name.png)

Ahora deberías ver tu función recién creada en la lista.

### Paso 4: Enlace a Braze AWS {#role-arn-4}

En la consola de AWS, busca en la lista el rol que acabas de crear. 

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Toma nota del **ARN del Rol** en la parte superior de la página de resumen del Rol.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Vuelve a tu cuenta de Braze y copia el ARN del rol en el campo correspondiente.

{% tabs %}
{% tab Braze Currents %}

 

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Dale un nombre a tu Corriente. 

También puedes añadir las siguientes personalizaciones en función de tus necesidades:

- Ruta de la carpeta (predeterminada a `currents`)
- Encriptación AES-256 del lado del servidor, en reposo (predeterminada en OFF) - Incluye la cabecera `x-amz-server-side-encryption` 

  AWS S3 debería estar ahora configurado para Braze Currents.

{% alert important %}
Si recibes un error "Las credenciales de S3 no son válidas", puede deberse a una integración demasiado rápida después de crear un rol en AWS. Espera y vuelve a intentarlo.
{% endalert %}

{% endtab %}
{% tab Exportación de datos del panel %}



![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

En la página de **credenciales de AWS**, asegúrate de que el botón de opción **ARN de rol de AWS** está seleccionado y, a continuación, introduce el ARN de tu rol y el nombre de contenedor de S3 de AWS en los campos designados. 

{% alert tip %}

{% endalert %}

Una notificación te informará de si tus credenciales se han validado correctamente. AWS S3 debería estar ahora integrado en tu cuenta Braze.

{% endtab %}
{% endtabs %}

## Comportamiento de la exportación

Los usuarios que hayan integrado una solución de almacenamiento de datos en la nube e intenten exportar API, informes de cuadros de mando o informes CSV experimentarán lo siguiente:

- Todas las exportaciones de la API no devolverán una URL de descarga en el cuerpo de la respuesta y deberán recuperarse a través del almacenamiento de datos.
- Todos los informes del panel y los informes CSV se enviarán al correo electrónico del usuario para su descarga (sin necesidad de permisos de almacenamiento) y se realizará una copia de seguridad en Almacenamiento de datos. 

## Conectores múltiples

Si pretendes crear más de un conector Currents para enviarlo a tu contenedor de S3, podrás utilizar las mismas credenciales, pero deberás especificar una ruta de carpeta diferente para cada uno. Pueden crearse en el mismo espacio de trabajo, o dividirse y crearse en varios espacios de trabajo. También tienes la opción de crear una única política para cada integración, o crear una política que cubra ambas integraciones. 

Si planeas utilizar el mismo contenedor de S3 tanto para Currents como para la exportación de datos, tendrás que crear dos políticas distintas, ya que cada integración requiere permisos diferentes.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
