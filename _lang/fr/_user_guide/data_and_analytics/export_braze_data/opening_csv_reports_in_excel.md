---
nav_title: Ouverture des rapports CSV dans Excel
article_title: Ouverture des rapports CSV dans Excel 
page_order: 9
page_type: reference
description: "Cet article de référence explique comment ouvrir les exportations CSV dans Excel."

---

# Ouverture des exports CSV dans Excel

## Définir Excel comme programme par défaut

Alors que les fichiers CSV sont généralement ouverts automatiquement dans Excel par défaut, ce n’est parfois pas le cas sous Windows 7. Reportez-vous à cette [article de dépannage][20] pour la procédure à suivre pour définir Excel comme programme par défaut pour les CSVs sur Windows 7.

## Conversion CSV vers XLSX ou XLS

Pour convertir un CSV en XLSX ou XLS, ou supprimer la virgule entre les valeurs de données, reportez-vous à [ce guide][19] sur l’importation de CSV dans Excel.

## Zéros à gauche retirées des ID Utilisateur

Vous remarquerez parfois que les zéros de tête sont supprimés des ID Utilisateur dans votre exportation CSV. Cela se produit parce que Excel traite les nombres dans un CSV comme des données, et non pas comme du texte. Pour résoudre ce problème, exécutez [l’Assistant d’importation de texte Excel][22].


[19]: https://www.ablebits.com/office-addins-blog/2014/05/01/convert-csv-excel/#import-csv-wizard
[20]: http://www.solveyourtech.com/how-to-open-csv-files-with-excel-by-default/
[22]: https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros
