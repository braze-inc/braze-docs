---
nav_title: "Migrar de Cartões de conteúdo"
article_title: "Migrar de Cartões de conteúdo para Banners"
description: "Aprenda como migrar de Cartões de conteúdo para Banners, incluindo exemplos de código para todos os SDKs suportados, limitações e benefícios."
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

# Migrar de Cartões de conteúdo para Banners

> Este guia ajuda você a migrar de Cartões de conteúdo para Banners para casos de uso de envio de mensagens em estilo banner. Banners são ideais para mensagens inline e persistentes no app e na web que aparecem em locais específicos na sua aplicação.

## Por que migrar para Banners?

- Se sua equipe de engenharia está construindo ou mantendo Cartões de conteúdo personalizados, migrar para Banners pode reduzir esse investimento contínuo. Banners permitem que os profissionais de marketing controlem a interface do usuário diretamente, liberando os desenvolvedores para outros trabalhos.
- Se você está lançando novas mensagens na página inicial, fluxos de integração ou anúncios persistentes, comece com Banners em vez de construir sobre Cartões de conteúdo. Você pode se beneficiar de personalização em tempo real, sem expiração de 30 dias, sem limite de tamanho e priorização nativa desde o primeiro dia.
- Se você está lidando com o limite de expiração de 30 dias, gerenciando lógica de reelegibilidade complexa ou frustrado com personalização desatualizada, Banners resolvem esses problemas de forma nativa.

Banners oferecem várias vantagens sobre Cartões de conteúdo para envio de mensagens em estilo banner:

### Produção acelerada

- **Suporte de engenharia contínuo reduzido**: Os profissionais de marketing podem criar mensagens personalizadas usando um editor de arrastar e soltar e HTML personalizado sem precisar de assistência de desenvolvedores para personalização
- **Opções de personalização flexíveis**: Desenhe diretamente no editor, use HTML ou aproveite modelos de dados existentes com propriedades personalizadas

### Melhor experiência do usuário

- **Atualizações de conteúdo dinâmico**: Banners atualizam a lógica Liquid e a elegibilidade a cada atualização, garantindo que os usuários vejam sempre o conteúdo mais relevante
- **Suporte de posicionamento nativo**: As mensagens aparecem em contextos específicos em vez de um feed, proporcionando melhor relevância contextual
- **Priorização nativa**: Controle sobre a ordem de exibição sem lógica personalizada, facilitando a gestão da hierarquia das mensagens

### Persistência

- **Sem limite de expiração**: Campanhas de banner não têm um limite de expiração de 30 dias como os Cartões de conteúdo, permitindo a verdadeira persistência das mensagens

## Quando migrar

Considere migrar para Banners se você estiver usando Cartões de conteúdo para:

- Destaques da página inicial, promoções de página de produto, ofertas de checkout
- Anúncios de navegação persistente ou mensagens na barra lateral
- Mensagens sempre ativas que duram mais de 30 dias
- Mensagens onde você deseja personalização em tempo real e elegibilidade

## Quando manter os Cartões de conteúdo

Continue usando os Cartões de conteúdo se você precisar de:

- **Experiências de feed:** Qualquer caso de uso envolvendo várias mensagens roláveis ou uma "Caixa de Entrada" baseada em cartões.
- **Recursos específicos:** Mensagens que requerem Conteúdo conectado ou Códigos Promocionais, pois os Banners não suportam isso nativamente.
- **Entrega disparada:** Casos de uso que exigem estritamente entrega disparada por API ou entrega baseada em ação. Embora os Banners não suportem entrega disparada por API ou entrega baseada em ação, a avaliação de elegibilidade em tempo real significa que os usuários se qualificam ou desqualificam instantaneamente com base na associação ao segmento a cada atualização.

## Guia de migração

### Pré-requisitos

Antes de migrar, certifique-se de que seu SDK da Braze atende aos requisitos mínimos de versão:

{% multi_lang_include sdk_versions.md feature='banners' %}

### Inscrever-se para receber atualizações

#### Abordagem de Cartões de conteúdo

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

#### Abordagem de Banners

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  // Get banner for specific placement
  const banner = braze.getBanner("sample_placement_id");
  if (banner) {
    console.log("Banner received for placement:", banner.placementId);
  }
});
```
{% endtab %}
{% tab Android %}
```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  // Get banner for specific placement
  val banner = Braze.getInstance(context).getBanner("sample_placement_id")
  if (banner != null) {
    Log.d(TAG, "Banner received for placement: ${banner.placementId}")
  }
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.subscribeToUpdates { banners in
  // Get banner for specific placement
  braze.banners.getBanner(for: "sample_placement_id") { banner in
    guard let banner = banner else { return }

    print("Banner received for placement: \(banner.placementId)")
  }
}
```
{% endtab %}
{% tab React Native %}
```javascript
Braze.addListener(Braze.Events.BANNER_CARDS_UPDATED, (data) => {
  const banners = data.banners;
  // Get banner for specific placement
  Braze.getBanner("sample_placement_id").then(banner => {
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
  braze.getBanner("sample_placement_id").then((banner) {
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
Os Cartões de conteúdo podem ser renderizados manualmente com lógica de UI personalizada, enquanto os Banners só podem ser renderizados com os métodos padrão do SDK.
{% endalert %}

#### Abordagem de Cartões de conteúdo

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

#### Abordagem de Banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");
  braze.insertBanner(banner, container);

  if (banner.isControl) {
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Android %}
```kotlin
// Using BannerView in XML
// <com.braze.ui.banners.BannerView
//     android:id="@+id/banner_view"
//     android:layout_width="match_parent"
//     android:layout_height="wrap_content"
//     app:placementId="sample_placement_id" />

// Or programmatically
val bannerView = BannerView(context).apply {
  placementId = "sample_placement_id"
}
container.addView(bannerView)

Braze.getInstance(context).requestBannersRefresh(listOf("sample_placement_id"))
```
{% endtab %}
{% tab Swift %}
```swift
// Using BannerUIView
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
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

braze.banners.requestBannersRefresh(placementIds: ["sample_placement_id"])
```
{% endtab %}
{% tab React Native %}
```javascript
// Using BrazeBannerView component
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>

// Or get banner data
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  // Render custom banner UI
}

Braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% tab Flutter %}
```dart
// Using BrazeBannerView widget
BrazeBannerView(
  placementId: "sample_placement_id",
)

// Or get banner data
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  // Render custom banner UI
}

braze.requestBannersRefresh(["sample_placement_id"]);
```
{% endtab %}
{% endtabs %}

### Registrar análise de dados (implementações personalizadas)

{% alert note %}
Tanto os Cartões de conteúdo quanto os Banners rastreiam automaticamente a análise de dados ao usar seus componentes de UI padrão. Os exemplos abaixo são para implementações personalizadas onde você está construindo sua própria UI.
{% endalert %}

#### Abordagem de Cartões de conteúdo

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

#### Abordagem de Banners

{% tabs %}
{% tab Web %}

{% alert important %}
A análise de dados é rastreada automaticamente ao usar `insertBanner()`. O registro manual não deve ser usado ao usar `insertBanner()`.
{% endalert %}

```javascript
// Analytics are automatically tracked when using insertBanner()
// Manual logging should not be used when using insertBanner()

// For custom implementations, use manual logging methods:
// Log impression
braze.logBannerImpressions([banner]);

// Log click (with optional buttonId)
braze.logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Android %}

{% alert important %}
A análise de dados é rastreada automaticamente ao usar BannerView. O registro manual não deve ser usado ao usar BannerView.
{% endalert %}

```kotlin
// Analytics are automatically tracked when using BannerView
// Manual logging should not be used for default BannerView

// For custom implementations, use manual logging methods:
// Log impression
Braze.getInstance(context).logBannerImpression("sample_placement_id");

// Log click (with optional buttonId)
Braze.getInstance(context).logBannerClick("sample_placement_id", buttonId);
```
{% endtab %}
{% tab Swift %}

{% alert important %}
A análise de dados é rastreada automaticamente ao usar BannerUIView. O registro manual não deve ser usado para o BannerUIView padrão.
{% endalert %}

```swift
// Analytics are automatically tracked when using BannerUIView
// Manual logging should not be used for default BannerUIView

// For custom implementations, use manual logging methods:
// Get banner for specific placement
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  // Log impression
  banner.context?.logImpression()

  // Log click (with optional buttonId)
  banner.context?.logClick(buttonId: buttonId)
}

// Control groups are automatically handled by BannerUIView
```
{% endtab %}
{% tab React Native %}

{% alert important %}
A análise de dados é rastreada automaticamente ao usar BrazeBannerView. Nenhum registro manual é necessário.
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
A análise de dados é rastreada automaticamente ao usar BrazeBannerView. Nenhum registro manual é necessário.
{% endalert %}

```dart
// Analytics are automatically tracked when using BrazeBannerView
// No manual logging required

// Note: Manual logging methods for Banners are not yet supported in Flutter
// Control groups are automatically handled by BrazeBannerView
```
{% endtab %}
{% endtabs %}

### Obtendo propriedades

#### Abordagem de Cartões de conteúdo

{% tabs %}
{% tab Web %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Android %}
```kotlin
cards.forEach { card ->
  Log.d(TAG, "Card id: ${card.id} Extras: ${card.extras}")
}
```
{% endtab %}
{% tab Swift %}
```swift
for card in cards {
  print("Card id: \(card.id) Extras: \(card.extras)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
cards.forEach(card => {
  console.log("Card id:", card.id, "Extras:", card.extras);
});
```
{% endtab %}
{% tab Flutter %}
```dart
for (final card in cards) {
  print("Card id: ${card.id} Extras: ${card.extras}");
}
```
{% endtab %}
{% endtabs %}

#### Abordagem de Banners

{% tabs %}
{% tab Web %}
```javascript
const banner = braze.getBanner("sample_placement_id");
if (!banner) {
  return;
}

console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
```
{% endtab %}
{% tab Android %}
```kotlin
val banner = Braze.getInstance(context).getBanner("sample_placement_id")
if (banner != null) {
  Log.d(TAG, "Banner placement: ${banner.placementId} Properties: ${banner.properties}")
}
```
{% endtab %}
{% tab Swift %}
```swift
braze.banners.getBanner(for: "sample_placement_id") { banner in
  guard let banner = banner else { return }

  print("Banner placement: \(banner.placementId) Properties: \(banner.properties)")
}
```
{% endtab %}
{% tab React Native %}
```javascript
const banner = await Braze.getBanner("sample_placement_id");
if (banner) {
  console.log("Banner placement:", banner.placementId, "Properties:", banner.properties);
}
```
{% endtab %}
{% tab Flutter %}
```dart
final banner = await braze.getBanner("sample_placement_id");
if (banner != null) {
  print("Banner placement: ${banner.placementId} Properties: ${banner.properties}");
}
```
{% endtab %}
{% endtabs %}

### Tratamento de grupos de controle

#### Abordagem de Cartões de conteúdo

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

#### Abordagem de Banners

{% tabs %}
{% tab Web %}
```javascript
braze.subscribeToBannersUpdates((banners) => {
  const banner = braze.getBanner("sample_placement_id");
  if (!banner) {
    return;
  }

  const container = document.getElementById("global-banner-container");

  // Always call insertBanner to track impression (including control)
  braze.insertBanner(banner, container);

  // Hide if control group
  if (banner.isControl) {
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
  placementId = "sample_placement_id"
}
```
{% endtab %}
{% tab Swift %}
```swift
// BannerUIView automatically handles control groups
// No additional code needed
let bannerView = BrazeBannerUI.BannerUIView(
  placementId: "sample_placement_id",
  braze: braze
)
```
{% endtab %}
{% tab React Native %}
```javascript
// BrazeBannerView automatically handles control groups
// No additional code needed
<Braze.BrazeBannerView
  placementID='sample_placement_id'
/>
```
{% endtab %}
{% tab Flutter %}
```dart
// BrazeBannerView automatically handles control groups
// No additional code needed
BrazeBannerView(
  placementId: "sample_placement_id",
)
```
{% endtab %}
{% endtabs %}

## Limitações

Ao migrar de Cartões de conteúdo para Banners, esteja ciente das seguintes limitações:

### Migrando mensagens disparadas

Banners suportam apenas campanhas de entrega agendada. Para migrar uma mensagem que era anteriormente disparada por API ou baseada em ação, converta-a para direcionamento baseado em segmento:

- **Exemplo:** Em vez de disparar um cartão "Completar Perfil" com a API, crie um segmento para usuários que se inscreveram nos últimos 7 dias, mas não completaram seu perfil.
- **Elegibilidade em tempo real:** Os usuários se qualificam ou desqualificam para o Banner instantaneamente a cada atualização com base na associação ao segmento.

### Diferenças de recursos

| Recurso | Cartões de conteúdo | Banners |
|---------|--------------|---------|
| **Estrutura de conteúdo** |
| Múltiplos cartões no feed | ✅ Suportado | ✅ É possível criar múltiplos posicionamentos para alcançar uma implementação semelhante a carrossel. Apenas um banner é retornado por posicionamento. |
| Múltiplos posicionamentos | N/D | ✅ Múltiplos posicionamentos suportados |
| Tipos de cartões (Clássico, Com legenda, Apenas imagem) | ✅ Múltiplos tipos predefinidos | ✅ Banner único baseado em HTML (mais flexível) |
| **Gerenciamento de conteúdo** |
| Editor de arrastar e soltar | ❌ Requer desenvolvedor para personalização | ✅ Profissionais de marketing podem criar/atualizar sem engenharia |
| HTML/CSS personalizado | ❌ Limitado à estrutura do cartão | ✅ Suporte total a HTML/CSS |
| Pares chave-valor para personalização | ✅ Necessário para personalização avançada | ✅ Pares chave-valor fortemente tipados chamados "propriedades" para personalização avançada |
| **Persistência e expiração** |
| Expiração do cartão | ✅ Suportado (limite de 30 dias) | ✅ Suportado (sem limite de expiração) |
| Persistência verdadeira | ❌ Máximo de 30 dias | ✅ Persistência ilimitada |
| **Exibição e direcionamento** |
| Interface do feed | ✅ Feed padrão disponível | ❌ Apenas baseado em posicionamento |
| Posicionamento específico de contexto | ❌ Baseado em feed | ✅ Suporte nativo a posicionamento |
| Priorização nativa | ❌ Requer lógica personalizada | ✅ Priorização integrada |
| **Interação do usuário** |
| Descarte manual | ✅ Suportado | ❌ Não suportado |
| Cartões fixados | ✅ Suportado | N/D |
| **Análise de dados** |
| Análise automática (UI padrão) | ✅ Suportado | ✅ Suportado |
| Classificação por prioridade | ❌ Não suportado | ✅ Suportado |
| **Atualizações de conteúdo** |
| Atualização de template Liquid | ❌ Uma vez por cartão ao enviar/lançar | ✅ Atualiza a cada atualização |
| Atualização de elegibilidade | ❌ Uma vez por cartão ao enviar/lançar | ✅ Atualiza a cada sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Limitações do produto

- Até 25 mensagens ativas por posicionamento.
- Até 10 IDs de posicionamento por solicitação de atualização; solicitações além disso são truncadas.

### Limitações do SDK

- Banners não são atualmente suportados em .NET MAUI (Xamarin), Cordova, Unity, Vega ou plataformas de TV.
- Certifique-se de que está usando as versões mínimas do SDK listadas nos pré-requisitos.

## Artigos relacionados

- [Posicionamentos de banner]({{site.baseurl}}/developer_guide/banners/placements)
- [Tutorial: Exibindo um banner pelo ID de posicionamento]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Análise de dados de banner]({{site.baseurl}}/developer_guide/banners/analytics)
- [Perguntas frequentes sobre banners]({{site.baseurl}}/developer_guide/banners/faq)