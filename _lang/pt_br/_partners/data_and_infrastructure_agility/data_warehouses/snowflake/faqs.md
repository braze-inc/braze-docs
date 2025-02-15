---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o compartilhamento de dados do Snowflake
page_order: 4
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

Caso contrário, use o compartilhamento de dados entre regiões. 

### O que devo fazer com meu compartilhamento de dados quando mudar para uma nova conta do Snowflake?
Você pode excluir o compartilhamento de dados antigo associado à sua conta antiga do Snowflake e, em seguida, criar um novo compartilhamento para a nova conta. Todos os dados históricos estarão disponíveis no novo compartilhamento. 

### Por que não vejo os dados em meu compartilhamento de dados?
Você pode ter usado o ID de conta do Snowflake errado ao criar seu compartilhamento de dados. O ID da conta no dashboard de compartilhamento de dados deve corresponder à saída de `CURRENT_ACCOUNT()` da sua conta do Snowflake.

Se seu compartilhamento de dados for inter-regional, talvez os dados não fiquem disponíveis imediatamente. Dependendo do volume de dados, pode levar algumas horas para que os dados sejam sincronizados na sua região.


