---
nav_title: "Création d'un modèle de webhook"
article_title: "Création d'un modèle de webhook"
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "Cet article de référence explique comment créer et personnaliser des modèles de webhook en vue d'une utilisation ultérieure au sein de la plateforme Braze."

---

# Création d'un modèle de webhook

> Au fur et à mesure que vous créez et personnalisez vos webhooks, vous pouvez créer et exploiter des modèles de webhooks pour une utilisation ultérieure au sein de la plateforme Braze. De cette façon, vous pouvez créer de manière cohérente une variété de webhooks à travers vos différentes campagnes.

## Étape 1 : Accédez à l'éditeur de modèles de webhook

Dans le tableau de bord de Braze, allez dans **Modèles** > **Modèles de webhook**.

La page "Modèles de webhook" contient des modèles de webhook prédéfinis et enregistrés.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Étape 2 : Choisissez votre modèle

À partir de là, vous pouvez choisir de créer un nouveau modèle, d'utiliser l'un des modèles de webhook prédéfinis ou de modifier un modèle existant.

Par exemple, si vous utilisez [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) comme canal de communication, vous pouvez configurer plusieurs webhooks à l'aide des modèles prédéfinis pour **LINE Carousel** ou **LINE Image.**

## Étape 3 : Remplir les détails du modèle

1. Donnez un nom unique à votre modèle de webhook.
2. (Facultatif) Ajoutez une description du modèle pour expliquer comment ce modèle est destiné à être utilisé.
3. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire pour faciliter la recherche et le filtrage de votre modèle.

## Étape 4 : Créez votre modèle

1. Saisissez l'URL du webhook.
2. Sélectionnez la méthode HTTP.
3. Ajoutez un corps de requête. Il peut s'agir de **paires clé-valeur JSON** ou de **texte brut**.
4. (Facultatif) Ajoutez un en-tête de requête. Cela peut être exigé par la destination de votre webhook.

\![L'onglet "Compose" lors de la création d'un modèle de webhook. Les champs disponibles sont l'URL du webhook, la méthode HTTP, le corps de la demande et les en-têtes de la demande. Vous pouvez également ajouter des langues.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Étape 5 : Testez votre modèle

Pour voir à quoi ressemble votre webhook avant de l'envoyer à vos utilisateurs, vous pouvez envoyer un webhook test à l'aide de l'onglet **Test.**  Ici, vous pouvez choisir de prévisualiser le message en tant qu'utilisateur aléatoire, utilisateur existant ou utilisateur personnalisé.

## Étape 6 : Enregistrez votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle.** Vous êtes maintenant prêt à utiliser ce modèle dans la campagne de votre choix.

{% alert note %}
Les modifications apportées à un modèle existant ne sont pas répercutées dans les campagnes créées à l'aide de versions antérieures de ce modèle.
{% endalert %}

## Gérer vos modèles

Vous pouvez [dupliquer et archiver des]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles de webhook pour mieux organiser et gérer votre liste de modèles.

Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

