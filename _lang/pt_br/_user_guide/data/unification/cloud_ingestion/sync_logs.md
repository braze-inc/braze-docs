---
nav_title: Sincronizar registros e observabilidade
article_title: Sincronizar registros e observabilidade
page_order: 10
page_type: reference
description: "Esta página fornece uma visão geral dos recursos de observabilidade disponíveis no CDI."
---

# Sincronizar registros e observabilidade

> O dashboard de **Registro de Sincronização** do Cloud Data Ingestion (CDI) permite monitorar todos os dados processados pelo CDI, verificar se os dados foram sincronizados com sucesso e diagnosticar quaisquer problemas com dados "incorretos" ou ausentes.

Para acessar os registros de sincronização, vá para **Configurações de Dados** > **Ingestão de Dados na Nuvem** e selecione a guia **Registro de Sincronização**.

## Entendendo o dashboard de Registro de Sincronização

A página principal de **Registro de Sincronização** fornece uma visão geral de alto nível de todas as suas execuções de sincronização, incluindo uma visão geral das sincronizações recentes pelo seu status atual ou final.

* **Executando:** Trabalhos de sincronização que estão atualmente em andamento.  
* **Sucesso:** Trabalhos de sincronização que foram concluídos e todas as linhas foram processadas com sucesso.  
* **Sucesso Parcial:** Trabalhos de sincronização que foram concluídos, mas uma ou mais linhas encontraram um erro.  
* **Erro:** Trabalhos de sincronização que falharam ao concluir.  
* **Limite Excedido:** Trabalhos de sincronização que pararam de processar porque um limite de dados foi excedido.

![Um exemplo de registros de sincronização com 6.576 sucessos totais.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Os registros de sincronização também fornecem os seguintes detalhes para cada sincronização:

* **Nome da sincronização:** O nome da configuração de sincronização.  
* **ID da Execução:** Um identificador único para uma execução específica da sincronização. Selecione este ID para ver mais detalhes. Isso também pode ser usado nos [endpoints da API CDI]({{site.baseurl}}/api/endpoints/cdi), ou para referenciar uma execução de sincronização com o suporte da Braze.   
* **Status:** O status da execução (sucesso, sucesso parcial, erro, em execução).  
* **Novas linhas lidas da fonte:** O número de novas linhas extraídas do seu data warehouse para esta execução.  
* **** Resultados:** Uma análise de quantas linhas foram bem-sucedidas ou falharam durante a execução.  
* **Último "UPDATED_AT":** O timestamp do registro mais recente processado nesta execução de sincronização.  
* **Hora de início da execução:** Quando o trabalho de sincronização começou.  
* **Duração da execução:** O tempo total que o trabalho de sincronização levou para ser concluído.

![Detalhes para um registro de sincronização.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Retenção de dados

Os dados do registro de sincronização, incluindo todas as cargas úteis em nível de linha e detalhes de erro, são retidos por até **30 dias**. Registros com mais de 30 dias serão automaticamente excluídos.

Metadados da execução de sincronização, como o número de linhas processadas, são retidos por pelo menos 12 meses.

### Filtrando registros de sincronização

Você pode filtrar a tabela de registros de sincronização para encontrar execuções específicas. Os filtros disponíveis incluem:

* **Data de início do trabalho:** Selecione um intervalo predefinido (como "Últimos 30 dias") ou um intervalo de datas personalizado.  
* **Status:** Filtre por um ou mais status de sincronização (como mostrar apenas **Error** e **Sucesso parcial**).  
* **Nome da sincronização:** Pesquise por uma sincronização específica pelo seu nome.

Para investigar uma sincronização específica, selecione o **ID da execução** relevante na tabela de logs de sincronização. Na página **Detalhes da execução**, você encontrará um log granular, linha por linha, da sincronização.

### Visão geral da execução

Esta seção resume a execução selecionada, incluindo seu horário de início, horário de término, duração e o número total de linhas lidas da fonte. Ela também fornece uma contagem de quantas linhas foram bem-sucedidas e quantas resultaram em erro.

### Linhas processadas nessa execução

Esta tabela fornece visibilidade em nível de linha sobre os dados processados durante a sincronização, permitindo que você valide registros individuais.

* **Pesquisar:** Você pode pesquisar por um usuário específico nos resultados da execução usando a barra **Pesquisar por ID de usuário**.  
* **Detalhes disponíveis:**   
  * **UPDATED_AT:** O timestamp da coluna `UPDATED_AT` para essa linha específica.  
  * **ID:** Os identificadores de usuário (como `external_id`, `email` ou `alias_name`) usados para corresponder o registro a um perfil de usuário Braze.  
  * **Status:** O status de processamento individual para essa linha (**Sucesso** ou **Error**).  
  * **Fonte da carga útil:** Um link para visualizar a carga de dados.  
  * **Razão do erro:** Se o status for **Error**, esta coluna fornece uma mensagem explicando por que a linha falhou na sincronização.

#### Visualizando cargas úteis

Para ver os dados exatos enviados para a Braze para uma linha específica, selecione **Ver carga útil** na coluna de carga útil **Fonte**. Isso exibe a carga útil JSON bruta que foi processada para esse usuário.

![Exemplo de carga útil para uma linha específica em um registro de sincronização.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exportando registros de sincronização

Selecione **Exportar linhas** para exportar os registros em nível de linha para uma execução de sincronização. Em seguida, escolha exportar por:

* **Linhas com erros:** Baixa um arquivo contendo apenas as linhas que tiveram um status de **Erro**.
* **Todas as linhas:** Baixa um arquivo contendo todas as linhas processadas na execução.

{% alert important %}
Exportar registros de sincronização para todas as linhas está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

Os registros não podem ser exportados diretamente do dashboard. Após a exportação ser gerada, você receberá um e-mail com um link para baixar o arquivo de exportação do registro. 

## Notificações

Você pode configurar notificações por e-mail para se manter informado sobre o status das suas sincronizações CDI. Essas configurações são configuradas quando você cria uma sincronização e podem ser atualizadas a qualquer momento.

### Notificações de erro

Pelo menos um endereço de e-mail de contato é necessário para receber notificações sobre erros em nível de sincronização. Esses alertas são enviados quando um trabalho de sincronização inteiro falha ao ser executado ou concluído, ou se a sincronização encontra um erro que requer intervenção do usuário para mudar, como credenciais expiradas ou uma tabela de origem ausente.

Notificações adicionais incluem:

- **Erro de linha:** Receber alertas quando uma certa porcentagem de linhas falhar ao atualizar dentro de uma sincronização.
- **Limite de falha (%):** Especifique a porcentagem de falhas de linha que deve disparar um alerta. Por exemplo, definir isso para **1** enviaria uma notificação se 1% ou mais das linhas em uma execução de sincronização resultar em um erro.
- **Sucesso da sincronização:** Receber uma notificação após a conclusão bem-sucedida de uma sincronização.
- **Alerta mesmo se nenhuma linha mudar:** Receber uma notificação mesmo quando uma execução de sincronização bem-sucedida processa zero novas ou atualizadas linhas.