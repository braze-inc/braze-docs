---
nav_title: Campagnes déclenchées par API et par événement
article_title: Tester des campagnes déclenchées par API et par événement
page_order: 2
page_type: reference
description: "Cet article de référence explique comment tester des campagnes déclenchées par API et par événement."

---

# Campagnes déclenchées par API et par événement

> Lorsque vous implémentez des campagnes, une bonne pratique consiste à tester vos messages avant le lancement. Cet article de référence explique comment créer un segment d’utilisateurs de test qui vous permettra d’inspecter les requêtes API et d’afficher les journaux de livrabilité.

## Étape 1 : Créer un segment d’utilisateurs de test

Le seul moyen de tester le déclenchement d’une campagne par API ou événement personnalisé est de la mettre en ligne. Dans le cadre du déploiement de votre campagne, nous vous conseillons vivement de lui ajouter un segment d’utilisateurs de test lorsque vous testez le déclenchement de la livrabilité. Ceci vous offrira un filet de sécurité pour vous garantir que, si une campagne est envoyée par erreur, elle n’ira qu’aux utilisateurs internes.

1. **Importer des utilisateurs test**<br>Les utilisateurs test peuvent être importés dans Braze à l'aide d'un fichier CSV ou d'une requête unique par lots via [Postman.]({{site.baseurl}}/api/postman_collection/) Lors de l'importation de ces utilisateurs, nous vous recommandons de définir un attribut personnalisé sur leurs profils (tel que `internal_test_user: true`) qui peut être utilisé pour créer un segment d'essai. <br><br>
2. **Ajouter des utilisateurs test reconnus par Braze**<br>En [marquant vos utilisateurs test comme utilisateurs test reconnus par Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) dans le tableau de bord, vous avez accès à la journalisation détaillée pour chaque utilisateur, ce qui vous permet d'inspecter les requêtes API et leurs données utiles, et d'afficher les journaux de livrabilité. Ces journaux vous aident à déterminer s’il y a eu des problèmes dans la livraison des campagnes aux utilisateurs finaux. <br><br>
3. **Créer un segment**<br>Pour créer un segment d’utilisateurs de test, créez un segment d’utilisateurs ayant l’attribut personnalisé `internal_test_user` défini sur `true`. Ce segment peut être enlevé quand la campagne est déployée. 

## Étape 2 : Tester les envois

Vous pouvez ensuite effectuer un test d’envoi depuis le tableau de bord de Braze ou utiliser Inbox Vision (e-mail uniquement) pour visualiser à quoi ressemblera la mise en page alors que la campagne est toujours à l’état d’ébauche. Vous pouvez alors envoyer la campagne à votre segment d’utilisateurs de test pour vérifier si elle se comporte comme prévu. Que la campagne soit déclenchée par API ou par événement, utilisez Postman pour envoyer une requête unique à l’API Braze pour déclencher la campagne. 

## Étape 3 : Utiliser la connexion à Braze pour inspecter les résultats entrants

Utilisez la connexion à Braze pour résoudre les problèmes de déclenchement, d’envoi et d’événements. 
- Le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) vous montrera la charge utile brute de la requête de déclenchement par API, l’événement personnalisé déclenchant la campagne et toutes les propriétés d’événements ou de déclencheurs associées.
- Le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) enregistre toutes les erreurs et vous aide à comprendre pourquoi un message particulier n'a pas été délivré.

## Étape 4 : Enlever le segment d’essai et déployer la campagne

Une fois que le message est déclenché et s’affiche correctement, avec tous les liens cliqués enregistrés, vous pouvez enlever le segment et mettre à jour la campagne. Si vous préférez recommencer la campagne depuis le début pour que les impressions des utilisateurs de test ne soient pas comprises, vous pouvez dupliquer la campagne et la recommencer sans le segment d’utilisateurs de test. 
