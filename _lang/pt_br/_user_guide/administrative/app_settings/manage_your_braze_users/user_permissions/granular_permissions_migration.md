---
nav_title: Migração de permissões granulares
article_title: Migrando para permissões granulares
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Este artigo de referência cobre como se preparar para a migração para permissões de usuário granulares no Braze."
tool: Dashboard
---

# Migrando para permissões granulares

> Gerenciar quem pode acessar sua conta e realizar ações específicas é crítico tanto para a segurança quanto para a eficiência operacional. Para lhe dar mais controle, o Braze está introduzindo permissões granulares, uma maneira mais flexível e precisa de gerenciar o acesso dos usuários em sua conta.

A migração inclui estes benefícios:

- **Controle mais preciso:** Permissões granulares oferecem mais controle, melhor segurança e supervisão mais clara. Os usuários recebem apenas o acesso de que precisam.
- **Mapeamento automático:** Todas as permissões atuais são mapeadas automaticamente para seus [equivalentes granulares](#legacy-to-granular-permissions-mapping). Seus usuários mantêm o mesmo nível de acesso, a menos que você o altere.

## O que analisar

Quando a migração for planejada para sua empresa, seus administradores do Braze receberão e-mails e banners no painel notificando-os sobre a migração de permissões granulares. Para se preparar para a migração, recomendamos que um administrador do Braze faça o seguinte.

1. Identifique usuários, funções ou conjuntos de permissões que podem precisar ser atualizados para um acesso mais personalizado após você migrar para a nova estrutura de permissões. 
2. Se sua empresa tem provisionamento automático de usuários usando SCIM ou ferramentas de conformidade que dependem de [strings de permissão]({{site.baseurl}}/scim_api_appendix/), atualize-as para corresponder à nova estrutura granular. 
3. Informe seus usuários do Braze sobre quaisquer mudanças futuras para evitar confusão.
4. Na data e hora programadas para a migração, sua empresa migrará automaticamente para permissões granulares. Nenhuma ação adicional é necessária por parte dos administradores da empresa.

{% alert important %}
A capacidade de atualizar permissões será bloqueada dentro de 15 minutos após o horário programado para a migração. Isso significa que você não pode alterar nenhuma permissão até que a migração termine, o que prevemos que levará até 15 minutos.
{% endalert %}

## Mapeamento de permissões legadas para permissões granulares

Esta tabela mostra como cada permissão legada se mapeia para as permissões granulares. Consulte esta tabela enquanto atualiza suas permissões. Por exemplo, para dar a um usuário o mesmo acesso que a permissão legada "Gerenciar Configurações de E-mail", esse usuário precisa ter tanto as permissões granulares "Visualizar Configurações de E-mail" quanto "Editar Configurações de E-mail".

| | Permissões legadas | Permissões granulares |
|---------------|---------------|---------------|
| **Nível** | **Nome** | **Nome** |
| Administrador | Administrador | Administrador |
| Espaço de trabalho | Administrador do Espaço de Trabalho | Administrador do Espaço de Trabalho |
| Empresa | Criar e excluir espaços de trabalho | Criar e excluir espaços de trabalho |
| Empresa | Gerenciar configurações da empresa | Gerenciar configurações da empresa |
| Espaço de trabalho | Acesse Campanhas, canvas, Cartões, Blocos de Conteúdo, Flags de Recursos, Segmentos, Biblioteca de Mídia, Localizações, Códigos de Promoção e Centros de Preferências | Ver campanhas<br>Editar campanhas<br>Arquivar campanha<br>Ver canvas<br>Editar canvas<br>Arquivar canvas<br>Ver regras de limite de frequência<br>Editar regras de limite de frequência<br>Ver priorização de mensagens<br>Editar priorização de mensagens<br>Ver blocos de conteúdo<br>Visualizar Feature Flags<br>Editar Feature Flag<br>Arquivar Feature Flags<br>Exibir segmentos<br>Editar segmentos<br>Editar grupo de controle global<br>Exibir modelos de IAM<br>Editar modelos de IAM<br>Arquivar modelos de IAM<br>Exibir modelos de e-mail<br>Editar modelo de e-mail<br>Arquivar modelos de e-mail<br>Exibir modelos de webhook<br>Editar modelos de webhook<br>Arquivar modelos de webhooks<br>Exibir modelos de links<br>Editar modelos de links<br>Exibir ativos da biblioteca de mídia<br>Ver locais<br>Editar locais<br>Arquivar locais<br>Visualizar Códigos de Promoção<br>Editar Códigos de Promoção<br>Exportar Códigos de Promoção<br>Ver Centrais de Preferências<br>Editar Centrais de Preferências<br>Editar Relatórios<br>Ver modelos de banner<br>Visualizar Configurações de Múltiplas Línguas<br>Usar Operador<br>Visualizar Agentes do Estúdio de Decisão<br>Visualizar Evento de Conversão do Estúdio de Decisão |
| Espaço de trabalho | Acessar console de desenvolvedores | Exibir chaves de API<br>Editar chaves de API<br>Visualizar Grupos Internos<br>Editar Grupos Internos<br>Excluir Grupos Internos<br>Visualizar registro de atividades de envio de mensagem<br>Exibir registro de usuários de eventos<br>Exibir identificadores de API<br>Exibir o dashboard de uso da API<br>Exibir limites da API<br>Exibir alertas de uso da API<br>Editar alertas de uso da API<br>Exibir depurador do SDK<br>Editar depurador do SDK |
| Espaço de trabalho | Aprovar e rejeitar campanhas | Aprovar campanha |
| Espaço de trabalho | Aprovar e rejeitar canvas | Aprovação de telas |
| Espaço de trabalho | Exportar dados de usuários | Exportar dados de usuários |
| Espaço de trabalho | Importar e atualizar dados de usuários | Exibir importação de usuários<br>Importar usuários<br>Editar dados de usuários |
| Espaço de trabalho | Editar segmentos | Arquivar segmentos |
| Espaço de trabalho | Lançar e gerenciar blocos de conteúdos | Editar blocos de conteúdo<br>Arquivar blocos de conteúdo<br>Lançar Blocos de Conteúdo |
| Espaço de trabalho | Gerenciar Biblioteca de Mídia | Editar ativos da biblioteca de mídia<br>Excluir ativos da biblioteca de mídia |
| Espaço de trabalho | Abrir Centrais de Preferências | Abrir Centrais de Preferências |
| Espaço de trabalho | Gerenciar apps | Exibir configurações do app<br>Editar configurações do app<br>Exibir configurações push<br>Editar configurações de push<br>Editar modelos de banner<br>Arquivar modelos de banner |
| Espaço de trabalho | Permissão para gerenciar catálogos do dashboard | Ver catálogos<br>Editar catálogos<br>Exportar catálogo<br>Excluir catálogos |
| Espaço de trabalho | Gerenciar usuários do dashboard | Editar usuários do painel |
| Espaço de trabalho | Gerenciar configurações de e-mail | Ver configurações de e-mail<br>Editar configurações de e-mail |
| Espaço de trabalho | Gerenciar eventos, atributos, compras | Visualizar atributos personalizados<br>Editar atributos personalizados<br>Lista de bloqueio de atributos personalizados<br>Excluir atributos personalizados<br>Exportar atributos personalizados<br>Visualizar eventos personalizados<br>Editar eventos personalizados<br>Lista de bloqueio de eventos personalizados<br>Excluir eventos personalizados<br>Exportar eventos personalizados<br>Editar segmentação de propriedades de eventos personalizados<br>Visualizar produtos<br>Editar produtos<br>Lista de bloqueio de produtos<br>Editar segmentação de propriedades de compra |
| Espaço de trabalho | Gerenciar integrações externas | Editar Parceiros de Tecnologia<br>Editar ingestão de dados na nuvem |
| Espaço de trabalho | Gerenciar configurações multilíngues | Editar configurações de localização<br>Excluir configurações de localização |
| Espaço de trabalho | Gerenciar grupos de inscrição | Editar inscrições |
| Espaço de trabalho | Gerenciar tags | Exibir tags<br>Editar tags<br>Excluir tags |
| Espaço de trabalho | Gerenciar equipes | Ver equipes<br>Editar equipe<br>Arquivar equipes |
| Espaço de trabalho | Ver Transformações de Dados | Ver transformação de dados |
| Espaço de trabalho | Editar Transformações de Dados | Editar transformação de dados |
| Espaço de trabalho | Gerenciar Criptografia de Dados de Usuários | Criptografia em nível de campo do identificador de edição |
| Espaço de trabalho | Enviar campanhas, canvas | Lançar campanha<br>Lançar canvas |
| Espaço de trabalho | Ver informações de faturamento | Ver informações de faturamento |
| Espaço de trabalho | Ver integrações com o Currents | Ver integrações com o Currents |
| Espaço de trabalho | Editar integrações com o Currents | Editar integrações com o Currents |
| Espaço de trabalho | Ver atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI |
| Espaço de trabalho | Ver IPI | Ver IPI |
| Espaço de trabalho | Ver perfis de usuário em conformidade com IPI | Ver perfis de usuário em conformidade com IPI |
| Espaço de trabalho | Ver dados de uso | Ver dados de uso |
| Espaço de trabalho | Mesclar usuários duplicados | Mesclar usuários duplicados |
| Espaço de trabalho | Prévia de usuários duplicados | Prévia de usuários duplicados |
| Espaço de trabalho | Criar e editar modelos de canva | Editar modelos de tela |
| Espaço de trabalho | Ver modelos de canva | Ver modelos de canva |
| Espaço de trabalho | Arquivar modelos de canva | Arquivar modelos de canva |
| Espaço de trabalho | Publicar landing page | Publicar landing page |
| Espaço de trabalho | Criar rascunhos de landing page | Editar rascunhos de landing page |
| Espaço de trabalho | Acessar landing page | Ver landing pages |
| Espaço de trabalho | Criar e editar modelos de landing page | Editar modelos de landing page |
| Espaço de trabalho | Exibir modelos de landing page | Exibir modelos de landing page |
| Espaço de trabalho | Arquivar modelos de landing page | Arquivar modelos de landing page |
| Espaço de trabalho | Exibir agentes de IA personalizados | Exibir agentes de IA personalizados |
| Espaço de trabalho | Editar agentes de IA personalizados | Editar agentes de IA personalizados<br> Arquivar Agentes de IA Personalizados |
| Espaço de trabalho | Ver colocações | Ver colocações |
| Espaço de trabalho | Editar Colocações | Editar Colocações |
| Espaço de trabalho | Arquivar colocações? | Arquivar colocações? |
| Espaço de trabalho | Novo | Ver Mesclar Usuários |
| Espaço de trabalho | Novo | Exibir registros de exclusão de usuários |
| Espaço de trabalho | Novo | Excluir usuários do dashboard |
| Espaço de trabalho | Novo | Ver modelos de banner |
| Espaço de trabalho | Novo | Editar modelos de banner |
| Espaço de trabalho | Novo | Arquivar modelos de banner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Perguntas frequentes

### Posso optar por não participar ou reverter a migração?

A Braze não suporta reverter a migração. Nós iremos apoiá-lo durante a migração e monitorar a migração de perto para resolver rapidamente quaisquer problemas.

### Os usuários existentes perderão o acesso à Braze durante a migração?

Não, não haverá tempo de inatividade na Braze durante a migração. No entanto, as atualizações de permissões estarão bloqueadas durante a migração. Prevemos que a migração levará até 15 minutos para ser concluída.