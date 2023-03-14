---
nav_title: Résolution des problèmes d’exportation
article_title: Résolution des problèmes d’exportation
page_order: 10
page_type: reference
description: "Cet article de référence couvre certains scénarios de résolution des problèmes courants pour les exportations API et CSV."

---

# Résolution des problèmes d’exportation

Voici quelques messages d’erreur que vous pouvez rencontrer lors de l’exportation des données via CSV ou API depuis Braze.

## Erreurs courantes

#### « AccessDenied » (Accès Refusé) 

Si vous utilisez **votre propre compartiment S3**, cela peut se produire si :
- L’objet attendu n’est plus dans le compartiment S3 ; voyez avec vos ingénieurs.
- Les informations d’identification S3 configurées dans le tableau de bord de Braze n’ont pas les bonnes autorisations ; confirmez les identifiants avec votre équipe.

Si vous utilisez **le compartiment S3 de Braze**, cela peut se produire si :
- L’objet n’est plus là. Cela pourrait se produire si vous avez cliqué sur un lien pour une exportation qui a fonctionné il y a plus de 4 heures. Si c’est le cas, relancez votre exportation.
- Vous avez cliqué immédiatement sur le lien de téléchargement, avant que le S3 n’ait été prêt à servir l’objet. Attendez quelques minutes et réessayez. Les rapports volumineux prendront généralement plus de temps. 
- L’exportation est trop grande, notre serveur a donc manqué de mémoire en essayant de créer ce fichier zip. Nous enverrons automatiquement un e-mail à l’utilisateur qui a lancé l’exportation si cela se produit. Si vous êtes constamment confronté à ce problème, nous vous recommandons d’utiliser vos propres compartiments S3 à l’avenir.

#### « ExpiredToken » (Jeton Expiré)

Cela se produira si l’e-mail a été envoyé il y a plus de 4 heures. Relancez l’exportation et téléchargez-la dans les 4 heures.
Cela pourrait également se produire si Braze n’a plus accès au compartiment S3 vers lequel vous téléchargez les données. Assurez-vous d’avoir mis à jour vos informations d’identification S3 en utilisant ces étapes.

#### « Il semble que le fichier n’existe plus, veuillez vérifier que rien ne supprime les objets de votre compartiment. »"

Il peut y avoir un léger décalage entre le moment où l’e-mail de Braze avec l’exportation est envoyé et le moment où S3 est véritablement prêt à servir l’objet. Si vous voyez cette erreur, attendez quelques minutes avant de réessayer.

