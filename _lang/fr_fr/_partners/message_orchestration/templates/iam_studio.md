---
nav_title: IAM Studio
article_title: IAM Studio
description: "Cet article de référence décrit le partenariat entre Braze et IAM Studio, une plateforme de personnalisation de message qui vous permet de créer des expériences personnalisées et riches dans l'application et de les diffuser via Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# IAM Studio

> [IAM Studio](https://www.inappmessage.com) est une plateforme de personnalisation de message sans code qui vous permet de créer des expériences personnalisées et riches dans l'application et de les diffuser via Braze.

_Cette intégration est maintenue par IAM Studio.\*s._

## À propos de l'intégration

L'intégration de Braze et d’IAM Studio, vous permet de facilement insérer des modèles de message in-app personnalisables dans vos messages in-app Braze, afin de rendre possible le remplacement d'image, la modification de texte, la définition de paramètres de lien profond, d’attributs personnalisés et de paramètres d'événement. En utilisant IAM Studio, vous pouvez réduire le temps de production de message et consacrer plus de temps à la planification du contenu. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| compte IAM Studio | Un [compte IAM Studio](https://www.inappmessage.com/register) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d'utilisation

- Encourager l'achat de biens
- Collecte d'informations utilisateur
- Augmentation du nombre de membres inscrits
- Informations sur l'émission de coupons

## Intégration

### Étape 1 : Choisissez un modèle

Choisissez un modèle de message in-app que vous souhaitez utiliser dans la galerie de modèles de messages in-app

![La galerie de modèles d'IAM Studio présente différents modèles tels que "carousel slide modal", "simple icon modal", "modal full image", et bien d'autres encore.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Étape 2 : Personnaliser le modèle

Tout d'abord, personnalisez l'image, le texte et le bouton de votre contenu. Assurez-vous de connecter **Deeplink** pour l'image et le bouton.

{% tabs local %}
{% tab Image %}
![L'interface utilisateur de IAM Studio montrant les options pour personnaliser l'image. Ces options incluent l'image, le rayon de l'image et l'image atténuée.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Texte %}
![L'interface utilisateur de IAM Studio montrant les options pour personnaliser le titre et le sous-titre de votre message. Ces options incluent le texte, la mise en forme et la police.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Bouton %}
![L'interface utilisateur de IAM Studio montrant les options pour personnaliser le bouton principal, gauche et droit. Ces options incluent la couleur, le lien profond, le texte et la mise en forme.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Ensuite, créez votre message in-app personnalisé en ajoutant des polices personnalisées et en utilisant des tags liquid. Pour activer la journalisation et le suivi, sélectionnez **Journaliser les données et suivre le comportement des utilisateurs**.

{% tabs local %}
{% tab Polices %}
![L'interface utilisateur IAM Studio montrant les options pour ajouter du liquid. Ces options comprennent l'élaboration de phrases personnalisées.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![L'interface utilisateur de IAM Studio montrant les options pour personnaliser la journalisation des événements/attributs. Ces options incluent ce journal de comportement des utilisateurs.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Journalisation et suivi %}
![L'interface utilisateur de IAM Studio montrant les options pour personnaliser la police. Ces options incluent une option permettant à l'utilisateur de personnaliser le style de police.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png  %})
{% endtab %}
{% endtabs %}

### Étape 3 : Exporter le modèle

Une fois toutes les modifications terminées, exportez le modèle en cliquant sur **Exporter**. Après l'exportation, le code HTML du message in-app sera généré. Copiez ce code en cliquant sur le bouton **Copier le code**. 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Étape 4 : Utilisez code dans Braze 

Accédez à Braze, et dans votre message in-app, collez le code personnalisé dans la boîte **HTML Input**. Assurez-vous de tester votre message pour vérifier qu'il s'affiche correctement.

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


