En Braze, **recomendamos encarecidamente** nombrar los ID de usuario, también denominados ID externos, en formato [UUID y GUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). Los UUID y GUID son identificadores únicos universales que consisten en un número de 128 bits utilizado para identificar información en sistemas informáticos. Esto significa que estos UUID son largos, aleatorios y están bien distribuidos. Si eliges un método diferente para nombrar tus ID de usuario, también deben ser largos, aleatorios y estar bien distribuidos. También es importante tener en cuenta que los ID de usuario **distinguen entre mayúsculas y minúsculas**. Por ejemplo, "Abcdef" es un usuario distinto de "abcdef".

Si descubres que tus ID de usuario incluyen nombres, direcciones de correo electrónico, marcas de tiempo o incrementadores, te sugerimos que utilices un nuevo método de asignación de nombres que sea más seguro para que tus ID de usuario no sean tan fáciles de adivinar o suplantar. Si decides incluir esto en tus ID de usuario, **te recomendamos encarecidamente** que añadas nuestra característica [de autenticación SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/) para evitar la suplantación de identidad de usuarios.

Facilitar esta información a terceros puede permitir que personas ajenas a tu organización obtengan información sobre cómo están estructurados tus ID de usuario, exponiendo a tu organización a actualizaciones potencialmente maliciosas o a la eliminación de información. Elegir la convención de nomenclatura correcta desde el principio es uno de los pasos más importantes en la configuración de los ID de usuario. Sin embargo, es posible realizar una migración utilizando nuestro [punto final de migración de ID externo]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Nomenclatura de ID de usuario |
| Recomendado | No recomendado |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | NombreEmpresa-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}