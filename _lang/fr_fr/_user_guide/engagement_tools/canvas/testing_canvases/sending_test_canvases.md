---
nav_title: "Envoi de toiles d'essai"
article_title: "Envoi de toiles d'essai"
page_order: 1
description: "Cet article de référence traite de la manière de tester un canvas avant son lancement et des meilleures pratiques."
page_type: reference
tool: Canvas
---

# Envoi de toiles d'essai

> Après avoir [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), vous pouvez effectuer plusieurs vérifications avant de le lancer, en fonction de détails tels que la taille de votre audience ou le nombre de filtres de segmentation.

Dans la mesure du possible, Braze recommande de tester une toile avant de la lancer. Ce test se déroule généralement dans votre environnement Braze. Tester votre Canvas peut impliquer de le dupliquer, d'emmener les utilisateurs tests à travers le parcours de l'utilisateur et de vérifier si le comportement de l'utilisateur s'aligne sur ce que vous avez décrit dans votre Canvas.

## Étape 1 : Créez votre plan de test

La création d'un plan de test est essentielle avant de commencer à tester votre Canvas. Un plan de test peut aider à identifier et à suivre des domaines spécifiques de votre parcours Canvas.

Lorsque vous créez votre plan de test, posez-vous les questions suivantes :
- Un utilisateur au moins a-t-il été créé pour chaque branche et chaque chemin de Canvas ?
- Des segments sont-ils utilisés dans votre canvas ? 
	- Si des segments sont utilisés, il peut y avoir des conditions préalables pour qu'un utilisateur tombe dans le Canvas avant d'être éligible pour un parcours utilisateur.
- Les messages du Canvas de test comportent-ils dans leur titre des éléments liquides qui renvoient à l'ID ou à l'adresse e-mail de l'utilisateur, afin de faciliter l'identification du message et de l'utilisateur à des fins de test ?

## Étape 2 : Identifier les utilisateurs test

Ensuite, identifiez un ensemble d'utilisateurs test qui passeront par les étapes du canvas sans réellement envoyer de messages à vos utilisateurs cibles. Les utilisateurs test peuvent être soit des adresses e-mail existantes qui ne sont pas utilisées pour des services réels sur votre tableau de bord de Braze, soit de nouvelles adresses e-mail utilisées exclusivement à des fins de test. 

## Étape 3 : Mettez en place votre Canvas

Ensuite, il est temps de tester votre Canvas ! Pour que les informations de votre Canvas original et de votre Canvas de test restent organisées, créez un double de votre Canvas à des fins de test.

Vous pouvez tester votre Canvas de deux manières. 

- **Méthode 1 :** Dans le canevas dupliqué, modifiez la segmentation d'**audience** du générateur de canevas afin que seuls les utilisateurs test soient éligibles pour le canevas. Vous pouvez également saisir votre propre adresse e-mail en tant qu'utilisateur test en ajoutant le filtre de test **Adresse e-mail.**  Dans l'exemple ci-dessous, nous avons limité le Canvas à deux utilisateurs test qui ont utilisé l'application pour la première fois il y a moins de trois jours.

!Un canvas dont l'audience d'entrée est "Première utilisation de ces applications il y a moins de 3 jours" et les adresses e-mail de deux utilisateurs test.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Méthode 2 :** [Prévisualisez vos parcours utilisateurs]({{site.baseurl}}/preview_user_paths/) en sélectionnant le bouton **Test Canvas** dans le pied de page du générateur de Canvas.

## Étape 4 : Lancez votre test

Lancez votre Canvas de test pour permettre aux utilisateurs de commencer à entrer. Complétez les comportements de l'utilisateur sur votre application qui enverraient les utilisateurs à travers le parcours Canvas respectif.

Vérifiez que les utilisateurs test reçoivent bien les messages prévus par les étapes du canvas. Notez que vos utilisateurs test peuvent ne pas recevoir de message pour des raisons diverses :

- Non éligible pour le groupe de contrôle global
- Limites de fréquence
- Mauvaise correspondance entre les membres du segmentation
- Envois de messages interrompus
- Jetons de poussée associés à différents utilisateurs

Continuez à itérer les tests de canvas pour vous assurer que votre canvas fonctionne comme prévu.

## Conseils généraux

### Identifiez vos étapes du canvas

Dans certains cas, un utilisateur peut potentiellement recevoir plusieurs messages lorsqu'il parcourt un Canvas. Si le délai entre les étapes a été considérablement réduit pour les tests, il n'est pas toujours évident de savoir quel message est déclenché pendant les tests. En veillant à ce que les messages test comprennent le nom de l'étape ou l'ID de l'utilisateur (en utilisant Liquid), il sera plus facile d'identifier et de confirmer si le bon message a été envoyé aux bons utilisateurs.

### Créer un groupe interne

Au lieu de créer des utilisateurs test individuels, vous pouvez créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), c'est-à-dire un groupe interne dont l'objectif est d'examiner le contenu de votre message. Il s'agit d'un groupe d'utilisateurs qui recevront des messages test des campagnes et des toiles. Vous pouvez ensuite ajouter ce groupe de test dans le champ **Ajouter des groupes de test de contenu** sous **Destinataires du test**.

### Réduire les délais

Pour améliorer l'efficacité des tests, nous vous conseillons de réduire les délais à quelques minutes ou secondes pour les tests, afin que vous puissiez consulter les messages en temps voulu. Par exemple, prévoyez au moins 2 à 3 minutes entre les tests pour pouvoir isoler des actions spécifiques à des parcours Canvas spécifiques.

### Exploiter les blocs de contenu

Si un contenu doit être répété dans votre cadre de test (par exemple, un liquide complexe pour filtrer les utilisateurs dans différentes étapes du canvas), essayez d'enregistrer ce contenu répété en tant que [bloc de contenu.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) Vous pouvez désormais inclure le bloc de contenu dans les différentes étapes du canvas.

### Utiliser Postman et l'endpoint Track user

Vous pouvez exécuter des tests avec Postman et la [collection Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer et suivre les événements personnalisés et les achats de vos différents utilisateurs test.

Notez que l'envoi de données à l'API de suivi des utilisateurs ne peut se faire qu'avec un ID externe. Ainsi, il peut être nécessaire d'ajouter des utilisateurs test au sein d'un groupe interne dans le tableau de bord de Braze afin que des erreurs spécifiques puissent faire l'objet d'une enquête plus approfondie. 

#### Test pour les branches multiples

Lorsque vous testez un canvas comportant plusieurs branches qui ciblent les utilisateurs en fonction de différents attributs et événements, suivez ce plan de test :

1. Pour chaque branche, identifiez les attributs et les événements que l'utilisateur doit avoir pour être inclus dans le parcours Canvas.
2. Créez des données JSON qui seront envoyées à l'aide de l'endpoint `/users/track`.

