---
nav_title: Exportación de eventos de seguridad con S3
article_title: Exportación de configuraciones de seguridad con S3
page_order: 1
page_type: reference
description: "Este artículo de referencia explica cómo exportar automáticamente los eventos de seguridad todos los días a medianoche UTC a Amazon S3."
---

# Exportación de eventos de seguridad con Amazon S3

> Puedes exportar automáticamente los eventos de seguridad a Amazon S3, un proveedor de almacenamiento en la nube, con una tarea diaria que se ejecuta a medianoche UTC. Tras la configuración, no tendrás que exportar manualmente los eventos de seguridad desde el panel. La tarea exportará los eventos de seguridad de las últimas 24 horas en formato CSV a tu almacenamiento S3 configurado. El archivo CSV tendrá la misma estructura que un informe exportado manualmente.

Braze admite dos métodos diferentes de autenticación y autorización de S3 para configurar la exportación a Amazon S3:

- Método de clave de acceso secreta de AWS
- Método ARN del rol de AWS

## Método de clave de acceso secreta de AWS

Este método genera una clave secreta y un ID de clave de acceso que permite a Braze autenticarse como usuario en tu cuenta de AWS para escribir datos en tu contenedor.

### Paso 1: Crear un usuario de mensajes dentro de la aplicación

Para recuperar tu clave de acceso secreta y tu ID de clave de acceso, tendrás que crear un usuario de mensajes dentro de la aplicación, siguiendo las instrucciones de [Configuración de tu cuenta de AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-account-iam.html#create-an-admin).

### Paso 2: Obtener credenciales

1. Tras crear un nuevo usuario, genera la clave de acceso y descarga tu ID de clave de acceso y tu clave de acceso secreta.

Página de resumen de un papel llamado "liyu-chen-test".]({% image_buster /assets/img/security_export/credentials1.png %})

{: start="2"}
2\. Toma nota de estas credenciales en algún sitio o descarga los archivos de credenciales, porque tendrás que introducirlas en Braze más adelante.

\![Campos que contienen la clave de acceso y la clave de acceso secreta.]({% image_buster /assets/img/security_export/retrieve_access_keys.png %})

### Paso 3: Crear política

1. Ve a **IAM** > **Políticas** > **Crear política** para añadir permisos para tu usuario. 
2. Selecciona **Crear tu propia política**, que otorga permisos limitados para que Braze sólo pueda acceder a los contenedores especificados.
3. Especifica un nombre de póliza de tu elección.
4. Introduce el siguiente fragmento de código en la sección **Documento de Política**. Asegúrate de sustituir "INSERTBUCKETNAME" por el nombre de tu contenedor. Sin estos permisos, la integración no superará la comprobación de credenciales y no se creará.

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

1. Tras crear una nueva política, ve a **Usuarios** y selecciona tu usuario concreto. 
2. En la pestaña **Permisos**, selecciona **Añadir permisos**, adjunta directamente la política y, a continuación, selecciona dicha política. 

Ahora, ¡ya estás listo para vincular tus credenciales de AWS a tu cuenta de Braze!

### Paso 5: Vincular Braze a AWS

1. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**.
2. Alterna la opción **Exportar a AWS S3** en **Exportar a almacenamiento en la nube** y selecciona la **clave de acceso secreta de AWS**, que habilita la exportación a S3. 
3. Introduce lo siguiente:
- ID de la clave de acceso de AWS
- Clave de acceso secreta de AWS
    - Cuando introduzcas esta clave, selecciona primero **Probar credenciales** para confirmar que tus credenciales funcionan.
- Nombre de contenedor AWS 

\![La página "Descarga de eventos de seguridad" con la cuenta Braze y los ID externos Braze rellenados.]({% image_buster /assets/img/security_export/security_event_download1.png %})

{: start="4"}
4\. Selecciona **Guardar cambios**. 

\!["Guardar cambios" botón.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:50%;"}

¡Has integrado AWS S3 en tu cuenta Braze!

## Método ARN del rol de AWS

El método ARN de rol de AWS genera un Nombre de Recurso de Amazon (ARN) de rol que permite a la cuenta de Amazon Braze autenticarse como miembro de ese rol.

### Paso 1: Crear política

1. Inicia sesión en la consola de administración de AWS como administrador de cuentas. 
2. En la consola de AWS, ve a la sección **IAM** > **Políticas** y, a continuación, selecciona **Crear política**.

Una página con una lista de políticas y un botón para "Crear política".]({% image_buster /assets/img/security_export/policies.png %})

{: start="3"}
3\. Abre la pestaña **JSON** e introduce el siguiente fragmento de código en la sección **Documento de política**. Asegúrate de sustituir `INSERTBUCKETNAME` por el nombre de tu contenedor. 

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

Página que te permite revisar tu política y, opcionalmente, añadir permisos.]({% image_buster /assets/img/security_export/specify_permissions.png %})

{: start="5"}
5\. Dale un nombre y una descripción a la política y, a continuación, selecciona **Crear política**.

Una página para revisar y crear tu política.]({% image_buster /assets/img/security_export/review_and_create.png %})

### Paso 2: Crear rol

1. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**. 
2. Selecciona **AWS Role ARN**. 
3. Toma nota de los identificadores, el ID de cuenta Braze y el ID externo Braze necesarios para crear tu rol.

\![La página "Descarga de eventos de seguridad" con la cuenta Braze y los ID externos Braze rellenados.]({% image_buster /assets/img/security_export/security_event_download2.png %})

4. En la consola de AWS, ve a la sección **IAM** > **Roles** > **Crear rol**. 
5. Selecciona **Otra cuenta de AWS** como tipo de selector de entidad de confianza. 
6. Proporciona tu ID de cuenta Braze, marca la casilla **Requerir ID externo** y, a continuación, introduce tu ID externo Braze. 
7. Selecciona **Siguiente** cuando hayas terminado.

\![Una página con opciones para seleccionar un tipo de entidad de confianza y proporcionar información sobre tu cuenta de AWS.]({% image_buster /assets/img/security_export/select_trusted_entity.png %})

### Paso 3: Adjuntar política

1. Busca la política que creaste anteriormente en la barra de búsqueda y, a continuación, coloca una marca de verificación junto a la política para adjuntarla. 
2. Selecciona **Siguiente**.

\![Una lista de políticas con columnas para su tipo y descripción.]({% image_buster /assets/img/security_export/add_permissions.png %})

{: start="3"}
3\. Dale al rol un nombre y una descripción, y selecciona **Crear rol**.

\![Campos para proporcionar detalles del rol, como el nombre, la descripción, la política de confianza, los permisos y las etiquetas.]({% image_buster /assets/img/security_export/name_review_create.png %})

¡Tu rol recién creado aparecerá en la lista!

### Paso 4: Enlace a Braze AWS

1. En la consola de AWS, busca en la lista el rol que acabas de crear. Selecciona el nombre para abrir los detalles de ese rol, y toma nota del **ARN**.

\![La página de resumen de un rol llamado "security-event-export-olaf".]({% image_buster /assets/img/security_export/credentials2.png %})

{: start="2"}
2\. En Braze, ve a **Configuración** > **Configuración de la empresa** > **Configuración de administrador** > **Configuración de seguridad** y desplázate hasta la sección **Descarga de eventos de seguridad**.

\!["Descarga de eventos de seguridad" sección con un alternador activado para "Exportar a AWS S3".]({% image_buster /assets/img/security_export/security_event_download3.png %})

{: start="3"}
3\. Asegúrate de que **el ARN del rol de AWS** está seleccionado, e introduce el ARN de tu rol y el nombre de contenedor de AWS S3 en los campos designados.
4\. Selecciona **Probar credenciales** para confirmar que tus credenciales funcionan correctamente.
5\. Selecciona **Guardar cambios**. 

\!["Guardar cambios" botón.]({% image_buster /assets/img/security_export/save_changes_button.png %}){: style="max-width:40%;"}

¡Has integrado AWS S3 en tu cuenta Braze!