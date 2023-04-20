---
nav_title: Style personnalisé
article_title: style personnalisé de carte de contenu pour le Web
page_order: 1
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article couvre les options de style personnalisé pour vos cartes de contenu dans votre application Web."

---

# Style personnalisé

> Cet article couvre les options de style personnalisé pour vos cartes de contenu dans votre application Web.

## Personnalisation de l’IU par défaut

Les éléments de l’IU de Braze sont dotés d’un aspect et une convivialité par défaut qui correspondent aux composeurs du tableau de bord de Braze et visent à assurer la cohérence avec d’autres plateformes mobiles Braze. Les styles par défaut de Braze sont définis en CSS au sein du SDK Braze.

En écrasant des styles sélectionnés dans votre application, il est possible de personnaliser notre fil standard avec vos propres images de fond, des familles de polices, des styles, des tailles, des animations, et bien plus encore. 

Par exemple, voici un exemple de remplacement qui entraînera l’apparition d’une carte de contenu de 800 px de large :

``` css
body .ab-feed {
  width: 800px;
}
```