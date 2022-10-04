### Sauvegarde automatique de l’historique d’utilisateur anonyme

| Contexte d’identification | Comportement de préservation |
| ---------------------- | -------------------------- |
| L’utilisateur **n’a pas été** identifié précédemment | L’historique anonyme **est fusionné** avec le profil utilisateur lors de l’identification |
| L’utilisateur **a été** identifié précédemment dans l’application ou via l’API | L’historique anonyme **n’est pas fusionné** avec le profil utilisateur lors de l’identification |
{: .reset-td-br-1 .reset-td-br-2}

### Remarques supplémentaires et meilleures pratiques
Veuillez noter les points suivants :

- **Si votre application est utilisée par plusieurs personnes, vous pouvez attribuer à chaque utilisateur un identifiant unique afin de le suivre.**
- **Une fois qu’un ID utilisateur a été défini, vous ne pouvez pas rétablir cet utilisateur à un profil anonyme**
- **Ne modifiez pas l’ID utilisateur lors de la « déconnexion » d’un utilisateur.**
  - Sinon, l’appareil sera séparé du profil utilisateur. Vous ne pourrez pas cibler l’utilisateur précédemment déconnecté avec des messages de ré-engagement. Si vous anticipez qu’il y aura plusieurs utilisateurs sur le même appareil, mais que vous souhaitez uniquement cibler l’un d’eux lorsque votre application est à l’état déconnecté, nous vous recommandons de suivre séparément l’ID utilisateur que vous souhaitez cibler durant la déconnexion et de basculer vers cet ID utilisateur dans le cadre du processus de déconnexion de votre application. Par défaut, seul le dernier utilisateur connecté recevra des notifications push de votre application.
- **Passer d’un utilisateur identifié à un autre est un fonctionnement relativement coûteux.**
  - Lorsque vous demandez un changement d’utilisateur, la session actuelle de l’utilisateur précédent est automatiquement fermée et une nouvelle session est lancée. En outre, Braze émet automatiquement une demande d’actualisation des données pour le fil d’actualité, les messages in-app et autres ressources de Braze pour le nouvel utilisateur.

{% alert tip %}
Si vous choisissez d’utiliser un hachage d’identifiant unique, votre ID utilisateur s’assure que vous normalisez l’entrée avec votre fonction de hachage. Par exemple, si vous comptez utiliser le hachage d’une adresse e-mail, assurez-vous de supprimer les espaces de début et de fin de l’entrée, et de prendre en compte la localisation.
{% endalert %}