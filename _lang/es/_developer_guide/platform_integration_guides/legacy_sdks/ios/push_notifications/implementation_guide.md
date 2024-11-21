---
nav_title: Aplicación avanzada (Opcional)
article_title: Implementación avanzada de notificaciones push para iOS (Opcional)
platform: iOS
page_order: 28
description: "Esta guía de implementación avanzada explica cómo aprovechar las extensiones de la aplicación de contenido de notificaciones push de iOS para sacar el máximo partido a tus mensajes push. También se incluyen tres casos de uso creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el análisis de registros."
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
¿Buscas la guía básica de integración para desarrolladores de notificaciones push? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).
{% endalert %}

# Guía de implementación de notificaciones push

> Esta guía de implementación opcional y avanzada cubre formas de aprovechar las extensiones de la aplicación de contenido de notificaciones push para sacar el máximo partido a tus mensajes push. Se incluyen tres casos de uso personalizados creados por nuestro equipo, fragmentos de código que los acompañan y orientaciones sobre el análisis de registros. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.

## Extensiones de la aplicación de contenido de notificación

![Dos mensajes push mostrados uno al lado del otro. El mensaje de la derecha muestra el aspecto de un push con la interfaz predeterminada. El mensaje de la derecha muestra un push de una tarjeta perforada de café realizado mediante la implementación de una interfaz de usuario push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Las notificaciones push, aunque parecen estándar en diferentes plataformas, ofrecen inmensas opciones de personalización más allá de lo que normalmente se implementa en la interfaz de usuario predeterminada. Cuando se amplía una notificación push, las extensiones de notificación de contenido habilitan una vista personalizada de la notificación push ampliada. 

Las notificaciones push se pueden ampliar de tres formas distintas: <br>\- Una pulsación larga en el banner push<br>\- Deslizar hacia abajo el banner push<br>\- Deslizar el banner hacia la izquierda y seleccionar "Ver" 

Estas vistas personalizadas ofrecen formas inteligentes de interacción con los clientes, permitiéndote mostrar muchos tipos distintos de contenido, como notificaciones interactivas, notificaciones rellenadas con datos de usuario e incluso mensajes push que pueden capturar información como números de teléfono y correo electrónico. Aunque implementar el push de esta forma puede resultar desconocido para algunos, una de nuestras características más conocidas en Braze, [las Historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), son un excelente ejemplo de cómo puede ser una vista personalizada para una extensión de aplicación de contenido de notificaciones.

#### Requisitos
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificaciones push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) integradas con éxito en tu aplicación
- iOS 10 o superior
- Los siguientes archivos generados por Xcode en función de tu lenguaje de codificación:

Swift<br>
- `NotificationViewController.swift`<br>
- `MainInterface.storyboard`<br><br>
Objective-C<br>
- `NotificationViewController.h`<br>
- `NotificationViewController.m`<br>
- `MainInterface.storyboard`

### Configuración personalizada de categorías

Para configurar una vista personalizada en el panel, debes alternar los botones de notificación e introducir tu categoría personalizada. La categoría personalizada de iOS prerregistrada que proporciones se cotejará con la `UNNotificationExtensionCategory` en la página `.plist` de tu objetivo de extensión de contenido de notificaciones. El valor dado aquí debe coincidir con el establecido en el panel Braze.

![Las opciones del botón de notificación que se encuentran en la configuración del creador de mensajes push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

{% alert tip %}
Dado que los push con extensiones de contenido no siempre son evidentes, se recomienda incluir una llamada a la acción para animar a tus usuarios a ampliar sus notificaciones push.
{% endalert %}

## Recorrido de casos de uso e implementación

Hay tres tipos de extensión de aplicación de contenido de notificaciones push. Cada tipo tiene un recorrido conceptual, posibles casos de uso y un vistazo a cómo pueden verse y utilizarse las variables de notificación push en el panel Braze:
- [Notificación push interactiva](#interactive-push-notification)
- [Notificaciones push personalizadas](#personalized-push-notifications)
- [Captura de información de notificaciones push](#information-capture-push-notification)

### Notificación push interactiva

Las notificaciones push pueden responder a acciones del usuario dentro de una extensión de contenido. Para los usuarios que ejecuten iOS 12 o posterior, ¡esto significa que puedes convertir tus mensajes de mensajería push en notificaciones push totalmente interactivas! Esta interactividad ofrece muchas posibilidades para que tus usuarios participen en tus notificaciones. El siguiente ejemplo muestra un push en el que los usuarios pueden jugar a un partido dentro de la notificación expandida.

![Un diagrama de cómo podrían ser las fases de una notificación push interactiva. Las imágenes muestran a un usuario pulsando en una notificación push que muestra un juego de correspondencias interactivo.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

#### Configuración del panel de control

Para configurar una vista personalizada en el panel, dentro de la configuración del botón de notificación introduce la categoría específica que quieres mostrar. A continuación, en la página `.plist` de tu Extensión de contenido de notificaciones, también debes establecer la categoría personalizada en el atributo `UNNotificationExtensionCategory`. El valor dado aquí debe coincidir con el establecido en el panel Braze. Por último, para habilitar las interacciones del usuario en una notificación push, establece la clave `UNNotificationExtensionInteractionEnabled` en verdadero.

![]({% image_buster /assets/img/push_implementation_guide/push3.png %}){: style="float:right;max-width:45%;"}

![Las opciones del botón de notificación que se encuentran en la configuración del creador de mensajes push.]({% image_buster /assets/img/push_implementation_guide/push14.png %}){: style="max-width:50%;"}

#### Otros casos de uso
Las extensiones de contenido push son una opción interesante para introducir interactividad en tus promociones y aplicaciones. Algunos ejemplos son un juego para que jueguen los usuarios, una ruleta para ganar descuentos o un botón "me gusta" para guardar un anuncio o una canción.

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos.

### Notificaciones push personalizadas
![Dos iPhones mostrados uno al lado del otro. El primer iPhone muestra la vista no ampliada del mensaje push. El segundo iPhone muestra la versión ampliada del mensaje push mostrando una imagen de "progreso" de hasta dónde han llegado en el curso, la siguiente sesión y cuándo debe estar lista la ID de la siguiente sesión.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Las notificaciones push pueden mostrar información específica del usuario dentro de una extensión de contenido. El ejemplo de la derecha muestra una notificación push después de que un usuario haya completado una tarea específica (curso de Braze Learning) y ahora se le anima a ampliar esta notificación para comprobar su progreso. La información que se proporciona aquí es específica del usuario y puede dispararse cuando se completa una sesión o se realiza una acción específica del usuario aprovechando un desencadenante de la API. 

#### Configuración del panel de control

Para configurar un push personalizado en el panel, debes registrar la categoría específica que quieres que se muestre y, a continuación, dentro de los pares clave-valor mediante Liquid estándar, establecer los atributos de usuario adecuados que quieres que muestre el mensaje. Estas vistas pueden personalizarse en función de atributos específicos de usuario de un perfil de usuario concreto.

![Cuatro conjuntos de pares clave-valor, en los que "next_session_name" y "next_session_complete_date" se configuran como una propiedad desencadenante de la API mediante Liquid, y "completed_session count" y "total_session_count" se configuran como un atributo personalizado del usuario mediante Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

#### Manejo de pares clave-valor

El siguiente método, `didReceive` se llama cuando la extensión de contenido ha recibido una notificación, se puede encontrar dentro de `NotificationViewController`. Los pares clave-valor proporcionados en el panel se representan en el código mediante el uso de un diccionario `userInfo`.

**Análisis sintáctico de los pares clave-valor de las notificaciones push**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

#### Otros casos de uso

Las ideas para extensiones de contenido push basadas en el progreso y centradas en el usuario son infinitas, algunos ejemplos incluyen añadir la opción de compartir tu progreso en distintas plataformas, expresar los logros desbloqueados, tarjetas perforadas o incluso listas de control de incorporación. 

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos.

### Captura de información de notificaciones push

Las notificaciones push pueden capturar información del usuario dentro de una extensión de contenido, permitiéndote superar los límites de lo que es posible con un push. Examinando el siguiente flujo mostrado, la vista es capaz de responder a los cambios de estado. Esos componentes del cambio de estado están representados en cada imagen. 

1. El usuario recibe una notificación push.
2. Se abre la notificación push y pide información al usuario.
3. Se proporciona información y, si es válida, se muestra el botón de registro.
3. Se muestra la vista de confirmación, y se descarta la notificación push. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

Ten en cuenta que la información solicitada aquí puede ser muy diversa, como la captura de números SMS, no tiene por qué ser específica del correo electrónico.

#### Configuración del panel de control

Para configurar un push capaz de capturar información en el panel, debes registrarte y configurar tu categoría personalizada, y proporcionar los pares clave-valor necesarios. Como se ve en el ejemplo, también puedes incluir una imagen en tu push. Para ello, debes integrar [notificaciones enriquecidas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/rich_notifications/), establecer el estilo de notificación de tu campaña en Notificación enriquecida e incluir una imagen push enriquecida.

![Un mensaje push con tres conjuntos de pares clave-valor. 1\. "Braze_id" establecido como una llamada Liquid para recuperar el ID de Braze. 2\. "cert_title" establecido como "Certificado de especialista en marketing de Braze". 3\. "Cert_description" establecido como "Los especialistas en marketing certificados de Braze conducen...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

#### Manejar las acciones de los botones

Cada botón de acción tiene un identificador único. El código comprueba si tu identificador de respuesta es igual a `actionIndentifier`, y si es así, sabe que el usuario ha hecho clic en el botón de acción.

**Manejar las respuestas del botón de acción para notificación push**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

##### Desestimar las notificaciones push

Las notificaciones push pueden descartarse automáticamente al pulsar un botón de acción. Existen tres opciones preestablecidas de descarte de notificaciones push que se recomiendan:

1. `completion(.dismiss)` - Desestima la notificación
2. `completion(.doNotDismiss)` - La notificación permanece abierta
3. `completion(.dismissAndForward)` - Al pulsar, el usuario es redirigido a la aplicación.

#### Otros casos de uso

Solicitar la opinión del usuario mediante notificaciones push es una oportunidad apasionante que muchas empresas no aprovechan. En estos mensajes push, no sólo puedes solicitar información básica como nombre, correo electrónico o número, sino que también puedes pedir a los usuarios que completen un perfil de usuario si está inacabado, o incluso que envíen sus comentarios. 

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos. 

## Análisis de registros

### Registro con la API de Braze (recomendado)

El análisis de los registros solo puede hacerse en tiempo real con la ayuda del servidor del cliente que accede a nuestro [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para registrar los análisis, envía el valor `braze_id` en el campo de los pares clave-valor (como se ve en la siguiente captura de pantalla) para identificar qué perfil de usuario hay que actualizar.

![Un mensaje push con tres conjuntos de pares clave-valor. 1\. "Braze_id" establecido como una llamada Liquid para recuperar el ID de Braze. 2\. "cert_title" establecido como "Certificado de especialista en marketing de Braze". 3\. "Cert_description" establecido como "Los especialistas en marketing certificados de Braze conducen...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Registrar manualmente

El registro manual requerirá que primero configures los grupos de aplicaciones en Xcode y luego crees, guardes y recuperes los análisis. Esto requerirá algún trabajo personalizado de tu desarrollador. Los siguientes fragmentos de código te ayudarán a solucionarlo. 

También es importante tener en cuenta que los análisis no se envían a Braze hasta que se lanza posteriormente la aplicación móvil. Esto significa que, dependiendo de tu configuración de rechazo, a menudo existe un periodo de tiempo indeterminado entre que se rechaza una notificación push y se lanza la aplicación móvil y se recuperan los análisis. Aunque este búfer de tiempo puede no afectar a todos los casos de uso, los usuarios deben considerar el impacto y, si es necesario, ajustar su recorrido de usuario para incluir la apertura de la aplicación con el fin de solucionar este problema. 

![Un gráfico que describe cómo se procesan los análisis en Braze. 1\. Se crean datos de análisis. 2\. Se guardan los datos de análisis. 3\. Se rechaza la notificación push. 4\. Período de tiempo indeterminado entre que se rechaza la notificación push y se inicia la aplicación móvil. 5\. Se inicia la aplicación móvil. 6\. Se reciben datos de análisis. 7\. Los datos de análisis se envían a Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Paso 1: Configurar grupos de aplicaciones en Xcode
Añade una capacidad `App Groups`. Si no tienes ningún grupo de aplicaciones en tu aplicación, ve a la capacidad del objetivo principal de la aplicación, activa el `App Groups`, y haz clic en el "+". Utiliza el ID del paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu grupo de aplicaciones `group.com.company.appname.xyz`. Asegúrate de que `App Groups` está activado tanto para el destino principal de tu aplicación como para el destino de la extensión de contenido.

![]({% image_buster /assets/img/ios/push_story/add_app_groups.png %})

#### Paso 2: Integrar fragmentos de código
Los siguientes fragmentos de código son una referencia útil sobre cómo guardar y enviar eventos personalizados, atributos personalizados y atributos de usuario. En esta guía se hablará en términos de UserDefaults, pero la representación del código será en forma de archivo de ayuda `RemoteStorage`. También existen archivos de ayuda adicionales `UserAttributes` y `EventName Dictionary` que se utilizan al enviar y guardar atributos de usuario. Todos los archivos de ayuda se encuentran al final de esta guía.

{% tabs local %}
{% tab Eventos personalizados %}

##### Guardar eventos personalizados

Para guardar eventos personalizados debes crear el análisis desde cero. Esto se hace creando un diccionario, rellenándolo con metadatos y guardando los datos mediante el uso de un archivo de ayuda.

1. Inicializar un diccionario con metadatos de eventos
2. Inicializa `userDefaults` para recuperar y almacenar los datos del evento
3. Si hay una matriz existente, añade los nuevos datos a la matriz existente y guarda
4. Si no existe una matriz, guarda la nueva matriz en `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1 
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3 
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envío de eventos personalizados a Braze

Después de inicializar el SDK es el mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificación. Para ello, haz un bucle con los eventos pendientes, busca la tecla "Nombre del evento", configura los valores adecuados en Braze y, a continuación, borra el almacenamiento para la próxima vez que se necesite esta función.

1. Recorre la matriz de eventos pendientes
2. Recorre cada par clave-valor del diccionario `pendingEvents` 
3. Comprobación explícita de la clave "Nombre del evento" para establecer el valor correspondiente
4. Cualquier otra clave-valor se añadirá al diccionario `properties` 
5. Registrar evento personalizado individual 
6. Eliminar todos los eventos pendientes del almacén

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1    
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3      
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4 
        properties[key] = value
      }
    }
  // 5    
    if let eventName = eventName {
      logCustomEvent(eventName, withProperties: properties)
    }
  }

  // 6    
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1 
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
  // 2 
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName != nil) {
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
    }
  }

  // 6  
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atributos personalizados %}

##### Guardar atributos personalizados

Para guardar atributos personalizados debes crear el análisis desde cero. Esto se hace creando un diccionario, rellenándolo con metadatos y guardando los datos mediante el uso de un archivo de ayuda.

1. Inicializar un diccionario con metadatos de atributos
2. Inicializa `userDefaults` para recuperar y almacenar los datos del atributo
3. Si hay una matriz existente, añade los nuevos datos a la matriz existente y guarda
4. Si no existe una matriz, guarda la nueva matriz en `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2 
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4 
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4 
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envío de atributos personalizados a Braze

Después de inicializar el SDK es el mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificación. Esto puede hacerse recorriendo en bucle los atributos pendientes, configurando el atributo personalizado apropiado en Braze y, a continuación, borrando el almacenamiento para la próxima vez que se necesite esta función.

1. Recorre la matriz de atributos pendientes
2. Recorre cada par clave-valor del diccionario `pendingAttributes` 
3. Registra un atributo personalizado individual con la clave y el valor correspondientes
4. Eliminar todos los atributos pendientes del almacén

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4 
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Atributos del usuario %}

##### Guardar atributos de usuario

Al guardar atributos de usuario, se recomienda crear un objeto personalizado para descifrar qué tipo de atributo se está actualizando (`email`, `first_name`, `phone_number`, etc.). El objeto debe ser compatible con ser almacenado/recuperado desde `UserDefaults`. Consulta el archivo de ayuda `UserAttribute` para ver un ejemplo de cómo conseguirlo.

1. Inicializa un objeto `UserAttribute` codificado con el tipo correspondiente
2. Inicializa `userDefaults` para recuperar y almacenar los datos del evento
3. Si hay una matriz existente, añade los nuevos datos a la matriz existente y guarda
4. Si no existe una matriz, guarda la nueva matriz en `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4 
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3 
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4 
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envío de atributos de usuario a Braze

Después de inicializar el SDK es el mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificación. Esto puede hacerse recorriendo en bucle los atributos pendientes, configurando el atributo personalizado apropiado en Braze y, a continuación, borrando el almacenamiento para la próxima vez que se necesite esta función.

1. Recorre la matriz de datos `pendingAttributes`
2. Inicializar un objeto `UserAttribute` codificado a partir de datos de atributos
3. Establecer un campo de usuario específico basado en el tipo de atributo de usuario (correo electrónico)
4. Eliminar todos los atributos de usuario pendientes del almacén

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1    
  for attributeData in pendingAttributes {
  // 2 
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
  // 3    
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4   
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1  
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
  
  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }
    
  // 3  
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Archivos de ayuda %}

##### Archivos de ayuda

{% details Archivo de ayuda RemoteStorage %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Archivo de ayuda UserAttribute %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Archivo de ayuda del diccionario EventName %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)
 
- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;
     
    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}

