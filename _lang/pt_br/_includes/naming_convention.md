No Braze, **recomendamos enfaticamente** nomear os IDs de usuário, também chamados de IDs externos, em um formato [UUIDs e GUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier). UUIDs e GUIDs são identificadores universalmente exclusivos que consistem em um número de 128 bits usado para identificar informações em sistemas de computador. Isso significa que esses UUIDs são longos, aleatórios e bem distribuídos. Se você escolher um método diferente para nomear seus IDs de usuário, eles também deverão ser longos, aleatórios e bem distribuídos. Também é importante notar que as IDs de usuário diferenciam **maiúsculas de minúsculas**. Por exemplo, "Abcdef" é um usuário diferente de "abcdef".

Se os IDs de usuário incluírem nomes, e-mails, carimbos de data e hora ou incrementos, sugerimos usar um novo método de nomenclatura mais seguro para que os IDs de usuário não sejam tão fáceis de adivinhar ou simular. Se optar por incluir isso em seus IDs de usuário, **recomendamos** adicionar nosso recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/) para evitar a simulação do usuário.

Fornecer essas informações a terceiros pode permitir que pessoas de fora da sua organização obtenham informações sobre como seus IDs de usuário estão estruturados, abrindo sua organização para atualizações potencialmente maliciosas ou remoção de informações. A escolha da convenção de nomenclatura correta desde o início é uma das etapas mais importantes na configuração de IDs de usuário. No entanto, é possível fazer uma migração usando nosso [endpoint de migração de ID externo]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

| Nomeação de ID de usuário |
| Recomendado | Não recomendado |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}