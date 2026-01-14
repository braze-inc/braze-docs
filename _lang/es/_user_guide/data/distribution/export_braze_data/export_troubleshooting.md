---
nav_title: Solución de problemas de exportación
article_title: Solución de problemas de exportación
page_order: 10
page_type: reference
description: "Este artículo de referencia cubre algunos escenarios comunes de solución de problemas para las exportaciones API y CSV."

---

# Solución de problemas de exportación

> Esta página enumera los mensajes de error que puedes encontrar al exportar datos a través de CSV o API desde Braze.

## Errores comunes

### Acceso denegado 

#### Si utilizas tu propio contenedor de S3

Si estás utilizando **tu propio contenedor de S3**, esto podría ocurrir porque:

- El objeto esperado ya no está en el contenedor de S3; compruébalo con tus ingenieros.
- Las credenciales de S3 configuradas en el panel de Braze no tienen los permisos correctos; confirma las credenciales adecuadas con tu equipo.

#### Al utilizar un contenedor de S3 Braze

Si estás utilizando un **contenedor de S3 Braze**, esto puede ocurrir porque

- El objeto ya no está ahí. Esto puede ocurrir si has hecho clic en un enlace para una exportación que ha caducado, ya que los archivos se eliminan automáticamente de S3 cuando caduca el enlace de descarga. Salvo que se indique lo contrario, los archivos se eliminan al cabo de cuatro horas. Si es así, vuelve a ejecutar la exportación.
- Seleccionaste el enlace de descarga enseguida, antes de que el S3 estuviera preparado para servir el objeto. Espera unos minutos y vuelve a intentarlo. Los informes de mayor tamaño suelen tardar más. 
- La exportación es demasiado grande, por lo que nuestro servidor se quedó sin memoria al intentar crear este archivo zip. Si esto ocurre, enviaremos automáticamente un correo electrónico al usuario que intenta exportar. Si te encuentras constantemente con este problema, te recomendamos que utilices tus propios contenedores de S3 en el futuro.

### ExpiredToken

Esto ocurre si el correo electrónico se envió hace tanto tiempo que el archivo S3 ha caducado. Salvo que se indique lo contrario, los archivos se eliminan al cabo de cuatro horas. Vuelve a ejecutar la exportación y descárgala antes de que caduque el archivo.

Esto también podría deberse a que Braze ya no tiene acceso al contenedor de S3 en el que estás descargando los datos. Asegúrate de haber actualizado tus credenciales de S3 siguiendo estos pasos.

### "Parece que el archivo ya no existe, por favor comprueba que nada está borrando objetos de tu contenedor"

Puede haber un ligero desfase entre el momento en que se envía el correo electrónico de Braze con la exportación y el momento en que S3 está realmente preparado para servir el objeto. Si aparece este error, espera unos minutos antes de volver a intentarlo.

### Apóstrofes añadidos a los campos

Braze antepondrá automáticamente un apóstrofo a un campo de la exportación CSV si el campo empieza por cualquiera de los siguientes caracteres:

- -
- =
- +
- @

Por ejemplo, el campo "-1943" se exportará como "'-1943". Esto no se aplica a las exportaciones JSON, como las devueltas por el [punto final`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).