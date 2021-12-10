---
nav_title: Erreurs & réponses
article_title: Erreurs API & Réponses
description: "Cet article de référence couvre les différentes erreurs et réponses du serveur qui peuvent apparaître en utilisant l'API Braze et comment les résoudre."
page_type: Référence
page_order: 2.3
---

# Erreurs et réponses de l'API

> Cet article de référence couvre les différentes erreurs et réponses du serveur qui peuvent apparaître en utilisant l'API Braze et comment les résoudre.

{% raw %}

## Réponses du serveur

Si votre bloc POST a été accepté par nos serveurs, alors les messages réussis seront traités avec la réponse suivante:

```json
{
  "message" : "success"
}
```

Notez que le succès signifie seulement que la charge utile de l'API RESTful a été correctement formée et transmise à nos services de notification push, d'e-mail ou d'autres services de messagerie. Cela ne signifie pas que les messages ont été effectivement envoyés, car des facteurs supplémentaires pourraient empêcher la transmission du message (e. ., un appareil peut être hors ligne, le jeton push pourrait être rejeté par les serveurs Apple, vous avez peut-être fourni un ID d'utilisateur inconnu, etc.)

Si votre message est réussi mais comporte des erreurs non fatales, vous recevrez la réponse suivante :

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En cas de succès, tous les messages qui n'ont pas été affectés par une erreur dans le tableau `erreurs` seront toujours délivrés. Si votre message a une erreur fatale, vous recevrez la réponse suivante:

```json
{
  "message" : <fatal error message>, "erreurs" : [<minor error message>]
}
```

## Réponses en attente {#messaging-queued}

En temps de maintenance, Braze peut mettre en pause le traitement en temps réel de l'API. Dans ces situations, le serveur retournera un code de réponse `HTTP Accepted 202` et le corps suivant, qui indique que nous avons reçu et mis en file d'attente l'appel à l'API mais que nous ne l'avons pas traité immédiatement. Toute la maintenance planifiée sera postée sur [http://status.braze.com](http://status.braze.com) à l'avance.

```json
{
  "message" : "mis en attente"
}
```

## Réponses pour les identifiants d'envoi suivis

Les analytiques sont toujours disponibles pour les campagnes. En outre, les analytiques sont disponibles pour une instance d'envoi de campagne spécifique lorsque la campagne est envoyée en tant que diffusion. Lorsque le suivi est disponible pour une instance d'envoi de campagne spécifique, vous recevrez la réponse suivante:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

L'identifiant d'envoi fourni peut être utilisé comme paramètre pour le point de terminaison send/data_series pour récupérer des analyses spécifiques.

## Erreurs fatales

Les codes de statut suivants et les messages d'erreur associés seront retournés si votre requête rencontre une erreur fatale. Tous ces codes d'erreur indiquent qu'aucun message ne sera envoyé.

| Code d'erreur                                                                        | Libellé                                                                                                                                             |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400 Mauvaise requête`                                                               | Syntaxe incorrecte.                                                                                                                                 |
| `400 Aucun destinataire`                                                             | Il n'y a aucun ID externe ou ID de segment ou aucun jeton push dans la requête.                                                                     |
| `400 ID de campagne invalide`                                                        | Aucune campagne API de messagerie n'a été trouvée pour l'ID de la campagne que vous avez fournie.                                                   |
| `400 Message Variant non spécifié`                                                   | Vous fournissez un ID de campagne mais pas d'ID de variation de message.                                                                            |
| `400 Variante de message invalide`                                                   | Vous avez fourni un ID de campagne valide, mais l'ID de variation du message ne correspond à aucun des messages de cette campagne.                  |
| `400 types de message ne correspondent pas`                                          | Vous avez fourni une variation du mauvais type de message pour au moins un de vos messages.                                                         |
| `400 Invalid Extra Push Payload`                                                     | Vous fournissez la clé `supplémentaire` pour `apple_push` ou `android_push` mais ce n'est pas un dictionnaire.                                      |
| `Taille max de l'entrée dépassée`                                                    | Cautionné en appelant plus de 75 identifiants externes en appuyant sur le point de terminaison User Track.                                          |
| `400 Le nombre maximum d'identifiants externes et d'alias par requête a été dépassé` | Cause en appelant plus de 50 identifiants externes.                                                                                                 |
| `400 Le nombre maximum d'ids par requête a été dépassé`                              | Cause en appelant plus de 50 identifiants externes.                                                                                                 |
| `400 Aucun message à envoyer`                                                        | Aucun bloc n'est spécifié pour le message.                                                                                                          |
| `La longueur de message du slideup 400 a été dépassée`                               | Le message du slideup contient plus de 140 caractères.                                                                                              |
| `La longueur de la poussée de la pomme est dépassée`                                 | Le bloc JSON fait plus de 1912 octets.                                                                                                              |
| `400 longueurs de poussée Android dépassées`                                         | Le bloc JSON fait plus de 4000 octets.                                                                                                              |
| `400 Mauvaise requête`                                                               | Impossible d'analyser la date de send_at.                                                                                                           |
| `400 Mauvaise requête`                                                               | Dans votre requête, `in_local_time` est vrai mais `temps` est passé dans le fuseau horaire de votre entreprise.                                     |
| `401 Non autorisé`                                                                   | Clé d'API REST inconnue ou manquante.                                                                                                               |
| `403 Interdit`                                                                       | L'abonnement ne prend pas en charge ou le compte est autrement inactivé.                                                                            |
| `403 Accès refusé`                                                                   | La clé d'API REST que vous utilisez n'a pas les permissions suffisantes, vérifiez les permissions de la clé API dans la console de Braze Developer. |
| `404 introuvable`                                                                    | Clé d'API REST inconnue.                                                                                                                            |
| `Tarif Limité 429`                                                                   | Limite de débit.                                                                                                                                    |
| `Erreur de serveur interne 5XX`                                                      | Vous devriez réessayer votre demande avec un retour en arrière plan.                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}
