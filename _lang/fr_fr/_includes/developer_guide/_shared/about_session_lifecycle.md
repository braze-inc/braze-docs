## À propos du cycle de vie de la session

Une session désigne la période pendant laquelle le SDK Braze suit l'activité des utilisateurs dans votre application après son lancement. Vous pouvez également forcer une nouvelle session en [appelant la`changeUser()`méthode]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab web %}
Par défaut, une session commence lorsque vous appelez pour la première`braze.openSession()` fois . La session restera active pendant un maximum de`30`minutes d'inactivité (à moins que vous [ne modifiiez le délai d'expiration par défaut de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web#change-session-timeout) ou que l'utilisateur ne ferme l'application).
{% endtab %}

{% tab android %}
{% alert note %}
Si vous avez configuré le rappel du cycle de ]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)vie des activités pour Android, Braze appellera automatiquement[`openSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/open-session.html) et[`closeSession()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/close-session.html)pour chaque activité de votre application.
{% endalert %}

Par défaut, une session commence lorsque`openSession()`  est appelé pour la première fois. Si votre application passe en arrière-plan puis revient au premier plan, le SDK vérifiera si plus de 10 secondes se sont écoulées depuis le début de la session (à moins que vous [ne modifiiez le délai d'expiration par défaut de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android#change-session-timeout)). Dans ce cas, une nouvelle session débutera. Veuillez noter que si l'utilisateur ferme votre application alors qu'elle est en arrière-plan, les données de session risquent de ne pas être envoyées à Braze tant qu'il n'aura pas rouvert l'application.

Appeler ne`closeSession()` mettra pas immédiatement fin à la session. Au lieu de cela, la session prendra fin après 10 secondes si l'utilisateur `openSession()`ne la relance pas en démarrant une autre activité.
{% endtab %}

{% tab swift %}
Par défaut, une session commence lorsque vous appelez `Braze.init(configuration:)`. Cela se produit lorsque le déclencheur`UIApplicationWillEnterForegroundNotification`de la notification est activé, ce qui signifie que l'application est passée au premier plan.

Si votre application passe en arrière-plan, le `UIApplicationDidEnterBackgroundNotification`déclencheur est activé. L'application ne reste pas dans une session active lorsqu'elle est en arrière-plan. Lorsque votre application revient au premier plan, le SDK compare le temps écoulé depuis le début de la session au délai d'expiration de la session (à moins que vous [ne modifiiez le délai d'expiration par défaut]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift#change-session-timeout)). Si le temps écoulé depuis le début de la session dépasse le délai d'expiration, une nouvelle session commence.
{% endtab %}
{% endtabs %}