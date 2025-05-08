---
nav_title: Lexer
article_title: Lexer
description: "Este artículo de referencia describe la asociación entre Braze y Lexer, una plataforma de datos de clientes que pone los datos de los clientes en manos de los profesionales del marketing para inspirar experiencias que impulsen las ventas."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer][6], una plataforma de datos de clientes creada para el comercio minorista, ayuda a las marcas a incrementar sus ventas mediante la mejora de la experiencia del cliente, combinando un sólido enriquecimiento de datos con las herramientas más intuitivas y el asesoramiento de expertos.

La integración de Braze y Lexer permite sincronizar datos entre las dos plataformas. Utilice sus datos de Lexer para crear valiosos segmentos Braze o importe los existentes a Lexer para desbloquear información. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de socio | Se necesita una cuenta Lexer para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con todos los permisos de `user` (excepto `user.delete`) y `segment.list`. El conjunto de permisos puede cambiar a medida que Lexer añada compatibilidad con más objetos Braze, por lo que es posible que desee conceder más permisos ahora o planificar la actualización de estos permisos en el futuro.<br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | La [URL de tu punto final REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Contenedor y credenciales de Amazon AWS S3 | Antes de comenzar la integración, debes tener credenciales de acceso para un contenedor de AWS S3 conectado a tu centro Lexer (puede ser un contenedor creado por ti o uno que Lexer cree y gestione por ti). Visite [Lexer](https://learn.lexer.io/docs/amazon-s3) para obtener orientación sobre este requisito. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

En Lexer, vaya a **Gestionar > Integración**, seleccione el mosaico **Braze** y haga clic en **Integrar Braze**. Facilite la siguiente información:
- **Punto final REST Braze**
- **Clave REST API de Braze**
- **Credenciales de AWS**
  - **Nombre de contenedor de AWS S3**
  - **AWS S3 [región del contenedor][4]**
  - **Ruta del contenedor de AWS S3**: Esta ruta debe coincidir con la que especificó al [conectar su bucket de S3 a Braze][5]. Debe estar en blanco si no ha especificado nada a Braze.
  - **Clave secreta de acceso a AWS S3**: Visite Amazon para obtener información sobre [la creación de una clave de acceso][3].
- **ID de segmento de exportación de Braze**: El ID del segmento que ha creado en Braze que contiene todos los usuarios que desea exportar a Lexer. Si hay usuarios que no desea exportar a Lexer, puede excluirlos del segmento que creó en Braze. Para encontrar su identificador de segmento, haga clic en el segmento deseado en Braze y localice el **Identificador API de segmento**.

![][1]

### Elección de una opción de AWS S3 (gestionada por Lexer o autogestionada)
Utilizar un contenedor administrado por Lexer es la forma preferida de conectar Braze a tu concentrador Lexer y reducirá la cantidad de configuraciones necesarias. Lexer le proporcionará los detalles puntuales que necesitará para configurar Braze.

Si ya has conectado un contenedor de S3 a Braze y lo estás utilizando para otros fines, tendrás que proporcionar a Lexer acceso a este contenedor autogestionado siguiendo los pasos anteriores.

Esta integración funciona proporcionando a Lexer su token y secretos de API existentes, lo que permite a Lexer realizar estas exportaciones en su nombre. También importa tus datos de Braze a Lexer utilizando estas credenciales y tu configuración de S3 para sincronizar tus datos en ambas plataformas automáticamente.

## Envío de segmentos a Braze

### Paso 1: Crear activación

Lexer Activate actualizará automáticamente sus perfiles Braze, añadiendo o eliminando atributos a medida que los clientes entren y salgan de su segmento.

1. En Lexer, en **Activaciones Lexer**, haga clic en **ACTIVAR NUEVA AUDIENCIA**.
2. Seleccione la activación Braze adecuada para esta campaña.
3. Añade tu segmento.
4. Actualice el nombre de su audiencia; éste se convertirá en el valor de su atributo en Braze.
5. Este es el atributo personalizado que actualizaremos en Braze. Póngase en contacto con [el servicio de asistencia de Lexer](support@lexer.io) para actualizarlo.
6. Marque la acción apropiada de la lista-en la mayoría de los casos, querrá mantener su lista.
7. Revise los términos y condiciones, y haga clic en **ENVIAR AUDIENCIA**.

![][7]

### Paso 2: Verificar la activación

Una vez que se haya confirmado el envío de su activación en Activar, verá que los registros comienzan a actualizarse en Braze. Sus perfiles no se actualizarán completamente en Braze hasta después de recibir un correo electrónico de confirmación de Lexer.

### Paso 3: Cree su segmento Braze

En Braze, verá que el nombre de su audiencia en Lexer es ahora un valor en su atributo personalizado `lexer_audience`. Braze tiene un límite de 100 valores por atributo.

Para crear su segmento, vaya a **Segmento > + Crear segmento** y seleccione **Atributo personalizado** como filtro. A continuación, selecciona `lexer_audience` como atributo y el nombre de la audiencia Lexer que desees. Cuando hayas terminado, **guarda** tu audiencia.

Ahora puede añadir este segmento recién creado a futuras campañas y lienzos Braze para dirigirse a estos usuarios finales.

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}
