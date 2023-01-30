---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus de carte de contenu pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre les indicateurs de messages non lus et lus pour iOS et la manière de les implémenter dans vos cartes de contenu."
channel:
  - cartes de contenu

---

# Indicateurs de messages non lus et lus

## Désactivation de l’indicateur non visionné

![Deux cartes de contenu affichées côte à côte. La carte sur la gauche a une ligne bleue en bas, indiquant qu’elle n’a pas été vue. La carte sur la droite n’a pas de ligne bleue, indiquant qu’elle a déjà été vue.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Vous pouvez choisir de désactiver la ligne bleue au bas de la carte, qui indique si la carte a été visualisée en définissant la propriété `disableUnviewedIndicator` dans `ABKContentCardsTableViewController` sur `YES`.

## Personnaliser l’indicateur non visionné

L’indicateur non visionné est accessible via la propriété `unviewedLineView` de la classe `ABKBaseContentCardCell`. Si vous utilisez les implémentations `UITableViewCell` de Braze, vous devez accéder à la propriété avant que la cellule ne soit créée.

Par exemple, pour définir la couleur de l’indicateur non visionné en rouge :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
