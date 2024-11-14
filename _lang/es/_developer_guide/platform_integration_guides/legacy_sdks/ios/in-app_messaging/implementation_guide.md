---
nav_title: Aplicación avanzada (Opcional)
article_title: Guía de implementación de mensajes dentro de la aplicación para iOS (Opcional)
platform: iOS
page_order: 6
description: "Esta guía de implementación avanzada abarca consideraciones sobre códigos de mensajes dentro de la aplicación de iOS, tres casos de uso creados por nuestro equipo y fragmentos de código que los acompañan."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
¿Buscas la guía básica de integración del desarrollador de mensajes dentro de la aplicación? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# Guía de implementación de la mensajería dentro de la aplicación

> Esta guía de implementación opcional y avanzada abarca consideraciones sobre códigos de mensajes dentro de la aplicación, tres casos de uso personalizados creados por nuestro equipo y fragmentos de código que los acompañan. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Esta guía de implementación se centra en una implementación Swift, pero se proporcionan fragmentos de código Objective-C para los interesados. ¿Buscas implementaciones HTML? ¡Echa un vistazo a nuestro [repositorio de plantillas HTML](https://github.com/braze-inc/in-app-message-templates)!

## Consideraciones sobre códigos

La siguiente guía ofrece una integración personalizada opcional para desarrolladores que se puede utilizar además de los mensajes predeterminados dentro de la aplicación. Se incluyen controladores de vista personalizados con cada caso de uso, que ofrecen ejemplos para ampliar la funcionalidad y personalizar de forma nativa el aspecto de tus mensajes dentro de la aplicación.

### Subclases de ABKInAppMessage

El siguiente fragmento de código es un método delegado de interfaz de usuario del SDK de Braze que determina con qué vista de subclase quieres rellenar tu mensaje dentro de la aplicación. En esta guía cubrimos una implementación básica y mostramos cómo las subclases completo, deslizar hacia arriba y modal pueden implementarse de forma cautivadora. Ten en cuenta que si quieres configurar tu controlador de vista personalizado, debes configurar todas las demás subclases de mensajes dentro de la aplicación. Una vez que tengas una sólida comprensión de los conceptos que hay detrás de las subclases, consulta nuestros [casos de uso](#sample-use-cases) para empezar a implementar subclases de mensajería dentro de la aplicación.

{% tabs %}
{% tab Swift %}
**Subclases de ABKInAppMessage**<br>

```swift
extension AppboyManager: ABKInAppMessageUIDelegate {
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return slideupViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageModal: 
      return modalViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageFull:
      return fullViewController(inAppMessage: inAppMessage) //Custom Method
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
    }
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Subclases de ABKInAppMessage**<br> 

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [self slideupViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [self modalViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [self fullViewControllerWithInAppMessage:inAppMessage]; //Custom Method
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

## Casos prácticos

A continuación te presentamos tres casos de uso. Cada caso de uso ofrece una explicación detallada, fragmentos de código relevantes y una visión de cómo pueden verse y utilizarse los mensajes dentro de la aplicación en el panel de Braze:
- [Mensaje personalizado deslizable dentro de la aplicación](#custom-slide-up-in-app-message)
- [Mensaje modal personalizado dentro de la aplicación](#custom-modal-in-app-message)
- [Mensaje completo personalizado dentro de la aplicación](#custom-full-in-app-message)

### Mensaje personalizado deslizable dentro de la aplicación

![Dos iPhone uno al lado del otro. El primer iPhone tiene el mensaje deslizante tocando la parte inferior de la pantalla del teléfono. El segundo iPhone tiene el mensaje deslizado más arriba en la pantalla, lo que te permite ver el botón de navegación de la aplicación.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

Mientras creas tu mensaje deslizable dentro de la aplicación, puede que notes que no puedes modificar la ubicación del mensaje utilizando los métodos predeterminados. Una modificación como esta es posible subclasificando `ABKInAppMessageSlideupViewController` y sustituyendo la variable `offset` por tu propia variable personalizada. La imagen de la derecha muestra un ejemplo de cómo se puede utilizar esto para ajustar tus mensajes deslizantes dentro de la aplicación. 

Visita la página [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) para empezar.

#### Añadir un comportamiento adicional a nuestra interfaz predeterminada<br><br>

{% tabs %}
{% tab Swift %}
**Actualiza la variable `offset` **<br>
Actualiza la variable `offset` y establece tu propio desplazamiento para adaptarlo a tus necesidades.
```swift
func setSlideConstraint() {
  offset = 0
}
```

```swift
override var offset: CGFloat {
  get {
    return super.offset
  }
  set {
    super.offset = newValue + adjustedOffset
  }
}
```

{% details Versión 3.34.0 o anterior  %}
**Actualiza la variable `slideConstraint` **<br>
La variable pública `slideConstraint` procede de la superclase `ABKInAppMessageSlideupViewController`. 

```swift
func setSlideConstraint() {
    slideConstraint?.constant = bottomSpacing
}
```

```swift
private var bottomSpacing: CGFloat {
    return AppboyManager.shared.activeApplicationViewController.topMostViewController().view.safeAreaInsets.bottom
}
``` 
Visita el repositorio de demostraciones Braze para ver la función [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17).
{% enddetails %}
{% endtab %}
{% tab Objective-C %}
**Actualiza la variable `offset` **<br>
Actualiza la variable `offset` y establece tu propio desplazamiento para adaptarlo a tus necesidades.
```objc
- (void)setOffset {
  self.offset = 0;
}
```

```objc
- (CGFloat)offset {
  return [super offset];
}
 
- (void)setOffset:(CGFloat)offset {
  [super setOffset:offset + [self adjustedOffset]];
}
```
{% details Versión 3.34.0 o anterior  %}
**Actualiza la variable `slideConstraint` **<br>
La variable pública `slideConstraint` procede de la superclase `ABKInAppMessageSlideupViewController`. 

```objc
- (void)self.setSlideConstraint:(NSLayoutConstraint *)slideConstraint {
  slideConstraint.constant = bottomSpacing;
}
```

```objc
- (CGFloat)bottomSpacing {
  return [AppboyManager shared].activeApplicationViewController.topMostViewController.view.safeAreaInsets.bottom;
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Anular y configurar restricción personalizada**<br>
Anula `beforeMoveInAppMessageViewOnScreen()` y establece tu propio valor de restricción personalizado para adaptarlo a tus necesidades. El valor original se establece en la superclase.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Versión 3.34.0 o anterior %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective-C %}
**Anular y configurar restricción personalizada**<br> 
Anula `beforeMoveInAppMessageViewOnScreen()` y establece tu propio valor de restricción personalizado para adaptarlo a tus necesidades. El valor original se establece en la superclase.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Versión 3.34.0 o anterior  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Ajustar la restricción para la orientación del dispositivo**<br>
Ajusta el valor correspondiente en `viewWillTransition()` porque la subclase asume la responsabilidad de mantener sincronizada la restricción durante los cambios de diseño.

### Mensaje modal personalizado dentro de la aplicación

![Un iPhone que muestra un mensaje dentro de la aplicación que te permite recorrer una lista de equipos deportivos y seleccionar tu favorito. En la parte inferior de este mensaje dentro de la aplicación, hay un gran botón azul de envío.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Una `ABKInAppMessageModalViewController` puede subclasificarse para aprovechar una `UIPickerView` que ofrezca formas atractivas de recopilar valiosos atributos de usuario. El mensaje modal personalizado dentro de la aplicación te permite utilizar Contenido conectado o cualquier lista disponible para mostrar y capturar atributos de una lista dinámica de elementos. 

Puedes interponer tus propias vistas en mensajes dentro de la aplicación subclasificados. Este ejemplo muestra cómo puede utilizarse un `UIPickerView` para ampliar la funcionalidad de un `ABKModalInAppMessageViewController`.

Visita el [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) para empezar.

#### Configuración del panel de control

Para configurar un mensaje modal dentro de la aplicación en el panel, debes proporcionar una lista de elementos formateada como una cadena separada por comas. En nuestro ejemplo, utilizamos Contenido conectado para extraer una lista JSON de nombres de equipos y darles el formato correspondiente.

![El creador de mensajes dentro de la aplicación muestra una vista previa del aspecto que tendrá el mensaje dentro de la aplicación, pero en su lugar muestra la lista de elementos que proporcionaste a Braze. Como la interfaz de usuario de Braze no muestra tu interfaz de usuario de mensajes dentro de la aplicación personalizada a menos que se envíe a un teléfono, la vista previa no es indicativa del aspecto que tendrá tu mensaje, por lo que te recomendamos que hagas una prueba antes de enviarlo.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

En los pares clave-valor, proporciona un `attribute_key`; esta clave, junto con el valor seleccionado por el usuario, se guardará en su perfil de usuario como un atributo personalizado. Tu lógica de vista personalizada debe gestionar los atributos de usuario enviados a Braze.

El diccionario `extras` del objeto `ABKInAppMessage` te permite consultar una clave `view_type` (si existe) que indique la vista correcta que se debe mostrar. Es importante tener en cuenta que los mensajes dentro de la aplicación se configuran para cada mensaje, por lo que las vistas modales personalizadas y predeterminadas pueden funcionar armoniosamente.

![Dos pares clave-valor encontrados en el creador de mensajes. El primer par clave-valor tiene "attribute_key" configurado como "Equipo favorito", y el segundo tiene "view_type" configurado como "selector".]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
Consulta el diccionario `extras` de tu `view_type` para cargar el controlador de vista subclase deseado.

```swift
func modalViewController(inAppMessage: ABKInAppMessage) -> ABKInAppMessageModalViewController {
  switch inAppMessage.extras?[InAppMessageKey.viewType.rawValue] as? String {
  case InAppMessageViewType.picker.rawValue:
    return ModalPickerViewController(inAppMessage: inAppMessage)
  default:
    return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
  }
}
```
{% endtab %}
{% tab Objective-C %}
**Utilizando `view_type` para el comportamiento de visualización de la IU**<br>
Consulta el diccionario `extras` de tu `view_type` para cargar el controlador de vista subclase deseado.

```objc
- (ABKInAppMessageModalViewController *)modalViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyViewType];
  NSString *viewType = [inAppMessageData rawValueForInAppMessageViewType:InAppMessageViewTypePicker];
   
  if ([inAppMessage.extras objectForKey:key] && [inAppMessage.extras[key] isEqualToString:viewType]) {
    return [[ModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Anula y proporciona una vista personalizada**<br>
Anula `loadView()` y configura tu propia vista personalizada para adaptarla a tus necesidades.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective-C %}
**Anula y proporciona una vista personalizada**<br>
Anula `loadView()` y configura tu propia vista personalizada para adaptarla a tus necesidades.
```objc
- (void)loadView {
  NSString *nibName = @"ModalPickerViewController";
  [[NSBundle mainBundle] loadNibNamed:nibName owner:self options:nil];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Variables de formato para una lista dinámica**<br>
Antes de recargar los componentes de `UIPickerView`, la variable de mensaje `inAppMessage` se muestra como una _cadena_. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Como ejemplo, esto se puede conseguir utilizando [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components).
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective-C %}
**Variables de formato para PickerView**<br>
Antes de recargar los componentes de `UIPickerView`, la variable de mensaje `inAppMessage` se muestra como una _cadena_. Este mensaje debe formatearse como una matriz de elementos para que se muestre correctamente. Por ejemplo, esto se puede conseguir utilizando [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
```objc
- (void)viewDidLoad {
  [super viewDidLoad];
   
  self.items = [[NSArray alloc] initWithArray:[self.inAppMessage.message componentsSeparatedByString:@", "]];
  [self.pickerView reloadAllComponents];
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Swift %}
**Asignar atributo personalizado**<br>
Utilizando la subclase, después de que un usuario pulse enviar, pasa el atributo con su correspondiente valor seleccionado a Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective-C %}
**Asignar atributo personalizado**<br>
Utilizando la subclase, después de que un usuario pulse enviar, pasa el atributo con su correspondiente valor seleccionado a Braze.
```objc
- (IBAction)primaryButtonTapped:(id)sender {
  InAppMessageData *inAppMessageData = [[InAppMessageData alloc] init];
  NSString *key = [inAppMessageData rawValueForInAppMessageKey:InAppMessageKeyAttributeKey];
   
  if (self.selectedItem.length > 0 && [self.inAppMessage.extras objectForKey:key]) {
    [[AppboyManager shared] setCustomAttributeWithKey:self.inAppMessage.extras[key] andStringValue:self.selectedItem];
  }
}
```
{% endtab %}
{% endtabs %}

{% alert tip %}
¿Te interesa aprovechar nuestros mensajes modales personalizados dentro de la aplicación para compartir videos a través de FaceTime? Consulta nuestra [guía de implementación de]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/) mensajes dentro de la aplicación de SharePlay.
{% endalert%}

### Mensaje completo personalizado dentro de la aplicación

![Un mensaje dentro de la aplicación que muestra una lista de opciones de configuración con alternadores al lado de cada opción. En la parte inferior del mensaje, hay un gran botón azul de envío.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Utiliza mensajes completos personalizados dentro de la aplicación para crear avisos interactivos y fáciles de usar para recopilar valiosos datos de clientes. El ejemplo de la derecha muestra una implementación del mensaje completo personalizado dentro de la aplicación reimaginado como una cartilla push interactiva con preferencias de notificación. 

Visita la página [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) para empezar.

#### Configuración del panel de control

Para configurar un mensaje completo personalizado dentro de la aplicación en el panel, debes proporcionar una lista de tus etiquetas formateadas como una cadena separada por comas. 

En los pares clave-valor, proporciona un `attribute_key`; esta clave, junto con los valores seleccionados por el usuario, se guardará en su perfil de usuario como un atributo personalizado. Tu lógica de vista personalizada debe gestionar los atributos de usuario enviados a Braze.

![Tres pares clave-valor encontrados en el creador de mensajes. El primer par clave-valor "attribute_key" se establece como "Push Tags", el segundo "subtitle_text" se establece como "La habilitación de las notificaciones también...", y el tercero "view_type" se establece como "table_list".]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Interceptar toques de mensajes dentro de la aplicación
![Un dispositivo Apple que muestra filas de configuraciones y alternancias. La vista personalizada maneja los botones, y cualquier toque fuera de los controles de los botones es manejado por el mensaje dentro de la aplicación y lo descartará.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Interceptar los toques de mensajes dentro de la aplicación es crucial para que los botones personalizados de mensajes completos dentro de la aplicación funcionen correctamente. Por predeterminado, `ABKInAppMessageImmersive` añade un reconocedor de gestos de pulsación sobre el mensaje, para que los usuarios puedan descartar mensajes sin botones. Al añadir un `UISwitch` o un botón a la jerarquía de la vista `UITableViewCell`, los toques pasan a ser gestionados por nuestra vista personalizada. A partir de iOS 6, los botones y otros controles tienen preferencia cuando trabajan con reconocedores de gestos, lo que hace que nuestro mensaje dentro de la aplicación personalizado funcione como debería. 

