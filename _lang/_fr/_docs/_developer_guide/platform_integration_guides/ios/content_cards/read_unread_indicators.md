---
nav_title: Lecture & Indicateurs non lus
article_title: Carte de contenu lue & Indicateurs non lus pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence couvre les indicateurs iOS lus et non lus et comment les implémenter dans vos Cartes de Contenu."
channel:
  - cartes de contenu
---

# Indicateurs lus et non lus

## Désactivation de l'indicateur non vu

 ![Lecture & Indicateur non lu]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: height="50%" width="50%"}

Vous pouvez choisir de désactiver la ligne bleue au bas de la carte qui indique si oui ou non la carte a été visualisée en définissant la propriété `disableUnviewedIndicator` dans `ABKContentCardsTableViewController` à OUI.

## Personnalisation de l'indicateur non vu

L'indicateur non vu est accessible via la propriété `unviewedLineView` de la classe `ABKBaseContentCardCell`. Si vous utilisez les implémentations `UITableViewCell` de Brase, vous devriez accéder à la propriété avant que la cellule ne soit dessinée.

Par exemple, pour définir la couleur de l'indicateur non vu à rouge:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(carte comme? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
