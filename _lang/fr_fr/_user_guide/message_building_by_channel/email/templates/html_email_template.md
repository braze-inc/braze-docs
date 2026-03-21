---
nav_title: "Télécharger un modèle d'e-mail HTML"
article_title: Télécharger un modèle d'e-mail HTML
page_order: 2
description: "Cet article de référence explique comment créer, gérer et résoudre les problèmes liés à un modèle d'e-mail HTML à l'aide du tableau de bord de Braze."
tool:
  - Templates
channel:
  - email

---

# Télécharger un modèle d'e-mail HTML

> Le tableau de bord de Braze vous permet de télécharger vos propres modèles d'e-mail HTML et de les enregistrer pour une utilisation ultérieure dans vos campagnes. Vous pouvez également [créer un modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) à l'aide de notre éditeur.

## Conditions préalables {#upload-requirements}

Commencez par créer votre modèle d'e-mail HTML. Il doit s'agir d'un fichier ZIP contenant les éléments suivants :

* Un seul fichier HTML : le corps de votre e-mail
* Un dossier d'images référencées dans le fichier HTML
* Moins de 50 fichiers image
* Une taille totale inférieure à 5&nbsp;Mo

## Téléchargement de votre modèle

### Étape 1 : Accéder à l'éditeur de modèles d'e-mail

Allez dans **Modèles** > **Modèles d'e-mail**.

### Étape 2 : Ouvrir le téléchargeur

Dans la section **Type de modèle**, sélectionnez **Éditeur HTML** et descendez jusqu'à la section **Démarrer à partir d'un modèle HTML de base**. Sélectionnez **Depuis le fichier**.

### Étape 3 : Télécharger votre modèle

Sélectionnez **Télécharger à partir d'un fichier** et sélectionnez votre modèle sur votre ordinateur. Reportez-vous à la section [Conditions préalables](#upload-requirements) pour vous assurer que votre modèle répond aux exigences de téléchargement.

### Étape 4 : Terminer et enregistrer votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle**. Vous pouvez désormais utiliser ce modèle dans toutes les campagnes ou Canvas de votre choix !

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes créées à partir des versions précédentes de ce modèle.
{% endalert %}

## Utilisation de vos modèles dans les campagnes API {#api_for_upload_email_templates}

Pour utiliser votre e-mail dans une campagne API, vous avez besoin de l'`email_template_id`, qui se trouve en bas de chaque modèle d'e-mail créé dans Braze.

![Section Identifiant API d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gestion des modèles d'e-mail

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) des modèles d'e-mail ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Résolution des problèmes

Plusieurs messages d'erreur peuvent apparaître lors du téléchargement d'un fichier de modèle HTML. Si vous recevez un message d'erreur, consultez le tableau suivant pour connaître les problèmes courants et les correctifs recommandés :

| Erreur | Correctif |
|------|---|
|`.zip de plus de 5&nbsp;Mo`| Réduisez la taille de votre fichier et essayez de le télécharger à nouveau.|
|`.zip corrompu`| Inspectez votre fichier et essayez de le télécharger à nouveau. |
|`Fichier HTML manquant`| Ajoutez le fichier HTML à votre fichier ZIP et essayez de le télécharger à nouveau.|
|`Plusieurs fichiers HTML`| Supprimez l'un des fichiers HTML et essayez de le télécharger à nouveau.|
|`Images de plus de 5&nbsp;Mo`| Réduisez le nombre d'images et essayez de télécharger à nouveau. |
|`Images supplémentaires`| Il se peut que votre fichier contienne des images supplémentaires qui ne sont pas référencées dans votre fichier HTML. Cela ne provoque pas d'erreur bloquante, mais les images supplémentaires sont ignorées. Si ces images étaient censées être référencées dans le fichier HTML, vérifiez le contenu, corrigez les erreurs et essayez de télécharger à nouveau.|
|`Images manquantes`| Si des images sont référencées dans votre fichier HTML mais ne sont pas incluses dans le dossier d'images du fichier ZIP, vous recevrez une erreur. Inspectez votre fichier et corrigez les erreurs (comme les fautes d'orthographe), ou ajoutez les images manquantes à votre fichier ZIP et essayez de télécharger à nouveau.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Notez que lors du téléchargement des fichiers pour les campagnes HTML, les étapes du canvas contenant des messages e-mail ou les modèles sur une machine Windows, le caractère `|` (barre verticale) n'est pas pris en charge. Vous devrez peut-être utiliser une autre application pour extraire le contenu du fichier ZIP.

## Foire aux questions

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre page [FAQ sur les modèles d'e-mail et de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).