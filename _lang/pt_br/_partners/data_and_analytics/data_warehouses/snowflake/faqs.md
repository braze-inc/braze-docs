---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o compartilhamento de dados do Snowflake
page_order: 50
page_type: FAQ
description: "Este artigo responde a perguntas frequentes sobre o compartilhamento de dados do Snowflake."

---

# Perguntas frequentes

### É possível ofuscar dados de IPI por meio do compartilhamento de dados do Snowflake?
Não, no momento não há suporte para isso.

### Preciso de compartilhamento de dados para a mesma região ou entre regiões?
Use o compartilhamento de dados para a mesma região nos seguintes cenários:
- Sua conta do Snowflake está em US-EAST-1 (AWS), e a região do dashboard da Braze é os EUA.
- Sua região do Snowflake é EU-CENTRAL-1, e sua região de Braze dashboard é a UE.
- Sua região do Snowflake está em AP-Southeast-2 (AWS) e sua região do dashboard do Braze está na Austrália.
- Sua região do Snowflake está em AP-Southeast-3 (AWS) e sua região do dashboard do Braze está na Indonésia.

Caso contrário, use o compartilhamento de dados entre regiões. 

### O que devo fazer com meu compartilhamento de dados quando mudar para uma nova conta do Snowflake?
Você pode excluir o compartilhamento de dados antigo associado à sua conta antiga do Snowflake e, em seguida, criar um novo compartilhamento para a nova conta. Todos os dados históricos estarão disponíveis no novo compartilhamento. 

### Por que não vejo os dados em meu compartilhamento de dados?
Você pode ter usado o ID de conta do Snowflake errado ao criar seu compartilhamento de dados. O ID da conta no dashboard de compartilhamento de dados deve corresponder à saída de `CURRENT_ACCOUNT()` da sua conta do Snowflake.

Se seu compartilhamento de dados for inter-regional, talvez os dados não fiquem disponíveis imediatamente. Dependendo do volume de dados, pode levar algumas horas para que os dados sejam sincronizados na sua região.

### Por que estou recebendo um erro de conformidade com a HIPAA ao criar um compartilhamento de dados?

A conta especificada não está em conformidade com a HIPAA ou está em [edições do Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inferiores à Business Critical. Sua conta Snowflake deve ser feita upgrade para a Business Critical Edition para estar em conformidade com a HIPAA para compartilhamento de dados. Entre em contato com o suporte da Snowflake para obter mais assistência para fazer upgrade da sua conta.

### Por que não consigo recriar um compartilhamento de dados depois de excluí-lo?

O sistema ainda pode estar processando a exclusão do seu compartilhamento de dados anterior. Aguarde alguns minutos para que o processo de desprovisionamento seja concluído e, em seguida, tente criar o novo compartilhamento de dados novamente.

### Quantas vezes preciso executar o `CREATE DATABASE` quando tenho vários espaços de trabalho compartilhando dados na mesma conta do Snowflake?

Você precisa executar o site `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` apenas uma vez. Quando vários compartilhamentos de dados de diferentes espaços de trabalho do Braze são compartilhados com a mesma conta do Snowflake, eles são automaticamente combinados no mesmo compartilhamento. Depois de criar o banco de dados inicial, os dados de espaços de trabalho adicionais são automaticamente adicionados ao banco de dados existente sem a necessidade de solicitações de compartilhamento adicionais ou etapas de criação de banco de dados.

Por exemplo, se você criar um compartilhamento de dados para a conta 123 do Snowflake a partir do espaço de trabalho A, aceitará a solicitação de compartilhamento e criará um banco de dados. Quando você cria posteriormente um compartilhamento de dados para a mesma conta Snowflake 123 do espaço de trabalho B, nenhuma nova solicitação de compartilhamento é enviada - os dados são imediatamente adicionados ao compartilhamento existente e ficam disponíveis no banco de dados criado anteriormente.

### Se eu tiver vários espaços de trabalho, um único banco de dados conterá dados de todos eles?

Sim. Quando você compartilha dados de vários espaços de trabalho do Braze com a mesma conta do Snowflake, todos os dados são combinados em um único compartilhamento e ficam disponíveis no mesmo banco de dados. Você pode filtrar os dados por `app_group_id` para distinguir os espaços de trabalho.

Como prática recomendada, sempre filtre por `app_group_id` em suas consultas para prepará-las para o futuro. Isso garante que seus dashboards e relatórios permaneçam precisos se você adicionar outros espaços de trabalho no futuro. Sem esse filtro, suas métricas podem incluir inesperadamente dados de espaços de trabalho recém-adicionados.

### Qual é a abordagem recomendada para o gerenciamento de dados de vários espaços de trabalho no Snowflake?

Envie todos os dados do Braze para o mesmo banco de dados e filtre por `app_group_id` para distinguir os espaços de trabalho. Essa abordagem simplifica o gerenciamento de dados e garante relatórios consistentes em toda a organização.

### Quantos Snowflake Data Share Connectors são necessários para vários espaços de trabalho?

O número de conectores necessários depende de sua configuração específica e de seus direitos. Entre em contato com a equipe da sua conta Braze para saber mais sobre quais direitos são adequados para o seu caso de uso.


