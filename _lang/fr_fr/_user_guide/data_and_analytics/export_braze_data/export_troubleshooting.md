---
nav_title: Résolution des problèmes d’exportation
article_title: Résolution des problèmes d’exportation
page_order: 10
page_type: reference
description: "Cet article de référence couvre certains scénarios de résolution des problèmes courants pour les exportations API et CSV."

---

# Résolution des problèmes d’exportation

> Cette page répertorie les messages d'erreur que vous pouvez rencontrer lors de l'exportation de données via CSV ou API depuis Braze.

## Erreurs courantes

### « AccessDenied » (Accès Refusé) 

#### Si vous utilisez votre propre compartiment S3

Si vous utilisez **votre propre compartiment S3**, cela peut se produire parce que :

- L’objet attendu n’est plus dans le compartiment S3 ; voyez avec vos ingénieurs.
- Les identifiants S3 configurés dans le tableau de bord de Braze ne disposent pas des bonnes autorisations ; confirmez les identifiants appropriés auprès de votre équipe.

#### Lors de l'utilisation d'un compartiment S3 de Braze

Si vous utilisez un **compartiment S3 de Braze**, cela peut se produire pour les raisons suivantes :

- L’objet n’est plus là. Cela peut se produire si vous avez cliqué sur un lien pour une exportation qui a eu lieu il y a plus de 4 heures. Si c’est le cas, relancez votre exportation.
- Vous avez sélectionné le lien de téléchargement immédiatement, avant que le S3 ne soit prêt à servir l'objet. Attendez quelques minutes et réessayez. Les rapports volumineux prendront généralement plus de temps. 
- L’exportation est trop grande, notre serveur a donc manqué de mémoire en essayant de créer ce fichier zip. Nous enverrons automatiquement un e-mail à l’utilisateur qui a lancé l’exportation si cela se produit. Si vous êtes constamment confronté à ce problème, nous vous recommandons d’utiliser vos propres compartiments S3 à l’avenir.

### « ExpiredToken » (Jeton Expiré)

Cela se produit si l'e-mail a été envoyé il y a plus de 4 heures. Relancez l’exportation et téléchargez-la dans les 4 heures.

Cela pourrait également se produire si Braze n’a plus accès au compartiment S3 vers lequel vous téléchargez les données. Assurez-vous d’avoir mis à jour vos informations d’identification S3 en utilisant ces étapes.

### "Il semble que le fichier n'existe plus, veuillez vérifier que rien ne supprime les objets de votre compartiment".

Il peut y avoir un léger décalage entre le moment où l’e-mail de Braze avec l’exportation est envoyé et le moment où S3 est véritablement prêt à servir l’objet. Si vous voyez cette erreur, attendez quelques minutes avant de réessayer.

### Apostrophes ajoutées aux champs

Braze ajoutera automatiquement une apostrophe à un champ dans l'exportation CSV si le champ commence par l'un des caractères suivants :

- -
- =
- +
- @

Par exemple, le champ "-1943" sera exporté sous la forme "'-1943". Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l' [endpoint`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).