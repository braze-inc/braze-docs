---
nav_title: Estilo
article_title: Personalização do estilo dos cartões de conteúdo
page_order: 1
description: "Este artigo cobre opções de estilo para seus Cartões de Conteúdo."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalização do estilo dos cartões de conteúdo

> Os Cartões de Conteúdo da Braze vêm com uma aparência padrão. Este artigo cobre opções de estilo para seus Cartões de Conteúdo para ajudá-lo a corresponder à identidade da sua marca. Para obter a lista completa dos tipos de cartões de conteúdo, consulte [Sobre cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/).

## Criação de um estilo personalizado

A interface padrão dos Cartões de Conteúdo é importada da camada de interface do SDK da Braze. A partir daí, você pode ajustar certas partes do estilo do cartão, a ordem em que os cartões são exibidos e como o feed é mostrado aos seus usuários.

![Dois cartões de conteúdo, um com a fonte padrão e os cantos quadrados e outro com os cantos arredondados e uma fonte encaracolada]({% image_buster/assets/img/content_cards/content-card-customization-attributes.png %})

{% alert note %}
Propriedades do cartão de conteúdo, como `title`, `cardDescription`, `imageUrl`, etc., são editáveis diretamente por meio do [dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details), que é o método preferido para alterar esses detalhes.
{% endalert %}


{% tabs %}
{% tab Android %}

Por padrão, os Cartões de Conteúdo do SDK do Android e do FireOS correspondem às diretrizes padrão da interface do usuário do Android para proporcionar uma experiência perfeita. Você pode ver esses estilos padrão no arquivo [`res/values/styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) na distribuição do SDK Braze:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_braze_description</item>
    <item name="android:textSize">15.0sp</item>
    <item name="android:includeFontPadding">false</item>
    <item name="android:paddingBottom">8.0dp</item>
    <item name="android:layout_marginLeft">10.0dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8.0dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_braze_content_cards_captioned_image_card_title_container</item>
  </style>
```

Para personalizar o estilo do seu cartão de conteúdo, substitua este estilo padrão. Para substituir um estilo, copie-o na sua totalidade para o arquivo `styles.xml` no seu projeto e faça modificações. Todo o estilo deve ser copiado para o seu arquivo `styles.xml` local para que todos os atributos sejam configurados corretamente.

{% subtabs local %}
{% subtab Correct style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16.0dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5.0dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

{% endsubtab %}
{% subtab Incorrect style override %}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/mint</item>
  <item name="android:cacheColorHint">@color/mint</item>
</style>
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Jetpack Compose %}

Por padrão, os Cartões de Conteúdo do SDK do Android e do FireOS correspondem às diretrizes padrão da interface do usuário do Android para proporcionar uma experiência perfeita.

Você pode aplicar estilo de duas maneiras. A primeira é passar um [`ContentCardListStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-list-styling/index.html) e [`ContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html) para [`ContentCardsList`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards/-content-cards-list.html)como no exemplo a seguir:

```kotlin
ContentCardsList(
    style = ContentCardListStyling(listBackgroundColor = Color.Red),
    cardStyle = ContentCardStyling(
        titleTextStyle = TextStyle(
            fontFamily = fontFamily,
            fontSize = 25.sp
        ),
        shadowRadius = 10.dp,
        shortNewsContentCardStyle = BrazeShortNewsContentCardStyling(
            shadowRadius = 15.dp
        )
    )
)
```

A segunda é usar [`BrazeStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose/-braze-style.html) para criar um estilo global para os componentes do Braze, como no exemplo a seguir:

```kotlin
BrazeStyle(
    contentCardStyle = ContentCardStyling(
        textAnnouncementContentCardStyle = BrazeTextAnnouncementContentCardStyling(
            cardBackgroundColor = Color.Red,
            descriptionTextStyle = TextStyle(
                fontFamily = fontFamily,
                fontSize = 25.sp,
            )
        ),
        titleTextColor = Color.Magenta
    )
) {
    // Your app here, including any ContentCardsList() in it
}
```

{% endtab %}
{% tab swift %}

O controlador de visualização de Cartões de Conteúdo permite que você personalize a aparência e o comportamento de todas as células através da [`BrazeContentCardUI.ViewController.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct) estrutura. Configurar cartões de conteúdo usando `Attributes` é uma opção fácil, permitindo que você lance sua interface de cartões de conteúdo com configuração mínima. 

{% alert important %}
A personalização via `Attributes` está disponível apenas em SWIFT.
{% endalert %}

{% subtabs %}
{% subtab Swift %}

**Modificando `Attributes.default`**

Personalize a aparência e a sensação de todas as instâncias do controlador de visualização da interface do usuário do cartão de conteúdo da Braze modificando diretamente a variável estática [`Attributes.defaults`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/defaults).

Por exemplo, para alterar o tamanho padrão da imagem e o raio do canto para todas as células:

```swift
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.cornerRadius = 20
BrazeContentCardUI.ViewController.Attributes.defaults.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)
```

**Inicializando o controlador de visualização com Atributos**

Se você deseja modificar apenas uma instância específica do controlador de visualização da interface do cartão de conteúdo da Braze, use o [`init(braze:attributes:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/init(braze:attributes:)/) inicializador para passar uma `Attributes` struct personalizada para o controlador de visualização.

Por exemplo, você pode alterar o tamanho da imagem e o raio do canto para uma instância específica do controlador de visualização:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.cornerRadius = 20
attributes.cellAttributes.classicImageSize = CGSize(width: 65, height: 65)

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Personalizando células por subclasse**

Como alternativa, você pode criar interfaces personalizadas registrando classes personalizadas para cada tipo de cartão desejado. Para usar sua subclasse em vez da célula padrão, modifique a propriedade [`cells`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cells) na estrutura `Attributes`. Por exemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
// Register your own custom cell
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

**Modificando cartões de conteúdo programaticamente**

Os cartões de conteúdo podem ser alterados programaticamente atribuindo o fechamento [`transform`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/transform) na sua estrutura `Attributes`. O exemplo abaixo modifica o `title` e o `description` de cartões compatíveis:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.transform = { cards in
  cards.map { card in
    var card = card
    if let title = card.title {
      card.title = "[modified] \(title)"
    }
    if let description = card.description {
      card.description = "[modified] \(description)"
    }
    return card
  }
}

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Confira o [app de exemplo Exemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para um exemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

Personalizar cartões de conteúdo por meio de `Attributes` não é compatível com Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Os estilos padrão do Braze são definidos em CSS dentro do SDK do Braze. Substituindo estilos selecionados em seu aplicativo, é possível personalizar nosso feed padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e muito mais. O seguinte é um exemplo de substituição que fará com que os cartões de conteúdo apareçam com 800 px de largura:

``` css
body .ab-feed {
  width: 800px;
}
```

{% endtab %}
{% endtabs %}

## Exemplos de personalização

### Fonte personalizada

Personalizar a fonte usada em seus Cartões de Conteúdo permite que você mantenha sua identidade de marca e crie uma experiência visualmente atraente para seus usuários. Use estas receitas para definir a fonte de todos os Cartões de Conteúdo programaticamente. 

{% tabs %}
{% tab Android %}

Para alterar a fonte padrão programaticamente, defina um estilo para os cartões e use o atributo `fontFamily` para instruir a Braze a usar sua família de fontes personalizada.

Por exemplo, para atualizar a fonte em todos os títulos para cartões de imagem legendados, substitua o estilo `Braze.ContentCards.CaptionedImage.Title` e faça referência à sua família de fontes personalizada. O valor do atributo deve apontar para uma família de fontes no seu diretório `res/font`.

Aqui está um exemplo truncado com uma família de fontes personalizadas, `my_custom_font_family`, referenciada na última linha:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
    ...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Para saber mais sobre a personalização de fontes no SDK do Android, consulte o [guia de famílias de fontes]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization).
{% endtab %}
{% tab Jetpack Compose %}
Para alterar a fonte padrão de forma programática, você pode definir o [`titleTextStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#715371549%2FProperties%2F-1725759721) de `ContentCardStyling`.

Você também pode definir `titleTextStyle` para um tipo de cartão específico, definindo-o em [`BrazeShortNewsContentCardStyling`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-braze-short-news-content-card-styling/index.html) e passando-o para a função [`shortNewsContentCardStyle`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#8580250%2FProperties%2F-1725759721) de `ContentCardStyling`.

```kotlin
val fontFamily = FontFamily(
    Font(R.font.sailec_bold)
)

ContentCardStyling(
    titleTextStyle = TextStyle(
        fontFamily = fontFamily
    )
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personalize suas fontes personalizando a `Attributes` da propriedade de instância [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por exemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.titleFont = .preferredFont(textStyle: .callout, weight: .bold)
attributes.cellAttributes.descriptionFont = .preferredFont(textStyle: .footnote, weight: .regular)
attributes.cellAttributes.domainFont = .preferredFont(textStyle: .footnote, weight: .medium)

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

A personalização de fontes via `Attributes` não é compatível com Objective-C. 

Confira o [app de exemplo de Exemplos](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/ObjC/Sources/ContentCards-Custom-UI/CardsInfoViewController.m#L97) para um exemplo de como criar sua própria interface com fontes personalizadas.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Assim como qualquer outro elemento da web, você pode personalizar facilmente a aparência dos cartões de conteúdo através do CSS. No seu arquivo CSS ou estilos embutidos, use a propriedade `font-family` e especifique o nome da fonte desejada ou a pilha de fontes.

```css
/* CSS selector targeting the Content Card element */
.card-element {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

{% endtab %}
{% endtabs %}

### Ícones fixados personalizados

Ao criar um cartão de conteúdo, os profissionais de marketing têm a opção de fixar o cartão. Um cartão fixado será exibido no topo do feed do usuário e não poderá ser descartado pelo usuário. À medida que você personaliza os estilos do seu cartão, você tem a capacidade de alterar a aparência do ícone fixado.

![Lado a lado da prévia do cartão de conteúdo no Braze para celular e Web com a opção "Fixar este cartão na parte superior do feed" selecionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

{% tabs %}
{% tab Android %}

Para definir um ícone fixado personalizado, substitua o estilo `Braze.ContentCards.PinnedIcon`. Seu ativo de imagem personalizado deve ser declarado no elemento `android:src`. Por exemplo:

```xml
  <style name="Braze.ContentCards.PinnedIcon">
    <item name="android:src">@drawable/{my_custom_image_here}</item>

    <item name="android:layout_width">wrap_content</item>
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_alignParentRight">true</item>
    <item name="android:layout_alignParentTop">true</item>
    <item name="android:contentDescription">@null</item>
    <item name="android:importantForAccessibility">no</item>
  </style>
```

{% endtab %}
{% tab Jetpack Compose %}

Para alterar o ícone fixo padrão, você pode definir o ícone [`pinnedResourceId`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#794044424%2FProperties%2F-1725759721) de `ContentCardStyling`.  Por exemplo:

```kotlin
ContentCardStyling(
    pinnedResourceId = R.drawable.pushpin,
    pinnedImageAlignment = Alignment.TopCenter
)
```

Você também pode especificar um criador em [`pinnedComposable`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#1460938052%2FProperties%2F-1725759721) de `ContentCardStyling`. Se `pinnedComposable` for especificado, ele substituirá o valor `pinnedResourceId`.

```kotlin
ContentCardStyling(
    pinnedComposable = {
        Box(Modifier.fillMaxWidth()) {
            Text(
                modifier = Modifier
                    .align(Alignment.Center)
                    .width(50.dp),
                text = "This message is not read. Please read it."
            )
        }
    }
)
```
{% endtab %}
{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Personalize o ícone do alfinete modificando as propriedades `pinIndicatorColor` e `pinIndicatorImage` da propriedade de instância [`cellAttributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller/attributes-swift.struct/cellattributes/). Por exemplo:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.pinIndicatorColor = .red
attributes.cellAttributes.pinIndicatorImage = UIImage(named: "my-image")

let viewController = BrazeContentCardUI.ViewController.init(braze: braze, attributes: attributes)
```

Você também pode usar a subclasse para criar sua própria versão personalizada de `BrazeContentCardUI.Cell`, que inclui o indicador de pino. Por exemplo: 

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cells[BrazeContentCardUI.ClassicImageCell.identifier] = CustomClassicImageCell.self

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

{% endsubtab %}
{% subtab Objective-C %}

A personalização do indicador de pin via `Attributes` não é compatível com Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

A estrutura do ícone fixado do cartão de conteúdo é:

```css
<div class="ab-pinned-indicator">
  <i class="fa fa-star"></i>
</div>
```

Se você quiser usar um ícone diferente do FontAwesome, basta substituir o nome da classe do elemento `i` pelo nome da classe do ícone desejado. 

Se você quiser trocar o ícone completamente, remova o elemento `i` e adicione o ícone personalizado como um filho de `ab-pinned-indicator`. Existem algumas formas diferentes de fazer isso, mas um método simples seria `replaceChildren()` no elemento `ab-pinned-indicator`.

Por exemplo:

```javascript
// Get the parent element
const pinnedIndicator = document.querySelector('.ab-pinned-indicator');

// Create a new custom icon element
const customIcon = document.createElement('span');
customIcon.classList.add('customIcon');

// Replace the existing icon with the custom icon
pinnedIndicator.replaceChildren(customIcon);
```

{% endtab %}
{% endtabs %}

### Alterando a cor do indicador de não lido

Os Cartões de Conteúdo contêm uma linha azul na parte inferior do cartão que indica se o cartão foi visualizado ou não. 

![Dois cartões de conteúdo exibidos lado a lado. O primeiro cartão tem uma LINE azul na parte inferior, indicando que não foi visto. O segundo cartão não tem uma linha azul, o que indica que ele já foi visto.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %})

{% tabs %}
{% tab Android %}

Altere a cor da barra indicadora de não lida alterando o valor em `com_braze_content_cards_unread_bar_color` no seu arquivo `colors.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

{% endtab %}
{% tab Jetpack Compose %}

Para alterar a cor da barra indicadora de não lidos, modifique o valor de [`unreadIndicatorColor`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.contentcards.styling/-content-card-styling/index.html#-1669590042%2FProperties%2F-1725759721) em `ContentCardStyling`:

```kotlin
ContentCardStyling(
    unreadIndicatorColor = Color.Red
)
```

{% endtab %}
{% tab swift %}

{% subtabs %}
{% subtab Swift %}

Altere a cor da barra indicadora de não lidos atribuindo um valor à cor de tonalidade da sua `BrazeContentCardUI.ViewController` instância:

```swift
let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze)
viewController.view.tintColor = .systemGreen
```

No entanto, se você deseja modificar apenas o indicador não visualizado, pode acessar a propriedade `unviewedIndicatorColor` da sua estrutura `BrazeContentCardUI.ViewController.Attributes`. Se você usar implementações da Braze `UITableViewCell`, deve acessar a propriedade antes que a célula seja desenhada.

Por exemplo, para definir a cor do indicador não visualizado para vermelho:

```swift
var attributes = BrazeContentCardUI.ViewController.Attributes.defaults
attributes.cellAttributes.unviewedIndicatorColor = .red

let viewController = BrazeContentCardUI.ViewController(braze: AppDelegate.braze, attributes: attributes)
```

Confira o [app de exemplo Exemplos](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift) para um exemplo completo.

{% endsubtab %}
{% subtab Objective-C %}

Altere a cor da barra indicadora de não lida atribuindo um valor à cor de tonalidade do seu `BRZContentCardUIViewController`:

```objc
BRZContentCardUIViewController *viewController = [[BRZContentCardUIViewController alloc] initWithBraze:AppDelegate.braze];
[viewController.view setTintColor:[UIColor systemGreenColor]];
```

A personalização apenas do indicador não visualizado via `Attributes` não é compatível com Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Para alterar a cor do indicador de não lido de um cartão, adicione CSS personalizado à sua página da web. Por exemplo, para definir a cor do indicador não visualizado para verde:

```css
.ab-unread-indicator { background-color: green; }
```

{% endtab %}
{% endtabs %}

### Desativando indicador de não lido

{% tabs %}
{% tab Android %}

Oculte a barra de indicador não lido configurando [`setUnreadBarVisible`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.view/-content-card-view-holder/set-unread-bar-visible.html?query=fun%20setUnreadBarVisible(isVisible:%20Boolean)) em `ContentCardViewHolder` para `false`. 

{% endtab %}

{% tab Jetpack Compose %}
Desativar o indicador de não lido não é suportado no Jetpack Compose.
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab Swift %}

Oculte a barra de indicador não lido definindo a propriedade `attributes.cellAttributes.unviewedIndicatorColor` em sua estrutura `Attributes` para `.clear`. 

{% endsubtab %}
{% subtab Objective-C %}

A personalização apenas do indicador não visualizado via `Attributes` não é compatível com Objective-C.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Oculte a barra indicadora de não lida adicionando o seguinte estilo ao seu `css`:

```css
.ab-unread-indicator { display: none; }
```

{% endtab %}
{% endtabs %}
