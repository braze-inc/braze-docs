---
nav_title: Compartilhamento de dados do Snowflake
hidden: true
---

# Integração do compartilhamento de dados do Snowflake

> Quando o Snowflake Data Share for usado como um método de integração, o Braze fornecerá um compartilhamento para sua instância do Snowflake em nome do cliente. Esse compartilhamento incluirá automaticamente todos os eventos de engajamento com mensagens e de comportamento do usuário.

Os compartilhamentos são provisionados por cliente após o cliente adquirir um direito de compartilhamento de dados do Snowflake. Quando um cliente solicita um compartilhamento de dados, o Braze adiciona um compartilhamento ao espaço de trabalho do cliente, e o cliente pode usar a interface de usuário de autoatendimento para adicionar os dados relevantes da conta Snowflake do parceiro.

![]({% image_buster /assets/img/snowflake.png %})

Depois que o compartilhamento é provisionado, todos os dados ficam imediatamente acessíveis a partir da instância do Snowflake como um compartilhamento de dados de entrada.

![]({% image_buster /assets/img/snowflake2.png %})

Na sua instância do Snowflake, você verá um compartilhamento por região. Cada tabela tem uma coluna, `app_group_id`, que é efetivamente uma chave de locatário para a Braze. À medida que novos clientes forem adicionados a uma ação dentro da mesma região, eles aparecerão como diferentes `app_group_ids` dentro das tabelas existentes.

{% alert important %}
A Braze hospeda todos os dados de nível de usuário nas regiões AWS US East-1 e EU-Central (Frankfurt) do Snowflake. Embora a Braze possa compartilhar entre regiões, é mais econômico para os clientes se compartilharmos com `US-EAST-1` e/ou `EU-CENTRAL-1`.
{% endalert %}

{% alert tip %}
Baixe os [esquemas de tabelas brutas]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) aqui ou use esse conjunto de [dados de eventos de amostra](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset) disponíveis no mercado do Snowflake para se familiarizar com os eventos compartilhados.
{% endalert %}

## Tratamento de eventos duplicados

Espera-se que haja duplicatas, mas todos os eventos têm um identificador exclusivo, a coluna ID. As duplicatas podem ser removidas com `select distinct(id)`.

## Alterações interruptivas e não interruptivas

### Alterações não interruptivas

Alterações não interruptivas podem ocorrer a qualquer momento e geralmente trazem novas funcionalidades. Exemplos de alterações não interruptivas:
- Adição de uma nova tabela ou visualização
- Adição de uma coluna a uma tabela ou exibição existente

{% alert important %}
Como as novas colunas são consideradas não interruptivas, a Braze recomenda enfaticamente listar de modo explícito as colunas de interesse em cada consulta, em vez de usar consultas `SELECT *`. Como alternativa, talvez você queira criar exibições que nomeiem explicitamente as colunas e, em seguida, consultar essas exibições em vez das tabelas diretamente.
{% endalert %}

### Mudanças significativas

Quando possível, as mudanças interruptivas serão precedidas de um anúncio e de um período de migração. Exemplos de mudanças significativas incluem:
- Remoção de uma tabela ou exibição
- Remoção de uma coluna de uma tabela ou exibição existente
- Alteração do tipo ou da capacidade de anulação de uma coluna existente

## Conformidade com o Regulamento Geral sobre a Proteção de Dados (GDPR)

Quase todos os registros de eventos armazenados pelo Braze incluem alguns campos que representam informações de identificação pessoal (IPI) dos usuários. Alguns eventos podem incluir endereço de e-mail, número de telefone, ID do dispositivo, idioma, gênero e local. Se a solicitação de esquecimento de um usuário for enviada ao Braze, anularemos esses campos de IPI para qualquer evento pertencente a esses usuários. Dessa forma, não removemos o registro histórico do evento, mas agora o evento jamais poderá ser vinculado a um indivíduo específico.
