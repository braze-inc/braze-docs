---
nav_title: Aperçu Canvas
article_title: Aperçu Canvas
page_order: 3
page_type: reference
description: "Cet article de référence traite de quatre cas d’utilisation Canvas utiles."
tool: Canvas

---

# Grandes lignes du Canvas

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/page/courses){: style="float:right;width:120px;border:0;" class="noimgborder"}

> Cet article présente plusieurs exemples qui montrent comment vous pouvez utiliser Canvas pour réaliser des envois de messages ciblés et personnalisés en combinant des étapes de [Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) et de [Message.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 

L’apprentissage Braze propose également plusieurs cours Canvas dédiés, passant en revue des Canvas fréquents. Consultez-les pour obtenir des informations précieuses sur les termes et concepts expliqués dans un mélange de vidéos, cours et exercices interactifs. 
- [Créer des parcours clients avec Canvas Flow](https://learning.braze.com/create-customer-journeys-with-canvas-flow)
- [Onboarding des nouveaux membres du programme de fidélité](https://learning.braze.com/new-loyalty-member-onboarding)
- [Utilisateurs inactifs](https://learning.braze.com/lapsing-users)
- [Créer un parcours utilisateur pour les paniers abandonnés](https://learning.braze.com/build-an-abandoned-cart-user-journey)

{% alert important %}
À compter du 28 février 2023, vous ne pourrez plus créer ou dupliquer de canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles dans Canvas Flow.]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)
{% endalert %}

### Onboarding

Imaginons que votre restaurant désire faciliter l’onboarding des utilisateurs pour qu’ils effectuent leur première réservation. Étant donné que Canvas n’est que pour l’onboarding, un moment idéal pour qu’il se lance serait au démarrage de la session pour tous les nouveaux clients. Un moyen rapide et efficace de contacter votre audience serait d’utiliser le canal de communication SMS.

![]({% image_buster /assets/img_archive/canvas_outline_onboarding.png %}){: style="max-width:90%;"}

### Vente incitative

Vous pouvez également encourager la vente additionnelle d’abonnements en construisant et en envoyant des Canvas efficaces. Par exemple, si vous désirez mettre à niveau les utilisateurs actifs qui utilisent une version gratuite de votre application, vous pouvez créer un Canvas par événement qui se déclencherait quand un client a atteint l’événement personnalisé « A diffusé en continu pendant 3 heures ». En utilisant une étape de message, vous pouvez inciter ces clients à s’inscrire aux abonnements premiums.

![]({% image_buster /assets/img_archive/canvas_outline_upsell.png %}){: style="max-width:90%;"}

### Paniers abandonnés

Les commerces de détail peuvent souvent avoir besoin de rappeler à leurs clients qu’ils ont des achats non finalisés. À l’aide d’un Canvas par événement, vous pouvez envoyer un rappel à tous les clients enregistrés pour qu’ils achètent les produits de leurs paniers abandonnés. Vous pouvez également tester la réceptivité de vous clients envers les envois de messages grâce à des périodes de délai différentes.

![]({% image_buster /assets/img_archive/canvas_outline_cart.png %}){: style="max-width:90%;"}

### Ressources client

Vous pouvez utiliser Canvas pour renseigner vos clients sur des ressources. Par exemple, dans le cas d’une compagnie aérienne, vous pouvez créer un Canvas qui prépare les clients qui ont réservé un voyage dans trois jours en planifiant un e-mail hebdomadaire avec leurs informations de vol et la FAQ des aéroports associés.

![]({% image_buster /assets/img_archive/canvas_outline_resource.png %}){: style="max-width:90%;"}
