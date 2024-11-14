---
nav_title: Implementação avançada (opcional)
article_title: Guia de implementação de mensagens no app para iOS (opcional)
platform: iOS
page_order: 6
description: "Este guia de implementação avançada aborda considerações sobre o código de mensagens no app do iOS, três casos de uso criados por nossa equipe e os trechos de código que os acompanham."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Está procurando o guia básico para desenvolvedores de integração de mensagens no app? Acesse [aqui]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/).
{% endalert %}

# Guia de implementação de envio de mensagens no app

> Este guia de implementação opcional e avançado aborda considerações sobre o código de mensagens no app, três casos de uso personalizados criados por nossa equipe e os trechos de código que os acompanham. Visite nosso repositório de demonstrações do Braze [aqui](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Este guia de implementação está centrado em uma implementação Swift, mas são fornecidos trechos em Objective C para os interessados. Procurando implementações em HTML? Dê uma olhada em nosso [repositório de modelos HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considerações de código

O guia a seguir oferece uma integração de desenvolvedor personalizada opcional para ser usada além das mensagens no app padrão. Os controladores de exibição personalizados estão incluídos em cada caso de uso, oferecendo exemplos para ampliar a funcionalidade e personalizar nativamente a aparência de suas mensagens no app.

### Subclasses de ABKInAppMessage

O trecho de código a seguir é um método delegado de interface do usuário do SDK do Braze que determina com qual visualização de subclasse você deseja preencher sua mensagem no app. Neste guia, abordamos uma implementação básica e mostramos como as subclasses completa, deslizante e modal podem ser implementadas de maneiras cativantes. Observe que, se quiser configurar seu view controller personalizado, você deverá configurar todas as outras subclasses de mensagens no app. Depois que você tiver uma sólida compreensão dos conceitos por trás da subclasse, confira nossos [casos de uso](#sample-use-cases) para começar a implementar subclasses de mensagens no app.

{% tabs %}
{% tab Swift %}
**Subclasses de ABKInAppMessage**<br>

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
{% tab Objective C %}
**Subclasses de ABKInAppMessage**<br> 

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

## Casos de uso

Fornecemos três casos de uso abaixo. Cada caso de uso oferece uma explicação detalhada, trechos de código relevantes e uma visão de como as mensagens no app podem parecer e ser usadas no dashboard do Braze:
- [Mensagem no app com slide personalizado](#custom-slide-up-in-app-message)
- [Mensagem modal personalizada no app](#custom-modal-in-app-message)
- [Mensagem no app completa personalizada](#custom-full-in-app-message)

### Mensagem no app com slide personalizado

![Dois iPhone lado a lado. O primeiro iPhone tem a mensagem deslizante tocando a parte inferior da tela do telefone. O segundo iPhone tem a mensagem deslizante na parte superior da tela, permitindo que você veja o botão de navegação do app exibido.]({% image_buster /assets/img/iam_implementation/slideup.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0;"}

Ao criar sua mensagem no app de slide-up, você pode notar que não é possível modificar a posição da mensagem usando métodos padrão. Modificações como essa são possíveis ao criar uma subclasse de `ABKInAppMessageSlideupViewController` e substituir a variável `offset` por sua própria variável personalizada. A imagem à direita mostra um exemplo de como isso pode ser usado para ajustar suas mensagens deslizantes no app. 

Visite o site [`SlideFromBottomViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/SlideFromBottomViewController.swift) para começar.

#### Adição de comportamento adicional à nossa UI padrão<br><br>

{% tabs %}
{% tab Swift %}
**Atualizar a variável `offset`**<br>
Atualize a variável `offset` e defina seu próprio deslocamento de acordo com suas necessidades.
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

{% details Versão 3.34.0 ou anterior  %}
**Atualizar a variável `slideConstraint`**<br>
A variável pública `slideConstraint` vem da superclasse `ABKInAppMessageSlideupViewController`. 

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
Acesse o repositório de demonstrações da Braze para obter a função [`topMostViewController()`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/Utils/UIViewController_Util.swift#L17).
{% enddetails %}
{% endtab %}
{% tab Objective C %}
**Atualizar a variável `offset`**<br>
Atualize a variável `offset` e defina seu próprio deslocamento de acordo com suas necessidades.
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
{% details Versão 3.34.0 ou anterior  %}
**Atualizar a variável `slideConstraint`**<br>
A variável pública `slideConstraint` vem da superclasse `ABKInAppMessageSlideupViewController`. 

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
**Substituir e definir restrições personalizadas**<br>
Substitua `beforeMoveInAppMessageViewOnScreen()` e defina seu próprio valor de restrição personalizado para atender às suas necessidades. O valor original é definido na superclasse.

```swift
override func beforeMoveInAppMessageViewOnScreen() {
  super.beforeMoveInAppMessageViewOnScreen()
  setOffset()
}
```

{% details Versão 3.34.0 ou anterior %}
```swift
override func beforeMoveInAppMessageViewOnScreen() {
  setSlideConstraint()
}
```
{% enddetails %}

{% endtab %}
{% tab Objective C %}
**Substituir e definir restrições personalizadas**<br> 
Substitua `beforeMoveInAppMessageViewOnScreen()` e defina seu próprio valor de restrição personalizado para atender às suas necessidades. O valor original é definido na superclasse.

```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [super beforeMoveInAppMessageViewOnScreen];
  [self setOffset];
}
```

{% details Versão 3.34.0 ou anterior  %}
```objc
- (void)beforeMoveInAppMessageViewOnScreen {
  [self setSlideConstraint:self.slideConstraint];
}
```
{% enddetails %}
{% endtab %}
{% endtabs %}

**Ajustar a restrição para a orientação do dispositivo**<br>
Ajuste o respectivo valor em `viewWillTransition()` porque a subclasse assume a responsabilidade de manter a restrição sincronizada durante as alterações de layout.

### Mensagem modal personalizada no app

![Um iPhone mostrando uma mensagem modal no app que permite percorrer uma lista de times esportivos e selecionar o seu favorito. Na parte inferior dessa mensagem no app, há um grande botão azul de envio.]({% image_buster /assets/img/iam_implementation/modal.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Um `ABKInAppMessageModalViewController` pode ser subclassificado para aproveitar um `UIPickerView` que oferece maneiras engajadas de coletar valiosas atribuições do usuário. A mensagem modal personalizada no app permite que você use o Connected Content ou qualquer lista disponível para exibir e capturar atribuições de uma lista dinâmica de itens. 

Você pode interpor suas próprias exibições em mensagens no app de subclasse. Este exemplo mostra como um `UIPickerView` pode ser utilizado para ampliar a funcionalidade de um `ABKModalInAppMessageViewController`.

Visite o [ModalPickerViewController](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/ModalPickerViewController/ModalPickerViewController.swift) para começar.

#### Configuração do dashboard

Para configurar uma mensagem modal no app no dashboard, você deve fornecer uma lista de itens formatada como uma string separada por vírgulas. Em nosso exemplo, usamos o conteúdo conectado para extrair uma lista JSON de nomes de equipes e formatá-los adequadamente.

![O criador de mensagens no app mostra uma prévia de como será a mensagem no app, mas, em vez disso, exibe a lista de itens que você forneceu à Braze. Como a UI do Braze não exibe sua mensagem personalizada no app, a menos que seja enviada para um telefone, a prévia não é indicativa da aparência da sua mensagem, portanto, recomendamos que você teste antes de enviar.]({% image_buster /assets/img/iam_implementation/dashboard1.png %})

Nos pares de chave-valor, forneça um `attribute_key`; essa chave, juntamente com o valor selecionado pelo usuário, será salva em seu perfil de usuário como um atributo personalizado. Sua lógica de visualização personalizada deve lidar com os atributos do usuário enviados ao Braze.

O dicionário `extras` no objeto `ABKInAppMessage` permite que você consulte uma chave `view_type` (se houver) que sinalize a exibição correta. É importante notar que as mensagens no app são configuradas por mensagem, de modo que as exibições modais personalizadas e padrão podem funcionar harmoniosamente.

![Dois pares de chave/valor encontrados no criador de mensagens. O primeiro par de valores-chave tem "attribute_key" definido como "Favorite Team" (Equipe favorita) e o segundo tem "view_type" definido como "picker" (selecionador).]({% image_buster /assets/img/iam_implementation/dashboard2.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Swift %}
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
Consulte o dicionário `extras` de `view_type` para carregar o view controller subclasse desejado.

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
{% tab Objective C %}
**Uso de `view_type` para comportamento de exibição da interface do usuário**<br>
Consulte o dicionário `extras` de `view_type` para carregar o view controller subclasse desejado.

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
**Substituir e fornecer exibição personalizada**<br>
Substitua o site `loadView()` e defina sua própria exibição personalizada para atender às suas necessidades.
```swift
override var nibname: String{
  return "ModalPickerViewController"
}

override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% tab Objective C %}
**Substituir e fornecer exibição personalizada**<br>
Substitua o site `loadView()` e defina sua própria exibição personalizada para atender às suas necessidades.
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
**Formatar variáveis para uma lista dinâmica**<br>
Antes de recarregar os componentes do site `UIPickerView`, a variável de mensagem `inAppMessage` é emitida como um _String_. Essa mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando [`components(separatedBy: ", ")`](https://developer.apple.com/documentation/foundation/nsstring/1413214-components).
```swift
override func viewDidLoad() {
  super.viewDidLoad()
 
  items = inAppMessage.message.separatedByCommaSpaceValue
  pickerView.reloadAllComponents()
}
```
{% endtab %}
{% tab Objective C %}
**Variáveis de formato para o PickerView**<br>
Antes de recarregar os componentes do site `UIPickerView`, a variável de mensagem `inAppMessage` é emitida como um _String_. Essa mensagem deve ser formatada como uma matriz de itens para ser exibida corretamente. Por exemplo, isso pode ser feito usando [`componentsSeparatedByString`](https://developer.apple.com/documentation/foundation/nsstring/1413214-componentsseparatedbystring?language=objc).
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
**Atribuir atributo personalizado**<br>
Usando a subclasse, depois que um usuário pressionar enviar, passe a atribuição com o valor selecionado correspondente para a Braze.
```swift
@IBAction func primaryButtonTapped(_ sender: Any) {
  guard let item = selectedItem, !item.isEmpty, let attributeKey = inAppMessage.extras?[InAppMessageKey.attributeKey.rawValue] as? String else { return }
     
  AppboyManager.shared.setCustomAttributeWithKey(attributeKey, andStringValue: item)
}
```
{% endtab %}
{% tab Objective C %}
**Atribuir atributo personalizado**<br>
Usando a subclasse, depois que um usuário pressionar enviar, passe a atribuição com o valor selecionado correspondente para a Braze.
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
Tem interesse em aproveitar nossas mensagens modais personalizadas no app para compartilhar vídeos no FaceTime? Confira nosso [guia de implementação]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/shareplay/) de mensagens no app SharePlay.
{% endalert%}

### Mensagem completa e personalizada no app

![Uma mensagem no app que exibe uma lista de opções de configuração com opções de alternância ao lado de cada opção. Na parte inferior da mensagem, há um grande botão azul de envio.]({% image_buster /assets/img/iam_implementation/fullscreen.png %}){: style="float:right;max-width:23%;margin-left:15px;border:0;"}

Use mensagens completas e personalizadas no app para criar prompts interativos e fáceis de usar para coletar dados valiosos de clientes. O exemplo à direita mostra uma implementação da mensagem no app personalizada e completa, reimaginada como um primer push interativo com preferências de notificação. 

Visite o site [`FullListViewController`](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/ViewController/In-App-Messages/FullListViewController/FullListViewController.swift) para começar.

#### Configuração do dashboard

Para configurar uma mensagem completa e personalizada no app no dashboard, você deve fornecer uma lista de suas tags formatadas como uma string separada por vírgulas. 

Nos pares de chave-valor, forneça um `attribute_key`; essa chave, juntamente com os valores selecionados pelo usuário, será salva em seu perfil de usuário como um atributo personalizado. Sua lógica de visualização personalizada deve lidar com os atributos do usuário enviados ao Braze.

![Três pares de chave/valor encontrados no criador de mensagens. O primeiro par de valores chave "attribute_key" é definido como "Push Tags", o segundo "subtitle_text" é definido como "Enabling notifications will also..." e o terceiro "view_type" é definido como "table_list".]({% image_buster /assets/img/iam_implementation/dashboard3.png %}){: style="max-width:65%;"}

#### Interceptação de toques em mensagens no app
![Um dispositivo Apple exibindo fileiras de configurações e botões. A exibição personalizada lida com os botões, e qualquer toque fora dos controles de botão é tratado pela mensagem no app e a dispensará.]({% image_buster /assets/img/iam_implementation_guide.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
A interceptação de toques em mensagens no app é crucial para fazer com que os botões personalizados de mensagem no app funcionem corretamente. Por padrão, o `ABKInAppMessageImmersive` adiciona um reconhecedor de gestos de toque à mensagem, para que os usuários possam descartar mensagens sem botões. Ao adicionar um `UISwitch` ou botão à hierarquia da visualização `UITableViewCell`, os toques agora são tratados pela nossa visualização personalizada. A partir do iOS 6, os botões e outros controles têm precedência ao trabalhar com reconhecedores de gestos, fazendo com que nossa mensagem completa personalizada no app funcione como deveria. 

