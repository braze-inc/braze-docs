---
nav_title: Importer votre liste d’e-mails dans Braze
article_title: Importer votre liste d’e-mails dans Braze
page_order: 4
page_type: reference
description: "Le présent article de référence couvre les bonnes pratiques d’importation de votre liste d’e-mails dans Braze."
channel: email

---

# Importer votre liste d’e-mails dans Braze {#importing-email-lists}

Une étape importante pour vous définir comme un expéditeur de courrier électronique à succès est de vous assurer que vous avez une liste de courriels de haute qualité. Une gestion appropriée de la liste des courriels peut améliorer votre capacité de délivrabilité et vous donner des résultats de campagne plus précis et plus propres.

1. **Validez votre liste pour vous assurer que vous importez uniquement des adresses e-mail authentiques.**<br>Un taux de rebond élevé peut endommager votre réputation d’expéditeur de courrier électronique. Les services de nettoyage des listes d’e-mails peuvent faire cela pour vous en déterminant si l’adresse e-mail respecte la syntaxe correcte et possède les propriétés physiques d’une adresse e-mail, en vérifiant le domaine de messagerie et en se connectant au serveur de messagerie pour s’authentifier si l’adresse e-mail existe.<br><br>
2. **Retirer les utilisateurs profondément inactifs.**<br>Il est recommandé de ne pas envoyer de courrier électronique à des utilisateurs qui n’ont pas fait l’objet d’un e-mail dans plus de six mois, car cela peut endommager votre réputation d’expéditeur de courrier électronique. Lors de l’importation de votre liste d’e-mails, assurez-vous de ne pas importer des utilisateurs qui n’ont pas ouvert d’e-mail de votre part au cours des six derniers mois. À long terme, vous devriez également envisager de mettre en œuvre une [politique de temporisation][60].<br><br>
3. **N’importez aucune liste de suppression.**<br>Si vous mettez en transition un fournisseur d’e-mails existant, assurez-vous de ne pas importer les utilisateurs à partir d’une liste de suppression. Les listes de suppression contiennent des adresses e-mail qui sont désabonnées, ont marquées de vos e-mails comme des spams ou qui ont subi un hard bounce.

[60]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
