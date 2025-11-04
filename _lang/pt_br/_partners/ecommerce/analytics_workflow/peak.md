---
nav_title: Peak
article_title: Peak
description: "Este artigo de referência descreve a parceria entre a Braze e a Peak, uma plataforma de inteligência de decisão, que permite que você pegue a probabilidade de churn prevista e os atributos com base nos comportamentos e interações dos clientes, e os importe para a Braze para usar na segmentação e direcionamento de clientes."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://platform.peak.ai/), uma plataforma de inteligência de decisão, é um sistema de ponta a ponta onde a inteligência de decisão é a aplicação comercial de IA para melhorar a tomada de decisões empresariais, aumentando a receita e os lucros.

_Esta integração é mantida pela Peak._

## Sobre a integração

A parceria entre a Braze e a Peak permite que você pegue a probabilidade de churn prevista e os atributos com base nos comportamentos e interações dos clientes, e os importe para a Braze para usar na segmentação e direcionamento de clientes. 

## Pré-requisitos

Como ponto de partida, um tenant da Peak deve hospedar a integração entre a Peak e a Braze. Isso é tradicionalmente criado durante a integração dos clientes da Peak. Além disso, uma solução de inteligência de decisões é necessária no início, pois gera os resultados orientados por IA que serão integrados à Braze depois.

| Requisito | Descrição |
| ----------- | ----------- |
| Inquilino de pico | Uma instância da plataforma Peak, conhecida como tenant, é necessária para hospedar e orquestrar a integração. |
| Solução de inteligência de decisão | A integração entre o Peak e o Braze é baseada em resultados impulsionados por IA e, portanto, requer uma solução implantada pelo Peak ou pelo Cliente em seu locatário. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |

## Integração

A inteligência do cliente da solução Peak utiliza um modelo para prever uma série de atributos futuros com base nos comportamentos e interações dos clientes. Esses atributos são armazenados na Peak e podem ser usados para gerar segmentação preditiva, incluindo a probabilidade de churn do cliente. A atualização desses atributos preditivos será baseada em uma cadência configurável (diária ou semanal).

### Etapa 1: Executar modelo e extrair clientes

A integração é disparada a partir do modelo de IA em execução e do recálculo dos atributos preditivos do cliente. Essas saídas de IA são armazenadas no Peak, inclusive quando um atributo é atualizado com um novo status ou valor.

Com base em quando os atributos foram atualizados, uma seleção é realizada para coletar todos os clientes com atributos preditivos atualizados desde a última sincronização entre Peak e Braze.

### Etapa 2: Atualizar Braze

Com os clientes atualizados e os atributos associados, a Peak enviará esses dados para a Braze usando o [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), com o cabeçalho [bulk]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates).

Após o recebimento de códigos de status bem-sucedidos da API, a Peak registrará a sincronização bem-sucedida entre a Peak e a Braze.

### Etapa 3: Usando esta integração

Depois que a sincronização entre Peak e Braze for bem-sucedida, os usuários atualizados agora incluem os novos atributos. Use esses atributos em campanhas e canvas para segmentar usuários e personalizar mensagens.


