---
nav_title: Configuración inicial del SDK con Eclipse
page_order: 1

page_type: update
description: "Este artículo archivado describe cómo realizar una configuración inicial del SDK con Eclipse. Braze ha dejado de ser compatible con el IDE Eclipse."
---

# Configuración inicial del SDK con Eclipse

{% alert update %}
Braze ha eliminado la compatibilidad con el IDE de Eclipse debido a que [Google ha anulado la compatibilidad con el complemento de herramientas para desarrolladores de Android de Eclipse](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Si necesitas ayuda con la integración de Eclipse antes de la migración [, envía un correo electrónico al equipo de soporte para recibir asistencia]({{site.baseurl}}/support_contact/).
{% endalert %}

## Paso 1
En tu línea de comandos, clona el [repositorio GitHub de Braze Android](https://github.com/braze-inc/braze-android-sdk).

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Paso 2
Importa el proyecto Braze a tu espacio de trabajo local

En Eclipse:

  - Ve a Archivo > Importar.

    ![Importación de archivos]({{site.baseurl}}/assets/img_archive/file_import.png)
  - Selecciona Android > Código Android existente en el espacio de trabajo.

    ![Importación de Android]({{site.baseurl}}/assets/img_archive/android_import.png)
  - Haz clic en "Examinar".

    ![Examinar]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Marca la carpeta del proyecto Braze UI, así como "copiar proyecto en espacio de trabajo" y haz clic en "Finalizar".

    ![Selecciona el proyecto de interfaz de usuario de Android]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## Paso 3
Haz referencia a Braze en tu propio proyecto.
En Eclipse:

  - Haz clic con el botón derecho en tu proyecto y selecciona "Propiedades".

    ![Haz clic en Propiedades]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - En "Android", haz clic en "Añadir..." en la sección Biblioteca y añade android-sdk-ui como biblioteca a tu aplicación.

    ![Braze Añadir]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## Paso 4
Resuelve los errores de dependencia y corrige el objetivo de compilación.

En este momento, es posible que aparezcan errores con el código Braze, esto se debe a que sus dependencias no están rellenadas y a que el objetivo de compilación es posiblemente incorrecto:

   - Haz clic con el botón derecho del ratón en el proyecto Braze UI y selecciona Propiedades->Android para asegurarte de que el objetivo de compilación está establecido en la versión actual de las herramientas de compilación de Braze.

      ![Versión objetivo]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Haz clic con el botón derecho del ratón en el proyecto Braze UI y selecciona Propiedades->Ruta de compilación de Java->Añadir JARs... y añade 'android-support-v4.jar' de la aplicación principal como biblioteca.

      ![Soporte]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## Paso 5

Añade las piezas finales.

  - Para la versión 1.10.0 o superior del SDK, tendrás que añadir
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  a tu AndroidManifest.xml, ya que Eclipse no admite la fusión de manifiestos.

  - Para la versión 1.7.0 o superior del SDK, tendrás que copiar "assets/fontawesome-webfont.ttf" de nuestro proyecto de biblioteca a tu aplicación. Eclipse no incluye automáticamente la carpeta de activos de las bibliotecas.

