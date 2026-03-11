---
nav_title: Exportación de eventos de seguridad con S3
article_title: Configuración de seguridad Exportar con S3
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo exportar automáticamente los eventos de seguridad cada día a medianoche UTC a Amazon S3."
---

# Exportación de eventos de seguridad con Amazon S3

> Puedes exportar automáticamente los eventos de seguridad a Amazon S3, un proveedor de almacenamiento en la nube, con una tarea diaria que se ejecuta a medianoche UTC. Una vez configurado, no es necesario exportar manualmente los eventos de seguridad desde el panel. El trabajo exporta los eventos de seguridad de las últimas 24 horas en formato CSV al almacenamiento S3 que hayas configurado. El archivo CSV tiene la misma estructura que un informe exportado manualmente.

{% alert note %}
El límite de 10 000 filas solo se aplica a la descarga manual de informes CSV desde el panel. Las exportaciones de eventos de seguridad a S3 no están sujetas a este límite de filas.
{% endalert %}

El soporte de Braze admite dos métodos diferentes de autenticación y autorización de S3 para configurar la exportación de Amazon S3:

- Método de clave de acceso secreta de AWS
- Método ARN del rol de AWS

## Método de clave de acceso secreta de AWS

Este método genera una clave secreta y una ID de clave de acceso que permite a Braze autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear un usuario de gestión de identidades y accesos (IAM)

Para recuperar tu clave de acceso secreta y tu ID de clave de acceso, deberás crear un usuario de IAM siguiendo las instrucciones que se [indican](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin) en [Configuración de tu cuenta de AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Paso 2: Obtener credenciales

1. Después de crear un nuevo usuario, genera la clave de acceso y descarga tu ID de clave de acceso y tu clave de acceso secreta.

![Página de resumen de una función denominada «liyu-chen-test».]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Anota estas credenciales en algún lugar o descarga los archivos de credenciales, ya que tendrás que introducirlas en Braze más adelante.

![Campos que contienen la clave de acceso y la clave de acceso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Paso 3: Crear política

1. Ve a **IAM** (Gestión de identidades y accesos) > **Políticas** > **Crear política** para añadir permisos para tu usuario. 
2. Selecciona **Crear tu propia política**, que otorga permisos limitados para que Braze solo pueda acceder a los contenedores especificados.
3. Especifica el nombre de la política que desees.
4. Introduce el siguiente fragmento de código en la sección **Documento de política**. Asegúrate de sustituir «INSERTBUCKETNAME» por el nombre de contenedor. Sin estos permisos, la integración no superará la comprobación de credenciales y no se creará.

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

### Paso 4: Adjuntar política

1. Después de crear una nueva política, ve a **Usuarios** y selecciona tu usuario específico. 
2. En la pestaña **Permisos**, selecciona **Agregar permisos**, adjunta directamente la política y, a continuación, selecciona esa política. 

¡Ahora ya estás listo para vincular tus credenciales de AWS a tu cuenta de Braze!

### Paso 5: Vincula Braze con AWS

1. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración administrativa** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**.
2. Alternar **Exportar a AWS S3** en **Exportar a almacenamiento en la nube** y selecciona **la clave secreta de acceso de AWS**, que habilita la exportación a S3. 
3. Introduce lo siguiente:
- ID de clave de acceso a AWS
- Clave de acceso secreta de AWS
    - Al introducir esta clave, primero selecciona **«Probar credenciales»** para confirmar que tus credenciales funcionan.
- Nombre del contenedor de AWS 

![La página «Descarga de eventos de seguridad» con la cuenta de Braze y los ID externos de Braze rellenados.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Selecciona **Guardar cambios**. 

![Botón «Guardar cambios».]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

¡Has realizado la integración de AWS S3 en tu cuenta de Braze!

## Método ARN del rol de AWS

El método ARN de rol de AWS genera un nombre de recurso de Amazon (ARN) que permite a la cuenta de Amazon de Braze autenticarse como miembro de ese rol.

### Paso 1: Crear política

1. Inicia sesión en la consola de administración de AWS como administrador de la cuenta. 
2. En la consola de AWS, ve a la sección **IAM** (Gestión de identidades y accesos) > **Políticas** y, a continuación, selecciona **Crear política**.

![Una página con una lista de políticas y un botón para «Crear política».]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Documento de Política**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. 

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

{: start="4"}
4\. Selecciona **Siguiente** después de revisar la política.

![Una página que te permite revisar tu política y, opcionalmente, añadir permisos.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Asigna un nombre y una descripción a la política y, a continuación, selecciona **Crear política**.

![Una página para revisar y crear tu política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Paso 2: Crear rol

1. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración administrativa** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**. 
2. Selecciona **el ARN de la función de AWS**. 
3. Toma nota de los identificadores, el ID de cuenta de Braze y el ID externo de Braze necesarios para crear tu función.

![La página «Descarga de eventos de seguridad» con la cuenta de Braze y los ID externos de Braze rellenados.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. En la consola de AWS, ve a la sección **IAM** (Gestión de identidades y accesos) > **Roles** > **Crear rol**. 
5. Selecciona **Otra cuenta de AWS** como tipo de SELECTOR de entidad de confianza. 
6. Proporciona tu ID de cuenta de Braze, marca la casilla **«Requerir ID externo**» y, a continuación, introduce tu ID externo de Braze. 
7. Seleccione **Siguiente** cuando haya terminado.

![Una página con opciones para seleccionar un tipo de entidad de confianza y proporcionar información sobre tu cuenta de AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Paso 3: Adjuntar política

1. Busca la política que creaste anteriormente en la barra de búsqueda y, a continuación, marca la casilla situada junto a la política para adjuntarla. 
2. Seleccione **Siguiente**.

![Una lista de políticas con columnas para su tipo y descripción.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Asigna un nombre y una descripción al rol y selecciona **Crear rol**.

![Campos para proporcionar detalles sobre la función, como el nombre, la descripción, la política de confianza, los permisos y las etiquetas.]({% image_buster /assets/img/security_export/name_review_create.png %})

¡Tu nuevo rol aparecerá en la lista!

### Paso 4: Enlace a Braze AWS

1. En la consola de AWS, busca en la lista el rol que acabas de crear. Selecciona el nombre para abrir los detalles de esa función y toma una nota del **ARN**.

![Página de resumen de una función denominada «security-event-export-olaf».]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración administrativa** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**.

![Sección «Descarga de eventos de seguridad» con la opción «Exportar a AWS S3» alternada.]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Asegúrate de que **la ARN de la función de AWS** esté seleccionada y, a continuación, introduce la ARN de tu función y el nombre del contenedor de S3 de AWS en los campos correspondientes.
4\. Selecciona **«Probar credenciales»** para confirmar que tus credenciales funcionan correctamente.
5\. Selecciona **Guardar cambios**. 

![Botón «Guardar cambios».]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

¡Has realizado la integración de AWS S3 en tu cuenta de Braze!