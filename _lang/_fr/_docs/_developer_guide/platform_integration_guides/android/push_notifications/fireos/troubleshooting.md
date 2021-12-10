---
nav_title: Dépannage
article_title: Push Troubleshooting for FireOS
platform: Pare-feu
page_order: 20
page_type: Solution
description: "Cet article fournit des scénarios de dépannage pour les éventuels problèmes que vous pourriez rencontrer avec les notifications push."
channel: Pousser
---

# Dépannage

## Utilisation des logs d'erreur push

Braze fournit un journal des erreurs de notification Push dans le journal d'activité des messages. Ce journal d'erreurs fournit une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos campagnes ne fonctionnent pas comme prévu.  Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

!\[Journal d'erreur\]\[11\]

## Dépannage des scénarios

### Aucun utilisateur "push registred" ne s'affiche dans le tableau de bord de Braze (avant d'envoyer des messages)
  - Assurez-vous que votre application est correctement configurée pour autoriser les notifications push.
  - Assurez-vous que l'identifiant du client et le secret du client configurés dans votre tableau de bord Braze sont corrects.

### Notifications push non affichées sur les appareils des utilisateurs
Il y a quelques scénarios pour lesquels cela pourrait se produire :

  - Si vous forcez l'arrêt de votre application, vos notifications push ne seront pas affichées tant que votre application ne sera pas en cours d'exécution.
  - Assurez-vous que le paramètre \["Priorité de notification"\]\[15\] est réglé sur "HAUT" dans votre campagne
  - La clé d'API ADM dans votre `api_key.txt` est incorrecte ou ne comporte pas de caractères invalides.
  - L'AppboyAdmReceiver n'est pas correctement enregistré dans `AndroidManifest.xml` avec des filtres d'intention pour `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` et `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`.

### Les utilisateurs "Push registered" ne sont plus activés après l'envoi de messages

  - Cela se produit généralement lorsque des utilisateurs ont désinstallé l'application, ce qui rend leur ID d'enregistrement ADM invalide.
[11]: {% image_buster /assets/img_archive/message_activity_log.png %} [15]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/advanced_settings/#notification-priority
