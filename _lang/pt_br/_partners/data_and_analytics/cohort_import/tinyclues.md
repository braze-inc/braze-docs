---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Este artigo de referência descreve a parceria entre o Braze e a Tinyclues, que oferece um recurso de criação de público para ajudá-lo a enviar campanhas com mais direcionamento, encontrar novas oportunidades de produtos e aumentar a receita usando uma interface de usuário incrivelmente fácil de usar."
page_type: partner
search_tag: Partner

---

# Tinyclues

> O [Tinyclues](https://www.tinyclues.com/) é um recurso de criação de público que oferece a capacidade de aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente e a análise de dados para rastrear a performance das campanhas de CRM on-line e off-line.

A integração entre Braze e Tinyclues oferece aos usuários uma jornada para melhorar o planejamento e a estratégia de CRM, permitindo que os usuários enviem campanhas mais direcionadas, encontrem novas oportunidades de produtos e aumentem a receita usando uma interface de usuário incrivelmente fácil de usar.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Tinyclues | É necessário ter uma conta Tinyclues para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de importação de dados

Para integrar o Braze e o Tinyclues, é necessário configurar a plataforma Tinyclues, exportar uma campanha existente do Tinyclues e criar um segmento de coorte de usuários no Braze que possa ser usado para direcionamento de usuários em campanhas futuras.

### Etapa 1: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Tinyclues**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"} 

Para concluir a integração, será necessário fornecer a chave de importação de dados e o ponto de extremidade REST à equipe de operações de dados da Tinyclues. A Tinyclues estabelecerá a conexão e entrará em contato com você após a conclusão da configuração.

### Etapa 2: Exportar uma campanha da plataforma Tinyclues

Sempre que quiser criar uma coorte de usuários da Tinyclues para usar na Braze, será necessário primeiro exportá-lo da plataforma Tinyclues.

No Tinyclues, selecione a(s) campanha(s) que deseja exportar e clique em **Export Campaigns (Exportar campanhas**). Após a exportação, o público será automaticamente enviado para sua conta Braze.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Etapa 3: Crie um segmento a partir do público personalizado da Tinyclues

No Braze, navegue até **Segments (Segmentos**), nomeie seu segmento de coorte Tinyclues e selecione **Tinyclues Cohorts (Coortes Tinyclues)** como seu filtro. Nessa tela, você pode escolher qual coorte da Tinyclues deseja incluir. Depois que o segmento de coorte do Tinyclues for criado, você poderá selecioná-lo como um filtro de público ao criar uma campanha ou uma tela.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![No criador de segmentos do Braze, o filtro de atribuições do usuário "Tinyclues cohort" está definido como "includes" e "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Está tendo problemas para localizar seu coorte? Consulte nossa seção [de solução de problemas](#troubleshooting) para obter orientação. 

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

## Usando essa integração

Para usar seu segmento da Tinyclues, crie uma campanha da Braze ou um canva e selecione o segmento como seu público-alvo. 

![No criador de campanhas do Braze, na etapa de direcionamento, o filtro "Target users by segment" (Direcionar usuários por segmento) está definido como "Tinyclues cohort" (coorte de Tinyclues).]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.

## Solução de problemas

Está tendo problemas para encontrar o coorte certo na lista? No Tinyclues, visualize os detalhes de sua campanha e verifique o nome verificando o **Nome do arquivo de exportação**.

![A parte inferior da página de detalhes da campanha mostra o nome do seu coorte.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Ainda está tendo problemas para recuperar seu público? Entre em contato com a [equipe da Tinyclues](mailto:support@tinyclues.com) para obter suporte adicional.

