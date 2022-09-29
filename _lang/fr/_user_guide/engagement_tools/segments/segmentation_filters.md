---
page_order: 1
nav_title: Filtres de segmentation
article_title: Filtres de segmentation
layout: glossary_page
glossary_top_header: "Filtres de segmentation"
glossary_top_text: Le SDK de Braze vous propose un vaste arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de caractéristiques et d’attributs spécifiques. Comme vous le voyez ici, vous pouvez rechercher ou affiner ces filtres en utilisant Filter Category (Catégorie de filtres).

page_type: glossary
tool: Segments
description: "Ce glossaire répertorie les filtres disponibles pour segmenter et cibler vos utilisateurs."

glossary_tag_name: Catégorie de filtres
glossary_filter_text: "Sélectionnez une catégorie pour affiner les résultats du glossaire :"

# catégorie à icône/fa ou mappage d’image
glossary_tags:
  - name: Données personnalisées
  - name: Activité de l’utilisateur
  - name: Reciblage
  - name: Activité de marketing
  - name: Attributs utilisateur
  - name: Attribution d’installation
  - name: Activité sociale
  - name: Test
  - name: Autre

glossaries:
  - name: Attributs personnalisés
    description: Détermine si un utilisateur correspond ou non à une valeur d’attribut personnalisé qui a été enregistrée (période de 24 heures) <br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Données personnalisées
  - name: Événement personnalisé
    description: Détermine si un utilisateur a effectué un événement spécialement enregistré.<br><br> Exemple :<br>Activité terminée avec le nom de l’actif_de la propriété.<br><br>Fuseau horaire :<br>UTC - Jour civil = 1 jour civil examinera l’historique des utilisateurs sur une période allant de 24 à 48 heures.
    tags:
      - Données personnalisées
  - name: Premier événement personnalisé
    description: Détermine la première fois qu’un utilisateur a effectué un événement spécialement enregistré (période de 24 heures) <br><br>Exemple :<br> Premier panier abandonné il y a moins d’un jour<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Données personnalisées
  - name: Dernier événement personnalisé
    description: Détermine la dernière fois qu’un utilisateur a effectué un événement spécialement enregistré (période de 24 heures) <br><br>Exemple :<br> Dernier panier d’achats abandonné il y a moins d’un jour<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Données personnalisées
  - name: Dernier SMS reçu
    description: Segmente vos utilisateurs en fonction de la dernière fois où ils ont reçu un SMS. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: X événements personnalisés en Y jours
    description: Détermine si un utilisateur a effectué un événement spécialement enregistré entre 0 et 50 fois au cours du dernier nombre de jours civils indiqué, c’est-à-dire entre 1 et 30. (Jour civil = 1 jour civil examinera l’historique des utilisateurs sur une période allant de 24 à 48 heures)<br> <a href="/docs/x-in-y-behavior/"> En savoir plus sur le comportement « X dans Y » ici.</a> <br><br>Exemple :<br>Le panier a été abandonné exactement 0 fois au cours du dernier jour civil<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, un jour civil examinera l’historique des utilisateurs sur une période allant de 24 à 28 heures (en fonction du moment où le segment est évalué), deux jours civils examineront l’historique des utilisateurs sur une période allant de 48 à 72 heures, etc.
    tags:
      - Données personnalisées
  - name: X Propriétés d’événement personnalisé en Y jours
    description: Détermine si un utilisateur a effectué un événement spécialement enregistré en relation avec la propriété spécifique entre 0 et 50 fois au cours du dernier nombre de jours civils indiqué, compris entre 1 et 30. (Jour civil = 1 jour civil examinera l’historique des utilisateurs sur une période allant de 24 à 48 heures)<br><a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a> <br><br>Exemple :<br> Ajouté aux favoris avec la propriété « event_name » exactement 0 fois au cours du dernier jour civil<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, un jour civil examinera l’historique des utilisateurs sur une période allant de 24 à 28 heures (en fonction du moment où le segment est évalué), deux jours civils examineront l’historique des utilisateurs sur une période allant de 48 à 72 heures, etc.
    tags:
      - Données personnalisées
  - name: Date de l’événement récurrent
    description: Ce filtre examine le mois et le jour de l’attribut personnalisé avec le type de données « date », mais ne prend pas l’année en compte. Ce filtre est utile pour les événements annuels.<br><br>Fuseau horaire&#58;<br>Ce filtre s’adapte au fuseau horaire de l’utilisateur.
    tags:
      - Données personnalisées
  - name: Premier achat
    description: Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont effectué un achat via votre application (période de 24 heures)<br><br>Fuseau horaire :<br>UTC
    tags:
      - Activité de l’utilisateur
  - name: Premier achat dans l’application
    description: Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont acheté un article dans votre application (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Premier produit acheté
    description: Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont acheté un article spécifique dans votre application (abonnement spécial, chèque-cadeau, etc.)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Première application utilisée
    description: Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont ouvert votre application. <em>Notez que cela enregistrera leur première session sur une version de votre application avec le SDK intégré de Braze.</em> (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Première application utilisée
    description: Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont utilisé l’une des applications de votre groupe d’apps. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Dernier achat effectué
    description: Segmente vos utilisateurs en fonction de la date la plus récente à laquelle ils ont effectué un achat à travers votre application. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Dernier achat dans l’application
    description: Segmente vos utilisateurs en fonction de la date la plus récente à laquelle ils ont acheté un article dans votre application. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Dernier produit acheté
    description: Segmente vos utilisateurs en fonction de la date la plus récente à laquelle ils ont acheté un article spécifique dans votre application. (abonnement spécial, chèque-cadeau, etc.)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Dernière application utilisée
    description: Segmente vos utilisateurs en fonction de la date la plus récente à laquelle ils ont ouvert votre application. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Dernière application utilisée
    description: Segmente vos utilisateurs en fonction de la date la plus récente à laquelle ils ont ouvert une application spécifique. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de l’utilisateur
  - name: Durée médiane des sessions
    description: Segmente vos utilisateurs en fonction de la durée médiane de leurs sessions dans votre application.
    tags:
      - Activité de l’utilisateur
  - name: Argent dépensé
    description: Segmente vos utilisateurs en fonction du montant qu’ils ont dépensé dans votre application.
    tags:
      - Activité de l’utilisateur
  - name: Version la plus récente de l’application
    description: Segmente vos utilisateurs en fonction de la dernière version de votre application qu’ils ont utilisée.
    tags:
      - Activité de l’utilisateur
  - name: Code de version de l’application
    description: "Les filtres App Version Code (Code de version d’application) sont basés sur les numéros de version de votre application. Ce filtre prend en charge des comparaisons numériques pour cibler plusieurs versions de votre application. Par exemple, vous pouvez utiliser les filtres les résultats « below (antérieur) », « above (ultérieure) » et « equal to (identique à) » certaines versions de l’application. Cette fonction est disponible avec le SDK Braze pour Android v3.6.0 et versions ultérieures, et peut être activée par votre gestionnaire de compte Braze."
    tags:
      - Activité de l’utilisateur
  - name: Emplacement le plus récent
    description: Segmente vos utilisateurs en fonction du dernier emplacement enregistré depuis lequel ils ont utilisé votre application.
    tags:
      - Activité de l’utilisateur
  - name: Produit acheté
    description: Segmente vos utilisateurs en fonction des produits qu’ils ont achetés dans votre application.
    tags:
      - Activité de l’utilisateur
  - name: Nombre de sessions
    description: Segmente vos utilisateurs en fonction du nombre de sessions qu’ils ont eus dans l’une des applications de votre groupe d’apps.
    tags:
      - Activité de l’utilisateur
  - name: Nombre de sessions pour l’application
    description: Segmente vos utilisateurs en fonction du nombre de sessions qu’ils ont eus dans une application désignée.
    tags:
      - Activité de l’utilisateur
  - name: Nombre total d’achats
    description: Segmente vos utilisateurs en fonction du nombre d’achats qu’ils ont effectués dans votre application.
    tags:
      - Activité de l’utilisateur
  - name: Date de désinstallation
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils ont désinstallé votre application.
    tags:
      - Activité de l’utilisateur
  - name: Application désinstallée
    description: Segmente vos utilisateurs selon s’ils ont désinstallé votre application sans l’avoir réinstallée.
    tags:
      - Activité de l’utilisateur
  - name: X argent dépensé dans les Y derniers jours
    description: Segmente vos utilisateurs en fonction du montant dépensé dans votre application au cours du dernier nombre de jours civils indiqué, compris entre 1 et 30. Ce montant ne comprendra que la somme des 50 derniers achats. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a>
    tags:
      - Activité de l’utilisateur
  - name: X produits achetés dans les Y derniers jours
    description: Segmente vos utilisateurs en fonction du nombre de fois (entre 0 et 50) qu’ils ont acheté un article spécifique dans votre application (abonnement spécial, chèque-cadeau, etc.) au cours du dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a>
    tags:
      - Activité de l’utilisateur
  - name: X propriétés d’achat en Y jours
    description: Segmente vos utilisateurs en fonction du nombre de fois où un achat a été effectué par rapport à une certaine propriété d’achat dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a>
    tags:
      - Activité de l’utilisateur
  - name: X achats dans les Y derniers jours
    description: Segmente vos utilisateurs en fonction du nombre de fois (entre 0 et 50) qu’ils ont effectué un achat dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a>
    tags:
      - Activité de l’utilisateur
  - name: X sessions dans les Y derniers jours
    description: Segmente vos utilisateurs en fonction du nombre de sessions (entre 0 et 50) qu’ils ont initiés dans votre application dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement « X dans Y » ici.</a>
    tags:
      - Activité de l’utilisateur
  - name: Carte cliquée
    description: Segmente vos utilisateurs selon s’ils ont cliqué ou non sur une carte ou une promotion donnée.
    tags:
      - Reciblage
  - name: Campagne cliquée/ouverte
    description: Segmente vos utilisateurs selon s’ils ont interagi ou non avec une campagne donnée.
    tags:
      - Reciblage
  - name: Campagne ou Canvas avec balise cliqué(e)/ouvert(e)
    description: Segmente vos utilisateurs selon s’ils ont interagi ou non avec une campagne ou un Canvas spécifiques en utilisant une balise.
    tags:
      - Reciblage
  - name: Étape cliquée/ouverte
    description: Segmente vos utilisateurs selon s’ils ont interagi ou non avec une Canvas Step donnée.
    tags:
      - Reciblage
  - name: Convertis par la campagne
    description: Segmente vos utilisateurs selon s’ils ont été convertis ou non grâce à une campagne donnée.
    tags:
      - Reciblage
  - name: Convertis par le Canvas
    description: Segmente vos utilisateurs selon s’ils ont été convertis ou non grâce à un Canvas donné. Ce filtre n’inclut pas les utilisateurs du groupe de contrôle.
    tags:
      - Reciblage
  - name: Entrés dans une variante du Canvas
    description: Segmente vos utilisateurs selon s’ils sont ou non rentrés dans une variante d’un Canvas donné.
    tags:
      - Reciblage
  - name: N’a jamais reçu une campagne ou une Canvas Step
    description: Segmente vos utilisateurs selon s’ils ont ou non reçu une campagne ou une Canvas Step.
    tags:
      - Reciblage
  - name: Dans le groupe de contrôle de campagne
    description: Segmente vos utilisateurs selon s’ils faisaient ou non partie du groupe de contrôle d’une campagne multivariée donnée.
    tags:
      - Reciblage
  - name: Dans le groupe de contrôle de Canvas
    description: Segmente vos utilisateurs selon s’ils faisaient ou non partie du groupe de contrôle d’un Canvas donné.
    tags:
      - Reciblage
  - name: Dans aucun segment
    description: Segmente vos utilisateurs selon s’ils sont inclus ou non dans un segment existant.
    tags:
      - Reciblage
  - name: Dernière campagne ou dernier Canvas reçu avec balise
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils ont reçu une campagne ou un Canvas donné avec une balise spécifique. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Reciblage
  - name: Dernière campagne spécifique reçue
    description: Segmente vos utilisateurs en fonction de la dernière date à laquelle ils ont reçu une campagne spécifique. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Reciblage
  - name: Dernière Canvas Step spécifique reçue
    description: Segmente vos utilisateurs en sélectionnant ceux qui ont reçu une Canvas Step spécifique. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Reciblage
  - name: Campagne reçue
    description: Segmente vos utilisateurs selon s’ils ont reçu ou non une campagne donnée.
    tags:
      - Reciblage
  - name: Campaign Variant reçue
    description: Segmente vos utilisateurs en fonction de la variante de campagne multivariée qu’ils ont reçue.
    tags:
      - Reciblage
  - name: Campagne ou Canvas reçu avec balise
    description: Segmente vos utilisateurs selon s’ils ont reçu ou non une campagne ou un Canvas spécifique avec une balise spécifique.
    tags:
      - Reciblage
  - name: Canvas Step reçue
    description: Segmente vos utilisateurs selon s’ils ont reçu ou non une Canvas Step donnée.
    tags:
      - Reciblage
  - name: Vous a marqué comme spam
    description: Segmente vos utilisateurs selon s’ils ont marqué vos messages comme spam.
    tags:
      - Activité de marketing
  - name: Dernière interaction avec un message
    description: Segmente vos utilisateurs en fonction de la dernière fois qu’ils ont ouvert ou cliqué sur l’un de vos messages (e-mail, messages in-app, notification push). (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernière inscription dans un groupe de contrôle
    description: Segmente vos utilisateurs en fonction de la dernière fois qu’ils ont été inscrits dans le groupe de contrôle d’une campagne. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernière impression des messages dans l’application
    description: Segmente vos utilisateurs en déterminant si la dernière impression de message dans l’application a bien été reçue. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernier message reçu
    description: Segmente vos utilisateurs en déterminant si le dernier message a bien été reçu (période de 24 heures)<br><br>Exemple :<br>Dernier message reçu il y a moins de 1 jour = il y a moins de 24 heures<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernier e-mail reçu
    description: Segmente vos utilisateurs en fonction de la dernière fois où ils ont reçu l’un de vos messages par e-mail. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernière notification push reçue
    description: Segmente vos utilisateurs en fonction de la dernière fois où ils ont reçu l’une de vos notifications push. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Dernier webhook reçu
    description: Segmente vos utilisateurs en fonction de la dernière fois que Braze a envoyé un webhook à chaque utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise
    tags:
      - Activité de marketing
  - name: Last Viewed News Feed (Dernier fil d’actualité vu)
    description: Segmente vos utilisateurs en fonction de la dernière fois qu’ils ont consulté l’interface du fil d’actualité de votre application.
    tags:
      - Activité de marketing
  - name: News Feed View Count (Nombre de vues du fil d’actualité)
    description: Segmente vos utilisateurs en fonction du nombre de fois qu’ils ont consulté l’interface du fil d’actualité de votre application.
    tags:
      - Activité de marketing
  - name: Âge
    description: Segmente vos utilisateurs en fonction de leur âge, comme indiqué dans votre application.
    tags:
      - Attributs utilisateur
  - name: Extensions pour Amplitude
    description: Les clients qui utilisent Amplitude pour compléter leurs segments peuvent importer ces extensions et choisir celles qui les intéressent.
    tags:
      - Attributs utilisateur
  - name: Notifications push en arrière-plan activées
    description: Segmente vos utilisateurs selon s’ils ont activé ou non les notifications push en arrière-plan.
    tags:
      - Attributs utilisateur
  - name: Anniversaire
    description: Segmente vos utilisateurs en fonction de leur date d’anniversaire, comme indiqué dans votre application. <br> Les utilisateurs dont l’anniversaire est le 29 février seront inclus dans les segments qui incluent le 1er mars.
    tags:
      - Attributs utilisateur
  - name: Braze Segment Extension
    description: Après avoir créé une Segment Extension dans le tableau de bord de Braze, vous pouvez choisir d’inclure ou d’exclure ces extensions de votre segment.
    tags:
      - Attributs utilisateur
  - name: Ville
    description: Segmente vos utilisateurs en fonction de leur dernière ville indiquée.
    tags:
      - Attributs utilisateur
  - name: Pays
    description: Segmente vos utilisateurs en fonction de leur dernier pays indiqué.
    tags:
      - Attributs utilisateur
  - name: Opérateur mobile
    description: Segmente vos utilisateurs en fonction de leur opérateur mobile.
    tags:
      - Attributs utilisateur
  - name: Nombre d’appareils
    description: Segmente vos utilisateurs en fonction du nombre d’appareils avec lequel ils ont consulté votre application.
    tags:
      - Attributs utilisateur
  - name: Modèle de l’appareil
    description: Segmente vos utilisateurs en fonction de la version du modèle de leur smartphone.
    tags:
      - Attributs utilisateur
  - name: Système d’exploitation de l’appareil
    description: Segmente vos utilisateurs en fonction du système d’exploitation de leur smartphone.
    tags:
      - Attributs utilisateur
  - name: Adresse e-mail disponible
    description: Segmente vos utilisateurs selon s’ils possèdent une adresse e-mail valide, et s’ils sont abonnés/inscrits aux communications par e-mail. Le filtre Email Available (Adresse e-mail disponible) vérifie trois critères&#58; : si l’utilisateur s’est désabonné des communications par e-mail, si Braze a reçu un rebond élevé, et si l’e-mail a été désigné comme spam. Si un utilisateur remplit l’un de ces critères ou si aucune adresse e-mail n’existe pour cet utilisateur, l’utilisateur en question ne sera pas inclus dans le segment.
    tags:
      - Attributs utilisateur
  - name: Date d’abonnement aux e-mails
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont abonnés aux communications par e-mail.
    tags:
      - Attributs utilisateur
  - name: Statut d’abonnement aux e-mails
    description: Segmente vos utilisateurs en fonction du statut de leur abonnement aux communications par e-mail.
    tags:
      - Attributs utilisateur
  - name: Groupes d’abonnement
    description: Segmente vos utilisateurs en fonction de leur groupe d’abonnement aux e-mails ou SMS/MMS. Les groupes archivés ne s’afficheront pas et ne peuvent pas être utilisés.
    tags:
      - Autre
  - name: Date de désinscription aux e-mails
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désabonnés des futures communications par e-mail.
    tags:
      - Attributs utilisateur
  - name: Prénom
    description: Segmente vos utilisateurs en fonction de leur prénom, comme indiqué dans votre application.
    tags:
      - Attributs utilisateur
  - name: Sexe
    description: Segmente vos utilisateurs en fonction de leur sexe, comme indiqué dans votre application.
    tags:
      - Attributs utilisateur
  - name: A une application
    description: Segmente vos utilisateurs selon s’ils ont installé ou non votre application à un moment donné. Cela inclura les utilisateurs qui ont actuellement votre application installée sur leur appareil et ceux qui l’ont désinstallée. 
    tags:
      - Attributs utilisateur
  - name: Langue
    description: Segmente vos utilisateurs en fonction de leur langue préférée.
    tags:
      - Attributs utilisateur
  - name: Nom
    description: Segmente vos utilisateurs en fonction de leur nom de famille, comme indiqué dans votre application.
    tags:
      - Attributs utilisateur
  - name: Localisation disponible
    description: Segmente vos utilisateurs selon s’ils ont indiqué ou non leur localisation. Pour utiliser ce filtre, votre application doit inclure une fonction de <a href="/docs/search/?query=location%20tracking">géolocalisation.</a>
    tags:
      - Attributs utilisateur
  - name: Modèle de montre le plus récent
    description: Segmente vos utilisateurs en fonction du modèle le plus récent de leur montre connectée.
    tags:
      - Attributs utilisateur
  - name: Numéro de téléphone
    description: Segmente vos utilisateurs en fonction de leur numéro de téléphone. Utilisez uniquement les chiffres allant de [0 à 9]. N’ajoutez pas de parenthèses, de tirets, etc.
    tags:
      - Attributs utilisateur
  - name: Notifications push activées
    description: Segmente vos utilisateurs qui ont explicitement activé les notifications push de n’importe quelle application de votre groupe d’apps. Ce compte inclut uniquement les notifications push de premier plan et n’inclut pas les utilisateurs qui se sont désabonnés. <br><br>Après avoir segmenté vos utilisateurs à l’aide de ce filtre, vous pourrez voir une répartition de ceux présents dans ce segment pour Android, iOS et Web dans le panneau inférieur, intitulé <em>Reachable Users (Utilisateurs joignables)</em>.
    tags:
      - Attributs utilisateur
  - name: Notifications push activées pour l’application
    description: Segmente vos utilisateurs selon s’ils ont activées ou non les notifications push de votre application sur leur appareil. Ce compte inclut les notifications push de premier plan et d’arrière-plan.
    tags:
      - Attributs utilisateur
  - name: Date d’activation des notifications push
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils ont activé les notifications push.
    tags:
      - Attributs utilisateur
  - name: Statut d’inscription aux notifications push
    description: Segmente vos utilisateurs en fonction du <a href="/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state">statut de leur inscription</a> aux notifications push.
    tags:
      - Attributs utilisateur
  - name: Date de désinscription aux notifications push
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désinscrits des notifications push.
    tags:
      - Attributs utilisateur
  - name: Numéro de compartiment aléatoire
    description: Segmente vos utilisateurs en utilisant un nombre attribué de manière aléatoire (compris entre 0 et 9 999). Ce filtre permet de créer des segments d’utilisateurs réellement aléatoires et distribués de manière uniforme pour les tests A/B et les tests multivariés.
    tags:
      - Attributs utilisateur
  - name: Mis à jour/importés depuis CSV
    description: Segmente vos utilisateurs selon s’ils font partie d’un téléchargement CSV ou non.
    tags:
      - Attributs utilisateur
  - name: Navigateur Web
    description: Segmente vos utilisateurs en fonction du navigateur Web qu’ils utilisent pour accéder à votre site Internet.
    tags:
      - Attributs utilisateur
  - name: Annonce d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de l’annonce à laquelle leur installation a été attribuée.
    tags:
      - Attributs utilisateur
  - name: Rebond élevé
    description: Segmentez vos utilisateurs selon si leur adresse e-mail a renvoyé un rebond élevé (c.-à-d. une adresse e-mail non valide).
    tags:
      - Attribution d’installation
  - name: Groupe d’annonces d’attribution d’installation
    description: Segmente vos utilisateurs en fonction du groupe d’annonces auquel leur installation a été attribuée.
    tags:
      - Attribution d’installation
  - name: Campagne d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de la campagne publicitaire à laquelle leur installation a été attribuée.
    tags:
      - Attribution d’installation
  - name: Source d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de la source à laquelle leur installation a été attribuée.
    tags:
      - Attribution d’installation
  - name: Connectés à Facebook
    description: Segmente vos utilisateurs qui ont autorisé l’accès à leur compte Facebook depuis votre application.
    tags:
      - Activité sociale
  - name: Connectés à Twitter
    description: Segmente vos utilisateurs qui ont autorisé l’accès à leur compte Twitter depuis votre application.
    tags:
      - Activité sociale
  - name: Nombre d’amis Facebook utilisant l’application
    description: Segmente vos utilisateurs en fonction du nombre de leurs amis Facebook qui utilisent votre application.
    tags:
      - Activité sociale
  - name: Nombre de followers sur Twitter
    description: Segmente vos utilisateurs en fonction du nombre de followers qu’ils ont sur Twitter.
    tags:
      - Activité sociale
  - name: IDFA du dispositif
    description: Ce filtre vous permet de désigner les destinataires de votre campagne par IDFA pour mener des tests.
    tags:
      - Test
  - name: IDFV du dispositif
    description: Ce filtre vous permet de désigner les destinataires de votre campagne par IDFV pour mener des tests.
    tags:
      - Test
  - name: Adresse e-mail
    description: Ce filtre vous permet de désigner les destinataires de votre campagne en fonction de leur adresse e-mail individuelle pour mener des tests. Il peut également être utilisé pour envoyer des e-mails transactionnels à tous vos utilisateurs (y compris les utilisateurs désabonnés) à l’aide du spécificateur « Email Address is not Blank (Adresse e-mail non vide) » dans le filtre.
    tags:
      - Test
  - name: ID utilisateur externe
    description: Ce filtre vous permet de désigner les destinataires de votre campagne en fonction de leurs ID individuels pour mener des tests.
    tags:
      - Test
  - name: Appartenance à un segment
    description: Ce filtre vous permet de filtrer vos utilisateurs en fonction de leur appartenance à un segment qui utilise des filtres (les segments, campagnes, etc.) et cible plusieurs segments différents au sein d’une même campagne. Notez que les segments qui utilisent déjà le filtre Segment Membership (Appartenance à un segment) ne peuvent pas être inclus ou ajoutés dans d’autres segments.
    tags:
      - Autre
  - name: Autorisés provisoirement sur iOS
    description: Ce filtre vous permet de trouver des utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée.
    tags:
      - Autre
  - name: "Canal intelligent"
    description: Filtre la partie de votre audience dont le canal le plus actif (le canal qui a la plus forte probabilité de susciter un engagement sur la base des trois derniers mois ou des activités antérieures de l’utilisateur) est celui que vous sélectionnez dans la liste déroulante : E-mail, Mobile push (Notifications push pour appareils mobiles) ou Web push (Notifications push pour le Web). <br> Vous pouvez également utiliser le filtre Not Enough Data (Données insuffisantes) pour contacter uniquement les utilisateurs ayant reçu des messages provenant d’au moins deux des trois canaux disponibles dans la liste déroulante, mais qui n’ont pas eu suffisamment d’activité sur un canal en particulier pour pouvoir déterminer leur canal préféré. <br> <a href="/docs/user_guide/intelligence/intelligent_channel/">Pour en savoir plus sur ce filtre, cliquez ici.</a> <br> <br> _À partir du <a href="/docs/help/release_notes/2019/november/#intelligence-suite">lancement de produit de novembre 2019</a>, le « canal préféré » a été renommé « canal intelligent »._
    tags:
      - Activité de l’utilisateur
  - name: Suivi des campagnes publicitaires activé
    description: Vous permet de filtrer vos utilisateurs selon si ces derniers ont activé le suivi des campagnes publicitaires. Le suivi des campagnes publicitaires est lié à l’IDFA (Identifier For Advertisers, ou identifiant pour les annonceurs) attribué par Apple pour identifier les appareils des utilisateurs d’iOS. Cet identifiant permet aux annonceurs de suivre les utilisateurs et de leur envoyer des publicités ciblées.
    tags:
      - Test
  - name: Numéro de téléphone non valide
    description: Segmente vos utilisateurs selon si leur numéro de téléphone est valide ou non valide.
    tags:
      - Attributs utilisateur
---
