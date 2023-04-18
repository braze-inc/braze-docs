---
nav_title: Gestion manuelle des clics
article_title: Gestion manuelle des clics de carte de contenu pour Android et FireOS
page_order: 4.2
platform: 
  - Android
  - FireOS
description: "Cet article explique comment gérer les clics de carte de contenu manuellement dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Gestion manuelle des clics

> Vous pouvez gérer les clics de carte de contenu manuellement en définissant un écouteur personnalisé. Cela permet des cas d’usage tels que l’utilisation sélective du navigateur Web natif pour ouvrir des liens Web.

Créez une classe qui implémente [`IContentCardsActionListener`][43] et enregistrez-la avec `BrazeContentCardsManager`. Implémentez la méthode `onContentCardClicked()`, qui sera appelée lorsque l’utilisateur clique sur une carte de contenu. Ensuite, demandez à Braze d’utiliser votre écouteur de clics sur la carte de contenu. L’extrait de code suivant montre un exemple d’écouteur de clics :

{% tabs %}
{% tab JAVA %}

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endtab %}
{% endtabs %}

[43]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html
