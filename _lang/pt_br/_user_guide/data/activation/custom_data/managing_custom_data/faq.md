---
nav_title: Perguntas frequentes
article_title: Gerenciando Dados Personalizados FAQ
page_order: 1
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre como gerenciar dados personalizados no Braze."
---

# Perguntas frequentes

> Esta página fornece respostas para algumas perguntas frequentes sobre como gerenciar dados personalizados.

### Por que meu atributo personalizado é detectado como um tipo de dado diferente em produção do que em desenvolvimento?

O Braze detecta automaticamente o tipo de dado de um atributo personalizado com base no primeiro valor que recebe. Se seu ambiente de desenvolvimento enviar um valor numérico como `100` primeiro, o atributo é armazenado como um número. Se o primeiro valor do seu ambiente de produção chegar como uma string (como `"100"` entre aspas), o atributo é armazenado como uma string.

Para evitar isso, certifique-se de que sua integração envie tipos de dados consistentes em todos os ambientes. Se o tipo errado já estiver definido, você pode forçar o tipo de dado correto em **Configurações de Dados** > **Atributos Personalizados** usando o [menu suspenso de tipo de dado]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#forcing-data-type-comparisons).

### Se eu forçar uma mudança de tipo de dado em um atributo personalizado, os dados existentes serão convertidos?

Não. Forçar uma mudança de tipo de dado afeta apenas os novos dados que entram no Braze. Quaisquer dados ingeridos antes da mudança de tipo continuam a ser armazenados como o tipo antigo e podem não ser segmentáveis com os filtros do novo tipo. Um aviso aparece nos perfis dos usuários afetados. Para novos dados que chegam, se um valor não corresponder ao tipo forçado, o Braze pode convertê-lo para o tipo forçado (por exemplo, a string `"100"` para o número `100`); valores que não podem ser convertidos são ignorados e não atualizam o atributo.

Se você precisar que todos os dados existentes dos usuários correspondam ao novo tipo, deve reenviar os valores dos atributos para esses usuários através do SDK, API ou uma importação CSV. Não há conversão em massa automática para dados existentes.

### Como posso evitar problemas de tipo de dado ao usar a Ingestão de Dados em Nuvem (CDI)?

Ao usar CDI para sincronizar dados de fontes externas (como Databricks ou Snowflake), certifique-se de que suas colunas de origem usem os tipos de dados corretos antes da sincronização. Problemas comuns incluem:

- **Carimbos de tempo armazenados como strings**: Certifique-se de que suas colunas de data usem um tipo de timestamp ou datetime em seu banco de dados de origem, não um varchar ou string.
- **Números armazenados como strings**: Converta colunas numéricas para tipos inteiro ou float em sua consulta de origem antes de sincronizar.
- **Tipos inconsistentes entre as sincronizações**: Se um tipo de coluna mudar entre as sincronizações, a Braze pode rejeitar os novos dados. Verifique se seu esquema de origem permanece consistente.
