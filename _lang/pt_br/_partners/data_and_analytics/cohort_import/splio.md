---
nav_title: Esplio
article_title: Esplio
alias: /partners/splio/
description: "Este artigo de referência descreve a parceria entre o Braze e a Splio, que permite que você envie campanhas mais direcionadas, encontre novas oportunidades de produtos e aumente a receita."
page_type: partner
search_tag: Partner

---

# Esplio

> [O Splio](https://splio.com/) é uma ferramenta de criação de público que permite aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, além de fornecer análises de dados para rastrear a performance das campanhas de CRM on-line e off-line.

A integração do Braze e do Splio permite planejar e executar melhores estratégias de CRM, enviar campanhas mais direcionadas, encontrar novas oportunidades de produtos e aumentar a receita.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Splio | Você precisa de uma conta Splio para essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de importação de dados

Para integrar o Braze e o Splio, é necessário configurar a plataforma do Splio, exportar uma campanha existente do Splio e criar um segmento de coorte no Braze para direcionamento de usuários em campanhas futuras.

### Etapa 1: Obter a chave de importação de dados do Braze

No Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **Splio**.

Encontre seu endpoint REST e gere sua chave de importação de dados do Braze. Depois de gerar a chave, você pode criar uma nova chave ou invalidar uma existente.<br><br>![A página do parceiro de tecnologia Splio com o ponto de extremidade REST e a chave de importação de dados.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Para concluir a integração, forneça a chave de importação de dados e o ponto de extremidade REST à sua equipe de operações de dados do Splio. O Splio estabelece a conexão e entra em contato com você após a conclusão da configuração.

### Etapa 2: Exportar uma campanha da plataforma Splio

Toda vez que quiser criar um coorte de usuários do Splio no Braze, você deve primeiro exportá-lo da plataforma do Splio.

Em Splio, selecione as campanhas que você deseja exportar e clique em **Export Campaigns (Exportar campanhas**). Após a exportação, o público é automaticamente feito upload para sua conta Braze.

![Exportação de campanhas da plataforma Splio.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Etapa 3: Criar um segmento a partir do público personalizado do Splio

No Braze, navegue até **Segments (Segmentos**), nomeie seu segmento de coorte Splio e selecione **Splio Cohorts (Coortes Splio** ) como seu filtro. A partir daí, escolha o coorte do Splio a ser incluído. Depois de criar seu segmento de coorte do Splio, você pode selecioná-lo como um filtro de público ao criar uma campanha ou um Canva.

![Criação de um segmento de coorte Splio no Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![No criador de segmentos do Braze, o filtro de atribuições do usuário "Splio cohort" é definido como "includes" e "Primary cohort".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Está tendo problemas para localizar seu coorte? Consulte a seção [de solução de problemas](#troubleshooting) para obter orientação.

{% alert important %}
Somente os usuários que já existem no Braze são adicionados ou removidos de um coorte. A importação de coorte não cria novos usuários no Braze.
{% endalert %}

## Usando essa integração

Para usar seu segmento Splio, crie uma campanha Braze ou uma tela e selecione o segmento como seu público-alvo.

![No criador de campanhas do Braze, na etapa de direcionamento, o filtro "Direcionar usuários por segmento" está definido como "Coorte de Splio".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Correspondência de usuários

O Braze faz a correspondência entre os usuários identificados pelo endereço `external_id` ou `alias`. Os usuários anônimos são combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser correspondidos por seu `device_id`, e devem ser correspondidos por seu `external_id` ou `alias`.

## Solução de problemas

Se não conseguir encontrar o coorte correto na lista, visualize os detalhes de sua campanha no Splio e verifique o nome verificando o **Nome do arquivo de exportação**.

![A parte inferior da página de detalhes da campanha mostra o nome de seu coorte.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Se estiver tendo problemas para recuperar seu público, entre em contato com a [equipe do Splio](mailto:support-team@splio.com) para obter suporte.