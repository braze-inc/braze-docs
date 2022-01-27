---
nav_title: Flux multiples
article_title: Utiliser plusieurs flux de cartes de contenu pour Android/FireOS
page_order: 6
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre comment implémenter plusieurs fils de cartes de contenu dans votre application Android."
channel:
  - cartes de contenu
---

# Utilisation de plusieurs flux de carte de contenu

Les cartes de contenu peuvent être filtrées sur l'application pour n'afficher que des cartes spécifiques, qui vous permet d'avoir plusieurs flux de cartes de contenu pour différents cas d'utilisation (comme pour avoir un flux "transactionnel" par rapport à un flux "Marketing").

La documentation suivante montre un exemple d'implémentation qui peut être modifié pour correspondre à votre intégration spécifique.

## Étape 1 : Définir les paires de valeur clé sur les cartes

Lors de la création d'une campagne de la carte de contenu, les données de la paire de valeur clé peuvent être définies sur chaque carte. Notre logique de filtrage utilisera cette paire de données de valeur clé pour catégoriser les cartes. Notez que nous ne recommandons pas d'envoyer des valeurs JSON imbriquées en tant que paires clé-valeur. Au lieu de cela, afin que les choses soient correctes, nous vous recommandons d'aplanir le JSON avant l'envoi.

Pour les besoins de cet exemple, Nous allons définir une paire clé-valeur avec la clé `feed_type` qui désignera le flux de la carte de contenu dans lequel la carte doit être affichée. La valeur sera quel que soit votre flux personnalisé, comme dans `Transactionnel`, `Marketing`, et plus.

## Étape 2 : Créer un gestionnaire de mise à jour de la carte de contenu

Pour effectuer un filtrage sur un [`ContentCardsFragment`][1], nous allons créer une utilisation d'un [`IContentCardsUpdateHandler personnalisé`][2]. Un [`IContentCardsUpdateHandler`][2] prend un [`ContentCardsUpdatedEvent`][3] du Braze SDK et renvoie une liste de cartes à afficher.

Dans notre gestionnaire d'exemple, nous allons d'abord trier les cartes en utilisant la valeur par défaut [`IContentCardsUpdateHandler`][2]. La valeur par défaut de Braze [`IContentCardsUpdateHandler`][2] trie uniquement les cartes et par défaut n'effectue pas de suppression ou de filtrage par défaut. Ensuite, nous allons supprimer toutes les cartes de la liste qui ne correspondent pas à la valeur souhaitée pour le `feed_type` que nous avons défini plus tôt.

{% tabs %}
{% tab JAVA %}

```java
private IContentCardsUpdateHandler getUpdateHandlerForFeedType(final String desiredFeedType) {
  return new IContentCardsUpdateHandler() {
    @Override
    public List<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
      // Utiliser le gestionnaire de mise à jour de la carte par défaut pour un premier
      // passer au tri des cartes. Ce n'est pas requis
      // mais est fait pour plus de commodité.
      liste finale<Card> cartes = new DefaultContentCardsUpdateHandler(). andleCardUpdate(event);

      Iterator final<Card> cardIterator = cards.iterator();
      while (cardIterator. asNext()) {
        carte finale = cardIterator. ext();

        // Assurez-vous que la carte a notre KVP personnalisé
        // depuis le tableau de bord avec la clé "feed_type"
        si (card. etExtras().containsKey("feed_type")) {
          final String feedType = card. etExtras().get("feed_type");
          if (!desiredFeedType. quals(feedType)) {
            // La carte a un type de flux, mais cela ne correspond pas à
            // le type de flux souhaité, supprimez-le.
            cardIterator. émotion();
          }
        } else {
          // La carte n'a pas de flux
          // type du tout, le retirer
          cardIterator. émotion();
        }
      }

      // À ce stade, toutes les cartes de cette liste ont
      // un type de flux qui correspond explicitement à la valeur que nous mettons
      // dans le tableau de bord.
      renvoyer les cartes;
    }
  };
}
```
{% endtab %}
{% tab KOTLIN %}

```kotlin
private fun getUpdateHandlerForFeedType(desiredFeedType: String): IContentCardsUpdateHandler {
  return IContentCardsUpdateHandler { event ->
    // Utiliser le gestionnaire de mise à jour de la carte par défaut pour un premier
    // passer au tri des cartes. Ce n'est pas requis
    // mais est fait pour plus de commodité.
    cartes val = DefaultContentCardsUpdateHandler().handleCardUpdate(event)

    val cardIterator = cards.iterator()
    tandis que (cardIterator. asNext()) {
      carte val = cardIterator. ext()

      // Assurez-vous que la carte a notre KVP personnalisé
      // à partir du tableau de bord avec la clé "feed_type"
      if (card. xtras.containsKey("feed_type")) {
        val feedType = card. xtras["feed_type"]
        if (desiredFeedType ! feedType) {
          // La carte a un type de flux, mais cela ne correspond pas à
          // notre type de flux, supprimez-le.
          cardIterator. emove()
        }
      } else {
        // La carte n'a pas de type feed
        // du tout, le retirer
        cardIterator. emove()
      }
    }

    // À ce stade, toutes les cartes de cette liste ont
    // un type de flux qui correspond explicitement à la valeur que nous mettons
    // dans le tableau de bord.
    cartes
  }
}
```
{% endtab %}
{% endtabs %}

## Étape 3 : Créer un flux de carte de contenu en utilisant le gestionnaire de mise à jour personnalisé

Maintenant que nous avons un [personnalisé`IContentCardsUpdateHandler`][2], nous pouvons créer un [`ContentCardsFragment`][1] qui l'utilise. Dans l'exemple suivant de code, nous allons créer un [`ContentCardsFragment`][1] qui affiche uniquement les cartes avec une valeur "Transactionnelle" pour `feed_type`:

{% tabs %}
{% tab JAVA %}

```java
// Nous voulons un flux de cartes de contenu qui n'affiche que les cartes "Transactional".
ContentCardsFragment customContentCardsFragment = new ContentCardsFragment();
customContentCardsFragment.setContentCardUpdateHandler(getUpdateHandlerForFeedType("Transactional"));
```
{% endtab %}
{% tab KOTLIN %}

```kotlin
// Nous voulons un flux de cartes de contenu qui n'affiche que les cartes "Transactional".
val customContentCardsFragment = ContentCardsFragment()
customContentCardsFragment.contentCardUpdateHandler = getUpdateHandlerForFeedType("Transactional")
```
{% endtab %}
{% endtabs %}

## Étape 4 : Utiliser le fragment de cartes de contenu

Ce flux personnalisé peut être utilisé comme n'importe quel autre [`ContentCardsFragment`][1]. Dans les différentes parties de votre application, vous pouvez afficher différents flux de carte de contenu en fonction de la clé fournie sur le tableau de bord. Chaque fil [`ContentCardsFragment`][1] aura un ensemble unique de cartes affiché grâce à la personnalisation [`IContentCardsUpdateHandler`][2] sur chaque fragment.

Lorsque vous créez une campagne de carte de contenu, définissez votre paire clé-valeur comme: `feed_type` > `Transactionnel` ou quel que soit le type de flux que vous désirez.

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.handlers/-i-content-cards-update-handler/index.html
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.events/-content-cards-updated-event/index.html
