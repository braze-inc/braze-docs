---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des notifications push pour FireOS
platform: FireOS
page_order: 20
page_type: solution
description: "Cet article de référence fournit des scénarios de résolution des problèmes FireOS pour les problèmes que vous pourriez rencontrer avec des notifications push."
channel: push

---

# Résolution des problèmes

> Cet article fournit plusieurs scénarios de résolution des problèmes concernant FireOS.

## Utiliser les journaux d’erreur de notification push

Braze fournit des erreurs de notification push dans le journal des activités de message. Ce journal d’erreurs fournit de nombreux avertissements qui peuvent être très utiles pour identifier les raisons pour lesquelles vos campagnes ne fonctionnent pas comme prévu. Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

![]({% image_buster /assets/img_archive/message_activity_log.png %})

## Scénarios de résolution des problèmes

### Aucun utilisateur « Push Registered » (Enregistré pour les notifications push) ne s’affiche dans le tableau de bord de Braze (avant l’envoi de messages)

- Assurez-vous que votre application est correctement configurée pour autoriser les notifications push.
- Assurez-vous que l’ID client et le secret client configurés dans votre tableau de bord de Braze sont corrects.

### Les notifications push ne sont pas affichées sur les appareils des utilisateurs

Il y a plusieurs raisons pour lesquelles cela pourrait se produire :

- Si vous forcez votre application à quitter, vos notifications push ne seront pas affichées tant que votre application n’est pas en cours d’exécution.
- Assurez-vous que le paramètre [Priorité de notification]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/push_notifications/fireos/customization/advanced_settings/#notification-display-priority) est réglé sur `HIGH` dans votre campagne.
- La clé API ADM dans votre `api_key.txt` est incorrecte ou contient des caractères non valides.
- Le `BrazeAmazonDeviceMessagingReceiver` n’est pas correctement enregistré dans `AndroidManifest.xml` avec des filtres d’intention pour `<action android:name="com.amazon.device.messaging.intent.RECEIVE" />` et `<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />`.

### Les utilisateurs « Push Registered » (Enregistré pour les notifications push) ne sont plus activés après l’envoi de messages

Cela se produit généralement lorsque les utilisateurs ont désinstallé l’application, ce qui rend invalide leur ID d’enregistrement ADM.

