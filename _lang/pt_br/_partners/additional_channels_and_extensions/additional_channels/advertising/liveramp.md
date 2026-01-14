---
nav_title: LiveRamp
article_title: LiveRamp
description: "Saiba como conectar a LiveRamp, o Snowflake e a Braze para criar campanhas de marketing altamente personalizadas e relevantes."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Como conectar a LiveRamp, o Snowflake e a Braze

> Saiba como conectar o LiveRamp, o Snowflake e o Braze, para que você possa criar campanhas de marketing altamente personalizadas e relevantes, reduzindo o tempo de insight, quebrando os silos de dados e otimizando o engajamento dos clientes. Essa integração aprimora o marketing baseado em dados, fornecendo insights práticos baseados em pessoas e consolidando pontos de contato com o consumidor para uma melhor segmentação do público e campanhas oportunas. Ele também aproveita os benchmarks fornecidos pelo Snowflake para ajudar a refinar suas estratégias de marketing em relação aos padrões do setor.

{% alert important %}
Os [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro) da Snowflake não transferem dados entre a LiveRamp, o Snowflake e a Braze. Os dados são compartilhados apenas por meio dos serviços e do armazenamento de metadados da Snowflake, o que significa que nenhum dado é copiado e não há cobranças adicionais de armazenamento. O acesso aos dados compartilhados é controlado e governado usando os controles de acesso da sua conta Snowflake.
{% endalert %}

## Casos de uso

- **Minimização de dados:** o app Ativação da LiveRamp usa o recurso Secure Data Share do Snowflake para ler com eficácia das tabelas diretamente da sua instância. Nenhum dado é movido do Snowflake até o ponto de entrega ao parceiro downstream.
- **Ativação segura de primeira parte:** ao usar o aplicativo "Resolução de identidade" acima, o aplicativo Ativação da LiveRamp utilizará apenas as tabelas baseadas no RampID na sua instância do Snowflake e, portanto, as IPI nunca precisarão sair do seu sistema.
- **Acelerar o TTL:** Ao resolver os dados para o RampID diretamente em seu ambiente, a entrega a um destino final pode ocorrer em questão de horas, em comparação com vários dias quando se usa a abordagem mais tradicional baseada em arquivos do LiveRamp. Isso aumenta muito a capacidade de otimizar a performance da campanha em tempo hábil.
- **Economia operacional:** conforme abordado acima, com o uso do recurso Secure Data Share do Snowflake, os clientes economizam tempo e dinheiro quando comparados à coordenação da saída de arquivos para a LiveRamp ou diretamente para qualquer destino final.

## Pré-requisitos

| Pré-requisito       | Descrição                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Conta Snowflake | Você precisa de uma conta do Snowflake com permissões de nível de administrador.                                                                                                                                      |
| Conta LiveRamp  | Entre em contato com a equipe da sua conta do LiveRamp ou com [snowflake@liveramp.com](mailto:snowflake@liveramp.com) para discutir os aplicativos necessários do LiveRamp no Snowflake.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Configuração da integração

### Etapa 1: Solicite um compartilhamento de dados ao Braze

Primeiro, entre em contato com o gerente de sua conta da Braze ou com o gerente de sucesso do cliente para adquirir um conector Snowflake Data Share para sua conta da Braze. Quando você solicitar um compartilhamento de dados, o Braze provisionará o compartilhamento a partir do(s) espaço(s) de trabalho em que o compartilhamento foi adquirido. Depois que o compartilhamento é provisionado, todos os dados ficam imediatamente acessíveis a partir de sua instância do Snowflake na forma de um compartilhamento de dados de entrada. Quando o compartilhamento estiver visível em sua instância, crie um banco de dados a partir do compartilhamento para poder ver e consultar as tabelas.

Para obter um passo a passo completo, consulte o [guia de integração do Snowflake com a Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Etapa 2: Configure o app LiveRamp no Snowflake 

Os recursos de tradução e resolução de identidade estão disponíveis no Snowflake por meio do app nativo "Resolução e tradução de identidade" da LiveRamp, que cria um compartilhamento para a sua conta. Para fazer isso, ele abre uma visualização para consultar o conjunto de dados de referência a partir do seu próprio ambiente do Snowflake.

Para configurar o app nativo, siga estas etapas na documentação da LiveRamp: [Configure o app nativo da LiveRamp no Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Quando terminar, passe para a próxima etapa.

### Etapa 3: Criar uma tabela de dados

{% alert warning %}
Antes de preparar qualquer tabela baseada em IPI, certifique-se de entender o [filtro de privacidade do LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html), que é executado durante os trabalhos para garantir que as colunas de atribuição (não identificadores) em suas tabelas de entrada não contenham valores muito exclusivos. Isso é fundamental para manter a privacidade do consumidor e evitar a reidentificação.
{% endalert %}

Em seguida, crie uma tabela de dados com o [formato necessário](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) que será chamado no app nativo da LiveRamp. Consulte as categorias a seguir para determinar quais de seus identificadores são elegíveis para resolução:

| Tipo de identificador | Descrição  |
|-----------------|--------------|
| IPI completa        | As informações de identificação pessoal (IPI) incluem o nome, o endereço postal, o e-mail e o número de telefone do usuário. **Nota:** Nem todos os identificadores são necessários para cada registro. |
| Apenas e-mail      | Os endereços de e-mail do usuário, como `alex-lee@email.com`. |
| Dispositivo          | Isso inclui cookies de terceiros, IDs de publicidade móvel (MAIDs), IDs de TV conectada (CTV IDs) e RampIDs (resolvidos para um RampID de residência). |
| CIDs            | Esses são identificadores de um parceiro de plataforma ou de uma sincronização de identidade com o LiveRamp, como seu ID de cliente interno. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Identificadores de Braze

Os registros de eventos do Braze contêm identificadores que podem ser usados no app nativo do LiveRamp. Para obter uma lista completa dos identificadores disponíveis para cada tipo de evento, baixe o [Braze Event Schemas and Identifiers (Esquemas e identificadores de eventos do Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)).

| Tipo de identificador | Descrição  |
|-----------------|--------------|
| `AD_ID` | IDs de publicidade, como `ios_idfa`, `google_ad_id`, `roku_ad_id`, capturados em tipos de eventos específicos, que podem ser usados em conjunto com os serviços de resolução de dispositivos da LiveRamp. Por padrão, os IDs de publicidade não são coletados—no entanto, você pode ativar o rastreamento seguindo a [documentação do Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default). |
| `EMAIL_ADDRESS`   | Endereço de e-mail que pode ser usado em conjunto com os serviços de resolução somente por e-mail da LiveRamp |
| `TO_PHONE_NUMBER` | Número de telefone, que pode ser usado em conjunto com os serviços de resolução de IPI da LiveRamp. |
| `EXTERNAL_USER_ID` | A ID externa associada a um usuário, que pode ser usada em conjunto com os serviços de resolução de dispositivos (CID) do LiveRamp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O uso de qualquer identificador personalizado específico do cliente ou da marca no aplicativo do LiveRamp requer uma [sincronização de identidade com o LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Etapa 4: Defina suas variáveis

Em seguida, defina suas variáveis para o trabalho na planilha de etapas de execução fornecida no app. Isso inclui detalhes como o banco de dados de direcionamento, as tabelas associadas (dados de entrada, métricas, registro) e a definição do nome da tabela de saída. Para obter um passo a passo completo, consulte [LiveRamp: Especifique as variáveis](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727).

### Etapa 5: Criar a tabela de metadados para resolução de IPI

Agora que suas variáveis estão definidas, crie a tabela de metadados para a resolução de IPI. Isso fornecerá detalhes sobre o tipo de trabalho específico a ser executado com base na categoria de identificadores envolvidos. Para obter um passo a passo completo, consulte [LiveRamp: Criar a tabela de metadados](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Etapa 6: Executar a operação de resolução de identidade

Por fim, execute a operação de resolução de identidade. Para obter um passo a passo completo, consulte [LiveRamp: Execute a operação de resolução de identidade](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab exemplo de entrada %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab exemplo de saída %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Próximas etapas

Com seus dados agora pseudonimizados para sua codificação dedicada de RampID, você pode compartilhar as tabelas baseadas em RampID com o Aplicativo de Ativação Gerenciada da LiveRamp para simplificar o atendimento aos seus principais parceiros de plataforma de publicidade. O aplicativo Ativação inclui uma interface amigável para o usuário comercial para segmentação adicional e seleção/configuração de parceiros de destinos downstream. Para obter mais detalhes sobre o aplicativo, entre em contato com a equipe da sua conta da LiveRamp ou escreva para [Snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Solução de problemas

{% alert note %}
Se tiver problemas ou perguntas mais específicas, escreva para [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Regiões do Snowflake

No momento, o aplicativo está disponível apenas para as seguintes regiões baseadas nos EUA:

  - AWS-us-east-1: POA18931
  - AWS-us-west-2: FAA28932
  - Azure-east-us-2: BL60425

### Privacidade e valores de coluna

O processo avalia a combinação de todos os valores de coluna em uma base por linha para valores exclusivos. Se uma determinada combinação de valores de coluna ocorrer 3 ou menos vezes, as linhas que contêm esses valores de coluna não serão compatíveis e não serão retornadas na tabela de saída. Da mesma forma, para garantir a privacidade, o serviço LiveRamp avalia a exclusividade das combinações de valores de coluna, garantindo que, se mais de 5% das linhas do arquivo se tornarem incompatíveis devido a combinações raras, o trabalho falhará.

### Dados históricos

Os dados históricos no Snowflake remontam a abril de 2019, mas pode haver pequenas diferenças nos dados anteriores a agosto de 2019 devido a alterações no produto.

### Velocidade, performance e custo

A velocidade e o custo das consultas dependem do tamanho do warehouse usado. Considere suas necessidades de acesso aos dados ao selecionar o tamanho do warehouse.

### Benchmarks do Braze

Os benchmarks permitem que você compare suas métricas com os padrões do setor, disponíveis diretamente no Snowflake Data Exchange.

### Alterações interruptivas e não interruptivas

Esteja ciente das mudanças que podem afetar sua integração. As mudanças interruptivas serão precedidas de um anúncio e de um período de migração.
