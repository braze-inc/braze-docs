---
nav_title: Envoyer des Canvas de test
article_title: Envoyer des Canvas de test
page_order: 1
description: "Cet article de référence explique comment tester un Canvas avant son lancement."
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

## Étape 2 : Identifier un utilisateur test

Identifiez ensuite un utilisateur test pour le tester dans les étapes de Canvas sans envoyer vraiment de messages aux utilisateurs prévus. Les utilisateurs de test peuvent être des adresses e-mail existantes qui ne sont pas utilisées pour des services sur votre tableau de bord de Braze ou de nouvelles adresses e-mail réservées à des fins de tes. 

## Étape 3 : Configurer votre Canvas

Il est ensuite temps de tester vos Canvas ! Créer un double de votre Canvas à des fins de test. Ceci vous permettra d’organiser les informations de votre Canvas d’origine et de test. 

![][1]

Modifiez la part de votre **audience d’entrée** dans le créateur Canvas pour que les utilisateurs de test soient les seuls éligibles pour le Canvas. Vous pouvez également saisir votre propre adresse e-mail comme utilisateur de test en ajoutant le filtre de test d’**adresse e-mail**. 

Dans l’exemple ci-dessous, nous avons limité le Canvas à deux utilisateurs de test qui ont utilisé l’application pour la première fois il y a moins de 3 jours.

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

### Délais réduits

Pour exécuter efficacement vos tests, nous vous conseillons, pour afficher les messages à une vitesse raisonnable, de réduire les délais à quelques minutes ou secondes à des fins de test. Par exemple, autorisés au moins 2 ou 3 minutes entre les tests pour pouvoir isoler des actions spécifiques dans les parcours Canvas donnés.

### Utiliser Postman et l’endpoint de suivi des utilisateurs

Vous pouvez effectuer des tests avec Postman et l’[ensemble Postman de Braze]({{site.baseurl}}/api/postman_collection/). Utilisez l’[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour enregistrer et suivre les événements personnalisés ainsi que les achats pour les différents utilisateurs de test.

Prenez en compte le fait qu’envoyer des données à l’API de suivi des utilisateurs ne peut être réalisé qu’avec un ID externe. Les utilisateurs de test peuvent devoir être ajoutés en tant qu’utilisateurs de test dans un groupe interne dans le tableau de bord de Braze pour que des erreurs données puissent être étudiées. 

#### Tester plusieurs branches

Lorsque vous testez un Canvas avec plusieurs branches ciblant les utilisateurs selon divers attributs ou événements, suivez ce plan de tes :

1. Pour chaque branche, identifiez les attributs et les événements que l’utilisateur doit posséder pour être inclus dans le parcours Canvas.
2. Intégrez-les dans la charge utile JSON pour être publiés en utilisant l’endpoint `/users/track`.

[1]: {% image_buster /assets/img_archive/canvas_test1.png %}
[2]: {% image_buster /assets/img_archive/canvas_test2.png %}