---
nav_title: Nettoyage
article_title: Nettoyage
page_order: 4
description: "Cet article définit l'assainissement et son objectif pour l'envoi de messages e-mail dans Braze."
channel:
  - email

---

# A propos de l'assainissement

> La désinfection est un processus qui se produit lorsque Braze détecte un type spécifique de JavaScript dans votre message e-mail.

## Pourquoi procéder à un nettoyage ?

L'objectif principal de l'assainissement est d'empêcher les acteurs malveillants d'accéder aux données de session d'autres utilisateurs du tableau de bord de Braze. Sans assainissement, un acteur malveillant disposant d'un accès de base en lecture seule peut créer un e-mail à l'aide du CKEditor avec du JavaScript qui "envoie la session actuelle du navigateur" à l'endroit souhaité par l'acteur malveillant à l'aide d'une requête réseau.

Lorsqu'un autre utilisateur du tableau de bord ouvre ce modèle d'e-mail, le JavaScript s'exécute et envoie les données de session de l'utilisateur actuel au mauvais acteur.

À noter que la plupart des fournisseurs de boîtes de réception d'e-mails ne traitent pas JavaScript. Cette mesure vise donc également à supprimer les éléments superflus des e-mails et à en réduire la taille. 

## Comment Braze désinfecte-t-il les messages ?

Si Braze détecte un JavaScript qui présente un risque pour la sécurité, nous vous demanderons de confirmer que Braze peut supprimer le JavaScript de votre message avant de passer à l'onglet **Prévisualisation et test** ou à l'éditeur HTML pour afficher le message e-mail.

![]({% image_buster /assets/img/email_sanitization.png %})

## Quand les mesures d'assainissement sont-elles maintenues ?

Dans l'éditeur par glisser-déposer et dans l'éditeur HTML, nous nettoyons, mais ne maintenons pas les résultats nettoyés pour les scénarios suivants :

* Le rendu de l’e-mail est généré dans les sections suivantes :
    * Section **Vision de la boîte réception** et onglet **Tests de courrier indésirable** 
    * Section **Prévisualisation et cartographie d’activité** dans le panneau **Performances des e-mails**
* L'e-mail est envoyé dans le cadre d'un envoi test

Pour l'éditeur par glisser-déposer, nous nettoyons et maintenons également les résultats nettoyés dans le message lorsque
est fermé et la campagne est enregistrée. Pour l'éditeur HTML, nous nettoyons et maintenons les résultats nettoyés dans le message lorsque l'utilisateur passe d'un type d'éditeur à l'autre et que la campagne est enregistrée.

Dans toutes ces instances, un message s'affiche si l'assainissement a modifié le code HTML. L'utilisateur doit l'accepter avant que l'assainissement ne soit terminé.