---
nav_title: Tangerine
article_title: Tangerine
description: "Este artigo descreve a parceria entre o Braze e a Tangerine Store360, uma plataforma omnicanal que conecta lojas físicas com lojas on-line para proporcionar experiências superiores na loja para consumidores e colaboradores. Por meio dessa integração, os dados brutos de campanhas e impressões da Braze estão disponíveis no Store360 via Snowflake Secure Data Sharing, e as marcas podem medir como suas campanhas afetam o engajamento e o tráfego na loja."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> A Tangerine projeta, constrói e opera uma plataforma omnicanal chamada Store360. O Store360 é uma plataforma de capacitação omnicanal que conecta lojas físicas com lojas on-line para melhorar a experiência do consumidor e dos colaboradores na loja. O Store360 rastreia e analisa o tráfego de visitas a lojas físicas, incluindo usuários de apps móveis de varejistas e seu engajamento na loja.

A integração entre a Braze e a Tangerine permite integrar dados brutos de campanhas e impressões da Braze à Store360 por meio do Snowflake Secure Data Sharing. As marcas agora podem medir o impacto dessas campanhas nas visitas às lojas físicas e no engajamento na loja.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Store360 | É necessário ter uma conta no Store360 para aproveitar essa parceria. |
| ID da conta Braze | Seu ID de grupo de apps da Braze. |
| Correspondência de IDs de usuário | Os dados de seus clientes no Store360 e no Braze devem ter IDs de usuário correspondentes nas duas plataformas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

### Analisar o impacto da campanha na visita à loja física

As marcas usam o Braze para enviar mensagens de campanha aos consumidores para aumentar as visitas às lojas. Durante a campanha, o Store360 captura visitas de usuários de apps móveis identificados por ID de usuário.

Usando o recurso de análise do Store360 Insight, as marcas podem visualizar os detalhes do impacto da campanha de mensagens enviadas e lidas (dados do Braze) para quem e quantos destinatários visitaram as lojas físicas (dados do Store360).

## Integração

### Etapa 1: Ativar o compartilhamento seguro de dados do Snowflake

Trabalhe com a equipe da Braze para ativar e configurar o Snowflake Secure Data Share.

### Etapa 2: Configurar o Store360 para obter dados do Braze

Configure o ID do grupo de app do Braze para sua conta de serviço do Store360 usando o console da Web do gerenciador de administração do Store360. Isso solicitará que a equipe de administração do Tangerine sincronize os dados do Braze com o Store360 usando o compartilhamento de dados do Snowflake.

### Etapa 3: integre os SDKs da Store360 ao app móvel

Para rastrear e analisar as visitas dos usuários do aplicativo móvel à loja e as atividades na loja, juntamente com a campanha Braze e os dados de impressão, é necessário integrar o SDK do Store360 em seu app móvel usando as etapas fornecidas na documentação de instalação do SDK do Store360. Essa documentação será fornecida após você assinar um contrato de cliente com o Tangerine Store 360.

## Analisar dados do Braze no Store360

Aproveite o compartilhamento seguro de dados do Snowflake para compartilhar seus dados brutos de campanha e impressão do Braze com a análise do Store360 Insight, fornecendo uma visão completa do ciclo de vida e das atividades dos usuários, do on-line ao off-line.

Para referência, aqui estão todos os [campos do Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) disponíveis para serem incorporados à análise de dados do Store360. Os detalhes dessa etapa são muito específicos para cada cliente e exigem configurações especiais. Fale com seu gerente de conta do Store360 ou support@tangerine.io para saber mais.

## Informações importantes e limitações

### Disponibilidade do serviço

No momento, o serviço Store360 está disponível comercialmente no Japão e na Indonésia.

A Tangerine planeja lançar o produto Store360 nos seguintes países em 2023.
- Estados Unidos da América
- Tailândia
- Singapura
- Vietnã
- Coreia

### Retenção de dados

Há uma política de retenção de dois anos para seus dados da Braze para compartilhamento de dados do Snowflake.

### Tempo de espera para preencher os dados de eventos do Braze

Os eventos da Braze são processados com tecnologia de streaming e estão disponíveis em tempo quase real. De modo geral, os eventos são disponibilizados em até 30 minutos após sua realização.
