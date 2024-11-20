---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Este artículo de referencia describe la asociación entre Braze y Fivetran, una herramienta de automatización del flujo de trabajo que puede ayudarle en la toma de decisiones basada en datos mediante la entrega de datos listos para consultar en su almacén en la nube."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) es una marca mundialmente reconocida cuyos productos centrados en el analista y pipelines totalmente gestionados permiten tomar decisiones basadas en datos mediante la entrega de datos listos para consultar en su almacén en la nube.

La integración de Braze y Fivetran permite a los usuarios crear una canalización sin mantenimiento que permite recopilar y analizar datos de Braze conectando todas sus aplicaciones y bases de datos a un almacén central. Una vez recopilados los datos en el almacén central, los equipos de datos pueden explorar los datos de Braze con eficacia utilizando sus herramientas de inteligencia empresarial preferidas. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Fivetran | Se necesita una cuenta [Fivetran](https://fivetran.com/login?next=%2Fdashboard) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave Braze REST API con los siguientes permisos:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia][1]. |
| Braze Currents | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) debe estar conectado a Amazon S3 o Google Cloud Storage. |
| Amazon S3 o Google Cloud Storage | Esta integración requiere que tengas acceso a un Amazon S3 o Google Cloud Storage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integración

La siguiente integración de Currents es compatible tanto con [Amazon S3](#setting-up-braze-currents-for-s3) como con [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage).

### Configuración de Braze Currents para S3

#### Paso 1: Localice su ID externo {#step-one}

En el [panel de control de Fivetran](https://fivetran.com/dashboard), haz clic en **\+ Conector** y selecciona el conector **Braze** para iniciar el formulario de configuración. A continuación, seleccione **Amazon S3**. Toma nota del ID externo proporcionado aquí; lo necesitarás para permitir que Fivetran acceda a tu contenedor de S3. 

![El Fivetran configura la forma del conector Braze. El campo ID externo necesario para este paso se encuentra en el centro de la página en un recuadro gris claro.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Paso 2: Dar acceso a Fivetran a un contenedor de S3 especificado

##### Creación de una política IAM

Abre [la consola de Amazon IAM](https://console.aws.amazon.com/iam/home#home) y ve a **Políticas > Crear política**.

![]({% image_buster /assets/img/fivetran_as3_iam.png %})

A continuación, haga clic en la pestaña **JSON** y pegue la siguiente política. Asegúrate de sustituir `{your-bucket-name}` por el nombre de tu contenedor de S3.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Por último, haga clic en **Revisar política** y asigne a la política un nombre y una descripción exclusivos. Haga clic en **Crear política** para crear su política. 

![]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Crear un rol IAM {#step-two}

En AWS, vaya a **Roles** y seleccione **Crear nuevo rol**.

![]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Seleccione **Otra cuenta de AWS** e indique el ID de la cuenta de Fivetran `834469178297`. Asegúrese de marcar la casilla **Requerir ID externo**. Aquí, usted proporcionará el ID externo encontrado en el paso 1.

![]({% image_buster /assets/img/fivetran_another_aws_account.png %})

A continuación, haz clic en **Siguiente: Permisos** para seleccionar la política que acaba de crear.

![]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Haga clic en **Siguiente: Revisa**, asigna un nombre a tu nuevo rol (como Fivetran) y haz clic en **Crear rol**. Una vez creada la función, haga clic en ella y anote el ARN de la función que se muestra.

![El ARN de Amazon S3 listado en el rol.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Puedes especificar permisos para el ARN de rol que designes para Fivetran. Dar permisos selectivos a esta función permitirá a Fivetran sincronizar sólo lo que tiene permiso para ver.
{% endalert %}

#### Paso 3: Completar el conector Fivetran

En Fivetran, haz clic en **\+ Conector** y selecciona el conector **Braze** para iniciar el formulario de configuración. En el formulario, rellene los campos indicados con los valores adecuados:
- `Destination schema`: Un nombre de esquema único.
- `API URL`: Tu punto final de la API REST Braze.
- `API Key`: Tu clave de API REST Braze. 
- `External ID`: El ID externo establecido en [el paso 2](#step-two) de las instrucciones de configuración de Currents. Este ID es un valor fijo.
- `Bucket`: Se encuentra en tu cuenta Braze navegando a **Integración > Currents > [Tu nombre actual] > Nombre de contenedor.**
- `Role ARN`: El ARN del rol se encuentra en [el paso 1](#step-one) de las instrucciones de Configuración actual.

{% alert important %}
Asegúrese de que **Amazon S3** está seleccionado como **almacenamiento en la nube**.
{% endalert %}

Por último, haz clic en **Guardar y probar**, y Fivetran hará el resto sincronizándose con los datos de tu cuenta Braze.

### Configuración de Braze Currents para Google Cloud Storage

#### Paso 1: Recupera tu correo electrónico de Fivetran de Google Cloud Storage {#step-one2}

En el [panel de control de Fivetran](https://fivetran.com/dashboard), haz clic en **\+ Conector** y selecciona el conector **Braze** para iniciar el formulario de configuración. A continuación, selecciona **Google Cloud Storage**. Anote la dirección de correo electrónico que aparece.

![El Fivetran configura la forma del conector Braze. El campo de correo electrónico necesario para este paso se encuentra en el centro de la página, en un recuadro gris claro.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Paso 2: Conceder acceso al contenedor

Accede a [Google Storage Console](https://console.cloud.google.com/storage/browser), selecciona el bucket con el que has configurado Braze Currents y haz clic en **Editar permisos de bucket**.

![Los buckets disponibles en Google Storage Console. Localice un cubo y haga clic en el símbolo vertical de tres puntos para abrir el menú desplegable que le permite editar los permisos del cubo.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

A continuación, conceda acceso a `Storage Object Viewer` al correo electrónico del [paso 1](#step-one2) añadiéndolo como miembro. Anota el nombre de contenedor; lo necesitarás en el siguiente paso para configurar Fivetran.

![]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Paso 3: Completar el conector Fivetran

En Fivetran, haz clic en **\+ Conector** y selecciona el conector **Braze** para iniciar el formulario de configuración. En el formulario, rellene los campos indicados con los valores adecuados:
- `Destination schema`: Un nombre de esquema único.
- `API URL`: Tu punto final de la API REST Braze.
- `API Key`: Tu clave de API REST Braze. 
- `Bucket Name`: Se encuentra en tu cuenta Braze navegando a **Integración > Currents > [Tu nombre actual] > Nombre de contenedor.**
- `Folder`: Se encuentra en su cuenta Braze navegando a **Integración > Corrientes > [Su nombre actual] > Prefijo**.

{% alert important %}
Asegúrese de que **Google Cloud Storage** está seleccionado como opción de **almacenamiento en la nube**.
{% endalert %}

Por último, haz clic en **Guardar y probar**, y Fivetran hará el resto sincronizándose con los datos de tu cuenta Braze.

[1]: {{site.baseurl}}/api/basics/#api-definitions