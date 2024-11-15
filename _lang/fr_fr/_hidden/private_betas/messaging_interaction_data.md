---
nav_title: "Données d'interaction de messagerie"
article_title: "Données d'interaction de messagerie"
permalink: "/messaging_interaction_data/"
hidden: true
---

# Disponibilité des données d'interaction de messagerie

> Cet article présente des informations sur les données d'interaction des campagnes et des canvas, ainsi que leur disponibilité.

### Qu'est-ce que les données d'interaction de messagerie ?

Les données d'interaction de messagerie se réfèrent à la manière dont un utilisateur interagit avec une campagne ou un Canvas qu'il a reçu (par exemple, lorsqu'un utilisateur ouvre la campagne A ou qu'un utilisateur reçoit la variante A). Ces données sont utilisées pour le reciblage.

{% alert important %}
À partir de début 2024, les données d'interaction de messagerie seront disponibles selon le processus décrit ici.
{% endalert %}

### Quand les données d'interaction de messagerie sont-elles disponibles ?

Les données d'interaction sont toujours disponibles. Pour les campagnes et les canvas actifs, les données d'interaction sont toujours disponibles en temps réel. 

Pour les campagnes et les Canvases arrêtés, leurs données d'interaction expirent après trois mois, sauf si elles sont utilisées dans des filtres de reciblage par des campagnes ou des Canvases actifs. Les données d'interaction expirées sont déplacées vers le stockage à long terme et ne sont pas disponibles pour une utilisation à moins d'être restaurées en utilisant le processus décrit ci-dessous.

Les données d'interaction expirées ne sont jamais supprimées et peuvent être restaurées à tout moment.

#### Fonctionnalités qui utilisent des données d'interaction

Les fonctionnalités suivantes utilisent les données d'interaction de messagerie :

- Filtres de reciblage qui reciblent sur une campagne ou un canvas spécifique
    - Alias cliqué dans la campagne
    - Alias cliqué dans l'étape de Canvas
    - Campagne cliquée/ouverte
    - Étape cliquée/ouverte
    - Convertis par la campagne
    - Convertis par le Canvas
    - Entrés dans une variante du Canvas
    - Dans le groupe de contrôle de campagne
    - Dans le groupe de contrôle de Canvas
    - Dernier message reçu d’une campagne donnée
    - Dernier message reçu de l’étape du canvas donnée
    - Variante de campagne reçue
    - Message reçu de la campagne
    - A reçu un message de l’étape du canvas
- Filtres de reciblage qui reciblent sur des campagnes ou des canvas d'une certaine étiquette
    - A reçu un message d’une campagne ou d’un canvas avec une balise
    - Campagne ou Canvas avec balise cliqué(e)/ouvert(e)
    - A reçu un message pour la dernière fois d’une campagne ou d’un canvas avec une balise
- Listes **Campagnes reçues** et **Messages de canvas reçus** sur le profil utilisateur
- `/users/export` point d'extrémité
- **Données utilisateur** Exportations CSV sur les pages de résumé de campagne et de Canvas

Ces fonctionnalités n'incluront pas les données d'interaction expirées dans leurs résultats. Pour inclure les données d'interaction expirées dans les résultats de ces fonctionnalités, restaurez la campagne ou le Canvas avec les données expirées.

#### Fonctionnalités qui n'utilisent pas les données d'interaction

Les fonctionnalités suivantes **ne** utilisent pas les données d'interaction de messagerie, ce qui signifie que ces fonctionnalités ne sont pas affectées par l'expiration des données d'interaction de messagerie :

- Configuration de la campagne et de la toile
- Analyses de campagne et de Canvas
- Rapports d'analyse (tels que le générateur de rapports, le générateur de requêtes et les rapports d’engagement)
- Currents
- Partage de données Snowflake
- Extensions de segments
- Points de données
- Les filtres de reciblage suivants :
    - Alias cliqué dans n'importe quelle campagne ou étape de canvas
    - Indicateurs de fonctionnalité
    - Échec d'envoi définitif
    - Vous a marqué comme spam
    - N’a jamais reçu un message issu d’une campagne ou d’une étape de canvas
    - Numéro de téléphone non valide
    - Dernière interaction avec un message
    - Dernière inscription dans un groupe de contrôle
    - Dernière impression des messages in-app
    - Dernier message reçu
    - Dernier e-mail reçu 
    - Dernière notification push reçue
    - Dernier SMS reçu
    - Dernier webhook reçu
    - Dernière réception WhatsApp
    - Dernier envoi SMS spécifique Entrant Catégorie de mot-clé
    - Dernier fil d’actualité vu
    - News Feed View Count (Nombre de vues du fil d’actualité)

### Comment puis-je restaurer les données d'interaction de messagerie ?

Pour restaurer vos données d'interaction, suivez ces étapes :

1. Allez à la campagne expirée ou à Canvas.
2. En haut de la page de campagne ou de la page de destination de Canvas, cliquez sur **Restaurer les données d'interaction** dans la bannière.

![][1]

Vous pouvez également restaurer les données d'interaction pour plusieurs campagnes depuis la page Campagnes en sélectionnant les campagnes et en cliquant sur le bouton Restaurer les données d'interaction.

Ceci varie en fonction du temps nécessaire pour restaurer les données d'interaction, mais dans la plupart des cas, ce processus peut prendre de 5 à 15 minutes. Vous recevrez un e-mail après la fin de la restauration.

#### Restauration par étiquette

Vous pouvez également restaurer les données d'interaction pour les campagnes ou les Canvases expirés avec une balise donnée.

1. Allez à la page **Campagnes** ou **Canvas** et recherchez par le tag pertinent.
2. Sélectionnez vos campagnes ou toiles.
3. Sélectionnez **Restaurer les données d'interaction** pour restaurer les données de ces campagnes ou Canvases.

Après trois autres mois d'inactivité, ces campagnes ou Canvases expireront à nouveau.

#### Reciblage par étiquette

Les campagnes qui utilisent des filtres de reciblage par étiquette ne sont pas exemptes d'expiration. Les filtres de reciblage par étiquette incluent :

- A reçu un message d’une campagne ou d’un canvas avec une balise
- Campagne ou Canvas avec balise cliqué(e)/ouvert(e)
- A reçu un message pour la dernière fois d’une campagne ou d’un canvas avec une balise

### Quand les données d'interaction de messagerie étaient-elles disponibles dans le passé ?

Auparavant, les données d'interaction des messages étaient supprimées lorsqu'une campagne ou un canvas :
- N'avait pas envoyé de messages en 25 mois calendaires, ET
- N'avait pas été utilisé pour le reciblage dans des campagnes, des canvas ou des cartes de contenus actifs.

Les campagnes et les toiles avec des données d'interaction de messagerie précédemment supprimées ne peuvent pas être utilisées dans les filtres de reciblage pour les campagnes, les toiles et les segments.

[1]: {% image_buster /assets/img/restore_interaction_data.png %}
