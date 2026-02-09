Avant de pouvoir envoyer une notification push iOS à l'aide de Braze, vous devez télécharger votre fichier de notification push `.p8`, comme indiqué dans [la documentation destinée aux développeurs d'Apple](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns):

1. Dans votre compte de développeur Apple, allez dans [**Certificats, identifiants & Profils**](https://developer.apple.com/account/ios/certificate).
2. Sous **Clés**, sélectionnez **Tous** et cliquez sur le bouton d'ajout (+) dans le coin supérieur droit.
3. Sous **Description de la clé**, saisissez un nom unique pour la clé de signature.
4. Sous **Services clés**, cochez la case **Service de notification push d'Apple (APN)**, puis cliquez sur **Continuer.** Cliquez sur **Confirmer**.
5. Notez l’ID de la clé. Cliquez sur **Télécharger** pour générer et télécharger la clé. Assurez-vous d’enregistrer le fichier téléchargé dans un endroit sécurisé, car vous ne pouvez pas le télécharger plus d’une fois.
6. Dans Braze, allez dans **Paramètres** > **Paramètres des applications** et téléchargez le fichier `.p8` sous **Certificat de notification push Apple**. Vous pouvez charger votre certificat de notifications push de développement ou de production. Pour tester les notifications push une fois que votre application est en ligne dans l'App Store, il est recommandé de créer un espace de travail distinct pour la version de développement de votre application.
7. Lorsque vous y êtes invité, saisissez l' [ID de l'offre groupée](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), l' [ID de la clé](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) et l' [ID de l'équipe de](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) votre application. Vous devrez également préciser si les notifications doivent être envoyées à l'environnement de développement ou de production de votre application, qui est défini par son profil de provisionnement. 
8. Lorsque vous avez terminé, sélectionnez **Enregistrer.**

