---
nav_title: Générateur de modèles WhatsApp
article_title: Générateur de modèles WhatsApp
description: "Découvrez comment créer, configurer et soumettre des modèles de messages WhatsApp directement dans Braze à l'aide du générateur de modèles WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Générateur de modèles WhatsApp

> Le générateur de modèles WhatsApp vous permet de créer et de soumettre des modèles de messages WhatsApp directement dans Braze, sans avoir à basculer entre Braze et le Meta Business Manager. Une fois votre modèle approuvé par Meta, utilisez-le dans autant de campagnes et de Canvas que vous le souhaitez.

{% alert note %}
Le générateur de modèles WhatsApp est actuellement en accès anticipé. Contactez votre Account Manager Braze pour y accéder.
{% endalert %}

## Conditions préalables

Avant de créer un modèle WhatsApp dans Braze, effectuez la [configuration de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/).

### Modèles carrousel WhatsApp

{% multi_lang_include whatsapp/carousel_template_prerequisites.md %}

## Créer un modèle

### Étape 1 : Accéder aux modèles WhatsApp

Accédez à **Modèles** > **Modèles WhatsApp**, puis sélectionnez **Créer un nouveau modèle**.

![Page des modèles WhatsApp avec un bouton pour créer un nouveau modèle.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Étape 2 : Configurer les paramètres du modèle

Remplissez les champs suivants :

| Champ | Description |
| ----- | ----- |
| **Compte** | Le compte WhatsApp Business (WABA) auquel vous souhaitez soumettre le modèle. Tous les groupes d'abonnement et numéros de téléphone d'un même WABA partagent l'accès aux modèles. |
| **Langue** | La langue de ce modèle. WhatsApp exige un modèle distinct pour chaque langue. |
| **Nom du modèle** | Un nom unique pour votre modèle. Les noms de modèles ne peuvent contenir que des lettres minuscules, des chiffres et des underscores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 3 : Choisir une disposition

Sous **Disposition**, sélectionnez le type de modèle :

- **Par défaut :** Un message WhatsApp standard. C'est la disposition décrite dans cet article.  
- **Carrousel :** Un message avec des cartes défilables horizontalement. Pour en savoir plus, consultez [Modèles carrousel]({{site.baseurl}}/whatsapp_carousel_templates/).

### Étape 4 : Construire votre modèle

#### En-tête (facultatif)

Ajoutez un en-tête qui apparaîtra au-dessus du corps du message. Vous pouvez choisir :

- **Texte :** Un court en-tête textuel.  
- **Média :** Une image, une vidéo ou un document (URL uniquement). Braze stocke la référence média et soumet un échantillon à Meta pour approbation.  
- **Aucun :** Pas d'en-tête 

#### Corps

Saisissez le contenu principal de votre message et personnalisez le corps selon vos besoins en utilisant Liquid ou des variables génériques :

{% raw %}
- Utilisez des étiquettes Liquid (par exemple, `{{${first_name}}}`). Braze enregistre votre Liquid et le restitue lorsque vous utilisez le modèle dans le compositeur d'une campagne ou d'un Canvas.  
- Utilisez des variables génériques, comme des marques substitutives numérotées (par exemple, `{{1}}`), si vous préférez ajouter la personnalisation plus tard lors de la création de votre message.
{% endraw %}

Vous pouvez ajouter de la personnalisation partout où le bouton **+** apparaît. Tous les champs ne prennent pas en charge la personnalisation.

#### Pied de page (facultatif)

Ajoutez un court pied de page qui apparaîtra sous le corps du message.

#### Boutons (facultatif)

Ajoutez jusqu'à 10 boutons à votre modèle. Les types de boutons ont des catégories et des spécifications différentes.

| Type de bouton | Catégorie | Spécifications |
| --- | --- | --- |
| Réponse rapide | Boutons de réponse rapide |{::nomarkdown}<ul><li><b>Nombre maximum :</b> 10</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li></ul> {:/}|
| Numéro de téléphone | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 1</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li><li><b>Numéro de téléphone :</b> Numéro de téléphone valide avec indicatif pays, sans le + (par exemple « 14155552671 »)</li></ul> {:/}|
| Visiter le site web | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 2</li><li><b>Texte du bouton :</b> Jusqu'à 25 caractères</li><li><b>URL du site web :</b> Jusqu'à 2 000 caractères</li></ul> {:/}|
| Copier le code promo | Boutons d'appel à l'action | {::nomarkdown}<ul><li><b>Nombre maximum :</b> 1</li><li><b>Texte du bouton :</b> « Copy offer code » (non modifiable)</li><li><b>Code promo :</b> Jusqu'à 15 caractères</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

![Compositeur de modèles WhatsApp avec des boutons de réponse rapide et d'appel à l'action.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Étape 5 : Prévisualiser votre modèle

Avant de soumettre, prévisualisez l'apparence de votre message pour les destinataires :

- **Prévisualiser en tant qu'utilisateur :** Affichez un aperçu générique du message.  
- **Prévisualiser en tant qu'utilisateur spécifique :** Sélectionnez un profil utilisateur pour prévisualiser le rendu du modèle avec les données de cet utilisateur.

### Étape 6 : Soumettre pour vérification

Sélectionnez **Envoyer** pour soumettre votre modèle à Meta pour vérification. Cette étape prend généralement quelques minutes, mais peut aller jusqu'à 24 heures. Le modèle apparaît sur votre page **Modèles WhatsApp** dès sa soumission, et l'état se met à jour lorsque vous actualisez la page **Modèles WhatsApp**.

## Catégories de modèles prises en charge

Seuls les modèles Marketing sont actuellement pris en charge dans le générateur de modèles WhatsApp.

## Utiliser un modèle approuvé dans une campagne

Une fois votre modèle approuvé par Meta, vous pouvez l'utiliser dans une campagne WhatsApp ou un Canvas.

1. Accédez à **Campagnes** et sélectionnez **Créer une campagne** > **WhatsApp**.  
2. Dans le compositeur de messages, sélectionnez votre modèle approuvé.  
3. Braze renseigne automatiquement le contenu du modèle, y compris les médias et le Liquid que vous avez saisis lors de la création du modèle, pour que vous n'ayez pas à les ressaisir.  
4. Mettez à jour le contenu variable ou la personnalisation selon vos besoins. Les champs verrouillés par Meta (affichés en gris) ne peuvent pas être modifiés. Pour modifier du contenu verrouillé, vous devez éditer et resoumettre le modèle pour approbation.  
5. Utilisez l'onglet **Test** pour prévisualiser le message, mettre à jour les variables du corps et confirmer que le message s'affiche comme prévu avant le lancement.

Pour en savoir plus sur la création de campagnes WhatsApp, consultez [Créer un message WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/).

## Questions fréquentes

### Combien de temps dure la vérification d'un modèle par Meta ?

Les vérifications sont généralement terminées en cinq minutes, mais peuvent prendre jusqu'à 24 heures.

### Puis-je modifier un modèle après son approbation ?

Toute modification du contenu verrouillé (texte du corps ou autres champs contrôlés par Meta) nécessite de resoumettre le modèle pour approbation, ce qui doit être fait depuis le WhatsApp Business Manager. Vous pouvez mettre à jour le contenu et la personnalisation lors de la création de votre campagne ou Canvas.

### Qu'advient-il des modèles soumis avant la disponibilité du générateur de modèles ?

Les modèles créés dans le Meta Business Manager restent disponibles dans Braze. Le générateur de modèles est un moyen supplémentaire de créer et de gérer des modèles sans quitter le tableau de bord de Braze.

### Pourquoi ne puis-je pas ajouter de la personnalisation à tous les champs ?

Meta restreint les parties d'un modèle pouvant être personnalisées. Le bouton **+** n'apparaît que dans les champs qui prennent en charge le contenu variable.