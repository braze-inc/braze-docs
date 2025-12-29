---
nav_title: "Campagnes déclenchées par l'API et basées sur des actions."
article_title: "Test des campagnes déclenchées par l'API et basées sur des actions"
page_order: 2
page_type: reference
description: "Cet article de référence explique comment tester les campagnes déclenchées par l'API et basées sur des actions."

---

# Campagnes déclenchées par l'API et basées sur des actions.

> Lorsque vous implantez des campagnes, il est toujours bon de tester vos messages avant de les lancer. Cet article de référence traite de la création d'un segment utilisateur test qui vous permettra d'inspecter les requêtes API, les charges utiles et d'afficher les journaux de livrabilité.

## Étape 1 : Créer un segment d'utilisateurs test

La seule façon de tester le déclenchement d'une campagne à l'aide de l'API ou d'un événement personnalisé est de mettre la campagne en ligne/en production/instantané. Dans le cadre du déploiement d'une nouvelle campagne, nous vous recommandons vivement d'ajouter un segment utilisateur test aux campagnes lorsque vous testez le déclenchement de la livrabilité. Cela permet de mettre en place un filet de sécurité, en s'assurant que même si une campagne est envoyée accidentellement, elle ne s'adressera qu'à des utilisateurs internes.

1. **Importation d'utilisateurs test**<br>Les utilisateurs test peuvent être importés dans Braze à l'aide d'un fichier CSV ou d'une requête unique par lots via [Postman]({{site.baseurl}}/api/postman_collection/). Lors de l'importation de ces utilisateurs, nous vous recommandons de définir un attribut personnalisé sur leurs profils (tel que `internal_test_user: true`) qui peut être utilisé pour créer un segment d'essai. <br><br>
2. **Ajouter des utilisateurs test en tant qu'utilisateurs test reconnus par Braze**<br>En [marquant vos utilisateurs test comme utilisateurs test reconnus par Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) dans le tableau de bord, vous avez accès à la journalisation détaillée pour chaque utilisateur, ce qui vous permet d'inspecter les requêtes API et leurs données utiles, et d'afficher les journaux de livrabilité. Ces journaux peuvent vous aider à déterminer s'il y a eu des problèmes lors de la diffusion des campagnes aux utilisateurs finaux. <br><br>
3. **Créer un segment**<br>Pour créer un segment d'utilisateurs test, créez un segment d'utilisateurs dont l'attribut personnalisé `internal_test_user` est défini sur `true`. Ce segment peut être supprimé lorsque la campagne est en ligne/en production/instantanée. 

## Étape 2 : Les tests envoient

Ensuite, vous pouvez effectuer un envoi test à partir du tableau de bord de Braze ou utiliser Inbox Vision (e-mail uniquement) pour voir à quoi ressemblera la mise en page alors que la campagne est encore en mode brouillon. Vous pouvez ensuite envoyer la campagne à votre segment utilisateur test pour vérifier qu'elle se comporte comme prévu. Que la campagne soit déclenchée par l'API ou par une action, utilisez Postman pour envoyer une requête unique à l'API de Braze, déclenchant ainsi la campagne. 

## Étape 3 : Utilisez la journalisation de Braze pour inspecter les résultats entrants

Utilisez la journalisation de Braze pour résoudre les problèmes de déclenchement, d'envoi et d'événement. 
- Le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) vous indiquera le contenu brut de la requête API, l'événement personnalisé qui déclenche la campagne et toutes les propriétés du déclencheur ou de l'événement associées.
- Le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) enregistre toutes les erreurs et vous aide à comprendre pourquoi un message particulier n'a pas été délivré.

## Étape 4 : Retirer le segment d'essai et lancer la campagne

Une fois que le message se déclenche et s'affiche correctement avec tous les liens cliqués enregistrés, vous pouvez supprimer le segment et mettre à jour la campagne. Si vous préférez recommencer la campagne depuis le début afin que les quelques impressions de l'utilisateur test ne soient pas incluses, vous pouvez dupliquer la campagne et la redémarrer sans le segment de l'utilisateur test. 
