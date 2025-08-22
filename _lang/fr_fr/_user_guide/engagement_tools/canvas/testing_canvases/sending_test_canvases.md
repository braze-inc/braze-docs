---
nav_title: Envoyer des Canvas de test
article_title: Envoyer des Canvas de test
page_order: 1
description: "Cet article de référence explique comment tester un Canvas avant son lancement et les bonnes pratiques."
page_type: reference
tool: Canvas
---

# Envoyer des Canvas de test

> Après avoir [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), vous pouvez effectuer plusieurs vérifications avant de le lancer, en fonction de détails tels que la taille de votre audience ou le nombre de filtres de segmentation.

Braze recommande de tester un Canvas avant son lancement lorsque cela est possible. Ce test aura généralement lieu dans votre environnement Braze. Pour tester votre Canvas, vous pouvez avoir à le dupliquer, à faire suivre le parcours utilisateur à vos utilisateurs de test et à vérifier si le comportement utilisateur est cohérent avec celui décrit dans votre Canvas.

## Étape 1 : Créer votre plan de test

Il est fondamental de créer un plan de test avant de commencer à tester votre Canvas. Un plan de test peut aider à identifier et à suivre des zones données de votre parcours Canvas.

Au fur et à mesure que vous construisez votre plan de test, envisagez les questions suivantes :
- Est-ce qu’au moins un utilisateur a été créé pour chaque branche ou parcours de votre Canvas ?
- Est-ce que votre Canvas utilise des segments ? 
	- Si des segments sont utilisés, un utilisateur peut être confronté à des prérequis pour entrer dans votre Canvas avant de devenir éligibles à un parcours utilisateur.
- Est-ce que les messages dans le Canvas de test comprennent du Liquid dans les titres de message qui extraient l’ID utilisateur ou l’adresse e-mail pour s’assurer que le message et l’utilisateur peuvent être facilement identifiés à des fins de test ?

## Étape 2 : Identifier des utilisateurs test

Ensuite, identifiez un ensemble d'utilisateurs test qui suivront les étapes de Canvas sans réellement envoyer de messages aux utilisateurs prévus. Les utilisateurs test peuvent être des adresses e-mail existantes qui ne sont pas utilisées pour des services sur votre tableau de bord de Braze ou de nouvelles adresses e-mail réservées à des fins de test. 

## Étape 3 : Configurer votre Canvas

Il est ensuite temps de tester vos Canvas ! Pour organiser votre Canvas d’origine et tester les informations Canvas, créez un double de votre Canvas à des fins de test.

Vous pouvez tester votre Canvas de deux manières. 

- **Méthode 1  :** Dans le canvas dupliqué, modifiez la partie **Audience d’entrée** du générateur de canvas afin que seuls les utilisateurs test soient éligibles pour le canvas. Vous pouvez également saisir votre propre adresse e-mail en tant qu'utilisateur test en ajoutant le filtre de test **Adresse e-mail.** Dans l’exemple ci-dessous, nous avons limité le Canvas à deux utilisateurs test qui ont utilisé l’application pour la première fois il y a moins de 3 jours. 

![Un canvas dont l'audience d'entrée est "Première utilisation de ces applications il y a moins de 3 jours" et les adresses e-mail de deux utilisateurs test.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **Méthode 2 :** [Prévisualisez vos parcours utilisateurs]({{site.baseurl}}/preview_user_paths/) en sélectionnant le bouton **Test Canvas** dans le pied de page du générateur de Canvas.

## Étape 4 : Lancer votre test

Lancez votre Canvas de test pour permettre à vos utilisateurs de commencer à y entrer. Complétez les comportements de l'utilisateur sur votre application qui enverraient les utilisateurs à travers le parcours Canvas respectif.

Vérifiez que vos utilisateurs de test reçoivent bien les messages attendus de vos étapes Canvas. Prenez en compte le fait que vos utilisateurs de test peuvent ne pas recevoir un message pour, entre autres, les raisons suivantes :

- Non éligible pour le groupe de contrôle global
- Limitations de la limite de fréquence
- Appartenance à un segment non concordant
- Messages abandonnés
- Jetons de notification push associés à des utilisateurs différents

Continuez à itérer les tests du canvas pour vous assurer que votre canvas fonctionne comme prévu.

## Conseils généraux

### Identifier vos étapes de Canvas

Dans certains cas, un utilisateur peut potentiellement recevoir plusieurs messages lorsqu’il progresse dans un Canvas. Si le délai entre les étapes a été considérablement réduit pour les tests, il se peut que le message déclenché pendant les tests ne soit pas toujours clair. S’assurer que les messages test, y compris le nom de l’étape ou l’ID utilisateur (à l’aide de Liquid), faciliteront l’identification et la confirmation que le bon message a été envoyé aux utilisateurs appropriés.

### Créer un groupe interne

Au lieu de créer des utilisateurs test individuels, vous pouvez créer un [groupe de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), c'est-à-dire un groupe interne dont l'objectif est d'examiner le contenu de votre message. Cela inclut un groupe d’utilisateurs qui recevront des messages test des campagnes et des Canvas. Vous pouvez ensuite ajouter ce groupe de test dans le champ **Ajouter des groupes de test de contenu** sous **Destinataires du test**.

### Délais réduits

Pour faciliter une exécution plus efficace de vos tests, nous vous conseillons, pour afficher les messages à une vitesse raisonnable, de réduire les délais à quelques minutes ou secondes à des fins de test. Par exemple, autorisés au moins 2 ou 3 minutes entre les tests pour pouvoir isoler des actions spécifiques dans les parcours Canvas donnés.

### Tirer parti des blocs de contenu

Si un contenu doit être répété dans votre cadre de test (par exemple, un Liquid complexe pour filtrer les utilisateurs dans différentes étapes de canvas), essayez d'enregistrer ce contenu répété en tant que [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Maintenant, vous pouvez inclure le bloc de contenu dans les différentes étapes de Canvas.

### Utiliser Postman et l'endpoint Suivi utilisateur

Vous pouvez exécuter des tests avec Postman et la [collection Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer et suivre les événements personnalisés et les achats de vos différents utilisateurs test.

Prenez en compte le fait qu’envoyer des données à l’API de suivi des utilisateurs ne peut être réalisé qu’avec un ID externe. Les utilisateurs de test peuvent devoir être ajoutés en tant qu’utilisateurs de test dans un groupe interne dans le tableau de bord de Braze pour que des erreurs données puissent être étudiées. 

#### Tester plusieurs branches

Lorsque vous testez un Canvas avec plusieurs branches ciblant les utilisateurs selon divers attributs ou événements, suivez ce plan de tes :

1. Pour chaque branche, identifiez les attributs et les événements que l’utilisateur doit posséder pour être inclus dans le parcours Canvas.
2. Intégrez-les dans la charge utile JSON pour être publiés en utilisant l’endpoint `/users/track`.

