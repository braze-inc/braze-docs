---
nav_title: Bon de réduction
article_title: Bon de réduction
alias: /fr/partners/voucherify/
description: "Cet article décrit le partenariat entre Braze et Voucherify, une plateforme de promotion tout-en-un qui permet aux utilisateurs d'envoyer automatiquement des coupons personnalisés, cartes-cadeaux, cartes de fidélité, codes de parrainage et plus encore – tout au long de leur compte Braze tout en suivant les remboursements et la croissance de la campagne à chaque étape."
page_type: partenaire
search_tag: Partenaire
---

# Bon de réduction

> [Voucherify](https://www.voucherify.io/) est une plateforme de promotion tout-en-un qui permet des campagnes personnalisées et des programmes de fidélité qui favorisent l'engagement et la fidélisation de l'utilisateur.

L'intégration de Braze et Voucherify vous permet de développer vos campagnes de promotion en envoyant des codes uniques grâce à l'utilisation de :

- [Contenu connecté](#generate-unique-codes-using-connected-content): Ajoutez des codes uniques aux campagnes de Braze via le Contenu connecté de Braze. Grâce à cette fonctionnalité, vous pouvez utiliser des bons de réduction, des campagnes de cartes-cadeaux, des cartes de fidélité et des codes de parrainage.
- [Attributs personnalisés](#assign-unique-codes-to-users-custom-attributes): Les attributs personnalisés vous permettent d'attribuer des bons de réduction, cartes-cadeaux, cartes de fidélité et codes de parrainage vers les profils des utilisateurs en Brésil. Par conséquent, vous pouvez envoyer des codes et des attributs joints dans des campagnes e-mail et les partager avec vos utilisateurs.
- [Liste des codes promotionnels](#upload-voucherify-codes-to-braze-promo-codes-lists): Utilisez les codes promotionnels générés et téléchargez-les dans Braze.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte de bon de réduction | Un compte Voucherify est requis pour profiter de ce partenariat.                                                                                                                                             |
| Braze clé API REST         | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Générer des codes uniques à l'aide du contenu connecté

#### Étape 1 : Construire un bon d'achat de contenu connecté

À partir du tableau de bord de Braze, créez une nouvelle campagne. Dans le corps de l'e-mail, ajoutez le code snippet suivant :

{% raw %}
```
{% assigner campaign_id = {{campaign.${api_id}}} %}
{% assigner customer_id = {{${user_id}}} %}
{% assigner source_id = campaign_id | ajouter: customer_id %}

{% connected_content
    https://api. « oucherif. » o/v1/publications
    :method post
    :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    }

    :body campaign=CAMPAIGN_ID&customer={{${user_id}}}&channel=Braze&source_id={{source_id}}
    :content_type application/json
    :save publication
%}
```
{% endraw %}

Après avoir copié le code dans le corps du courriel, ajoutez les clés de votre application et `CAMPAIGN_ID` comme décrit ci-dessous :

1. Ajoutez `VOUCHERIFY-APP-ID` et `VOUCHERIFY-APP-TOKEN` à partir des paramètres de votre projet Voucherify sous **Clefs d'application**.<br><br>
2. Remplacez `CAMPAIGN_ID`, vous pouvez trouver l'ID de la campagne dans l'URL de la campagne Voucherify.<br>![ID CAMPAGNE DE VOUCHERIFIE]({% image_buster /assets/img/voucherify-cc-campaignId.png %})<br><br>
3. Enfin, ajoutez {% raw %}`{{publication.voucher.code}}`{% endraw %} au corps de l'e-mail pour afficher le code publié, et sélectionnez **Aperçu et Test**. <br><br>Nous vous conseillons fortement d'envoyer plusieurs messages de test pour confirmer que tout fonctionne comme il se doit.

{% alert important %}
Le paramètre {% raw %}`{{source_id}}`{% endraw %} dans le corps de l'e-mail garantit que chaque client ne recevra qu'un seul code unique dans une seule campagne d'email Braze, et lors du renvoi, recevra le même code. Visitez [Coupon](https://support.voucherify.io/article/113-braze#sourceid) pour modifier ce comportement et voir d'autres configurations.
{% endalert %}

#### Étape 2 : Envoyer et suivre les codes d'utilisateur
![Code publié]({% image_buster /assets/img/voucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Lancez votre campagne Braze pour envoyer des codes à vos utilisateurs, ces codes seront automatiquement assignés à leur profil dans Voucherify.

Lorsqu'un code arrive à l'utilisateur, il est publié dans son profil dans Voucherify.

Si un utilisateur récupère le code, vous verrez les détails de l’échange dans votre tableau de bord de bons d’achat.

![Rachat de code]({% image_buster /assets/img/voucherify-redemption.png %})

{% alert important %}
-   Lorsque vous testez le modèle de courriel, soyez au courant du cache du contenu connecté (au moins 5 minutes). Si vous voulez que chaque prévisualisation de test publie un nouveau coupon, vous pouvez omettre le cache en ajoutant un paramètre de requête à l'URL, e. . {%raw%}`?t=1`{%endraw%}, et incrémentez le nombre à chaque test.<br><br>
-   Lors de la configuration de la publication `source_id`, vous pouvez différencier vos utilisateurs en utilisant deux variables différentes : {%raw%}`${user_id}`{%endraw%} qui est un id externe (vu comme identifiant source dans un profil client dans Voucherify) et {%raw%}`${braze_id}`{%endraw%} qui est un id interne.
{% endalert %}

### Assigner des codes uniques aux attributs personnalisés des utilisateurs

#### Étape 1 : Connectez le compte Voucherify

Pour connecter votre compte Voucherify, visitez le **Répertoire Intégrations** dans votre tableau de bord Voucherify, localisez l'intégration de Braze et ajoutez votre clé API Braze.

![hub d'intégration de Vouhcerify]({% image_buster /assets/img/voucherify-integrations-hub.png %}){: style="largeur-max-70%;"}

#### Étape 2 : Répartition du code

Ensuite, vous devez décider si vous voulez distribuer des codes à Braze en mode manuel ou définir un flux de travail qui déclenche la livraison de code en réponse aux actions de votre utilisateur. Dans les deux situations, Voucherify envoie des codes uniques avec leurs attributs et les assigne comme attributs personnalisés dans les profils des utilisateurs.

![Attributs personnalisés]({% image_buster /assets/img/voucherify-custom-attributes-mapping.png %})

En plus du code unique, vous pouvez également attacher des attributs comme quand le code a été distribué, la valeur du code et les URL qui dirigent le client vers le cockpit, où tous les codes assignés et les récompenses disponibles seront listés.

{% alert important %}
Veuillez noter qu'avant de configurer la distribution, vous devez ajouter vos utilisateurs Braze au tableau de bord de Voucherify. [Rendez-vous ici pour en savoir plus](https://support.voucherify.io/article/67-how-to-import-my-customers).
{% endalert %}

{% tabs %}
{% tab Manual Message %}

Le mode manuel fonctionne comme une action unique qui assigne des codes à un public choisi. Vous pouvez sélectionner un segment des utilisateurs ou un seul utilisateur comme récepteurs et choisir une campagne qui sera une source de codes uniques.

![Mode manuel]({% image_buster /assets/img/voucherify-manual-conditions.png %}){: style="largeur-max-60%;"}

Pour configurer la distribution manuelle avec Braze et Voucherify, [visitez un tutoriel Voucherify étape par étape](https://support.voucherify.io/article/113-braze#CustomAttributes).
{% endtab %}
{% tab Automatic Workflow %}

Définissez un flux de travail automatisé qui délivre des codes à Braze en réponse aux actions entreprises par vos utilisateurs :
-   __Le client a saisi/quitté le segment spécifique du bon de réduction.__
-   __Publication de code réussie__ – le message est envoyé une fois que le code d'une campagne est publié (assigné) à un client dans Voucherify.
-   __Le statut de la commande a changé__ (commande créée, mise à jour de la commande, commande payée, commande annulée).
-   __Crédits cadeaux ajoutés__ – le message est envoyé une fois que des crédits de carte-cadeau sont ajoutés à la carte du client.
-   __Points de fidélité ajoutés__ – le message est envoyé une fois que les points de fidélité sont ajoutés au profil du client.
-   __Bon d’achat__ – le message est envoyé aux clients qui ont encaissé avec succès les bons d’achat.
-   __Annulation du remboursement du bon__ – le message est envoyé au client dont le remboursement a été annulé avec succès.
-   __Rachat de la récompense__ – le message est envoyé lorsqu'un client encaisse une récompense de fidélité ou de parrainage.

Pour configurer un flux de travail automatique avec Braze et Voucherify, [visitez un tutoriel Voucherify étape par étape](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).
{% endtab %}
{% endtabs %}

#### Étape 3 : Utilisez les attributs personnalisés de bon de réduction dans votre campagne Braze

![Attribut personnalisé assigné]({% image_buster /assets/img/voucherify-custom-attribute.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
Quand l'attribut personnalisé avec du code est ajouté, vous pouvez l'utiliser dans les campagnes de Braze. Pour cela, modifiez le corps de votre e-mail et ajoutez {%raw%}`{{custom_attribute.${custom_attribute_with_code}}}`{%endraw%} pour afficher le code unique.<br><br>![Attribut personnalisé dans le corps de l'e-mail]({% image_buster /assets/img/voucherify-custom-attribute-in-email.png %})

Vous pouvez voir le code dans l'aperçu de votre message quand il est prêt. ![email avec un attribut personnalisé de prévisualisation]({% image_buster /assets/img/voucherify-email-preview-custom-attribute.png %})

#### Étape 4: Suivre les codes envoyés dans le bon de réduction

![Code publié]({% image_buster /assets/img/voucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Lancez votre campagne Braze pour envoyer des codes à vos utilisateurs; ces codes seront automatiquement assignés à leur profil dans Voucherify.

Lorsqu'un code arrive à l'utilisateur, il est publié dans son profil dans Voucherify.

Si un utilisateur récupère le code, vous verrez les détails de l’échange dans votre tableau de bord de bons d’achat.

![Rachat de code]({% image_buster /assets/img/voucherify-redemption.png %})

### Télécharger les codes promo dans les listes de codes promo Braze

À côté du contenu connecté et des attributs personnalisés, vous pouvez partager des codes promo en utilisant le snippet Braze Promo Codes.

#### Étape 1 : Exportez des codes uniques de votre campagne Voucherify

Exportez la liste de codes de coupons et éditez le fichier CSV pour supprimer le nom de la colonne pour ne laisser que la liste des codes.

![Rédemption réussie]({% image_buster /assets/img/voucherify-export-Codes.png %})

#### Étape 2 : Créez une liste de codes promotionnels dans Braze

Naviguez vers **Codes de Promotion** et cliquez sur **Créer une Liste de Code Promotion**.

Ensuite, mettez à jour le code snippet Liquid qui sera utilisé pour appeler de la liste. Une fois le message envoyé, ce snippet sera rempli avec un code unique.

![DÉTAILS DE LA LISTE DE LA PROMOTION]({% image_buster /assets/img/voucherify-promotion-codes-details.png %}){: style="largeur-max-70%;"}

Vous pouvez définir des attributs pour des codes tels que l'expiration de la liste et les alertes de seuil. Cependant, notez que Voucherify gère la logique derrière vos codes indépendamment des paramètres de la liste.

Ensuite, téléchargez le fichier CSV avec les codes Voucherify.

![Import CSV]({% image_buster /assets/img/promocodes/promocode6.png %})

Une fois l'import terminé, cliquez sur **Enregistrer**.

#### Étape 3 : Utilisez le code snippet dans votre campagne Braze

Pour utiliser les codes de la liste dans une campagne Braze, copiez le snippet et ajoutez-le au corps de l'e-mail.

![Copier le snippet]({% image_buster /assets/img/voucherify-promotion-list-copy-snippet.png %}){: style="largeur-max-60%;"}

![Lister le code snippet dans l'e-mail]({% image_buster /assets/img/voucherify-promotion-list-snippet-email.png %})

Une fois le message avec le code envoyé, le même code ne sera pas réutilisé.

Si vous avez besoin d'aide pour l'une des étapes ci-dessus, visitez [les codes promotionnels]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
