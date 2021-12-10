---
nav_title: Exporter le dépannage
article_title: Exporter le dépannage
page_order: 10
page_type: Référence
description: "Cet article de référence couvre certains scénarios communs de dépannage pour les exportations API et CSV."
---

# Exporter le dépannage

Voici quelques messages d'erreur que vous pouvez rencontrer lors de l'exportation de données via CSV ou API depuis Braze.

## Erreurs courantes

#### « Accès refusé »

Si vous utilisez __votre propre bucket S3__, cela pourrait se produire parce que :
- L'objet attendu n'est plus dans le compartiment S3 ; vérifiez auprès de vos ingénieurs.
- Les identifiants S3 configurés dans le tableau de bord de Braze n'ont pas les autorisations correctes ; confirmez les identifiants appropriés avec votre équipe.

Si vous utilisez le bucket __Braze S3__, cela pourrait se produire parce que :
- L'objet n'est plus là. Cela pourrait se produire si vous cliquiez sur un lien pour une exportation qui a fonctionné il y a plus de 4 heures. Si c'est le cas, veuillez relancer l'exportation.
- Vous avez cliqué sur le lien de téléchargement tout de suite, avant que le S3 soit prêt à servir l'objet. Veuillez patienter quelques minutes et réessayer. Les rapports plus importants prendront généralement plus de temps.
- L'exportation est trop grande, donc notre serveur a manqué de mémoire en essayant de créer ce fichier zip. Nous enverrons automatiquement un e-mail à l'utilisateur tentant d'exporter si cela se produit. Si vous rencontrez constamment ce problème, nous vous recommandons d'utiliser vos propres segments S3 à l'avenir.

#### ‘ExpiredToken’

Cela se produira si le courriel a été envoyé il y a plus de 4 heures. Relancez l'export et téléchargez-le dans les 4 heures. Cela pourrait également être causé par Braze n'ayant plus accès au seau S3 vers lequel vous téléchargez les données. Assurez-vous d'avoir mis à jour vos identifiants S3 en utilisant ces étapes.

#### "On dirait que le fichier n'existe plus, veuillez vérifier que rien ne supprime des objets de votre seau"

Il peut y avoir un léger décalage entre le moment où le courriel de Braze avec l'exportation est envoyé, et quand S3 est réellement prêt à servir l'objet. Si vous voyez cette erreur, attendez quelques minutes avant de réessayer.

