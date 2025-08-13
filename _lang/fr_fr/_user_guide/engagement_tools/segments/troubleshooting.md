---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de segments
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Cet article de référence couvre les étapes de résolution des problèmes et les considérations à garder à l'esprit lors de l'utilisation des segments."
---

# Résolution des problèmes de segmentation

## Comportement des utilisateurs

### L'utilisateur n'est plus dans une segmentation

Si un utilisateur n'est pas disponible lors de la création d'un segment, les données utilisateur qui déterminent son éligibilité au segment peuvent avoir changé en raison de sa propre activité ou d'autres campagnes et canevas avec lesquels il a interagi précédemment. Si la rééligibilité est activée, leur profil utilisateur affichera les données les plus récentes de la campagne reçue.

### Les informations s'affichent pour les utilisateurs d'autres applications lorsque je filtre pour une application spécifique

Les utilisateurs peuvent avoir plusieurs applications, donc en sélectionnant une application spécifique dans la section **Apps utilisées de** la page de segmentation, vous obtiendrez des résultats pour les utilisateurs qui ont au moins cette application. Le filtre ne donne pas de résultats pour les utilisateurs qui ont exclusivement cette application.

## Analyses et rapports

### Les *messages envoyés* ou les *destinataires uniques* dans Campaign Analytics ne correspondent pas au nombre de segments. 

Si le nombre de *messages envoyés* ou de *destinataires uniques* de votre analyse de campagne ne correspond pas au nombre d'utilisateurs dans le filtre du segment `Has received message from campaign X`, il peut y avoir deux raisons à cela :

1. **Les utilisateurs peuvent avoir été archivés, rendus orphelins ou supprimés depuis le lancement de la campagne.**<br><br>Par exemple, admettons que 1 000 utilisateurs reçoivent une campagne et que vous fassiez une exportation CSV le même jour. Vous verrez que 1 000 utilisateurs ont été signalés. Au cours du mois suivant, 50 de ces 1 000 utilisateurs sont supprimés (par exemple, par l'endpoint `users/delete`). Lorsque vous effectuez une autre exportation CSV, vous verrez 950 utilisateurs déclarés alors que le nombre de *destinataires uniques* dans **Campaign Analytics** est toujours de 1 000.<br><br>En d'autres termes, la mesure des *destinataires uniques* est un décompte incrémenté, tandis que le segmentateur et l'exportation CSV fournissent un décompte des utilisateurs existants.<br><br>

2. **La campagne est rééligible, de sorte que les utilisateurs peuvent participer plusieurs fois à la campagne**<br><br>Prenons l'exemple d'une campagne e-mail dont la rééligibilité est définie sur zéro minute (les utilisateurs peuvent réintégrer la campagne tant qu'ils répondent aux exigences de segmentation de l'audience), et qui est en cours depuis plus d'un mois. Le nombre de *messages envoyés* dans **Campaign Analytics** ne correspondrait pas à celui du segment, car ce champ inclurait les messages envoyés à des utilisateurs en double.<br><br>En effet, Braze comptabilise les utilisateurs uniques en tant que *destinataires uniques quotidiens*, c'est-à-dire le nombre d'utilisateurs ayant reçu un message particulier au cours d'une journée. Cela signifie que les utilisateurs rééligibles seront comptés plus d'une fois en tant que destinataire unique, car la fenêtre "unique" ne dure qu'un jour. Le nombre de *destinataires uniques quotidiens* peut ainsi être supérieur au nombre de profils utilisateurs dans l'exportation CSV. Les profils utilisateurs figurant dans le fichier CSV seront véritablement uniques.