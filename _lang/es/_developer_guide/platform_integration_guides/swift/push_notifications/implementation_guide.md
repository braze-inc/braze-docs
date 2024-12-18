---
nav_title: Aplicación avanzada (Opcional)
article_title: Implementación avanzada de notificaciones push para iOS (Opcional)
platform: Swift
page_order: 30
description: "Esta guía de implementación avanzada explica cómo aprovechar las extensiones de aplicación de contenido de notificaciones push de iOS para sacar el máximo partido a tus mensajes push con el SDK de Swift."
channel:
  - push
---

<br>
{% alert important %}
¿Buscas la guía básica de integración para desarrolladores de notificaciones push? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
{% endalert %}

# Guía de implementación avanzada

> Esta guía de implementación opcional y avanzada cubre las formas de aprovechar las extensiones de la aplicación de contenido de notificaciones para sacar el máximo partido a tus mensajes push. 

Esta guía proporciona tres ejemplos de implementación de extensiones de aplicaciones de contenido de notificaciones, cada una con un recorrido conceptual, posibles casos de uso y una visión de cómo pueden verse y utilizarse las variables de notificación push en el panel de Braze:
- [Notificación push interactiva](#interactive-push-notification)
- [Notificaciones push personalizadas](#personalized-push-notifications)
- [Captura de información de notificaciones push](#information-capture-push-notification)

Este artículo también proporciona [orientación sobre los análisis de registro](#logging-analytics) para estas implementaciones personalizadas.

Ten en cuenta que esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados.

## Extensiones de la aplicación de contenido de notificación

![Dos mensajes push mostrados uno al lado del otro. El mensaje de la izquierda muestra el aspecto de un push con la interfaz predeterminada. El mensaje de la derecha muestra un push de una tarjeta perforada de café realizado mediante la implementación de una interfaz de usuario push personalizada.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Las extensiones de la aplicación de contenido de notificaciones te ofrecen una gran opción para personalizar las notificaciones push. Las extensiones de aplicación de contenido de notificación muestran una interfaz personalizada para las notificaciones de tu aplicación cuando se expande una notificación push. 

Las notificaciones push se pueden ampliar de tres formas distintas:
- Una pulsación larga en el banner push
- Deslizar hacia abajo el banner push
- Deslizar el banner hacia la izquierda y seleccionar "Ver" 

Estas vistas personalizadas ofrecen formas inteligentes de interactuar con los clientes mostrando distintos tipos de contenido, como notificaciones interactivas, notificaciones rellenadas con datos de usuario e incluso mensajes push que pueden capturar información como números de teléfono y correo electrónico. Una de nuestras características más conocidas en Braze, [las Historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ¡son un excelente ejemplo de cómo puede ser una extensión de aplicación de contenido de notificación push!

### Requisitos
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notificaciones push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) integradas con éxito en tu aplicación
- Los siguientes archivos generados por Xcode en función de tu lenguaje de codificación:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notificación push interactiva

Las notificaciones push pueden responder a acciones del usuario dentro de una extensión de una aplicación de contenidos. Para los usuarios con iOS 12 o posterior, esto significa que puedes convertir tus notificaciones push en mensajes totalmente interactivos. Esto proporciona una opción interesante para introducir interactividad en tus promociones y aplicaciones. Por ejemplo, tu notificación push puede incluir un juego para que jueguen los usuarios, una ruleta para ganar descuentos o un botón "me gusta" para guardar un anuncio o una canción.

El siguiente ejemplo muestra una notificación push en la que los usuarios pueden jugar a un partido dentro de la notificación expandida.

![Un diagrama de cómo podrían ser las fases de una notificación push interactiva. Una secuencia muestra a un usuario pulsando en una notificación push que muestra un juego interactivo de correspondencias.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuración del panel de control

Para crear una notificación push interactiva, debes establecer una vista personalizada en tu panel. 

1. En la página **Campañas**, haz clic en **Crear campaña** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Redactar**, alterna **los botones de notificación**. 
3. Introduce una categoría iOS personalizada en el campo **Categoría de notificación iOS**. 
4. En la página `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor dado aquí debe coincidir con lo establecido en el panel de Braze en **Categoría de notificación de iOS**. 
5. Configura la tecla `UNNotificationExtensionInteractionEnabled` en `true` para habilitar las interacciones del usuario en una notificación push.

![Las opciones del botón de notificación que se encuentran en la configuración del creador de mensajes push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

### ¿Listo para el análisis de registros?
Visita la [sección Análisis de registro](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos.

## Notificaciones push personalizadas
![Dos iPhones mostrados uno al lado del otro. El primer iPhone muestra la vista no ampliada del mensaje push. El segundo iPhone muestra la versión ampliada del mensaje push mostrando una imagen de "progreso" de hasta dónde han llegado en un curso, el nombre de la siguiente sesión y cuándo debe completarse la siguiente sesión.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Las notificaciones push pueden mostrar información específica del usuario dentro de una extensión de contenido. Esto te permite crear contenido push centrado en el usuario, como añadir la opción de compartir su progreso en distintas plataformas, mostrar los logros desbloqueados o mostrar listas de control de incorporación. Este ejemplo muestra una notificación push mostrada a un usuario después de que haya completado una tarea específica en el curso de Braze Learning. Al ampliar la notificación, el usuario puede ver su progreso a través de su ruta de aprendizaje. La información que se proporciona aquí es específica del usuario y puede dispararse cuando se completa una sesión o se realiza una acción específica del usuario aprovechando un desencadenante de la API. 

### Configuración del panel de control

Para crear una notificación push personalizada, debes establecer una vista personalizada en tu panel. 

1. En la página **Campañas**, haz clic en **Crear campaña** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Redactar**, alterna **los botones de notificación**. 
3. Introduce una categoría iOS personalizada en el campo **Categoría de notificación iOS**. 
4. En la pestaña **Configuración**, crea pares clave-valor utilizando el estándar Liquid. Configura los atributos de usuario adecuados que quieres que muestre el mensaje. Estas vistas pueden personalizarse en función de atributos específicos de usuario de un perfil de usuario concreto.
5. En la página `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor dado aquí debe coincidir con lo establecido en el panel de Braze en **Categoría de notificación de iOS**. 

![Cuatro conjuntos de pares clave-valor, en los que "next_session_name" y "next_session_complete_date" se configuran como una propiedad desencadenante de la API mediante Liquid, y "completed_session count" y "total_session_count" se configuran como un atributo personalizado del usuario mediante Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Manejo de pares clave-valor

Se llama al método `didReceive` cuando la extensión de la aplicación de contenido de notificaciones ha recibido una notificación. Este método se encuentra en `NotificationViewController`. Los pares clave-valor proporcionados en el panel se representan en el código mediante el uso de un diccionario `userInfo`.

#### Análisis sintáctico de los pares clave-valor de las notificaciones push

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

### ¿Listo para el análisis de registros?
Visita la [sección Análisis de registro](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos.

## Captura de información de notificaciones push

Las notificaciones push pueden capturar información del usuario dentro de una extensión de una aplicación de contenido, ampliando los límites de lo que es posible con un push. Solicitar la opinión del usuario a través de notificaciones push te permite no sólo solicitar información básica como el nombre o el correo electrónico, sino también pedir a los usuarios que envíen sus comentarios o completen un perfil de usuario inacabado. 

En el siguiente flujo, la vista personalizada es capaz de responder a los cambios de estado. Esos componentes del cambio de estado están representados en cada imagen. 

1. El usuario recibe una notificación push.
2. Se abre el push. Una vez expandido, el push pide información al usuario. En este ejemplo, se solicita la dirección de correo electrónico del usuario, pero podrías solicitar cualquier tipo de información.
3. Se proporciona información y, si está en el formato esperado, se muestra el botón de registro.
3. Se muestra la vista de confirmación, y se descarta la notificación push. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### Configuración del panel de control

Para crear una notificación push de captura de información, debes establecer una vista personalizada en tu panel. 

1. En la página **Campañas**, haz clic en **Crear campaña** para iniciar una nueva campaña de notificaciones push.
2. En la pestaña **Redactar**, alterna **los botones de notificación**. 
3. Introduce una categoría iOS personalizada en el campo **Categoría de notificación iOS**. 
4. En la pestaña **Configuración**, crea pares clave-valor utilizando el estándar Liquid. Configura los atributos de usuario adecuados que quieres que muestre el mensaje. 
5. En la página `.plist` de tu objetivo de extensión de contenido de notificación, establece el atributo `UNNotificationExtensionCategory` en tu categoría personalizada de iOS. El valor dado aquí debe coincidir con lo establecido en el panel de Braze en **Categoría de notificación de iOS**. 

Como se ve en el ejemplo, también puedes incluir una imagen en tu notificación push. Para ello, debes integrar [notificaciones enriquecidas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), establecer el estilo de notificación de tu campaña en Notificación enriquecida e incluir una imagen push enriquecida.

![Un mensaje push con tres conjuntos de pares clave-valor. 1\. "Braze_id" establecido como una llamada Liquid para recuperar el ID de Braze. 2\. "cert_title" establecido como "Certificado de especialista en marketing de Braze". 3\. "Cert_description" establecido como "Los especialistas en marketing certificados de Braze conducen...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Manejar las acciones de los botones

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

### Desestimar las notificaciones push

Las notificaciones push pueden descartarse automáticamente al pulsar un botón de acción. Hay tres opciones de descarte push preconstruidas que recomendamos:

1. `completion(.dismiss)` - Desestima la notificación
2. `completion(.doNotDismiss)` - La notificación permanece abierta
3. `completion(.dismissAndForward)` - Se expulsa el push y el usuario es redirigido a la aplicación

### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos. 

## Análisis de registros

### Registro con la API de Braze (recomendado)

El análisis de los registros puede hacerse en tiempo real con la ayuda del [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de la API Braze. Para registrar los análisis, envía el valor `braze_id` en el campo de los pares clave-valor (como se ve en la siguiente captura de pantalla) para identificar qué perfil de usuario hay que actualizar.

![Un mensaje push con tres conjuntos de pares clave-valor. 1\. "Braze_id" establecido como una llamada Liquid para recuperar el ID de Braze. 2\. "cert_title" establecido como "Certificado de especialista en marketing de Braze". 3\. "Cert_description" establecido como "Los especialistas en marketing certificados de Braze conducen...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Registrar manualmente

El registro manual requerirá que primero configures espacios de trabajo dentro de Xcode, y luego crees, guardes y recuperes análisis. Esto requerirá algún trabajo personalizado de tu desarrollador. Los siguientes fragmentos de código te ayudarán a solucionarlo. 

Es importante tener en cuenta que los análisis no se envían a Braze hasta que se lanza posteriormente la aplicación móvil. Esto significa que, dependiendo de tu configuración de rechazo, a menudo existe un periodo de tiempo indeterminado entre que se rechaza una notificación push y se lanza la aplicación móvil y se recuperan los análisis. Aunque es posible que este búfer de tiempo no afecte a todos los casos de uso, debes tener en cuenta este impacto y ajustar tu recorrido de usuario según sea necesario para incluir la apertura de la aplicación con el fin de solucionar este problema. 

![Un gráfico que describe cómo se procesan los análisis en Braze. 1\. Se crean datos de análisis. 2\. Se guardan los datos de análisis. 3\. Se rechaza la notificación push. 4\. Período de tiempo indeterminado entre que se rechaza la notificación push y se inicia la aplicación móvil. 5\. Se inicia la aplicación móvil. 6\. Se reciben datos de análisis. 7\. Los datos de análisis se envían a Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Paso 1: Configura grupos de aplicaciones en Xcode
En Xcode, añade la función `App Groups`. Si no tienes ningún espacio de trabajo en tu aplicación, ve a la capacidad del objetivo principal de la aplicación, activa `App Groups`, y haz clic en el botón **+** Añadir. A continuación, utiliza el ID del paquete de tu aplicación para crear el espacio de trabajo. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu espacio de trabajo `group.com.company.appname.xyz`. Asegúrate de que `App Groups` está activado tanto para el destino principal de tu aplicación como para el destino de la extensión de contenido.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

#### Paso 2: Integrar fragmentos de código
Los siguientes fragmentos de código son una referencia útil sobre cómo guardar y enviar eventos personalizados, atributos personalizados y atributos de usuario. En esta guía se hablará en términos de `UserDefaults`, pero la representación del código se hará en forma del archivo de ayuda `RemoteStorage`. Hay archivos de ayuda adicionales, `UserAttributes` y `EventName Dictionary`, que se utilizan al enviar y guardar atributos de usuario.

{% tabs local %}
{% tab Eventos personalizados %}

##### Guardar eventos personalizados

Para guardar eventos personalizados, debes crear el análisis desde cero. Esto se hace creando un diccionario, rellenándolo con metadatos y guardando los datos mediante el uso de un archivo de ayuda.

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

El mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificaciones es justo después de inicializar el SDK. Esto se puede hacer recorriendo en bucle los eventos pendientes, buscando la clave "Nombre del evento", configurando los valores adecuados en Braze y, a continuación, borrando el almacenamiento para la próxima vez que se necesite esta función.

1. Recorre la matriz de eventos pendientes
2. Recorre cada par clave-valor del diccionario `pendingEvents` 
3. Comprueba explícitamente la clave de "Nombre del evento" para establecer el valor correspondiente
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
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
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
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
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

Para guardar atributos personalizados, debes crear el análisis desde cero. Esto se hace creando un diccionario, rellenándolo con metadatos y guardando los datos mediante el uso de un archivo de ayuda.

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

El mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificaciones es justo después de inicializar el SDK. Esto puede hacerse recorriendo en bucle los atributos pendientes, configurando el atributo personalizado apropiado en Braze y, a continuación, borrando el almacenamiento para la próxima vez que se necesite esta función.

1. Recorre la matriz de atributos pendientes
2. Recorre cada par clave-valor del diccionario `pendingAttributes` 
3. Registra atributos personalizados individuales con la clave y el valor correspondientes
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

Al guardar atributos de usuario, recomendamos crear un objeto personalizado para descifrar qué tipo de atributo se está actualizando (`email`, `first_name`, `phone_number`, etc.). El objeto debe ser compatible con ser almacenado/recuperado desde `UserDefaults`. Consulta el archivo de ayuda `UserAttribute` para ver un ejemplo de cómo conseguirlo.

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

El mejor momento para registrar cualquier análisis guardado de una extensión de aplicación de contenido de notificaciones es justo después de inicializar el SDK. Esto puede hacerse recorriendo en bucle los atributos pendientes, configurando el atributo personalizado apropiado en Braze y, a continuación, borrando el almacenamiento para la próxima vez que se necesite esta función.

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

