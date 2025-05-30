## Mise en place d'un suivi des désinstallations

### Étape 1 : Activer les notifications push d’arrière-plan

Dans votre projet Xcode, allez dans **Capacités** et assurez-vous que les **Modes d'arrière-plan** sont activés. Pour plus d'informations, voir la [notification push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Étape 2 : Ignorer les notifications push internes

Le SDK de Swift Braze utilise des notifications push en arrière-plan pour collecter des analyses/analytiques de suivi de désinstallation. Pour que votre appli n'effectue pas d'actions non désirées lorsque celles-ci sont envoyées, vous devrez vous assurer que [les notifications push internes sont ignorées]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Étape 3 : Envoyer un push de test (optionnel)

Ensuite, envoyez-vous une notification push de test à partir du tableau de bord de Braze (ne vous inquiétez pas, elle ne mettra pas à jour votre profil utilisateur).

1. Allez dans **Envoi de messages** > **Campagnes** et créez une campagne de notification push à l'aide de la plateforme correspondante.
2. Allez dans **Settings** > **App Settings** et ajoutez la clé `appboy_uninstall_tracking` avec la valeur `true` correspondante, puis cochez **Add Content-Available Flag**.
3. Utilisez la page **Aperçu** pour vous envoyer une notification push de suivi de désinstallation test.
4. Vérifiez que votre app n'effectue pas d'actions automatiques non désirées lorsqu'elle reçoit une notification push.

{% alert note %}
Un numéro de badge sera envoyé avec la notification push de test - toutefois, une véritable notification push de suivi de désinstallation n'enverra aucun numéro de badge.
{% endalert %}

### Étape 3 : Activer le suivi de désinstallation

Enfin, activez le suivi des désinstallations dans Braze. Pour une description complète, voir [Activer le suivi de la désinstallation]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Le suivi des désinstallations peut être imprécis. Les indicateurs que vous voyez sur Braze peuvent être retardés ou inexacts.
{% endalert %}
