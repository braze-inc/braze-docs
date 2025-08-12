---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre la sincronización de audiencias
description: "Este artículo ofrece respuestas a las preguntas más frecuentes sobre la Sincronización de audiencias."
page_order: 80
Tool:
  - Canvas

---

# Preguntas más frecuentes

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre la Sincronización de audiencias.

### ¿Cuánto tardan mis audiencias en aparecer en mi panel de socios de Audience Sync?

El tiempo que se tarda en poblar una audiencia depende del socio concreto. Todas las redes procesarán las solicitudes de Braze e intentarán emparejar a los usuarios. Este proceso suele durar entre 6 y 48 horas.

Puedes consultar el intervalo de tiempo específico en la sección Solución de problemas de la documentación de cada socio de Audience Sync.

### ¿Qué tipo de datos propios puedo utilizar en mi Audience Sync?

Los campos específicos utilizados para cada socio pueden variar en función de los requisitos del socio. 

Por ejemplo, cuando configure una Sincronización de Audiencia con Facebook, podrá utilizar una amplia variedad de campos de origen como correo electrónico, teléfono, nombre y apellidos, mientras que, con Snapchat, sólo podrá seleccionar correo electrónico, teléfono o ID de anunciante móvil. 

Es importante tener en cuenta que los campos de usuario que puede seleccionar para sincronizar se correlacionan con los atributos estándar de Braze y los ID de publicidad móvil. Debe asegurarse de que transmite adecuadamente estos datos a través de nuestros SDK o API. 

### ¿Qué ocurre cuando se procesan mis datos para enviarlos a cada socio de Audience Sync?

Los datos que selecciones para enviar a tu destino de Sincronización de Audiencias estarán normalizados. Cada socio puede tener especificaciones diferentes para la normalización de datos en función de los requisitos de su API, así que revisa el punto final específico de cada socio para obtener más detalles.

Además, Braze aplicará hash a todos los datos antes de sincronizar a los usuarios con nuestros socios de Audience Sync, garantizando que toda la información de identificación personal se somete a hash SHA256.

### ¿Por qué puedo seleccionar varios identificadores en un paso para algunos socios, pero sólo puedo seleccionar un identificador para otros?

Esto lo determinan los métodos de integración del socio, y no lo controla Braze. Algunos socios (como Meta) permiten sincronizar varios identificadores, y otros socios (como Google) sólo permiten sincronizar un único identificador con un usuario en un momento dado.

### ¿Cómo vuelvo a conectar mi integración?

Si el usuario anterior que conectó la integración ya no está en tu empresa, tendrás que actualizar la integración con el nuevo usuario. Puedes hacerlo seleccionando **Confirmar**. Ten en cuenta que esto puede interrumpir los Lienzos activos.

El usuario que se vuelva a conectar debe tener acceso de lectura y escritura a todas las audiencias para que los usuarios puedan sincronizarse correctamente con los socios. Comprueba que el usuario que está reconectando la integración tiene acceso a las mismas cuentas de anuncios y audiencias. No debería ser necesario editar ningún paso en Canvas existente. 

### ¿Cuáles son los errores más comunes que pueden producirse al crear y gestionar mis Audience Syncs?

- **Token no válido**<br>
  - Las causas típicas incluyen si ha cambiado su contraseña para iniciar sesión en una red publicitaria específica o si sus credenciales caducan.
  - Para resolver este problema, sólo tienes que entrar en la página del socio en cuestión para desconectar y volver a conectar tu cuenta.
- **Tamaño de la audiencia demasiado bajo**<br>
  - Este error suele producirse si ha creado un paso de Sincronización de audiencias que elimina usuarios de sus audiencias. Si el tamaño de tu audiencia se acerca a cero, la red puede marcar que el tamaño de la audiencia es demasiado bajo para servir. 
  - Para resolver este problema, asegúrese de que está considerando una estrategia de Sincronización de Audiencias que añada y elimine usuarios con regularidad y que no agote por completo el tamaño de la audiencia.
- **La audiencia no existe**<br>
  - Este error se produce porque el paso Sincronización de público utiliza un público que no existe. Esto también puede activarse si no tienes el permiso necesario para acceder a la audiencia. 
  - Para resolver este problema, añade una audiencia activa dentro de tu configuración de Sincronización de Audiencias o crea una nueva audiencia.
- **Intento de acceso a la cuenta publicitaria**<br>
  - Este error se produce si no tiene permisos para la cuenta publicitaria y/o el público que ha seleccionado.
  - Para resolver este problema, trabaje con los administradores de su cuenta publicitaria para obtener el acceso y los permisos adecuados. 
- **Configuración no válida**<br>
  - Este error se activará si no ha configurado un destino específico de Audience Sync en Canvas, incluidos los campos de cuenta de anuncios, público o usuario con los que debe coincidir. 
  - Para resolver este problema, completa la configuración de cada socio antes de lanzarlo.
- **Las condiciones de servicio**<br>
  - Para algunos destinos de Sincronización de Audiencias, como Facebook, la red publicitaria exige aceptar unas condiciones de servicio específicas para utilizar la característica de Sincronización de Audiencias. Este error se producirá si no ha aceptado las condiciones correspondientes. 
  - Para resolver este problema, asegúrese de haber aceptado las condiciones exigidas por cada socio. Para Facebook en concreto, revisa [la solución de problemas de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). 
