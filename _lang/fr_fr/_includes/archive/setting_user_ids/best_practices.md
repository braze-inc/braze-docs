### Sauvegarde automatique de l’historique d’utilisateur anonyme

| Contexte d’identification | Comportement de préservation |
| ---------------------- | -------------------------- |
| L'utilisateur **n'a pas** été identifié au préalable | L'historique anonyme **est fusionné** avec le profil utilisateur lors de l'identification. |
| L'utilisateur **a été** préalablement identifié dans l'application ou via l'API. | L'historique anonyme **n'est pas fusionné** avec le profil utilisateur lors de l'identification. |
{: .reset-td-br-1 .reset-td-br-2}

Reportez-vous à la section [Profils utilisateurs identifiés]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) pour plus d'informations sur ce qui se passe lorsque vous identifiez des utilisateurs anonymes.

### Remarques supplémentaires et meilleures pratiques

Notez ce qui suit :

- Si votre appli est utilisée par plusieurs personnes, vous pouvez attribuer à chaque utilisateur un identifiant unique pour le suivre.
- Une fois qu'un ID d'utilisateur a été défini, vous ne pouvez pas ramener cet utilisateur à un profil anonyme.
- Ne changez pas l'ID de l'utilisateur lorsqu'il se déconnecte, car cela risque de dissocier l'appareil du profil utilisateur.
  - Par conséquent, vous ne pourrez pas cibler l'utilisateur précédemment déconnecté avec des messages de réengagement. Si vous anticipez plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l’un d’eux lorsque votre application est à l’état déconnecté, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application. Par défaut, seul le dernier utilisateur connecté recevra des notifications push de votre application.
- Le passage d'un utilisateur identifié à un autre est une opération relativement coûteuse.
  - Lorsque vous demandez un changement d’utilisateur, la session actuelle de l’utilisateur précédent est automatiquement fermée et une nouvelle session est lancée. Braze effectuera automatiquement une demande d'actualisation des données pour les messages in-app et les autres ressources de Braze pour le nouvel utilisateur.

{% alert tip %}
Si vous optez pour un hachage d'un identifiant unique comme ID utilisateur, veillez à normaliser l'entrée de votre fonction de hachage. Par exemple, si vous allez utiliser un hachage d'une adresse e-mail, confirmez que vous supprimez les espaces de début et de fin de l'entrée et que vous tenez compte de la localisation.
{% endalert %}