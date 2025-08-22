---
nav_title: Téléchargement d’un modèle d’e-mail HTML
article_title: Téléchargement d’un modèle d’e-mail HTML
page_order: 2
description: "Le présent article de référence explique comment créer, gérer et réparer un modèle d’e-mail HTML à l’aide du tableau de bord de Braze."
tool:
  - Templates
channel:
  - email

---

# Téléchargement d’un modèle d’e-mail HTML

> Le tableau de bord de Braze vous permet de télécharger vos propres modèles d’e-mail HTML et de les enregistrer pour une utilisation ultérieure dans vos campagnes. Vous pouvez également [créer un modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) à l'aide de notre éditeur.

## Conditions préalables {#upload-requirements}

Tout d'abord, vous devez créer votre modèle d'e-mail HTML. Il doit s'agir d'un fichier ZIP contenant les éléments suivants :

* Un seul fichier HTML : le corps de votre e-mail
* Un dossier d’images référencé dans le fichier HTML
* Moins de 50 fichiers image
* Moins de 5 Mo

## Téléchargement de votre modèle

### Étape 1 : Accéder à l’éditeur de modèles d’e-mail

Allez dans la section **Modèles** > **Modèles d'e-mail**.

### Étape 2 : Ouvrir le téléchargeur

Dans la section **Type de modèle**, sélectionnez **Editeur HTML** et descendez jusqu'à la section **Démarrer à partir d'un modèle HTML de base.** Sélectionnez **Depuis le fichier**.

### Étape 3 : Télécharger votre modèle

Sélectionnez **Télécharger à partir d'un fichier** et sélectionnez votre modèle sur votre ordinateur. Reportez-vous à la section [Conditions préalables](#upload-requirements) pour vous assurer que votre modèle répond aux exigences de téléchargement.

#### Résoudre les problèmes liés aux erreurs de téléchargement de modèles

Vous pouvez recevoir différents messages d’erreur d’e-mail lors du téléchargement d’un fichier de modèle HTML. Si vous recevez un message d’erreur, reportez-vous au tableau suivant pour connaître les problèmes courants et les correctifs recommandés :

| Erreur | Correctif |
|------|---|
|.zip plus de 5 MB| Réduisez la taille de votre fichier et essayez de le télécharger à nouveau.|
|.zip corrompu| Inspectez votre fichier et essayez de le télécharger à nouveau. |
|Fichier HTML manquant| Ajoutez le fichier HTML à votre fichier ZIP et essayez de le télécharger à nouveau.|
|HTML multiple| Supprimez l’un des fichiers HTML et essayez de le télécharger à nouveau.|
|Images de plus de 5 Mo| Réduisez le nombre d’images et essayez de les télécharger à nouveau. |
|Images supplémentaires| Il se peut que votre fichier contienne des images supplémentaires qui ne sont pas référencées dans votre fichier HTML. Cela ne provoque pas de message d’échec, mais les images supplémentaires sont ignorées. Si ces images étaient censées être référencées dans le fichier HTML, vérifiez le contenu, corrigez les erreurs et essayez de les télécharger à nouveau.|
|Images manquantes| Si des images sont référencées dans votre fichier HTML, mais que ces images ne sont pas incluses dans le dossier d’images du fichier ZIP, vous recevrez une erreur de fichier. Inspectez votre fichier et corrigez les erreurs (comme les fautes d’orthographe), ou ajoutez les images manquantes à votre fichier ZIP et essayez de les télécharger à nouveau.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 4 : Terminer et enregistrer votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle.** Vous êtes maintenant prêt à utiliser ce modèle dans toutes les campagnes ou Canvas de votre choix !

{% alert note %}
Si vous apportez des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes créées qui utilisent les versions précédentes de ce modèle.
{% endalert %}

## Utilisation de vos modèles dans les campagnes API {#api_for_upload_email_templates}

Pour utiliser votre e-mail dans une campagne API, vous avez besoin de `email_template_id`, qui se trouve au bas des modèles d’e-mails créés dans Braze.

![Section de l'identifiant API d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gestion des modèles d’e-mail

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) et [archiver des]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles d'e-mail ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Foire aux questions

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre page [FAQ sur les modèles d'e-mail et de lien.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) 


