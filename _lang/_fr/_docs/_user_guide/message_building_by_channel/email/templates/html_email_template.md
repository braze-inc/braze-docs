---
nav_title: Télécharger un modèle d'email
article_title: Comment télécharger un modèle de courriel HTML
page_order: 2.1
description: "Cet article de référence traite de la création, de la gestion et du dépannage d'un modèle de courriel HTML à l'aide du tableau de bord Braze."
tool:
  - Modèles
channel:
  - Email
---

# Comment télécharger un modèle de courriel HTML

> Cet article couvre la création, la gestion et le dépannage des modèles de courriels HTML dans le tableau de bord de Braze.

Les messages électroniques sont parfaits pour diffuser du contenu à l'utilisateur selon ses conditions. Ce sont également de merveilleux outils pour réengager les utilisateurs qui ont même désinstallé votre application. Le tableau de bord de Braze a un éditeur de modèle d'e-mail qui vous permet de créer des e-mails personnalisés et attractifs et de les enregistrer pour une utilisation ultérieure dans des campagnes. Vous pouvez également [créer un modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/) en utilisant notre éditeur.

## Pré-requis {#upload-requirements}

Avant de commencer, vous devez créer votre modèle de courriel HTML. Ce doit être un seul fichier ZIP contenant les éléments suivants :

* Un seul fichier HTML - le corps de votre e-mail
* Un dossier d'images référencées dans le fichier HTML
* Moins de 50 fichiers image

Ce fichier ZIP doit être inférieur à 5 Mo.

## Téléchargement de votre modèle

### Étape 1 : Accédez à l'éditeur de modèle d'e-mail

Allez à la page __Modèles & Médias__ , sous la section __Engagement__. Ceci ouvre la page __Modèles d'e-mail__.

### Étape 2 : Ouvrir le chargeur

Sous la section **Type de gabarit** , sélectionnez **Éditeur HTML**. Faites ensuite défiler vers le bas jusqu'à la section **Commencez à partir d'un modèle HTML de base** et sélectionnez **À partir du fichier**.

### Étape 3 : Téléchargez votre modèle

Cliquez sur **Télécharger à partir du fichier** et sélectionnez votre modèle à partir de votre ordinateur. Reportez-vous à la section [Prérequis](#upload-requirements) pour vous assurer que votre modèle répond aux exigences de téléchargement.

#### Résoudre les erreurs du modèle d'email de téléchargement

Il y a plusieurs messages d'erreur par courriel que vous pouvez recevoir lorsque vous téléchargez un fichier modèle HTML. Si vous recevez une erreur, reportez-vous au tableau ci-dessous pour les problèmes courants et leurs corrections recommandées :

| Erreur                 | Corriger                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .zip de plus de 5 Mo   | Réduisez la taille de votre fichier et essayez de télécharger à nouveau.                                                                                                                                                                                                                                                                                                 |
| .zip corrompu          | Inspectez votre fichier et essayez de le télécharger à nouveau.                                                                                                                                                                                                                                                                                                          |
| HTML manquant          | Ajoutez un fichier HTML à votre fichier ZIP et essayez à nouveau de le télécharger.                                                                                                                                                                                                                                                                                      |
| HTML multiple          | Supprimez l'un des fichiers HTML et essayez de télécharger à nouveau.                                                                                                                                                                                                                                                                                                    |
| Images de plus de 5 Mo | Réduisez le nombre d'images et essayez de télécharger à nouveau.                                                                                                                                                                                                                                                                                                         |
| Images supplémentaires | Il se peut que vous ayez des images supplémentaires dans votre fichier qui ne sont pas référencées dans votre fichier HTML. Cela ne causera pas d'erreur, mais les images supplémentaires seront ignorées. Si ces images étaient censées être référencées dans le fichier HTML, veuillez vérifier son contenu, corriger les erreurs et essayez de télécharger à nouveau. |
| Images manquantes      | S'il y a des images référencées dans votre fichier HTML, mais ces images ne sont pas incluses dans le dossier image du fichier ZIP, vous recevrez une erreur de fichier. Inspectez votre fichier et corrigez toutes les erreurs (comme les erreurs d'orthographe), ou ajoutez les images manquantes à votre fichier ZIP et essayez de télécharger à nouveau.             |
{: .reset-td-br-1 .reset-td-br-2}

### Étape 4 : Terminer et enregistrer votre modèle

Assurez-vous de sauvegarder votre modèle en cliquant sur **Enregistrer le modèle** dans le coin inférieur droit de l'éditeur. Vous êtes maintenant prêt à utiliser ce modèle dans n'importe quelle campagne ou Canvas que vous choisissez.

{% alert note %}
Si vous faites des modifications à un modèle existant, ces modifications ne seront pas reflétées dans les campagnes qui ont été créées en utilisant les versions précédentes de ce modèle.
{% endalert %}

## Utiliser vos modèles dans les campagnes API {#api_for_upload_email_templates}

Pour utiliser votre email pour une campagne API, vous avez besoin d'un `email_template_id`, qui peuvent être trouvés au bas de n'importe quel modèle d'e-mail créé en Brésil.

!\[Section de l'identifiant de l'API d'un modèle d'e-mail HTML\]\[4\]

## Gestion des modèles d'e-mails

Vous pouvez [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) et [archiver]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) modèles d'e-mails ! En savoir plus sur la création et la gestion de modèles et de contenus créatifs dans [Modèles & Médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Foire aux questions

Pour obtenir des réponses aux questions les plus fréquemment posées sur les modèles de courriel, consultez notre page [FAQ][10] sur les modèles d'e-mails et de liens.
[4]: {% image_buster /assets/img_archive/email_template_id.png %}

[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/