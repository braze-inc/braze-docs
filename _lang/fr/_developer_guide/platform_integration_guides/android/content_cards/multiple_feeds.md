---
nav_title: Flux multiples
article_title: Utiliser plusieurs flux de cartes de contenu pour Android et FireOS
page_order: 5
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment implémenter plusieurs flux de carte de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Utilisation de plusieurs flux de carte de contenu

Les cartes de contenu peuvent être filtrées sur l’application pour afficher uniquement des cartes spécifiques, ce qui vous permet d’avoir plusieurs flux de carte de contenu pour différents cas d’usage (par exemple, un flux transactionnel ou un flux marketing).

La documentation suivante montre un exemple d’implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir des paires clé-valeur sur les cartes

Lors de la création d’une campagne de carte de contenu, les données de paires clé-valeur peuvent être définies pour chaque carte. Notre logique de filtrage utilisera les données de cette paire clé-valeur pour catégoriser les cartes. Notez que nous ne recommandons pas d’envoyer des valeurs JSON imbriquées en tant que paires clé-valeur. Au lieu de cela, nous recommandons d’aplatir le JSON avant de l’envoyer. 

Pour cet exemple, nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera dans quel flux la carte de contenu doit s’afficher. La valeur sera ce qu’est votre flux personnalisé, comme dans `Transactional`, `Marketing` et plus encore.

## Étape 2 : Créer un gestionnaire de mise à jour de carte de contenu

Pour effectuer un filtrage sur un [`ContentCardsFragment`][1], nous créerons une utilisation [`IContentCardsUpdateHandler`][2] personnalisée. Un [`IContentCardsUpdateHandler`][2] prend un [`ContentCardsUpdatedEvent`][3] du SDK Braze et retourne une liste de cartes à afficher.

Dans notre exemple de gestionnaire, nous allons tout d’abord trier les cartes en utilisant le [`IContentCardsUpdateHandler`][2] par défaut. Le [`IContentCardsUpdateHandler`][2] par défaut Braze ne fait que trier les cartes et, par défaut, ne procède pas à des retraits ou à un filtrage seul. Ensuite, nous supprimerons les cartes de la liste qui ne correspondent pas à la valeur souhaitée pour le `feed_type` que nous avons défini plus tôt :

{% tabs %}
{% tab JAVA %}

```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Use the default card update handler for a first
      // pass at sorting the cards. This is not required
      // but is done for convenience.
      final List<Card> cards = new DefaultContentCardsUpdateHandler().handleCardUpdate(event);

      final Iterator<Card> cardIterator = cards.iterator();
      while (cardIterator.hasNext()) {
        final Card card = cardIterator.next();

        // Make sure the card has our custom KVP
        // from the dashboard with the key "feed_type"
        if (card.getExtras().containsKey("feed_type")) {
          final String feedType = card.getExtras().get("feed_type");
          if (!desiredFeedType.equals(feedType)) {
            // The card has a feed type, but it doesn't match
            // our desired feed type, remove it.
            cardIterator.remove();
          }
        } else {
          // The card doesn't have a feed
          // type at all, remove it
          cardIterator.remove();
        }
      }

      // At this point, all of the cards in this list have
      // a feed type that explicitly matches the value we put
      // in the dashboard.
      return cards;
    }
  };
}
```
{% endtab %}
{% tab KOTLIN %}

```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Use the default card update handler for a first
    // pass at sorting the cards. This is not required
    // but is done for convenience.
    val cards = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    while (cardIterator.hasNext()) {
      val card = cardIterator.next()

      // Make sure the card has our custom KVP
      // from the dashboard with the key "feed_type"
      if (card.extras.containsKey("feed_type")) {
        val feedType = card.extras["feed_type"]
        if (desiredFeedType != feedType) {
          // The card has a feed type, but it doesn't match
          // our desired feed type, remove it.
          cardIterator.remove()
        }
      } else {
        // The card doesn't have a feed
        // type at all, remove it
        cardIterator.remove()
      }
    }

    // At this point, all of the cards in this list have
    // a feed type that explicitly matches the value we put
    // in the dashboard.
    cards
  }
}
```
{% endtab %}
{% endtabs %}

## Étape 3 : Créer un flux de carte de contenu à l’aide du gestionnaire de mise à jour personnalisé

Maintenant que nous avons un [`IContentCardsUpdateHandler`][2] personnalisé, nous pouvons créer un [`ContentCardsFragment`][1] qui l’utilise. Dans l’exemple de code suivant, nous allons créer un [`ContentCardsFragment`][1] qui affiche uniquement les cartes où `feed_type` est « transactionnel » :

{% tabs %}
{% tab JAVA %}

```java
// We want a Content Cards feed that only shows "Transactional" cards.
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% endtab %}
{% tab KOTLIN %}

```kotlin
// We want a Content Cards feed that only shows "Transactional" cards.
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% endtab %}
{% endtabs %}

## Étape 4 : Utiliser le fragment de cartes de contenu

Ce flux personnalisé peut être utilisé comme n’importe quel autre [`ContentCardsFragment`][1]. Dans les différentes parties de votre application, vous pouvez afficher différents flux de carte de contenu en fonction de la clé fournie sur le tableau de bord. Chaque flux [`ContentCardsFragment`][1] aura un ensemble unique de cartes affichées grâce au [`IContentCardsUpdateHandler`][2] personnalisé sur chaque fragment.

Lors de la création d’une campagne de carte de contenu, définissez votre paire clé-valeur dans laquelle la clé est `feed_type` et la valeur est `Transactional`.

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html
