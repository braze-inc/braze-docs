---
nav_title: Outgrow
article_title: Outgrow
alias: /partners/outgrow/
description: "Este artigo fornece um guia abrangente sobre a configuração de uma integração nativa entre o Outgrow e o Braze para sincronização aprimorada de dados de usuários e campanhas personalizadas."
page_type: partner
search_tag: Partner
---

# Outgrow

> A [Outgrow](https://outgrow.co/) é uma plataforma de conteúdo interativo que lhe permite criar questionários, calculadoras, pesquisas e outros tipos de conteúdo envolvente para coletar dados e insights de usuários. A integração Braze e Outgrow permite transferir automaticamente os dados de usuários da Outgrow para o Braze, ativando campanhas altamente personalizadas e direcionadas.

Quando você usa a integração do Braze e do Outgrow para conteúdo interativo, os benefícios que você obtém incluem:

- **Personalização aprimorada**: Colete dados de questionários, pesquisas e calculadoras do Outgrow que podem ser mapeados para atributos personalizados no Braze. Esses dados permitem uma segmentação precisa e campanhas personalizadas.
- **Sincronização de dados em tempo real**: Receba os dados do Outgrow no Braze em tempo real, o que lhe permite agir imediatamente com base nos insights dos usuários. Isso permite o acompanhamento oportuno ou o envio de mensagens personalizadas com base nas interações mais recentes dos usuários.
- **Gerenciamento de dados simplificado**: Automatize a transferência de dados entre o Outgrow e o Braze, eliminando as exportações e importações manuais de dados, reduzindo as discrepâncias de dados e economizando tempo.
- **Melhoria da experiência do usuário**: Aproveite os insights do usuário para criar experiências mais relevantes, levando a uma maior satisfação, retenção e valor do tempo de vida.
- **Direcionamento e segmentação flexíveis**: Refine a segmentação no Braze usando os dados da Outgrow, permitindo o direcionamento de usuários com base em interações específicas (como pontuações de questionários ou respostas a pesquisas) para criar campanhas que repercutam entre seus usuários.

## Pré-requisitos

Antes de configurar a integração do Outgrow e do Braze, confirme que você tem o seguinte:

| Requisito | Descrição |
|-------------|-------------|
| **Superar a conta** | Uma conta Outgrow registrada para configurar e gerenciar o conteúdo interativo e as configurações de transferência de dados |
| **Conta Braze** | Uma conta Braze com acesso às credenciais da API REST |
| **Chave de API** | Uma chave de API do Braze com a permissão `users.track` para ativar a transferência de dados de usuários |
| **Atributos personalizados no Braze** | Atributos personalizados configurados no Braze para capturar respostas do Outgrow (como pontuações de questionários, segmentos e outros) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Siga estas etapas para configurar a integração do Braze e do Outgrow:

### Etapa 1: Gerar a chave de API do Braze

1. Na sua conta Braze, acesse o **console do desenvolvedor** > **Configurações de API**.
2. Selecione **Create New API Key (Criar nova chave de API)**.
3. Dê um nome à sua chave de API, ative a permissão `users.track` e salve a chave de API.

### Etapa 2: Configurar a integração do Braze no Outgrow

1. Registre-se em sua conta do Outgrow.
2. No dashboard, acesse **Integrações**.
3. Na lista de integrações disponíveis, selecione **Braze**.
4. Digite sua **chave da API do Braze** e o **URL do ponto de extremidade da API REST**:
   - **Chave de API**: Digite a chave de API que foi gerada no Braze
   - **Sua URL de endpoint REST**: Digite o endpoint de sua instância do Braze (por exemplo, `https://rest.iad-01.braze.com`)
5. Selecione **Salvar** para ativar a integração.

### Etapa 3: Mapear dados do Outgrow para atribuições do Braze

No Outgrow, você pode mapear respostas de conteúdo interativo (como resultados de questionários, segmentos personalizados ou pontuações de engajamento) para atributos personalizados do Braze.

1. Nas **Configurações de integração** do Outgrow para o Braze, defina quais respostas do Outgrow devem ser mapeadas para as atribuições do Braze.
2. Certifique-se de que cada resposta selecionada esteja alinhada com um atributo personalizado no Braze. Por exemplo:
   - A pontuação do questionário é mapeada em `outgrow_quiz_score`.
   - Mapas de segmentos personalizados para `outgrow_custom_segment`.
3. Salve suas configurações de mapeamento.

### Etapa 4: Teste a integração

Depois de configurar a integração, execute um teste para confirmar se os dados estão sendo transferidos corretamente do Outgrow para o Braze.

1. Publique uma experiência do Outgrow (como um questionário ou uma calculadora) e conclua-a como um usuário teste.
2. Em sua conta Braze, acesse a seção **User Profile (Perfil do usuário)** e verifique se há atribuições atualizadas (como `outgrow_quiz_score` ou `outgrow_custom_segment`).
3. Verifique se os dados estão preenchidos corretamente nos atributos personalizados apropriados.

## Uso de dados do Outgrow no Braze para segmentação e direcionamento

### Criação de segmentos no Braze com dados do Outgrow

Com a integração, você pode criar segmentos do Braze com base em atributos personalizados preenchidos a partir das respostas do Outgrow.

1. No Braze, acesse **Engagement** (Engajamento)  > **Segments** (Segmentos) e selecione **Create New Segment (Criar novo segmento)**.
2. Dê um nome ao seu segmento e defina filtros com base nos dados do Outgrow. Por exemplo:
   - Filtre por `outgrow_quiz_score` para direcionar os usuários que pontuaram acima de um determinado limite.
   - Filtre por `outgrow_custom_segment` para direcionar os usuários que pertencem a um determinado segmento definido pelo Outgrow.
3. Salve seu segmento para uso em campanhas e telas.

### Lançamento de campanhas com segmentos definidos pelo Outgrow

É possível usar os segmentos personalizados criados a partir dos dados da Outgrow para personalizar suas campanhas no Braze e direcionar os usuários com base em suas respostas ao conteúdo interativo. Para fazer isso e criar uma experiência de usuário mais personalizada, siga estas etapas:

1. No Braze, acesse **Engajamento** > **Campanhas**.
2. Selecione **Criar campanha** e escolha o tipo de campanha (e-mail, push, mensagem no app ou outros).
3. Na etapa de direcionamento do público, selecione o segmento criado a partir das atribuições do Outgrow (como usuários com pontuações ou segmentos de questionário específicos).
4. Personalize o conteúdo e as configurações de sua campanha e, em seguida, lance-a.

## Solução de problemas comuns

| Problema | Solução |
|-------|----------|
| **Os dados não estão sendo transferidos para o Braze** | Verifique se a chave de API e o URL do ponto de extremidade estão corretos em suas configurações de integração do Outgrow. Certifique-se de que a chave de API tenha a permissão `users.track` ativada. |
| **Mapeamento incorreto de dados** | Certifique-se de que cada resposta Outgrow mapeada corresponda a um atributo personalizado Braze válido e que os nomes dos atributos correspondam exatamente. |
| **O segmento não está sendo filtrado corretamente** | Certifique-se de que os atributos personalizados no Braze estejam configurados corretamente e recebendo dados. Verifique novamente a lógica do filtro de segmento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Considerações adicionais

- **Privacidade de dados**: Cumpra as normas de privacidade de dados (como GDPR e CCPA) ao transferir dados de usuários entre plataformas.
- **Limites de taxa**: Os dados de crescimento são enviados ao Braze em tempo real, mas os limites de frequência da API do Braze podem se aplicar a grandes volumes de envios de dados. Planeje adequadamente as experiências de alto tráfego.
- **Configuração de atributos personalizados**: Verifique se os atributos personalizados do Braze usados nessa integração estão configurados corretamente para capturar os dados enviados pelo Outgrow.

Para obter assistência adicional, consulte a [documentação da Outgrow](https://support.outgrow.co/docs/configuring-native-integration-between-outgrow-braze) ou entre em contato com o Suporte da Outgrow.