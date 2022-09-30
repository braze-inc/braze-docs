Chez Braze, nous **recommandons vivement** de nommer les ID utilisateur, également connus sous le nom de `external_user_ids`, dans un format [UUID/GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). Les UUID/GUID sont des identificateurs uniques universellement composés d’un nombre de 128 bits servant à identifier les informations dans les systèmes informatiques. Cela signifie que ces UUID sont longs, aléatoires et bien distribués. Si vous choisissez une méthode différente pour nommer vos ID utilisateur, ces ID doivent également être longs, aléatoires et bien distribués. Il est également important de noter que les ID utilisateur sont **sensibles à la casse**. Par exemple, « Abcdef » est un utilisateur différent de « abcdef ».

Si vous constatez que vos `external_user_ids` incluent des noms, adresses e-mail, horodatages ou incrémenteurs, nous vous **recommandons vivement** de choisir une nouvelle méthode de dénomination qui soit plus sécurisée. Nous ne voulons pas que des noms, adresses e-mail, horodatages ou incrémenteurs soient inclus dans vos ID utilisateur. En effet, les personnes au sein de votre organisation pourraient alors sans difficulté identifier rapidement les autres utilisateurs, **ce qui n’en fait pas une méthode sûre**.

Si vous fournissez ces informations à d’autres personnes, des individus extérieurs à votre organisation risquent de collecter des informations sur la manière dont vos ID utilisateur sont structurés. Votre organisation serait alors exposée à des mises à jour potentiellement malveillantes ou à la suppression d’informations. Le choix de la convention de dénomination correcte dès le début est l’une des étapes les plus importantes de la configuration des ID d’utilisateur, mais il est possible d’effectuer une migration en utilisant notre [endpoint d’API de migration de l’ID externe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Dénomination des ID utilisateur |
| Exemple correct | Exemple incorrect |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 83nmas45-eks1-083m-mk36-426655440000 | Anna@e-mail.com |
| Mbfjla32-937z-09es-sbv6-064026245228 | NomSociété-1-2-19 |
| k6twn923-8234-7354-lzpd-139317000652 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}