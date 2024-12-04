### Conservación automática del historial de usuarios anónimos

| Contexto de identificación | Comportamiento de conservación |
| ---------------------- | -------------------------- |
| El usuario **no ha** sido identificado previamente | El historial anónimo **se fusiona** con el perfil de usuario en el momento de la identificación. |
| El usuario **ha sido** previamente identificado en la aplicación o a través de la API | El historial anónimo **no se fusiona** con el perfil de usuario al identificarse. |
{: .reset-td-br-1 .reset-td-br-2}

Consulta [Perfiles de usuario identificados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) para obtener más información sobre lo que ocurre cuando identificas a usuarios anónimos.

### Notas adicionales y buenas prácticas

Toma nota de lo siguiente:

- Si tu aplicación la utilizan varias personas, puedes asignar a cada usuario un identificador único para su seguimiento.
- Una vez configurado un ID de usuario, no puedes revertir ese usuario a un perfil anónimo.
- No cambies el ID de usuario cuando un usuario cierre la sesión, ya que esto puede separar el dispositivo del perfil de usuario.
  - Como resultado, no podrás dirigirte al usuario que se desconectó previamente con mensajes de reactivación de la interacción. Si prevés varios usuarios en el mismo dispositivo, pero sólo quieres dirigirte a uno de ellos cuando tu aplicación esté desconectada, te recomendamos que hagas un seguimiento por separado del ID de usuario al que quieres dirigirte mientras está desconectado y que vuelvas a cambiar a ese ID de usuario como parte del proceso de cierre de sesión de tu aplicación. Por predeterminado, sólo el último usuario que haya iniciado sesión recibirá notificaciones push de tu aplicación.
- Pasar de un usuario identificado a otro es una operación relativamente costosa.
  - Cuando solicitas el cambio de usuario, la sesión actual del usuario anterior se cierra automáticamente y se inicia una nueva sesión. Braze realizará automáticamente una solicitud de actualización de datos para los mensajes dentro de la aplicación y otros recursos de Braze para el nuevo usuario.

{% alert tip %}
Si optas por utilizar un hash de un identificador único como ID de usuario, asegúrate de que normalizas la entrada a tu función hash. Por ejemplo, si vas a utilizar un hash de una dirección de correo electrónico, confirma que estás eliminando los espacios en blanco iniciales y finales de la entrada, y teniendo en cuenta la localización.
{% endalert %}