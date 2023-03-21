---
nav_title: Cas d’utilisation
article_title: "Cas d’utilisation de Shopify dans Braze"
description: "Cet article de référence décrit les cas d’utilisation pour utilisateurs débutants et avancés de Shopify."
page_type: partner
search_tag: Partenaire
alias: "/shopify_use_cases/"
page_order: 5
---

# Cas d’utilisation de Shopify

> Vous voulez savoir comment tirer parti de votre intégration Shopify pour créer des communications efficaces et en temps opportun pour vos utilisateurs ? Pour en savoir plus, reportez-vous aux sections suivantes des cas d’utilisation pour [utilisateur débutant](#beginner) et [utilisateur avancé](#advanced).

## Débutant

Ce sont des exemples d’utilisation simples mais efficaces que vous pouvez créer peu de temps après la configuration de Shopify. Aucun travail supplémentaire n’est requis. 

### Campagnes

Ces cas d’utilisations transactionnelles vous permettent d’alerter vos utilisateurs lorsqu’il y a une mise à jour de leur commande Shopify.

{% tabs local %}
{% tab Refund %}
**Événement de remboursement Shopify** - `shopify_created_refund`

Les utilisateurs ont reçu un remboursement, partiel ou complet. Cette campagne permet à l’utilisateur de savoir que sa commande a été remboursée avec succès.

![Campagne par événement qui enregistre les utilisateurs qui effectuent l’événement personnalisé « shopify_created_refund ».]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Exemple d’envoi de messages**

![E-mail avec le texte « Votre commande a été remboursée, nous sommes désolés que vous n’ayez pas été satisfait de votre commande. Nous avons bien envoyé votre remboursement. Veuillez attendre 3 à 5 jours ouvrables pour que les fonds apparaissent dans votre relevé, accessible via le bouton « Afficher le compte ».]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Événement d’annulation Shopify** - `shopify_cancelled_order`

Les utilisateurs ont pu annuler leurs commandes avant l’exécution. Cette campagne permet à l’utilisateur de savoir que son achat a été annulé avec succès.

![Campagne par événement qui enregistre les utilisateurs qui effectuent l’événement personnalisé « shopify_cancelled_order ».]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Exemple d’envoi de messages**

![E-mail avec le texte « Votre commande a été annulée, nous sommes désolés de vous voir partir ! Nous avons annulé votre commande avec succès. Veuillez attendre 3 à 5 jours ouvrables pour que les fonds apparaissent dans votre relevé, accessible via le bouton « Afficher le compte ».]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Evénement réalisé Shopify** - `shopify_fulfilled_order`

Tous les articles de la commande d’un utilisateur ont bien été préparés. Cette campagne permet à l’utilisateur de savoir que sa commande a été réalisée avec succès.

![Campagne par événement qui enregistre les utilisateurs qui effectuent l’événement personnalisé « shopify_fulfilled_order ».]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Exemple d’envoi de messages**

![Message texte avec le texte « Votre commande a été préparée ! Tous les articles de votre panier ont été livrés ! Veuillez accéder à votre compte et confirmer la réception. Points bonus pour avoir donné son avis. »]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Evénement partiellement réalisé Shopify** - `shopify_partially_fulfilled_order`

Certains articles de la commande d’un utilisateur ont été préparés avec succès. Cette campagne permet à l’utilisateur de savoir qu’une partie de sa commande a été réalisée avec succès.

![Campagne par événement qui enregistre les utilisateurs qui effectuent l’événement personnalisé « shopify_partially_fulfilled_order ».]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Exemple d’envoi de messages**

![Message texte avec le texte « Votre commande a été partiellement préparée ! Nous avons livré certains des articles de votre commande et le reste est en cours d’acheminement ! Nous vous enverrons une autre alerte lorsque la livraison sera complètement terminée. »]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Événement commande payée Shopify** - `shopify_paid_order`

L’utilisateur paie sa commande et le statut de la commande passe en « payé ». Cette campagne permet à l’utilisateur de savoir que le paiement de sa carte de crédit a été réalisé ou que la commande a été marquée comme payée si un paiement manuel est effectué.

![Campagne par événement qui enregistre les utilisateurs qui effectuent l’événement personnalisé « shopify_paid_order ».]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Exemple d’envoi de messages**

![E-mail avec le texte « Nous avons reçu votre paiement ! Votre commande est payée ! Veuillez attendre 1 à 2 jours ouvrables pour que nous permettre de traiter le paiement et préparer vos articles. Puis nous l'expédierons ! » et un bouton « View Account » (Afficher le compte).]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvas

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**Paiement abandonné pour Canvas**

Les utilisateurs abandonnent le paiement et ne réalisent pas les transactions avant la déconnexion. Ce Canvas vous permet d’envoyer des rappels automatisés aux utilisateurs qui n’ont pas terminé leurs transactions pour les ramener dans le processus de paiement.

Événement d’entrée basé sur une action : `shopify_abandoned_checkout`<br>
Événement d’exception : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**Canvas post-achat**

Les utilisateurs ont effectué un achat avec succès, et maintenant vous voulez savoir s’ils ont aimé leur achat. Ce Canvas vous permet d’envoyer des messages de suivi à votre utilisateur pour recueillir des commentaires. 

Événement d’entrée basé sur une action : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Avancée

Lorsque vous maîtriserez la plateforme, vous pourrez configurer des cas d’utilisation plus complexes.

### Campagnes

{% tabs local %}
{% tab User recommendations %}
**Recommandations pour les utilisateurs**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

L’utilisateur a cliqué ou regardé un article, mais n’a pas l’acheté. Cette campagne envoie un message de suivi à l’utilisateur avec les mêmes éléments ou éléments similaires (recommandés par le contenu connecté) pour inviter l’utilisateur à en acheter un.

Événement d’entrée basé sur une action : `shopify_product_clicked` ou `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Événement d’exception : `shopify_created_order` ou achat<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Refund winback Canvas %}

**Remboursement Canvas**

Les utilisateurs ont reçu un remboursement, partiel ou complet. Ce Canvas envoie des messages de suivi pour permettre à l’utilisateur de recommencer son achat.

Événement d’entrée basé sur une action : `shopify_created_refund`<br>
Événement d’exception : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**Canvas – Récupération d’annulation**

Les utilisateurs ont pu annuler leurs commandes avant l’exécution. Ce Canvas envoie des messages de suivi pour permettre à l’utilisateur de recommencer son achat.

Événement d’entrée basé sur une action : `shopify_cancelled_order`<br>
Événement d’exception : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}