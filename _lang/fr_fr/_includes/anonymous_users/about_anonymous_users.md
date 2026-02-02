Après avoir [intégré le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/), les utilisateurs qui lancent votre application pour la première fois seront considérés comme "anonymes" jusqu'à ce que vous appeliez la méthode `changeUser` et que vous leur attribuiez un `external_id`. Une fois attribués, vous ne pouvez plus les rendre anonymes. Cependant, s'ils désinstallent et réinstallent votre application, ils redeviendront anonymes jusqu'à ce que `changeUser` soit appelé.

Si un utilisateur anonyme démarre une session sur un nouvel appareil, toute son activité anonyme sera automatiquement synchronisée avec son profil existant après que vous ayez appelé `changeUser` sur cet appareil à l'aide de son `external_id`. Cela inclut tous les attributs, événements ou historiques collectés au cours de la session sur le nouvel appareil.

{% if include.section == "user_guide" %}
{% alert tip %}
Pour une description complète, consultez la section [Définition des ID utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).
{% endalert %}
{% endif %}