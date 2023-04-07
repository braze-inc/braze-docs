---
nav_title: IAM Studio
article_title: IAM Studio
description: "Cet article de référence présente le partenariat entre Braze et IAM Studio, une plateforme de personnalisation des messages qui vous permet de créer des expériences in-app riches et personnalisées et de les diffuser via Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partenaire

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) est une plateforme de personnalisation de messages sans code qui vous permet de créer des expériences in-app enrichies et personnalisées et de les diffuser via Braze.

Avec l’intégration Braze et IAM Studio, vous pouvez facilement insérer des modèles de messages in-app personnalisables dans vos messages in-app Braze, proposant le remplacement d’image, la modification de texte, les paramètres de lien profond, les attributs personnalisés et les paramètres d’événement. Grâce à IAM Studio, vous pouvez réduire le temps de production des messages et consacrer plus de temps à la planification du contenu. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte IAM Studio | Un [compte IAM Studio](https://www.inappmessage.com/register) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

- Des expériences d'onboarding personnalisées
- Expériences in-app pour des événements personnalisés et des promotions
- Collecte de commentaires et notations des clients en fonction du comportement des applications
- Test rapide des idées potentielles des produits d’application

## Intégration

### Étape 1 : Choisir un modèle

Connectez-vous à IAM Studio et choisissez un modèle de message in-app que vous souhaitez utiliser dans la galerie de modèles de messages in-app.

![La galerie de modèles d’IAM Studio présente différents modèles tels que « modal slick contents », « full survey », « modal full image », et plus encore.][1]

### Étape 2 : Personnaliser le modèle

Ensuite, remplacez les images, le texte et les boutons par le contenu que vous souhaitez.

{% tabs local %}
{% tab Customize Image %}
![L'interface utilisateur d'IAM Studio affichant les options de personnalisation de l'image. Ces options incluent l'image, le rayon de l'image et l'image atténuée.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Customize Text %}
![L'interface utilisateur d'IAM Studio affiche les options permettant de personnaliser le titre et le sous-titre de votre message. Ces options incluent le texte, la mise en forme et la police.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Customize Button %}
![L'interface utilisateur d'IAM Studio affichant les options de personnalisation des boutons principal, gauche et droit. Ces options incluent la couleur, le lien profond, le texte et la mise en forme.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

### Étape 3 : Exporter le modèle

Une fois toutes les modifications terminées, exportez le modèle en cliquant sur **Export (Exporter)**. Après l'exportation, le code HTML du message in-app sera généré. Copiez ce code en cliquant sur le bouton **Copy code (Copier le code)**. 

![][2]{: style="max-width:45%;"}

### Étape 4 : Utiliser le code dans Braze 

Naviguez vers Braze, et dans votre message in-app, collez le code personnalisé dans la zone **HTML Input (Saisie HTML)**. Veillez à tester votre message pour vous assurer qu'il s'affiche correctement.

![][3]{: style="max-width:85%;"}

[1]: {% image_buster /assets/img/iam_studio/iam_template_gallery.png %}
[2]: {% image_buster /assets/img/iam_studio/export_iam_code.png %}
[3]: {% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}