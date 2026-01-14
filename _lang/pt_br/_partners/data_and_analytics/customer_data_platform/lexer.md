---
nav_title: Lexer
article_title: Lexer
description: "Este artigo de referência descreve a parceria entre o Braze e a Lexer, uma plataforma de dados do cliente que coloca os dados do cliente nas mãos dos profissionais de marketing para inspirar experiências que impulsionam as vendas."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [A Lexer](https://lexer.io/), uma plataforma de dados do cliente criada para o varejo, ajuda as marcas a aumentar as vendas por meio de experiências aprimoradas do cliente, combinando o enriquecimento robusto de dados com as ferramentas mais intuitivas e a consultoria especializada.

_Essa integração é mantida pela Lexer._

## Sobre a integração

A integração da Braze e da Lexer permite sincronizar dados entre as duas plataformas. Use seus dados do Lexer para criar segmentos valiosos do Braze ou importe os existentes para o Lexer para obter insights. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta de parceiro | É necessário ter uma conta Lexer para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST Braze com todas as permissões `user` (exceto `user.delete`) e permissões `segment.list`. O conjunto de permissões pode mudar à medida que o Lexer adiciona suporte a mais objetos do Braze, portanto, talvez você queira conceder mais permissões agora ou planejar a atualização dessas permissões no futuro.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| endpoint REST do Braze | [URL de seu endpoint REST]({{site.baseurl}}/api/basics/#endpoints). Seu endpoint dependerá da URL do Braze para sua instância. |
| Bucket S3 e credenciais do Amazon AWS | Antes de iniciar a integração, é necessário ter credenciais de acesso para um bucket S3 do AWS conectado ao seu hub da Lexer (pode ser um bucket criado por você ou um que a Lexer crie e gerencie para você). Visite [a Lexer](https://learn.lexer.io/docs/amazon-s3) para obter orientação sobre esse requisito. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

No Lexer, navegue até **Manage > Integration (Gerenciar > Integração**), selecione o bloco **Braze** e clique em **Integrate Braze (Integrar Braze**). Forneça as seguintes informações:
- **Endpoint REST  do Braze**
- **chave da API REST Braze**
- **Credenciais da AWS**
  - **Nome do bucket S3 do AWS**
  - **[Região do bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) S3 da AWS**
  - **Caminho do bucket S3 da AWS**: Essa jornada deve corresponder à jornada que você especificou ao [conectar seu bucket S3 ao Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/). Isso deve estar em branco se você não especificou nada para o Braze.
  - **Chave de acesso secreto do AWS S3**: Visite a Amazon para obter informações sobre como [criar uma chave de acesso](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **ID do segmento de exportação do Braze**: O ID do segmento que você criou no Braze contendo todos os usuários que deseja exportar para o Lexer. Se houver usuários que não deseja exportar para o Lexer, você poderá excluí-los do segmento criado no Braze. Para encontrar seu identificador de segmento, clique no segmento desejado no Braze e localize o **Segment API Identifier**.

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Escolha de uma opção do AWS S3 (gerenciada pela Lexer ou autogerenciada)
Usar um bucket gerenciado pela Lexer é a maneira recomendável de conectar a Braze ao seu hub da Lexer e reduz a quantidade de configurações necessárias. A Lexer fornecerá os detalhes necessários para configurar a Braze.

Se já tiver conectado um bucket S3 à Braze e o estiver usando-o para outros fins, será necessário fornecer à Lexer acesso a esse bucket autogerenciado seguindo as etapas anteriores.

Para a integração funcionar, a Lexer precisa ter acesso ao seu token e aos seus segredos de API existentes, permitindo que a Lexer faça essas exportações em seu nome. Ele também importa seus dados do Braze para o Lexer usando essas credenciais e sua configuração do S3 para sincronizar seus dados em ambas as plataformas automaticamente.

## Envio de segmentos para o Braze

### Etapa 1: Criar ativação

O Lexer Activate atualizará automaticamente seus perfis do Braze, adicionando ou removendo atribuições à medida que os clientes entram e saem do seu segmento.

1. Na Lexer, em **Lexer Activations** (Ativações da Lexer), clique em **ACTIVATE NEW AUDIENCE** (ATIVAR NOVO PÚBLICO).
2. Selecione a ativação Braze apropriada para essa campanha.
3. Adicione seu segmento.
4. Atualize o nome de seu público; esse será seu valor de atributo na Braze.
5. Esse é o atributo personalizado que estaremos atualizando no Braze. Entre em contato com [o suporte da Lexer](support@lexer.io) para atualizar.
6. Marque a ação de lista apropriada - na maioria dos casos, você desejará manter sua lista.
7. Revise os termos e condições e clique em **SEND AUDIENCE**.

![]({% image_buster /assets/img/lexer/lexer.png %})

### Etapa 2: Verificar a ativação

Depois que a ativação for confirmada como enviada no Activate, os registros começarão a ser atualizados na Braze. Seus perfis só estarão totalmente atualizados na Braze após o recebimento de um e-mail de confirmação da Lexer.

### Etapa 3: Crie seu segmento Braze

Na Braze, você verá que o nome do público na Lexer agora é um valor no atributo personalizado `lexer_audience`. A Braze tem um limite de 100 valores por atributo.

Para criar seu segmento, navegue até **Segment > + Create Segment** e selecione **Atributo personalizado** como filtro. Em seguida, selecione `lexer_audience` como seu atributo e o nome do público da Lexer desejado. Quando terminar, **salve** seu público.

Agora é possível adicionar esse segmento recém-criado a futuras campanhas e canvas do Braze para direcionamento a esses usuários finais.


