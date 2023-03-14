---
nav_title: Envoyer des Canvas de test
article_title: Envoyer des Canvas de test
page_order: 1
description: "Cet article de référence explique comment tester un Canvas avant son lancement et les bonnes pratiques."
page_type: reference
tool: Canvas
---

# Envoyer des Canvas de test

Après avoir [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), vous pouvez effectuer plusieurs vérifications avant le lancement, en fonction de détails tels que la taille de votre audience ou le nombre de filtres de segmentation.

Braze recommande de tester un Canvas avant son lancement lorsque cela est possible. Ce test aura généralement lieu dans votre environnement Braze. Pour tester votre Canvas, vous pouvez avoir à le dupliquer, à faire suivre le parcours utilisateur à vos utilisateurs de test et à vérifier si le comportement utilisateur est cohérent avec celui décrit dans votre Canvas.

## Étape 1 : Créer votre plan de test

Il est fondamental de créer un plan de test avant de commencer à tester votre Canvas. Un plan de test peut aider à identifier et à suivre des zones données de votre parcours Canvas.

Au fur et à mesure que vous construisez votre plan de test, envisagez les questions suivantes :
- Est-ce qu’au moins un utilisateur a été créé pour chaque branche ou parcours de votre Canvas ?
- Est-ce que votre Canvas utilise des segments ? 
	- Si des segments sont utilisés, un utilisateur peut être confronté à des prérequis pour entrer dans votre Canvas avant de devenir éligibles à un parcours utilisateur.
- Est-ce que les messages dans le Canvas de test comprennent du Liquid dans les titres de message qui extraient l’ID utilisateur ou l’adresse e-mail pour s’assurer que le message et l’utilisateur peuvent être facilement identifiés à des fins de test ?

## Étape 2 : Identifier des utilisateurs test

Ensuite, identifiez un ensemble d'utilisateurs test qui suivront les Canvas Steps sans réellement envoyer de messages aux utilisateurs prévus. Les utilisateurs test peuvent être des adresses e-mail existantes qui ne sont pas utilisées pour des services sur votre tableau de bord de Braze ou de nouvelles adresses e-mail réservées à des fins de test. 

## Étape 3 : Configurer votre Canvas

Il est ensuite temps de tester vos Canvas ! Pour organiser votre Canvas d’origine et tester les informations Canvas, créez un double de votre Canvas à des fins de test. 

![][1]

Dans ce double, modifiez la part de votre **audience d’entrée** dans le créateur Canvas pour que les utilisateurs test soient les seuls éligibles pour le Canvas. Vous pouvez également saisir votre propre adresse e-mail comme utilisateur test en ajoutant le filtre de test d’**adresse e-mail**. 

Dans l’exemple ci-dessous, nous avons limité le Canvas à deux utilisateurs test qui ont utilisé l’application pour la première fois il y a moins de 3 jours. 

![][2]

## Étape 4 : Lancer votre test

Lancez votre Canvas de test pour permettre à vos utilisateurs de commencer à y entrer. Complétez ensuite les comportements utilisateurs de votre application qui enverraient les utilisateurs dans leurs parcours Canvas respectifs. 

Vérifiez que vos utilisateurs de test reçoivent bien les messages attendus de vos étapes Canvas. Prenez en compte le fait que vos utilisateurs de test peuvent ne pas recevoir un message pour, entre autres, les raisons suivantes :

- N’est pas éligible au groupe de contrôle global
- Limitations de la limite de fréquence
- Appartenance à un segment non concordant
- Messages abandonnés
- Jetons de notification push associés à des utilisateurs différents

Continuez à itérer vos tests de Canvas pour vous assurer qu’il fonctionne comme prévu.

## Conseils généraux

### Identifier vos Canvas Steps

Dans certains cas, un utilisateur peut potentiellement recevoir plusieurs messages lorsqu’il progresse dans un Canvas. Si le délai entre les étapes a été considérablement réduit pour les tests, il se peut que le message déclenché pendant les tests ne soit pas toujours clair. S’assurer que les messages test, y compris le nom de l’étape ou l’ID utilisateur (à l’aide de Liquid), faciliteront l’identification et la confirmation que le bon message a été envoyé aux utilisateurs appropriés.

### Créer un groupe interne

Au lieu de créer des utilisateurs test individuels, vous pouvez créer un [Groupe de tests de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/), qui est un groupe interne dont l’objectif est d’examiner le contenu de votre message. Cela inclut un groupe d’utilisateurs qui recevront des messages test des campagnes et des Canvas. Vous pouvez ensuite ajouter ce groupe de tests dans le champ **Add Content Test Groups (Ajouter des groupes de tests de contenu)** sous **Test Recipients (Destinataires de tests)**.

### Délais réduits

Pour faciliter une exécution plus efficace de vos tests, nous vous conseillons, pour afficher les messages à une vitesse raisonnable, de réduire les délais à quelques minutes ou secondes à des fins de test. Par exemple, autorisés au moins 2 ou 3 minutes entre les tests pour pouvoir isoler des actions spécifiques dans les parcours Canvas donnés.

### Tirer parti des blocs de contenu

Si un contenu doit être répété dans votre cadre de test (par ex., Liquid complexe pour filtrer les utilisateurs en différents Canvas Steps), essayez d’enregistrer ce contenu répété en tant que [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks). Maintenant, vous pouvez inclure le bloc de contenu dans les différents Canvas Steps.

### Utiliser Postman et l’endpoint de suivi des utilisateurs

Vous pouvez effectuer des tests avec Postman et l’[ensemble Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utilisez l’[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer et suivre les événements personnalisés ainsi que les achats pour les différents utilisateurs de test.

Prenez en compte le fait qu’envoyer des données à l’API de suivi des utilisateurs ne peut être réalisé qu’avec un ID externe. Les utilisateurs de test peuvent devoir être ajoutés en tant qu’utilisateurs de test dans un groupe interne dans le tableau de bord de Braze pour que des erreurs données puissent être étudiées. 

#### Tester plusieurs branches

Lorsque vous testez un Canvas avec plusieurs branches ciblant les utilisateurs selon divers attributs ou événements, suivez ce plan de tes :

1. Pour chaque branche, identifiez les attributs et les événements que l’utilisateur doit posséder pour être inclus dans le parcours Canvas.
2. Intégrez-les dans la charge utile JSON pour être publiés en utilisant l’endpoint `/users/track`.

[1]: {% image_buster /assets/img_archive/canvas_test1.png %}
[2]: {% image_buster /assets/img_archive/canvas_test2.png %}