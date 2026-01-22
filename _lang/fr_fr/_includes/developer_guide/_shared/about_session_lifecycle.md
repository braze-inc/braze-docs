## À propos du cycle de vie de la session

Une session désigne la période pendant laquelle le SDK de Braze suit l'activité de l'utilisateur dans votre application après son lancement. Vous pouvez également forcer une nouvelle session en [appelant la méthode `changeUser()` ]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab android %}
{% alert note %}
Si vous avez configuré le [rappel du cycle de vie de l'activité]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) pour Android, Braze appellera automatiquement [`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) et [`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html) pour chaque activité de votre application.
{% endalert %}

Par défaut, une session démarre lorsque `openSession()` est appelé pour la première fois. Si votre application passe en arrière-plan puis revient au premier plan, le SDK vérifiera si plus de 10 secondes se sont écoulées depuis le début de la session (sauf si vous [modifiez le délai d'expiration de la session par défaut]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Si c'est le cas, une nouvelle session commencera. Gardez à l'esprit que si l'utilisateur ferme votre application alors qu'elle est en arrière-plan, les données de session peuvent ne pas être envoyées à Braze jusqu'à ce qu'il rouvre l'application.

L'appel à `closeSession()` ne met pas immédiatement fin à la session. Au lieu de cela, il mettra fin à la session au bout de 10 secondes si `openSession()` n'est pas appelé à nouveau par l'utilisateur qui démarre une autre activité.
{% endtab %}

{% tab swift %}
Par défaut, une session démarre lorsque vous appelez `Braze.init(configuration:)`. Cela se produit lorsque la notification `UIApplicationWillEnterForegroundNotification` est déclenchée, ce qui signifie que l'application est passée au premier plan.

Si votre application passe en arrière-plan, `UIApplicationDidEnterBackgroundNotification` sera déclenché. Lorsque votre application revient au premier plan, le SDK vérifie si plus de 10 secondes se sont écoulées depuis le début de la session (sauf si vous [modifiez le délai d'attente par défaut de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Si c'est le cas, une nouvelle session commencera.
{% endtab %}

{% tab web %}
Par défaut, une session démarre lorsque vous appelez `braze.openSession()` pour la première fois. La session restera active jusqu'à `30` minutes d'inactivité (sauf si vous [modifiez le délai par défaut de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) ou si l'utilisateur ferme l'application).
{% endtab %}
{% endtabs %}