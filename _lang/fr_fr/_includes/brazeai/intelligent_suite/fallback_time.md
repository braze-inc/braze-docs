Vous pouvez choisir l'une des options suivantes :

- **Les plus populaires :** C'est le moment où votre application est la plus utilisée par l'ensemble des utilisateurs.
- **Personnalisé :** Il s'agit d'une solution de repli personnalisée de votre choix. Le message sera envoyé en fonction du fuseau horaire local de chaque utilisateur.

{% subtabs local %}
{% subtab most popular %}
L'heure de l'application la plus populaire est déterminée par l'heure moyenne de début de session pour votre espace de travail (en heure locale). Ce temps est affiché en rouge sur le graphique de prévisualisation.

Dans le cas improbable où votre application ne dispose pas de suffisamment de données de session pour calculer le moment où l'application est la plus utilisée (une toute nouvelle application sans aucune donnée), le message sera envoyé à 17 heures dans le fuseau horaire local de l'utilisateur. Si le fuseau horaire local de l’utilisateur est inconnu, il s’enverra à 17 h dans le fuseau horaire de votre société.

Il est important de connaître les limitations de l’utilisation précoce du timing intelligent dans le cycle de vie d’un utilisateur lorsque des données limitées sont disponibles. Il est toujours utile, car même les utilisateurs avec peu de sessions enregistrées peuvent offrir des informations sur leur comportement. Cependant, Braze peut calculer plus efficacement l’heure d’envoi optimale plus tard dans le cycle de vie d’un utilisateur.

{% if include.type == "campaigns" %}
{% alert note %}
Pour les campagnes, si vous avez spécifié une [fenêtre de réception/distribution](#sending-within-specific-hours) et que le moment le plus populaire pour utiliser votre application tombe en dehors de cette fenêtre, le message sera envoyé au plus près du bord de la fenêtre de réception. Par exemple, si votre fenêtre de livraison est entre 13 h et 20 h et que l’heure la plus populaire pour l’application est 22 h, le message s’enverra à 20 h.
{% endalert %}
{% endif %}
{% endsubtab %}

{% subtab custom %}
Utilisez l'heure de repli personnalisée pour choisir une autre heure d'envoi du message. De la même manière que pour l’heure la plus populaire de l’application, le message s’enverra à l’heure de secours dans le fuseau horaire local de l’utilisateur. Si le fuseau horaire local de l’utilisateur est inconnu, il s’enverra dans le fuseau horaire de votre société.

Pour les campagnes avec une heure de repli personnalisée spécifiée, si vous lancez la campagne dans les 24 heures suivant la date d'envoi, les utilisateurs dont les heures optimales sont déjà passées recevront la campagne à l'heure de repli personnalisée. Si l’heure de secours personnalisée spécifiée est déjà passée dans leur fuseau horaire, le message s’enverra immédiatement.
{% endsubtab %}
{% endsubtabs %}