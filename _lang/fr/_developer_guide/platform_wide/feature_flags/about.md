---
nav_title: À propos des indicateurs de fonctionnalité
article_title: À propos des indicateurs de fonctionnalité
page_order: 1
description: "Découvrez comment coordonner les nouveaux déploiements de fonctionnalités avec les indicateurs de fonctionnalité de Braze."
platform:
  - iOS
  - Android
  - Web
channel:
  - Indicateurs de fonctionnalité
---

# À propos des indicateurs de fonctionnalité

> Cet article de référence couvre les bases des indicateurs de fonctionnalité et la raison pour laquelle vous les utiliseriez dans Braze. Vous cherchez les étapes permettant de créer un indicateur de fonctionnalité dans Braze ? Consulter [Créer des indicateurs de fonctionnalité][3].

Les indicateurs de fonctionnalité vous permettent d’activer ou de désactiver à distance la fonctionnalité d’une sélection d’utilisateurs spécifique ou aléatoire. Il est important de noter qu’ils vous permettent d’activer et de désactiver la production sans déploiement supplémentaire de codes ou mises à jour d’applications. Cela vous permet de déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance. 

{% alert important %} 
Les indicateurs de fonctionnalité sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé. 
{% endalert %}

## Conditions préalables

Pour utiliser des indicateurs de fonctionnalité, assurez-vous que vos SDK sont à jour avec au moins ces versions minimales :

{% sdk_min_versions android:24.2.0 web:4.6.0 swift:5.9.0 %}

## Cas d’utilisation
Les indicateurs de fonctionnalité ont quelques utilisations stratégiques différentes, décrites ci-dessous. Pour découvrir comment mettre en œuvre ces exemples d’utilisation, consultez l’article sur les [cas d’utilisation des indicateurs de fonctionnalités][2].

### Déploiements progressifs
Utilisez des indicateurs de fonctionnalités pour activer progressivement les entités à une population d’échantillons. Par exemple, vous pouvez commencer par lancer une nouvelle fonctionnalité pour vos utilisateurs VIP. Cette stratégie aide à atténuer les risques associés à l’expédition de nouvelles fonctionnalités à tout le monde en même temps et permet de détecter les bogues rapidement. 

![L’image mobile du curseur du trafic de déploiement passe de 0 % à 100 %.][1]

Imaginez, par exemple, que vous disposez d’un produit de commerce électronique qui est désormais disponible en plusieurs couleurs et que vous souhaitez mettre en œuvre un nouveau sélecteur de couleurs afin que les utilisateurs puissent spécifier la couleur à acheter. Vous pouvez libérer cette nouvelle fonction, mais seulement l’activer pour 5 % de vos utilisateurs dans Braze. Si tout va bien, vous pouvez augmenter progressivement 20 %, 50 % et finalement 100 %. Si un bogue critique est découvert, vous pouvez restaurer l’activation des fonctions à 0 % sans nécessiter de libération supplémentaire de code. 

### Contrôle à distance des variables d’application 
Utilisez des indicateurs de fonctionnalité pour modifier la fonctionnalité de votre application en production. Cela peut être particulièrement important pour les applications mobiles, où les approbations d’App Store empêchent de déployer rapidement les modifications à tous les utilisateurs.

Par exemple, vous pouvez utiliser les valeurs de propriété d’un indicateur d’entité pour modifier rapidement les liens ou le texte de la page d’accueil de votre application. Vous pouvez même personnaliser dynamiquement ce contenu en utilisant les attributs de profil Braze.

### Coordination des messages
{% alert important %} 
Cette fonctionnalité n’est pas encore prise en charge dans la version bêta.
{% endalert %}

Utilisez des indicateurs de fonctionnalité pour synchroniser le déploiement et l’envoi de messages d’une entité. Cela vous permettra d’utiliser Braze comme source de vérité pour votre expérience utilisateur et l’envoi de messages correspondant. Pour ce faire, cibler la nouvelle entité dans un segment particulier ou une partie filtrée de votre public. Créez ensuite une campagne ou un Canvas qui cible uniquement ce segment. 

### Expérimentation des fonctionnalités
{% alert important %} 
Cette fonctionnalité n’est pas encore prise en charge dans la version bêta.
{% endalert %}

Utilisez des indicateurs de caractéristiques pour expérimenter et confirmer vos hypothèses autour de votre nouvelle fonctionnalité. En répartissant le trafic en deux groupes ou plus, vous pouvez comparer l’impact d’un indicateur d’entité entre les groupes et déterminer le meilleur plan d’action en fonction des résultats.

Avec Canvas, vous pouvez suivre l’impact du déploiement des fonctions sur les conversations. Et, en utilisant [Chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths), vous pouvez optimiser ces conversions en testant différents messages ou chemins entre eux et en déterminant ce qui est le plus efficace. Utilisez le chemin gagnant pour déployer progressivement votre fonction à un public plus large.

<!-- For example, imagine that your ecommerce team has a new checkout page design that they believe will improve purchase conversion rates. When you release this feature, you can display the new page to 50% of your users for one month. If it performs better than the old design, you can increase the rollout traffic to 100%. If it performs poorly, you can turn it off completely and revisit the designs. In either case, you have avoided a poor experience for 50% of your users. -->

[1]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %} 
[2]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/use_cases/
[3]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
