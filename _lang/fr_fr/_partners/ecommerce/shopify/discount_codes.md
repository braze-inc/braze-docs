---
nav_title: Codes de réduction uniques 
article_title: Envoi de codes de réduction uniques
alias: /shopify_discount_codes/
page_order: 6
description: "Cet article de référence couvre un cas d'utilisation soumis par la communauté qui consiste à utiliser les codes de promotion Braze avec le Shopify Bulk Discount Code Bot pour envoyer des codes de promotion uniques par le biais de vos campagnes et Canvases."
---

# Envoi de codes de réduction uniques via Shopify

> Ce cas d'utilisation soumis par la communauté montre comment utiliser les [codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) Braze avec le Shopify Bulk Discount Code Bot pour générer des codes de réduction uniques pour vos campagnes et vos toiles. Des codes de promotion uniques permettent d'éviter l'exploitation de codes de promotion génériques.

{% alert important %}
Il s'agit d'une intégration proposée par la communauté et qui n'est pas directement prise en charge par Braze. Le Bulk Discount Code Bot est directement pris en charge par Shopify. Seuls les codes de promotion de Braze sont pris en charge par Braze.
{% endalert %}

## Conditions

| Exigence | Description |
| --- | --- |
| Créer une boutique Shopify | Confirmez que vous avez déjà [configuré une boutique Shopify avec Braze]({{site.baseurl}}/shopify_overview/). |
| Installez l'application Bulk Discount Code Bot | Téléchargez l'app [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) dans la boutique d'applications de Shopify. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Générer des codes de réduction uniques

### Étape 1 : Configurez vos codes de réduction

Utilisez le Bulk Discount Code Bot pour configurer vos codes de réduction en fonction du nombre de codes à générer, de la longueur du code, de la valeur de la réduction, etc.

![Les options de configuration d'un ensemble de remises.][1]

### Étape 2 : Exporter vos codes

Trouvez votre jeu de codes de réduction dans la barre de recherche du Bulk Discount Code Bot, puis sélectionnez **Exporter** les codes > **Télécharger les codes** pour télécharger un fichier CSV dans votre dossier Téléchargements.

![Barre de recherche avec une liste déroulante affichant l'ensemble des remises et une rangée de boutons à sélectionner.][2]{: style="max-width:70%;"}

Dans le fichier CSV, supprimez la ligne 1 pour supprimer l'en-tête de colonne "Promo". Cela évitera que "Promo" ne devienne un code de réduction dans Braze.

![Organigramme montrant la suppression de l'en-tête de ligne "Promo" dans un fichier CSV.][3]{: style="max-width:60%;"}

### Étape 3 : Ajoutez vos codes de réduction à Braze

Dans Braze, allez dans **Paramètres des données** > **Codes promotionnels** > **Créer une liste de codes promotionnels** et [configurez votre liste de codes de réduction]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Veillez à respecter la date d'expiration configurée par le Bulk Discounts Code Bot.

Téléchargez ensuite votre fichier CSV et sélectionnez **Enregistrer la liste**.

### Étape 4 : Ajoutez vos codes de réduction à une campagne Braze ou à une étape du canvas.

Si vous souhaitez utiliser vos codes de réduction uniques dans une campagne à envoi unique, ou si vous ne voyez pas d'inconvénient à ce que les utilisateurs reçoivent plusieurs codes uniques dans différentes campagnes ou étapes du Canvas, copiez l'extrait de code Liquid du code dans la liste des codes de promotion que vous avez enregistrée.

![Un extrait de code liquide avec un bouton pour le copier.][4]{: style="max-width:60%;"}

Collez l'extrait de code liquide dans une campagne ou une étape du canvas. 

![Un GIF montrant l'extrait de code Liquid ajouté à une étape du canvas.][5]

Si vous souhaitez que les utilisateurs reçoivent un code de réduction unique, quel que soit le nombre de fois où le code de réduction est référencé dans les campagnes ou les canevas, créez une étape de [mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) directement avant la première étape de message qui attribue le code de réduction à un attribut personnalisé, tel que "Code promo".

{% alert tip %}
Vous pouvez également [créer un attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) en allant dans **Paramètres des données** > **Attributs personnalisés**.
{% endalert %}

Dans l'étape de mise à jour de l'utilisateur, procédez comme suit pour chaque champ :
- **Nom de l'attribut :** Sélectionnez le **code promo**.
- **Action :** Sélectionnez **Mise à jour**.
- **Valeur clé :** Collez l'extrait de code Liquid.

![Une étape de mise à jour de l'utilisateur qui met à jour un attribut "Code promo" avec l'extrait de code liquide.][6]

Désormais, vous pouvez ajouter l'attribut personnalisé {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} à n'importe quel message, et le code de réduction sera intégré dans le modèle.

## Comportement du code de réduction

{% details Campagne multicanal ou étape du canvas %}

Lorsqu'un extrait de code de réduction est utilisé dans une campagne multicanal ou une étape du canvas, les utilisateurs reçoivent toujours un code unique. Si un utilisateur peut recevoir un code par plusieurs canaux, il recevra le même code par chaque canal. En d'autres termes, un utilisateur éligible ne recevra qu'un seul code pour tous les messages envoyés par cette campagne ou cette étape du canvas.

{% enddetails %}

{% details Différentes étapes du canvas ou des campagnes distinctes %}

Lorsqu'un code de réduction est référencé par plusieurs étapes du même Canvas ou par des campagnes distinctes, un utilisateur éligible recevra plusieurs codes de promotion uniques (un code pour chaque étape du Canvas ou chaque campagne).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}