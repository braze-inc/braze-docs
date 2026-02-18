---
nav_title: "Migrar de cartões de conteúdo"
article_title: "Migrar de cartões de conteúdo de banners"
description: "Saiba como migrar de cartões de conteúdo de banner, incluindo exemplos de código para todos os SDKs suportados, limitações e benefícios."
page_order: 5
toc_headers: h2
channel:
  - banners
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Migrar de cartões de conteúdo de banners

> Este guia o ajuda a migrar de cartões de conteúdo de banner para casos de uso de envio de mensagens no estilo de banner. Os banners são ideais para mensagens inline e persistentes no app e na Internet que aparecem em locais específicos do aplicativo.

## Por que migrar para Banners?

- Se a sua equipe de engenharia estiver criando ou mantendo cartões de conteúdo personalizados, a migração para Banners pode reduzir esse investimento contínuo. Os banners permitem que os profissionais de marketing controlem a interface do usuário diretamente, liberando os desenvolvedores para outros trabalhos.
- Se estiver lançando novas mensagens na página inicial, fluxos de integração ou anúncios persistentes, comece com Banners em vez de usar cartões de conteúdo. Você pode se beneficiar da personalização em tempo real, sem expiração de 30 dias, sem limite de tamanho e com priorização nativa desde o primeiro dia.
- Se estiver trabalhando com o limite de expiração de 30 dias, gerenciando uma lógica complexa de reelegibilidade ou frustrado com uma personalização obsoleta, o Banners resolve esses problemas nativamente.

Os banners oferecem várias vantagens em relação aos cartões de conteúdo de banner para envio de mensagens no estilo de banner:

### Produção acelerada

- **Redução da necessidade de suporte contínuo de engenharia**: Os profissionais de marketing podem criar mensagens personalizadas usando um editor de arrastar e soltar e HTML personalizado sem precisar da assistência do desenvolvedor para a personalização
- **Opções flexíveis de personalização**: Projete diretamente no editor, use HTML ou aproveite os modelos de dados existentes com propriedades personalizadas

### Melhor UX

- **Atualizações dinâmicas de conteúdo**: Os banners atualizam a lógica e a elegibilidade do Liquid a cada atualização, garantindo que os usuários sempre vejam o conteúdo mais relevante
- **Suporte à colocação de nativos**: O envio de mensagens aparece em contextos específicos em vez de em um feed, proporcionando melhor relevância contextual
- **Priorização de nativos**: Controle sobre a ordem de exibição sem lógica personalizada, facilitando o gerenciamento da hierarquia de mensagens

### Persistência

- **Sem limite de validade**: As campanhas de banner não têm um limite de expiração de 30 dias como os cartões de conteúdo, o que permite a verdadeira persistência das mensagens

## Quando migrar

Considere migrar para Banners se estiver usando cartões de conteúdo para:

- Heróis da página inicial, promoções de páginas de produtos, ofertas de checkout
- Anúncios de navegação persistentes ou mensagens na barra lateral
- Mensagens sempre ativas com duração superior a 30 dias
- Envio de mensagens onde você deseja personalização e elegibilidade em tempo real

## Quando manter os cartões de conteúdo

Continue usando os cartões de conteúdo, se necessário:

- **Experiências de feed:** Qualquer caso de uso que envolva várias mensagens roláveis ou uma "Caixa de entrada" baseada em cartões.
- **Características específicas:** Envio de mensagens que exigem Conteúdo conectado ou Códigos promocionais, pois os Banners não oferecem suporte nativo a esses recursos.
- **Entrega disparada:** Casos de uso que exigem estritamente a entrega baseada em ação ou disparada por API. Embora os banners não ofereçam suporte à entrega baseada em ação ou disparada por API, a avaliação de elegibilidade em tempo real significa que os usuários se qualificam ou desqualificam instantaneamente com base na associação ao segmento a cada atualização.

## Guia de migração

### Pré-requisitos

Antes de migrar, verifique se o SDK do Braze atende aos requisitos mínimos de versão:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Inscrever-se para receber atualizações

#### Abordagem de cartões de conteúdo

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((cards) => {
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToContentCardsUpdates { cards ->
  // Handle array of cards
  cards.forEach { card ->
    Log.d(TAG, "Card: ${card.id}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.contentCards.subscribeToUpdates { cards in
  // Handle array of cards
  for card in cards {
    print("Card: \(card.id)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  // Handle array of cards
  cards.forEach(card => {
    console.log("Card:", card.id);
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle array of cards
  for (final card in contentCards) {
    print("Card: ${card.id}");
  }
});
```
{% endtab %}
{% endtabs %}

#### Abordagem de banners

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const globalBanner = braze.getBanner("global_banner");
  if (globalBanner) {
    console.log("Banner received for placement:", globalBanner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val globalBanner = Braze.getInstance(context).getBanner("global_banner")
  if (globalBanner != null) {
    Log.d(TAG, "Banner received for placement: ${globalBanner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "global_banner") { banner in
    if let banner = banner {
      print("Banner received for placement: \(banner.placementId)")
    }
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("global_banner").then(banner => {
    if (banner) {
      console.log("Banner received for placement:", banner.placementId);
    }
  });
});
```
{% endtab %}
{% tab Flutter %}
```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  // Get banner for specific placement
  braze.getBanner("global_banner").then((banner) {
    if (banner != null) {
      print("Banner received for placement: ${banner.placementId}");
    }
  });
});
```
{% endtab %}
{% endtabs %}

### Exibir conteúdo

{% alert note %}
Os cartões de conteúdo de banner podem ser renderizados manualmente com lógica de IU personalizada, enquanto os banners só podem ser renderizados com os métodos SDK prontos para uso.
{% endalert %}

#### Abordagem de cartões de conteúdo

{% tabs %}
{% tab Web %}
```javascript
// Show default feed UI
braze.showContentCards(document.getElementById("feed"));

// Or manually render cards
const cards = braze.getCachedContentCards();
cards.forEach(card => {
  // Custom rendering logic
  if (card instanceof braze.ClassicCard) {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// Using default fragment
val fragment = ContentCardsFragment()
supportFragmentManager.beginTransaction()
  .replace(R.id.content_cards_container, fragment)
  .commit()

// Or manually render cards
val cards = Braze.getInstance(context).getCachedContentCards()
cards.forEach { card ->
  when (card) {
    is ClassicCard -> {
      // Render classic card
    }
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
// Using default view controller
let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
navigationController?.pushViewController(contentCardsController, animated: true)

// Or manually render cards
let cards = braze.contentCards.cards
for card in cards {
  switch card {
  case let card as Braze.ContentCard.Classic:
    // Render classic card
  default:
    break
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
// Launch default feed
Braze.launchContentCards();

// Or manually render cards
const cards = await Braze.getContentCards();
cards.forEach(card => {
  if (card.type === 'CLASSIC') {
    // Render classic card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
// Launch default feed
braze.launchContentCards();

// Or manually render cards
final cards = await braze.getContentCards();
for (final card in cards) {
  if (card.type == 'CLASSIC') {
    // Render classic card
  }
}
```
{% endtab %}
{% endtabs %}

#### Abordagem de banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(globalBanner, container);

  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="global_banner" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("global_banner"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze,
  processContentUpdates: { result in
    switch result {
    case .success(let updates):
      if let height = updates.height {
        // Update height constraint
      }
    case .failure:
      break
    }
  }
)
view.addSubview(bannerView)

braze.banners.requestBannersRefresh(placementIds: ["global_banner"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='global_banner'
/>

// Or get banner data
const banner = await Braze.getBanner("global_banner");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "global_banner",
)

// Or get banner data
final banner = await braze.getBanner("global_banner");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["global_banner"]);
```
{% endtab %}
{% endtabs %}

### Análise de dados (implementações personalizadas)

{% alert note %}
Tanto os cartões de conteúdo de banner quanto os cartões de conteúdo rastreiam automaticamente a análise de dados ao usar seus componentes de interface do usuário padrão. Os exemplos abaixo são para implementações personalizadas em que você está criando sua própria interface do usuário.
{% endalert %}

#### Abordagem de cartões de conteúdo

{% tabs %}
{% tab Web %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
    braze.logContentCardImpressions([card]);
});

// Manual click logging required for custom implementations
card.logClick();
```
{% endtab %}
{% tab Android %}
```kotlin
// Manual impression logging required for custom implementations
cards.forEach { card ->
    card.logImpression()
}

// Manual click logging required for custom implementations
card.logClick()
```
{% endtab %}
{% tab Swift %}
```swift
// Manual impression logging required for custom implementations
for card in cards {
    card.context?.logImpression()
}

// Manual click logging required for custom implementations
card.context?.logClick()
```
{% endtab %}
{% tab React Native %}
```javascript
// Manual impression logging required for custom implementations
cards.forEach(card => {
    Braze.logContentCardImpression(card.id);
});

// Manual click logging required for custom implementations
Braze.logContentCardClicked(card.id);
```
{% endtab %}
{% tab Flutter %}
```dart
// Manual impression logging required for custom implementations
for (final card in cards) {
    braze.logContentCardImpression(card);
}

// Manual click logging required for custom implementations
braze.logContentCardClicked(card);
```
{% endtab %}
{% endtabs %}

#### Abordagem de banners

{% tabs %}
{% tab Web %}

{% alert important %}
A análise de dados é automaticamente rastreada ao usar `insertBanner()`. O registro manual não deve ser usado quando se usa `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([globalBanner]);

// Log click (with optional buttonId)
braze.logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
A análise de dados é automaticamente rastreada ao usar o BannerView. O registro manual não deve ser usado ao utilizar o BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("global_banner");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("global_banner", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
A análise de dados é automaticamente rastreada ao usar o BannerUIView. O registro manual não deve ser usado para o BannerUIView padrão.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Log impression
braze.banners.logImpression(placementId: "global_banner")

// Log click (with optional buttonId)
braze.banners.logClick(placementId: "global_banner", buttonId: buttonId)

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
A análise de dados é automaticamente rastreada ao usar o BrazeBannerView. Não é necessário registro manual.
{% endalert %}

```javascript
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in React Native
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% tab Flutter %}

{% alert important %}
A análise de dados é automaticamente rastreada ao usar o BrazeBannerView. Não é necessário registro manual.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Manuseio de grupos de controle

#### Abordagem de cartões de conteúdo

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  if card.isControl {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  if (card.isControl) {
    // Logic for control cards ie. don't display but log analytics
  } else {
    // Logic for cards ie. render card
  }
}
```
{% endtab %}
{% endtabs %}

#### Abordagem de banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  
  // Always call insertBanner to track impression (including control)
  braze.insertBanner(globalBanner, container);
  
  // Hide if control group
  if (globalBanner.isControl) {
    container.style.display = "none";
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
// BannerView automatically handles control groups
// No additional code needed
val bannerView = BannerView(context).apply {
  placementId = "global_banner"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "global_banner",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "global_banner",
)
```
{% endtab %}
{% endtabs %}

## Limitações

Ao migrar de cartões de conteúdo de banner para cartões de conteúdo, esteja ciente das seguintes limitações:

### Envio de mensagens disparadas

Os banners são compatíveis apenas com campanhas de entrega programada. Para migrar uma mensagem que anteriormente era disparada por API ou baseada em ação, converta-a em um direcionamento baseado em segmento:

- **Exemplo:** Em vez de disparar um cartão "Complete Profile" com a API, crie um segmento para usuários que inscreveram-se nos últimos 7 dias, mas não completaram o perfil.
- **Elegibilidade em tempo real:** Os usuários se qualificam ou desqualificam para o Banner instantaneamente a cada atualização com base em sua associação ao segmento.

### Diferenças de recursos

| Recurso | Cartões de conteúdo | Banners |
|---------|--------------|---------|
| **Estrutura de conteúdo** |
| Vários cartões no feed | ✅ Suportado | Pode criar vários posicionamentos para obter uma implementação semelhante a um carrossel. Apenas um banner é devolvido por colocação. |
| Múltiplas colocações | N/D | Suporte a múltiplas colocações |
| Tipos de cartão (clássico, com legenda, somente imagem) | Vários tipos predefinidos | Banner único baseado em HTML (mais flexível) |
| **Gerenciamento de conteúdo** |
| Editor de arrastar e soltar | Requer desenvolvedor para personalização | Os profissionais de marketing podem criar/atualizar sem engenharia |
| HTML/CSS personalizado | Limitado à estrutura do cartão | Suporte completo a HTML/CSS |
| Pares de valores-chave para personalização | Necessário para personalização avançada | Pares de valores-chave com tipagem forte chamados "propriedades" para personalização avançada |
| **Persistência & Expiração** |
| Vencimento do cartão | Suportado (limite de 30 dias) | Suportado (sem limite de validade) |
| Verdadeira persistência | Máximo de 30 dias | Persistência ilimitada |
| **Display & Direcionamento** |
| Interface do usuário do feed | Feed padrão disponível | Somente com base em colocação |
| Posicionamento específico do contexto | ❌ Baseado em feed | Suporte à colocação de nativos |
| Priorização de nativos | Requer lógica personalizada | Priorização incorporada |
| **Interação com o usuário** |
| Demissão manual | ✅ Suportado | Não suportado |
| Cartões fixados | ✅ Suportado | N/D |
| **Análise de dados** |
| Análise automática de dados (UI padrão) | ✅ Suportado | ✅ Suportado |
| Classificação de prioridades | Não suportado | ✅ Suportado | 
| **Atualizações de conteúdo** |
| Atualização de modelos Liquid | Uma vez por cartão no envio/lançamento | Atualiza-se a cada atualização |
| Atualização elegível | Uma vez por cartão no envio/lançamento | Atualiza-se a cada sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limitações do produto

- Até 25 mensagens ativas por posicionamento.
- Até 10 IDs de posicionamento por solicitação de atualização; solicitações além disso são truncadas.

### Limitações do SDK

- No momento, os banners não são compatíveis com as plataformas .NET MAUI (Xamarin), Cordova, Unity, Vega ou TV.
- Verifique se você está usando as versões mínimas do SDK listadas nos pré-requisitos.

## Artigos relacionados

- [Posicionamento de banners]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Exibição de um banner por ID de posicionamento]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Análise de dados de banner]({{site.baseurl}}/developer_guide/banners/analytics)
- [Perguntas frequentes sobre banners]({{site.baseurl}}/developer_guide/banners/faq)

