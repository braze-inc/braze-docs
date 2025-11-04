---
nav_title: "Téléchargement d'un modèle d'e-mail HTML"
article_title: "Téléchargement d'un modèle d'e-mail HTML"
page_order: 2
description: "Cet article de référence explique comment créer, gérer et résoudre les problèmes d'un modèle d'e-mail HTML à l'aide du tableau de bord de Braze."
tool:
  - Templates
channel:
  - email

---

# Téléchargement d'un modèle d'e-mail HTML

> Le tableau de bord de Braze vous permet de télécharger vos propres modèles d'e-mails HTML et de les enregistrer pour les utiliser ultérieurement dans des campagnes. Vous pouvez également [créer un modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) à l'aide de notre éditeur.

## Conditions préalables {#upload-requirements}

Tout d'abord, vous devez créer votre modèle d'e-mail HTML. Il doit s'agir d'un fichier ZIP contenant les éléments suivants :

* Un seul fichier HTML - le corps de votre e-mail
* Un dossier d'images qui sont référencées dans le fichier HTML
* Moins de 50 fichiers d'images
* Être inférieur à 5 Mo

## Téléchargement de votre modèle

### Étape 1 : Accédez à l'éditeur de modèles d'e-mail

Allez dans la section **Modèles** > **Modèles d'e-mail**.

### Étape 2 : Ouvrez l'uploader

Dans la section **Type de modèle**, sélectionnez **Editeur HTML** et descendez jusqu'à la section **Démarrer à partir d'un modèle HTML de base**. Sélectionnez **From File**.

### Étape 3 : Téléchargez votre modèle

Sélectionnez **Télécharger à partir d'un fichier** et sélectionnez votre modèle sur votre ordinateur. Reportez-vous à la section [Conditions préalables](#upload-requirements) pour vous assurer que votre modèle répond aux exigences de téléchargement.

#### Résolution des problèmes liés aux erreurs de téléchargement des modèles

Vous pouvez recevoir plusieurs messages d'erreur par e-mail lorsque vous téléchargez un fichier de modèle HTML. Si vous recevez une erreur, reportez-vous au tableau suivant pour connaître les problèmes courants et les solutions recommandées :

| Erreur | Fixer |
|------|---|
|.zip plus de 5 MB| Réduisez la taille de votre fichier et essayez de le télécharger à nouveau.|
|.zip corrompu| Inspectez votre fichier et essayez de le télécharger à nouveau. |
|HTML manquant| Ajoutez le fichier HTML à votre fichier ZIP et essayez à nouveau de télécharger.|
|Plusieurs HTML| Supprimez l'un des fichiers HTML et réessayez de télécharger.|
|Images de plus de 5 Mo| Réduisez le nombre d'images et essayez de les télécharger à nouveau. |
|Images supplémentaires| Il se peut que votre fichier contienne des images supplémentaires qui ne sont pas référencées dans votre fichier HTML. Cela ne provoquera pas d'erreur d'échec, mais les images supplémentaires seront rejetées. Si ces images étaient censées être référencées dans le fichier HTML, vérifiez le contenu, corrigez les erreurs éventuelles et essayez de télécharger à nouveau.|
|Images manquantes| Si des images sont référencées dans votre fichier HTML, mais que ces images ne sont pas incluses dans le dossier image du fichier ZIP, vous recevrez une erreur de fichier. Inspectez votre fichier et corrigez les éventuelles erreurs (comme les fautes d'orthographe), ou ajoutez les images manquantes à votre fichier ZIP et essayez à nouveau de le télécharger.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 4 : Terminez et enregistrez votre modèle

Veillez à enregistrer votre modèle en sélectionnant **Enregistrer le modèle.** Vous êtes maintenant prêt à utiliser ce modèle dans la campagne ou la toile de votre choix !

{% alert note %}
Si vous modifiez un modèle existant, ces modifications ne seront pas répercutées dans les campagnes créées à l'aide des versions précédentes de ce modèle.
{% endalert %}

## Utilisation de vos modèles dans les campagnes API {#api_for_upload_email_templates}

Pour utiliser votre e-mail dans le cadre d'une campagne API, vous avez besoin de l'adresse `email_template_id`, qui se trouve au bas de tout modèle d'e-mail créé dans Braze.

!section API Identifier d'un modèle d'e-mail HTML.]({% image_buster /assets/img_archive/email_template_id.png %}){: style="max-width:50%;"}

## Gestion des modèles d'e-mail

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) et [archiver des]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles d'e-mail ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Questions fréquemment posées

Pour obtenir des réponses aux questions fréquemment posées sur les modèles d'e-mail, consultez notre page [FAQ sur les modèles d'e-mail et de lien.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) 


