---
nav_title: Voucherify
article_title: Voucherify
alias: /partners/voucherify/
description: "Cet article présente le partenariat entre Braze et Voucherify, une plateforme promotionnelle tout-en-un qui permet aux utilisateurs d’envoyer automatiquement des coupons personnalisés, des cartes-cadeaux, des cartes de fidélité, des codes de recommandation et plus encore - le tout par le biais du compte Braze tout en suivant les échanges de points et la croissance de la campagne à chaque étape."
page_type: partner
search_tag: Partenaire

---

# Voucherify

{% multi_lang_include video.html id="Xh_c53cBA9w" align="right" %}

> [Voucherify](https://www.voucherify.io/) est une plateforme promotionnelle tout-en-un qui permet de mettre en place des campagnes personnalisées et des programmes de fidélité qui stimulent l’engagement et la rétention des utilisateurs.

L’intégration de Braze et Voucherify vous permet de développer vos campagnes promotionnelles en envoyant des codes uniques grâce à l’utilisation de :

- [Contenu connecté](#generate-unique-codes-using-connected-content) : Ajoutez des codes uniques aux campagnes Braze via le Contenu connecté de Braze. Grâce à cette fonction, vous pouvez utiliser les coupons de réduction de Voucherify, les campagnes de cartes-cadeaux, les cartes de fidélisation et les codes de recommandation.
- [Attributs personnalisés](#assign-unique-codes-to-users-custom-attributes) : Les attributs personnalisés vous permettent d’attribuer des coupons uniques, des cartes-cadeaux, des cartes de fidélisation et des codes de recommandation de Voucherify aux profils des utilisateurs dans Braze. Ainsi, vous pouvez envoyer des codes et des attributs joints dans les campagnes d’e-mail et les partager avec vos utilisateurs.
- [Promotion Codes](#upload-voucherify-codes-to-braze-promo-codes-lists) : Utilisez les codes de promotion de Voucherify et téléchargez-les dans Braze.

## Conditions préalables

| Configuration requise | Description |
| ----------- | ----------- |
|Compte Voucherify | Un compte Voucherify est nécessaire pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br>
<br>
 Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Générer des codes uniques à l’aide du Contenu connecté

#### Étape 1 : Développer un appel de Contenu connecté de Voucherify

Dans le Tableau de bord de Braze, créez une nouvelle campagne. Dans le corps de l’e-mail, ajoutez l’extrait de code suivant :

{% raw %}
```
{% assign campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = campaign_id | append: customer_id %}

{% connected_content
	https://api.voucherify.io/v1/publications
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

Après avoir copié le code dans le corps de l’e-mail, ajoutez vos clés d’application et `CAMPAIGN_ID` :

1. Ajoutez `VOUCHERIFY-APP-ID` et `VOUCHERIFY-APP-TOKEN` à partir des paramètres de votre projet Voucherify sous **Application Keys** (Clés d’application).<br>
<br>

2. Remplacez `CAMPAIGN_ID`, vous pouvez trouver l’ID de la campagne dans l’URL de la campagne Voucherify.<br>
![ID DE CAMPAGNE VOUCHERIFY]({% image_buster /assets/img/voucherify/vvoucherify-cc-campaignId.png %})<br><br>
3. Enfin, ajoutez {% raw %}`{{publication.voucher.code}}`{% endraw %} dans le corps de l’e-mail pour afficher le code publié, et sélectionnez **Preview and Test** (Prévisualiser et tester). <br>
<br>
Nous vous conseillons vivement d’envoyer plusieurs messages de test pour vous assurer que tout fonctionne comme il se doit.

{% alert important %}
Le paramètre {% raw %}`{{source_id}}`{% endraw %} dans le corps de l’e-mail garantit que chaque client ne recevra qu’un seul code unique dans une seule campagne e-mail de Braze, et qu’en cas de renvoi, il recevra le même code. Accédez à [Voucherify](https://support.voucherify.io/article/113-braze#sourceid) pour changer ce comportement et voir d’autres configurations.
{% endalert %}

#### Étape 2 : Envoyer et suivre les codes utilisateur
![Code publié]({% image_buster /assets/img/voucherify/vvoucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Lancez votre campagne Braze pour envoyer des codes à vos utilisateurs, ces codes seront automatiquement attribués à leur profil dans Voucherify.

Lorsqu’un code arrive à l’utilisateur, il est publié dans son profil dans le champ « Voucherify ».

Si un utilisateur échange le code, vous verrez les détails de l’échange dans votre Tableau de bord de Voucherify.

![Échange de code]({% image_buster /assets/img/voucherify/vvoucherify-redemption.png %})

{% alert important %}
-   Lorsque vous testez le modèle d’e-mail, tenez compte du cache du Contenu connecté (au moins 5 minutes). Si vous voulez que chaque aperçu de test publie un nouveau bon, vous pouvez omettre le cache en ajoutant un paramètre de requête à l’URL, par exemple, {%raw%}`?t=1`{%endraw%}, et incrémenter le nombre à chaque test.<br>
<br>

-   En configurant la valeur `source_id` de la publication, vous pouvez différencier vos utilisateurs en employant deux variables différentes : {%raw%}`${user_id}`{%endraw%} qui est un ID externe (vu comme l’ID de la source dans un profil client dans Voucherify), et {%raw%}`${braze_id}`{%endraw%} qui est un ID interne.  
{% endalert %}

### Attribuer des codes uniques aux attributs personnalisés des utilisateurs

#### Étape 1 : Connecter le compte Voucherify

Pour connecter votre compte Voucherify, accédez au **dossier Integrations** (Intégrations) dans votre Tableau de bord de Voucherify, localisez l’intégration Braze, et ajoutez votre clé d’API Braze.

![Plateforme d’intégration de Voucherify]({% image_buster /assets/img/voucherify/vvoucherify-integrations-hub.png %}){: style="max-width:70%;"}

#### Étape 2 : Distribution du code

Ensuite, vous devez décider si vous voulez distribuer les codes à Braze en mode manuel ou définir un flux de travail qui déclenche la livraison des codes en réponse aux actions de votre utilisateur. Dans les deux situations, Voucherify envoie des codes uniques avec leurs attributs et les affecte comme attributs personnalisés dans les profils des utilisateurs.

![Attributs personnalisés]({% image_buster /assets/img/voucherify/vvoucherify-custom-attributes-mapping.png %})

Outre le code unique, vous pouvez également joindre des attributs tels que la date de livraison du code, la valeur du code et des URL qui dirigent le client vers le cockpit, où tous les codes attribués et les récompenses disponibles seront répertoriés.

{% alert important %}
Notez qu’avant de configurer la distribution, vous devez ajouter vos utilisateurs Braze au Tableau de bord de Voucherify. [Cliquez ici pour en savoir plus](https://support.voucherify.io/article/67-how-to-import-my-customers).
{% endalert %}

{% tabs %}
{% tab Manual Message %}

Le mode manuel fonctionne comme une action ponctuelle qui attribue des codes à une audience choisie. Vous pouvez sélectionner un segment d’utilisateurs de Voucherify ou un utilisateur unique comme destinataires et choisir une campagne qui sera une source de codes uniques.

![Mode manuel]({% image_buster /assets/img/voucherify/vvoucherify-manual-conditions.png %}){: style="max-width:60%;"}

Pour configurer la distribution manuelle avec Braze et Voucherify, [reportez-vous au tutoriel étape par étape de Voucherify](https://support.voucherify.io/article/113-braze#CustomAttributes).
{% endtab %}
{% tab Automatic Workflow %}

Définissez un flux de travail automatisé qui fournit des codes à Braze en réponse aux actions entreprises par vos utilisateurs :
-   **Segment de Voucherify spécifique à l’entrée/sortie du client.**
-   **Successful code publication** (Publication de code réussie) – le message est envoyé lorsque le code d’une campagne est publié (attribué) à un client dans Voucherify.
-   **Order status changed** (Statut de commande modifié) – commande créée, mise à jour de la commande, commande payée, commande annulée.
-   **Gift credits added** (Crédits-cadeaux ajoutés) – le message est envoyé lorsque des crédits de carte-cadeau sont ajoutés à la carte du client.
-   **Loyalty points added** (Points de fidélisation ajoutés) – le message est envoyé une fois que les points de fidélisation sont ajoutés au profil du client.
-   **Voucher redeemed** (Bon échangé) – le message est envoyé aux clients qui ont réussi à échanger des coupons.
-   **Voucher redeemed rollback** (Annulation de l’échange du bon) – le message est envoyé aux clients qui ont réussi à annuler l’échange des bons.
-   **Reward redemption** (Échange de récompense) – le message est envoyé lorsqu’un client échange une récompense de fidélisation ou de recommandation.

Pour configurer un flux de travail automatique avec Braze et Voucherify, [reportez-vous au tutoriel étape par étape de Voucherify](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).
{% endtab %}
{% endtabs %}

#### Étape 3 : Utiliser les attributs personnalisés de Voucherify dans votre campagne Braze

![Attribut personnalisé affecté]({% image_buster /assets/img/voucherify/vvoucherify-custom-attribute.png %}){: style="float:right;max-width:30%;margin-left:15px;"}
Lorsque l’attribut personnalisé avec code est ajouté, vous pouvez l’utiliser dans les campagnes Braze. Pour ce faire, modifiez le corps de votre e-mail et ajoutez {%raw%}`{{custom_attribute.${custom_attribute_with_code}}}`{%endraw%} pour afficher le code unique.<br>
<br>
![Attribut personnalisé dans le corps de l’e-mail]({% image_buster /assets/img/voucherify/vvoucherify-custom-attribute-in-email.png %})

Vous pouvez voir le code dans votre aperçu de message quand il est prêt.
![E-mail avec aperçu d’attribut personnalisé]({% image_buster /assets/img/voucherify/vvoucherify-email-preview-custom-attribute.png %})

#### Étape 4 : Suivez les codes envoyés dans Voucherify

![Code publié]({% image_buster /assets/img/voucherify/vvoucherify-cc-code-published.png %}){: style="float:right;max-width:30%;margin-bottom:15px;"}
Lancez votre campagne Braze pour envoyer des codes à vos utilisateurs ; ces codes seront automatiquement attribués à leur profil dans Voucherify.

Lorsqu’un code arrive à l’utilisateur, il est publié dans son profil dans le champ « Voucherify ».

Si un utilisateur échange le code, vous verrez les détails de l’échange dans votre Tableau de bord de Voucherify.

![Échange de code]({% image_buster /assets/img/voucherify/vvoucherify-redemption.png %})

### Télécharger les codes Voucherify dans les listes de codes de promotion Braze

Outre le Contenu connecté et les attributs personnalisés, vous pouvez partager les codes de Voucherify en utilisant l’extrait de code de promotion de Braze.

#### Étape 1 : Exporter des codes uniques depuis votre campagne Voucherify

Exportez la liste des codes Voucherify et modifiez le fichier CSV pour supprimer le nom de la colonne afin de ne laisser que la liste des codes.

![Réussite de l’échange]({% image_buster /assets/img/voucherify/vvoucherify-export-Codes.png %})

#### Étape 2 : Créer une liste de codes de promotion dans Braze

Accédez à **Promotion Codes** (Codes de promotion) et cliquez sur **Create Promotion Code List** (Créer une liste de codes de promotion).

Ensuite, mettez à jour l’extrait de code Liquid qui sera utilisé pour appeler depuis la liste. Une fois le message envoyé, cet extrait de code sera rempli avec un code unique.   

![DÉTAILS DE LA LISTE DE PROMOTION]({% image_buster /assets/img/voucherify/vvoucherify-promotion-codes-details.png %}){: style="max-width:70%;"}

Vous pouvez définir des attributs pour des codes tels que les alertes d’expiration de la liste et les alertes de seuil. Cependant, notez que Voucherify gère la logique derrière vos codes, quels que soient les paramètres de la liste.

Ensuite, téléchargez le fichier CSV avec les codes de Voucherify.

![Importation de CSV]({% image_buster /assets/img/promocodes/promocode6.png %})

Une fois l’importation terminée, cliquez sur **Save** (Enregistrer).

#### Étape 3 : Utiliser l’extrait de code de votre campagne Braze

Pour utiliser des codes dans la liste dans une campagne Braze, copiez l’extrait de code et ajoutez-le au corps de l’e-mail.

![Copie de l’extrait de code]({% image_buster /assets/img/voucherify/vvoucherify-promotion-list-copy-snippet.png %}){: style="max-width:60%;"}

![Extrait de code de liste dans l’e-mail]({% image_buster /assets/img/voucherify/vvoucherify-promotion-list-snippet-email.png %})

Une fois le message envoyé, le même code ne sera pas réutilisé.

Si vous avez besoin d’assistance pour l’une de ces étapes, consultez [Promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) (Codes de promotion).
