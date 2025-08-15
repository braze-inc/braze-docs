---
nav_title: "Cas d'utilisation"
article_title: "Cas d'utilisation de Shopify à Braze"
description: "Cet article de référence présente des cas d'utilisation courants de Shopify pour débutants et avancés."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# Cas d'utilisation

> Vous souhaitez savoir comment tirer parti de votre intégration Shopify pour créer un envoi de messages rapide et efficace pour vos utilisateurs ? Consultez les sections suivantes sur les cas d'utilisation courants pour [débutants](#beginner) et [avancés](#advanced) pour en savoir plus !

## Débutant

Voici quelques cas d'utilisation simples mais efficaces que vous pouvez créer peu de temps après avoir configuré Shopify. Aucun travail supplémentaire n'est requis. 

### Campagnes

Ces cas d'utilisation transactionnels vous permettent d'alerter vos utilisateurs lorsqu'une mise à jour est apportée à leur commande Shopify.

{% tabs local %}
{% tab Remboursement %}
**Événement de remboursement Shopify** - `shopify_created_refund`

Les utilisateurs ont reçu un remboursement, partiel ou complet. Cette campagne permet à l'utilisateur de savoir que sa commande a été remboursée avec succès.

![Campagne basée sur l'action qui saisit les utilisateurs qui organisent l'événement personnalisé « shopify_created_refund ». ]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Exemple de messagerie**

![E-mail avec le texte « Votre commande a été remboursée. Nous sommes désolés que votre commande ne vous ait pas apporté entière satisfaction. Nous avons envoyé votre remboursement avec succès. Veuillez attendre 3 à 5 jours ouvrables pour que les fonds apparaissent sur votre relevé » et un bouton « Afficher le compte ». ]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Annulation %}
**Événement d'annulation Shopify** - `shopify_cancelled_order`

Les utilisateurs ont pu annuler leurs commandes avant leur traitement. Cette campagne permet à l'utilisateur de savoir que son achat a été annulé avec succès. 

![Campagne basée sur l'action qui saisit les utilisateurs qui réalisent l'événement personnalisé « shopify_cancelled_order ». ]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Exemple de messagerie**

![E-mail avec le texte « Votre commande a été annulée. Nous sommes désolés de vous voir partir ! Nous avons annulé votre commande avec succès. Veuillez attendre 3 à 5 jours ouvrables pour que les fonds apparaissent sur votre relevé » et un bouton « Afficher le compte ». ]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Commande exécutée %}
**Événement réalisé par Shopify** - `shopify_fulfilled_order`

Tous les articles de la commande d'un utilisateur ont été traités avec succès. Cette campagne permet à l'utilisateur de savoir que l'intégralité de sa commande a été traitée.

![Campagne basée sur l'action qui permet de saisir les utilisateurs qui réalisent l'événement personnalisé « shopify_fulfillment led_order ». ]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Exemple de messagerie**

![Message avec le texte « Votre commande a été traitée ! Tous les articles de votre panier ont été livrés ! Accédez à votre compte et confirmez la réception. Des points bonus pour avoir laissé des commentaires. « ] ({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Commande partiellement exécutée %}
**Événement Shopify partiellement réalisé** - `shopify_partially_fulfilled_order`

Certains articles de la commande d'un utilisateur ont été traités avec succès. Cette campagne permet aux utilisateurs de savoir qu'une partie de la totalité de leur commande a été traitée.

![Campagne basée sur l'action qui saisit les utilisateurs qui réalisent l'événement personnalisé « shopify_partially_fulfillment led_order ». ]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Exemple de messagerie**

![Message avec le texte « Votre commande a été partiellement traitée ! Nous avons livré certains articles de votre commande et les autres sont en route ! Nous vous enverrons une autre alerte lorsque la livraison sera complète. « ] ({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Commande payée %}
**Événement de commande payante Shopify** - `shopify_paid_order`

L'utilisateur paie sa commande et le statut de la commande passe à Payée. Cette campagne permet à l'utilisateur de savoir que son paiement par carte de crédit a été capturé ou que la commande a été marquée comme payée en cas de paiement manuel.

![Campagne basée sur l'action qui saisit les utilisateurs qui réalisent l'événement personnalisé « shopify_paid_order ». ]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Exemple de messagerie**

![E-mail avec le texte « Nous avons reçu votre paiement ! Woohoo, votre commande a été payée ! Veuillez attendre 1 à 2 jours ouvrables pour que nous puissions traiter le paiement et préparer vos articles. Ensuite, nous l'expédierons !» ainsi qu’un bouton « Afficher le compte ». ]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvas

{% tabs local %}
{% tab Canvas de paiement abandonné %}

**Canvas de paiement abandonné**

Les utilisateurs abandonnent le processus de paiement et ne parviennent pas à effectuer leurs transactions avant de partir. Ce Canvas vous permet d'envoyer des rappels automatisés aux utilisateurs qui n'ont pas terminé leurs transactions afin de les ramener dans le flux de paiement.

Événement d'entrée basé sur l'action : `shopify_abandoned_checkout`<br>
Événement exceptionnel : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Canvas après achat %}

**Canvas après achat**

Les utilisateurs ont effectué un achat avec succès et vous voulez maintenant savoir s'ils ont apprécié leur achat. Ce canevas vous permet d'envoyer des messages de suivi à votre utilisateur pour recueillir ses commentaires. 

Événement d'inscription basé sur l'action : ou achat `shopify_created_order`

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Avancé

Une fois que vous vous êtes familiarisé avec la plateforme, vous pouvez configurer des cas d'utilisation plus complexes.

### Campagnes

{% tabs local %}
{% tab Recommandations aux utilisateurs %}
**Recommandations aux utilisateurs**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

L'utilisateur a cliqué ou consulté un article mais ne l'a pas acheté. Cette campagne envoie un message de suivi à l'utilisateur proposant des articles identiques ou similaires (recommandés par du contenu connecté) pour l'inciter à les acheter.

Événement de participation basé sur l'action : ou `shopify_product_clicked` `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Événement exceptionnel : `shopify_created_order` ou achat<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Canvas de remboursement et de retour %}

**Canvas de remboursement et de retour**

Les utilisateurs ont reçu un remboursement, partiel ou complet. Ce Canvas envoie des messages de suivi pour inciter l'utilisateur à effectuer à nouveau son achat.

Événement d'entrée basé sur l'action : `shopify_created_refund`<br>
Événement exceptionnel : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Canvas d'annulation de reconquête %}

**Canvas d'annulation de reconquête**

Les utilisateurs ont pu annuler leurs commandes avant leur traitement. Ce Canvas envoie des messages de suivi pour inciter l'utilisateur à effectuer à nouveau son achat.

Événement d'entrée basé sur l'action : `shopify_cancelled_order`<br>
Événement exceptionnel : `shopify_created_order` ou achat

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}