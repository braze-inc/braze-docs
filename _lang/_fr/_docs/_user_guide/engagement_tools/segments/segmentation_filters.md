---
page_order: 1
nav_title: Filtres de segmentation
article_title: Filtres de segmentation
layout: glossary_page
glossary_top_header: "Filtres de segmentation"
glossary_top_text: Le SDK de Braze vous fournit un arsenal puissant de filtres pour segmenter et cibler vos utilisateurs en fonction de caractéristiques et d'attributs spécifiques. Comme vous pouvez le voir, vous pouvez rechercher ou restreindre ces filtres par catégorie de filtres.
page_type: glossary
tool: Segments
description: "Ce glossaire répertorie les filtres disponibles pour segmenter et cibler vos utilisateurs."
glossary_tag_name: Filtrer la catégorie
glossary_filter_text: "Sélectionnez les catégories ci-dessous pour affiner le glossaire :"
#category to icon/fa or image mapping
glossary_tags:
  - 
    name: Données personnalisées
  - 
    name: Activité de l'utilisateur
  - 
    name: Reciblage
  - 
    name: Activité marketing
  - 
    name: Attributs de l'utilisateur
  - 
    name: Installer Attribution
  - 
    name: Activité sociale
  - 
    name: Tests en cours
  - 
    name: Autres
glossaries:
  - 
    name: Attributs personnalisés
    description: Détermine si un utilisateur correspond ou non à une valeur d'attribut enregistrée personnalisée. (24 heures) <br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Données personnalisées
  - 
    name: Événement personnalisé
    description: Détermine si un utilisateur a effectué ou non un événement enregistré spécialement.<br><br> Exemple :<br>Activité complétée avec la propriété activty_name.<br><br>Fuseau horaire :<br>UTC - Jours du calendrier = 1 jour du calendrier examinera 24-48 heures de l'historique de l'utilisateur
    tags:
      - Données personnalisées
  - 
    name: Premier événement personnalisé
    description: Détermine la première fois qu'un utilisateur a effectué un événement enregistré. (Période 24 heures) <br><br>Exemple :<br> Premier Panier Abandonné moins d'un jour il y a<br><br>Fuseau horaire de la société :<br>Fuseau horaire de la société
    tags:
      - Données personnalisées
  - 
    name: Dernier événement personnalisé
    description: Détermine la dernière fois qu'un utilisateur a effectué un événement enregistré. (Période de 24 heures) <br><br>Exemple :<br> Dernier Panier Abandonné moins d'un jour il y a<br><br>Fuseau horaire de la société :<br>Fuseau horaire de la société
    tags:
      - Données personnalisées
  - 
    name: Dernier SMS reçu
    description: Segments de vos utilisateurs par la dernière fois qu'ils ont reçu un SMS. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: X Événement personnalisé en Y jours
    description:
      - Données personnalisées
  - 
    name: Propriété d'événements personnalisés X en Y jours
    description: Détermine si un utilisateur a effectué ou non un événement enregistré spécialement par rapport à une propriété spécifique, entre 0 et 50 fois dans le dernier nombre de jours du calendrier entre 1 et 30. (Calendar Day = 1 jour du calendrier examinera 24-48 heures de l'historique de l'utilisateur)<br><a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a> <br><br>Exemple :<br> Ajouté aux Favoris avec la propriété "event_name" exactement 0 fois dans le dernier 1 jour du calendrier<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, Un jour du calendrier examinera 24-28 heures de l'historique de l'utilisateur, en fonction de l'heure à laquelle le segment est évalué; pendant 2 jours de calendrier, regardera 48-72 heures de l'historique de l'utilisateur, etc.
    tags:
      - Données personnalisées
  - 
    name: Date de l'évènement récurrent
    description: 'Ce filtre regarde le mois et le jour de l''attribut personnalisé avec le type de données de "date", mais ne regarde pas l''année. Ce filtre est utile pour les événements annuels.<br><br>Fuseau horaire&#58 ;<br>Ce filtre s''ajuste pour n''importe quel fuseau horaire de l''utilisateur.'
    tags:
      - Données personnalisées
  - 
    name: Premier achat
    description: Segments de vos utilisateurs dans les plus brefs délais enregistrés qu'ils ont fait un achat dans votre application. (24 heures)<br><br>Fuseau horaire :<br>UTC
    tags:
      - Activité de l'utilisateur
  - 
    name: Premier achat pour l'application
    description: Segments que vos utilisateurs ont enregistrés le plus tôt temps qu'ils ont acheté n'importe quel élément de votre application. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Premier produit acheté
    description: Segments de vos utilisateurs dès le plus tôt temps enregistré qu'ils ont acheté un élément spécifique de votre application (adhésion spéciale, certificat cadeau, etc…). (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Première application utilisée
    description: Segmente vos utilisateurs par le plus tôt temps enregistré où ils ont ouvert votre application. <em>Notez que cela va capturer la première session qu'ils ont en utilisant une version de votre application avec le SDK Braze intégré.</em> (période 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la société
    tags:
      - Activité de l'utilisateur
  - 
    name: Première application spécifique utilisée
    description: Segments de vos utilisateurs dès le plus jeune moment où ils ont ouvert l'une de vos applications dans votre groupe d'applications. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Dernier achat
    description: Segmente vos utilisateurs par le moment le plus récent où ils ont effectué un achat dans votre application. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Dernier achat pour l'app
    description: Segmente vos utilisateurs par la dernière fois qu'ils ont acheté un article de votre application. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Dernier produit acheté
    description: Segmente vos utilisateurs par la dernière fois qu'ils ont acheté un article spécifique de votre application (adhésion spéciale, certificat cadeau, etc…). (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Dernière application utilisée
    description: Segmente vos utilisateurs par la période la plus récente où ils ont ouvert votre application. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Dernière application spécifique utilisée
    description: Segmente vos utilisateurs par le moment le plus récent où ils ont ouvert une application spécifique et désignée. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité de l'utilisateur
  - 
    name: Durée de la session médiane
    description: Segmente vos utilisateurs par la durée médiane de leurs sessions dans votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Argent dépensé
    description: Segmente vos utilisateurs par le montant d'argent qu'ils ont dépensé dans votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Version de l'application la plus récente
    description: Segmente vos utilisateurs par la dernière version de votre application qu'ils ont utilisée.
    tags:
      - Activité de l'utilisateur
  - 
    name: Code de version de l'application
    description: "Filtres de code de version de l'application basés sur les numéros de version de votre application. Ce filtre prend en charge les comparaisons numériques pour cibler une gamme de versions d'applications. Par exemple, vous pouvez filtrer en utilisant « ci-dessous», « ci-dessus» et « égal à» certaines versions de l’application. Le support de cette fonctionnalité est disponible avec Braze Android SDK v3.6.0 et plus récent, et peut être activé par votre gestionnaire de compte Braze."
    tags:
      - Activité de l'utilisateur
  - 
    name: Lieu le plus récent
    description: Segments de vos utilisateurs par le dernier emplacement enregistré où ils ont utilisé votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Produit acheté
    description: Segments de vos utilisateurs par produits achetés dans votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Nombre de sessions
    description: Segmente vos utilisateurs par le nombre de sessions qu'ils ont eues dans n'importe laquelle de vos applications dans votre groupe d'applications.
    tags:
      - Activité de l'utilisateur
  - 
    name: Nombre de sessions pour l'application
    description: Segments de vos utilisateurs par le nombre de sessions qu'ils ont eues dans une application spécifique et désignée.
    tags:
      - Activité de l'utilisateur
  - 
    name: Nombre total d'Achats
    description: Segmente vos utilisateurs en fonction du nombre d'achats qu'ils ont effectués dans votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Date de désinstallation
    description: Segmente vos utilisateurs en fonction de la date de désinstallation de votre application.
    tags:
      - Activité de l'utilisateur
  - 
    name: Désinstallé
    description: Segmente vos utilisateurs en fonction de s'ils ont désinstallé votre application et ne l'ont pas réinstallée.
    tags:
      - Activité de l'utilisateur
  - 
    name: X Argent dépensé dans les derniers Y Jours
    description: Segmente vos utilisateurs par le montant d'argent qu'ils ont dépensé dans votre application dans le dernier nombre de jours de calendrier entre 1 et 30. Ce montant ne comprendra que la somme des 50 derniers achats. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a>
    tags:
      - Activité de l'utilisateur
  - 
    name: Produit X acheté au cours des Y derniers jours
    description: Segments de vos utilisateurs par le nombre de fois (entre 0 et 50) qu'ils ont acheté un élément spécifique à votre application dans le dernier nombre de jours de calendrier entre 1 et 30 (adhésion spéciale, certificat cadeau, etc…). <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a>
    tags:
      - Activité de l'utilisateur
  - 
    name: X Achat de propriété en Y Jours
    description: Segments de vos utilisateurs par le nombre de fois qu'un achat a été effectué par rapport à une certaine propriété d'achat dans le dernier nombre de jours calendaires spécifiés entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a>
    tags:
      - Activité de l'utilisateur
  - 
    name: X Achats au cours des derniers Y jours
    description: Segments de vos utilisateurs par le nombre de fois (entre 0 et 50) qu'ils ont fait un achat dans le dernier nombre spécifié de jours de calendrier entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a>
    tags:
      - Activité de l'utilisateur
  - 
    name: X sessions dans les derniers Y jours
    description: Segmente vos utilisateurs par le nombre de sessions (entre 0 et 50) qu'ils ont eu dans votre application au cours du dernier nombre spécifié de jours de calendrier entre 1 et 30. <br> <a href="/docs/x-in-y-behavior/">En savoir plus sur le comportement X-in-Y ici.</a>
    tags:
      - Activité de l'utilisateur
  - 
    name: Carte cliquée
    description: Segmente vos utilisateurs par s'ils ont cliqué sur une carte ou une promotion spécifique.
    tags:
      - Reciblage
  - 
    name: Campagne cliquée/ouverte
    description: Segmente vos utilisateurs selon qu'ils ont ou non interagi avec une campagne spécifique.
    tags:
      - Reciblage
  - 
    name: Campagne ou Canvas avec étiquette cliqué/ouverte
    description: Segmente vos utilisateurs selon qu'ils ont ou non interagi avec une campagne spécifique ou Canvas avec un tag spécifique.
    tags:
      - Reciblage
  - 
    name: Étape cliquée/ouverte
    description: Segmente vos utilisateurs selon qu'ils ont ou non interagi avec une étape spécifique de Canvas .
    tags:
      - Reciblage
  - 
    name: Converti de la campagne
    description: Segmente vos utilisateurs en fonction de s'ils ont ou non converti sur une campagne spécifique.
    tags:
      - Reciblage
  - 
    name: Converti depuis Canvas
    description: Segmente vos utilisateurs en fonction de s'ils ont ou non converti sur une toile spécifique.
    tags:
      - Reciblage
  - 
    name: Variation de la toile entrée
    description: Segmente vos utilisateurs selon qu'ils ont ou non entré un chemin de variation d'un Canvas spécifique.
    tags:
      - Reciblage
  - 
    name: N'a jamais reçu l'étape d'une campagne ou d'une toile
    description: Segmente vos utilisateurs en fonction de s'ils ont ou non reçu une campagne ou une étape de Canvan.
    tags:
      - Reciblage
  - 
    name: Groupe de contrôle de campagne
    description: Segmente vos utilisateurs selon qu'ils étaient ou non dans le groupe de contrôle pour une campagne multivariée spécifique.
    tags:
      - Reciblage
  - 
    name: Dans le Groupe de Contrôle de Canvas
    description: Segmente vos utilisateurs selon qu'ils étaient ou non dans le groupe de contrôle pour un Canva spécifique.
    tags:
      - Reciblage
  - 
    name: N'est pas dans le segment
    description: Segmente vos utilisateurs en fonction de s'ils sont inclus ou non dans un segment existant.
    tags:
      - Reciblage
  - 
    name: Dernière campagne ou toile reçue avec étiquette
    description: Segmente vos utilisateurs quand ils ont reçu une campagne spécifique ou Canvas avec un tag spécifique. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Reciblage
  - 
    name: Dernière campagne spécifique reçue
    description: Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont reçu une campagne spécifique. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Reciblage
  - 
    name: Dernière étape de Canvas Spécifique Reçu
    description: Segmente vos utilisateurs en sélectionnant ceux qui ont reçu un Canvas Step. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Reciblage
  - 
    name: Campagne reçue
    description: Segmente vos utilisateurs selon qu'ils ont ou non reçu une campagne spécifique.
    tags:
      - Reciblage
  - 
    name: Variante de campagne reçue
    description: Segments de vos utilisateurs par lesquels la variante d'une campagne multivariée qu'ils ont reçue.
    tags:
      - Reciblage
  - 
    name: Campagne reçue ou Canvas avec étiquette
    description: Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique ou Canvas avec un tag spécifique.
    tags:
      - Reciblage
  - 
    name: Étape de la toile reçue
    description: Segmente vos utilisateurs selon qu'ils ont ou non reçu ou non une étape de Canvas spécifique.
    tags:
      - Reciblage
  - 
    name: Vous a marqué comme spam
    description: Segmente vos utilisateurs en fonction de s'ils ont marqué ou non vos messages comme spams.
    tags:
      - Activité marketing
  - 
    name: Dernier engagement avec le message
    description: Segmente vos utilisateurs par la dernière fois qu'ils ont cliqué ou ouvert un de vos canaux de messagerie (e-mail, dans l'application, push). (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Dernier inscrit dans n'importe quel groupe de contrôle
    description: Segments de vos utilisateurs pour la dernière fois qu'ils sont tombés dans le groupe de contrôle dans une campagne. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Impression du dernier message dans l'application
    description: Segments de vos utilisateurs en déterminant la dernière impression de message dans l'application a été reçue. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Dernier message reçu
    description: Segmente vos utilisateurs en déterminant le dernier message reçu. (Période de 24 heures)<br><br>Exemple :<br>Dernier Message Reçu Il y a moins d'un jour = il y a moins de 24 heures<br><br>Fuseau horaire de la société :<br>Fuseau horaire de l'entreprise
    tags:
      - Activité marketing
  - 
    name: Dernier e-mail reçu
    description: Segments de vos utilisateurs pour la dernière fois qu'ils ont reçu un de vos courriels. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Dernier Push reçu
    description: Segmente vos utilisateurs par la dernière fois qu'ils ont reçu une de vos notifications push. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Dernier Webhook reçu
    description: Segments de vos utilisateurs par la dernière fois que Braze a envoyé un webhook pour cet utilisateur. (24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de la compagnie
    tags:
      - Activité marketing
  - 
    name: Dernier fil d'actualité consulté
    description: Segmente vos utilisateurs pour la dernière fois qu'ils ont visité l'interface du fil d'actualité de votre application.
    tags:
      - Activité marketing
  - 
    name: Nombre de nouvelles vues de flux
    description: Segmente vos utilisateurs par le nombre de fois qu'ils ont consulté l'interface du fil d'actualité de votre application.
    tags:
      - Activité marketing
  - 
    name: Âge
    description: Segmente vos utilisateurs selon leur âge, comme ils l'ont indiqué dans votre application.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Extension d'Amplitude
    description: Les clients qui utilisent Amplitude pour compléter leurs segments peuvent importer et choisir parmi ces exntensions.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Push d'arrière-plan activé
    description: Segmente vos utilisateurs sur s'ils ont activé ou non le push en arrière-plan.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Date d'anniversaire
    description: Segments de vos utilisateurs d'ici leur anniversaire, comme ils l'ont indiqué dans votre application. <br> Les utilisateurs ayant un anniversaire le 29 février seront inclus dans les segments y compris le 1er mars.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Extension du segment de Braze
    description: Après avoir créé une extension de segment dans le tableau de bord de Braze, vous pouvez choisir d'inclure/exclure ces extensions dans votre segment.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Ville
    description: Segmente vos utilisateurs par leur dernier emplacement de ville.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Pays
    description: Segmente vos utilisateurs par leur dernier emplacement de pays indiqué.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Transporteur de l'appareil
    description: Segmente vos utilisateurs par leur opérateur de périphérique.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Nombre d'appareils
    description: Segmente vos utilisateurs en fonction du nombre d'appareils sur lesquels votre application a été utilisée.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Modèle de l'appareil
    description: Segmente vos utilisateurs par la version modèle de leur téléphone mobile.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Système d'exploitation de l'appareil
    description: Segmente vos utilisateurs par le système d'exploitation de leur téléphone mobile.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Courriel disponible
    description: 'Segmente vos utilisateurs en fonction de s''ils ont ou non une adresse e-mail valide, et s''ils sont abonnés/optés à l''email. Le filtre de courriel disponible vérifie trois critères&#58; si l''utilisateur est désabonné des e-mails, si Braze a reçu un bounce dur, et si l''e-mail a été marqué comme spam. Si l''un de ces critères est satisfait, ou si un email n''existe pas pour un utilisateur, l''utilisateur ne sera pas inclus.'
    tags:
      - Attributs de l'utilisateur
  - 
    name: Date d'activation de l'e-mail
    description: Segments de vos utilisateurs avant la date à laquelle ils ont choisi de recevoir des e-mails.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Statut de l'abonnement par courriel
    description: Segmente vos utilisateurs par leur statut d'abonnement pour l'email.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Groupes d'Abonnement
    description: Segments de vos utilisateurs par leur groupe d'abonnement pour e-mail ou SMS/MMS. Les groupes archivés n'apparaîtront pas et ne pourront pas être utilisés.
    tags:
      - Autres
  - 
    name: Date de désinscription par e-mail
    description: Segments de vos utilisateurs avant la date à laquelle ils se sont désabonnés de futurs e-mails.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Prénom
    description: Segmente vos utilisateurs par leur prénom, comme ils l'ont indiqué dans votre application.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Sexe
    description: Segmente vos utilisateurs par sexe, comme indiqué dans votre application.
    tags:
      - Attributs de l'utilisateur
  - 
    name: A une application
    description: Segments selon si un utilisateur a déjà installé ou non votre application. Cela inclura les utilisateurs qui ont actuellement votre application installée et ceux qui ont désinstallé dans le passé.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Langue
    description: Segments de vos utilisateurs par leur langue préférée.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Nom de famille
    description: Segmente vos utilisateurs par leur nom de famille, comme ils l'ont indiqué dans votre application.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Localisation disponible
    description: Segmente vos utilisateurs en fonction de s'ils ont signalé ou non leurs emplacements. Afin d'utiliser ce filtre, votre application a besoin que <a href="/docs/search/?query=location%20tracking">le suivi de localisation soit intégré.</a>
    tags:
      - Attributs de l'utilisateur
  - 
    name: Modèle de veille le plus récent
    description: Segments de vos utilisateurs par leur dernier modèle intelligent.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Numéro de téléphone
    description: Segmente vos utilisateurs par leur numéro de téléphone. Utilisez uniquement des chiffres [0-9]. Ne pas inclure les parenthèses, tirets, etc.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Push activé
    description: Segmente vos utilisateurs qui ont explicitement activé les notifications push pour toutes les applications de votre groupe d'applications. Ce nombre ne comprend que la poussée en premier plan, et n'inclut pas les utilisateurs qui se sont désabonnés. <br><br>Après la segmentation avec ce filtre, vous serez en mesure de voir une ventilation de qui est dans ce segment pour Android, iOS, et web dans le panneau inférieur, appelé <em>Utilisateurs accessibles</em>.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Push activé pour l'application
    description: Segments selon si votre utilisateur a activé ou non pour votre application sur son appareil. Ce nombre comprend à la fois la poussée en premier et en arrière-plan.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Date d'Opt-In Push
    description: Segments de vos utilisateurs à la date à laquelle ils ont choisi push.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Statut de l'abonnement Push
    description: 'Segmente vos utilisateurs par leur <a href="/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state">statut d''abonnement</a> pour push.'
    tags:
      - Attributs de l'utilisateur
  - 
    name: Date de désinscription
    description: Segmente vos utilisateurs avant la date à laquelle ils se sont désabonnés des futures notifications push.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Nombre aléatoire de Seaux
    description: Segmente vos utilisateurs par un nombre assigné aléatoirement (0 à 9999 inclus). Il peut permettre la création de segments uniformément distribués d'utilisateurs vraiment aléatoires pour les tests A/B et multivariés.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Mise à jour/Importé à partir de CSV
    description: Segments de vos utilisateurs en fonction du fait qu'ils faisaient ou non partie d'un téléchargement CSV.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Navigateur Web
    description: Segments de vos utilisateurs par le navigateur Web qu'ils utilisent pour accéder à votre site Web.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Installer la pub d'attribution
    description: Segmente vos utilisateurs par la publicité à laquelle leur installation a été attribuée.
    tags:
      - Attributs de l'utilisateur
  - 
    name: Bounce dur
    description: Segmentez vos utilisateurs en fonction si leur adresse e-mail a un rebond dur (c'est-à-dire que l'adresse e-mail n'est pas valide).
    tags:
      - Installer Attribution
  - 
    name: Installer le groupe d'attribution
    description: Segments de vos utilisateurs par le groupe de publicités auquel leur installation a été attribuée.
    tags:
      - Installer Attribution
  - 
    name: Installer la campagne d'attribution
    description: Segmente vos utilisateurs par la campagne publicitaire à laquelle leur installation a été attribuée.
    tags:
      - Installer Attribution
  - 
    name: Installer la source d'attribution
    description: Segmente vos utilisateurs par la source à laquelle leur installation a été attribuée.
    tags:
      - Installer Attribution
  - 
    name: Connecté à Facebook
    description: Segmente vos utilisateurs qui ont donné accès à votre compte Facebook dans votre application.
    tags:
      - Activité sociale
  - 
    name: Connecté à Twitter
    description: Segmente vos utilisateurs qui ont accordé l'accès à votre compte Twitter dans votre application.
    tags:
      - Activité sociale
  - 
    name: Nombre d'amis Facebook utilisant l'application
    description: Segmente vos utilisateurs par le nombre d'amis qu'ils ont sur Facebook qui utilisent votre application.
    tags:
      - Activité sociale
  - 
    name: Nombre de suiveurs Twitter
    description: Segmente vos utilisateurs par le nombre de suiveurs qu'ils ont sur Twitter.
    tags:
      - Activité sociale
  - 
    name: Périphérique IDFA
    description: Vous permet de désigner les destinataires de votre campagne par IDFA pour les tests.
    tags:
      - Tests en cours
  - 
    name: Périphérique IDFV
    description: Vous permet de désigner les destinataires de votre campagne par IDFV pour les tests.
    tags:
      - Tests en cours
  - 
    name: Adresse e-mail
    description: Vous permet de désigner les destinataires de votre campagne par des adresses e-mail individuelles pour les tests. Ceci peut également être utilisé pour envoyer des courriels transactionnels à tous vos utilisateurs (y compris ceux qui se sont désabonnés) en utilisant le spécificateur « Adresse e-mail n'est pas vide » dans le filtre.
    tags:
      - Tests en cours
  - 
    name: ID d'utilisateur externe
    description: Vous permet de désigner les destinataires de votre campagne par des identifiants individuels pour les tests.
    tags:
      - Tests en cours
  - 
    name: Adhésion au segment
    description: Vous permet de filtrer en fonction de l'appartenance à un segment où les filtres sont utilisés (segments, campagnes, etc.) et de cibler plusieurs segments différents au sein d'une seule campagne. Veuillez noter que les segments qui utilisent déjà le filtre d'abonnement de segment ne peuvent pas être inclus ou imbriqués dans d'autres segments.
    tags:
      - Autres
  - 
    name: Autorisé provisoirement sur iOS
    description: Permet de trouver des utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée.
    tags:
      - Autres
  - 
    name: "Canal Intelligent"
    description: 'Filtre la portion de votre auditoire dont le canal le plus actif (le canal qui a la plus grande probabilité d''engagement étant donné les trois derniers mois de l''utilisateur ou l''activité) est celui que vous sélectionnez dans la liste déroulante suivante (Email), Push mobile, ou Push Web). <br> Vous pouvez également choisir de filtrer par données insuffisantes, qui envoie uniquement aux utilisateurs qui ont reçu des messages d''au moins deux des trois canaux disponibles dans la liste déroulante, mais qui n''ont pas eu assez d''activité distincte pour déterminer un canal le plus engagé. <br> <a href="/docs/user_guide/intelligence/intelligent_channel/">En savoir plus sur ce filtre ici.</a> <br> <br> À partir de la <a href="/docs/help/release_notes/2019/november/#intelligence-suite">version de produit de novembre 2019</a>, ''Chaîne la plus gagnée'' a été renommée en ''Chaîne intelligente''._'
    tags:
      - Activité de l'utilisateur
  - 
    name: Suivi des publicités activé
    description: Vous permet de filtrer selon si vos utilisateurs ont opté pour le suivi des annonces. Le suivi des publicités se rapporte à l'IDFA ou "identifiant pour les annonceurs" attribué à tous les appareils iOS par Apple. Cet identifiant permet aux annonceurs de suivre les utilisateurs et de les diffuser des publicités ciblées.
    tags:
      - Tests en cours
---

