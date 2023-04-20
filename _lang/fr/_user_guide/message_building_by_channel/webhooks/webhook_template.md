---
nav_title: Créer un modèle de webhook
article_title: Créer un modèle de webhook
page_order: 2
tool:
  - Templates
channel:
  - Webhooks
description: "Cet article de référence décrit comment créer et personnaliser des modèles de webhooks pour les utiliser par la suite dans la plateforme Braze."

---

# Créer un modèle de webhook

> Cet article de référence décrit comment créer et personnaliser des modèles de webhooks pour les utiliser par la suite dans la plateforme Braze.

## Étape 1 : Vous rendre sur l’éditeur de modèle de webhook

Vous pouvez accéder à l’éditeur de modèle de webhook en cliquant tout d’abord sur l’onglet **Campaigns** dans **Engagement** sur la barre de navigation, ce qui affichera un menu déroulant avec un onglet Modèles et styles.  Cliquez sur cet onglet pour accéder à l’éditeur de modèle de webhook.

![Onglet Modèles de webhook sur la page Modèles et médias du tableau de bord de Braze.][1]

## Étape 2 : Créer un nouveau modèle

Vous pouvez maintenant créer un nouveau modèle, éditer un modèle existant ou utiliser un des modèles de webhook préécrits qui sont proposés.

## Étape 3 : Personnaliser votre modèle

Mes modèles de webhook peuvent être utilisés pour plusieurs cas d’utilisation.  Vous pouvez commencer par saisir un nom de modèle unique à utiliser.  Vous pouvez également rempli l’URL du webhook, le corps de la requête, les en-têtes de la requête et sélectionner la méthode HTTP qui doit être utilisée.

![Onglet Composer lors de la création d’un webhook dans Braze. Les champs disponibles sont la langue, l’URL du webhook et le corps de la requête.][2]{: style="max-width:80%"}

Si vous désirez voir comment s’affiche votre webhook avant de l’envoyer à vos utilisateurs, vous pouvez envoyer un webhook de test depuis l’onglet **Paramètres**.

## Étape 4 : Enregistrer votre modèle

Assurez-vous d’enregistrer votre modèle en cliquant sur le bouton **Enregistrer le modèle**. Vous êtes maintenant prêt à utiliser ce modèle dans toutes les campagnes de votre choix.

![Enregistrer le modèle de webhook][3]{: style="max-width:50%"}

{% alert note %}
Les modifications apportées à un modèle existant ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle.
{% endalert %}

## Gestion des modèles de webhook

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) vos modèles de webhook ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

[1]: {% image_buster /assets/img_archive/webhook_template_campaign.png %}
[2]: {% image_buster /assets/img_archive/Webhook_template_test.png %}
[3]: {% image_buster /assets/img_archive/Webhook_template_save.png %}
