---
nav_title: Migração de permissões granulares
article_title: Migrando para permissões granulares
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Este artigo de referência cobre como se preparar para a migração para permissões de usuário granulares na Braze."
tool: Dashboard
---

# Migrando para permissões granulares

> Gerenciar quem pode acessar sua conta e realizar ações específicas é fundamental tanto para a segurança quanto para a eficiência operacional. Para dar a você mais controle, a Braze está introduzindo permissões granulares, uma maneira mais flexível e precisa de gerenciar o acesso dos usuários em toda a sua conta.

A migração inclui estes benefícios:

- **Controle mais preciso:** Permissões granulares oferecem mais controle, melhor segurança e supervisão mais clara. Os usuários recebem apenas o acesso de que precisam.
- **Mapeamento automático:** Todas as permissões atuais são mapeadas automaticamente para seus [equivalentes granulares](#legacy-to-granular-permissions-mapping). Seus usuários mantêm o mesmo nível de acesso, a menos que você o altere.

## O que analisar

Quando a migração for planejada para sua empresa, os administradores da Braze receberão e-mails e banners no dashboard notificando-os sobre a migração de permissões granulares. Para se preparar para a migração, recomendamos que um administrador da Braze faça o seguinte.

1. Identifique usuários, funções ou conjuntos de permissões que podem precisar ser atualizados para um acesso mais personalizado após você migrar para a nova estrutura de permissões. 
2. Se sua empresa tem provisionamento automático de usuários usando SCIM ou ferramentas de conformidade que dependem de [strings de permissão]({{site.baseurl}}/scim_api_appendix/), atualize-as para corresponder à nova estrutura granular. 
3. Informe seus usuários da Braze sobre quaisquer mudanças futuras para evitar confusão.
4. Na data e hora programadas para a migração, sua empresa migrará automaticamente para permissões granulares. Nenhuma ação adicional é necessária por parte dos administradores da empresa.

{% alert important %}
A capacidade de atualizar permissões será bloqueada dentro de 15 minutos do horário programado para a migração. Isso significa que você não poderá alterar nenhuma permissão até que a migração termine, o que prevemos que levará até 15 minutos.
{% endalert %}

## Mapeamento de permissões legadas para permissões granulares

Esta tabela mostra como cada permissão legada se mapeia para as permissões granulares. Consulte esta tabela enquanto atualiza suas permissões. Por exemplo, para dar a um usuário o mesmo acesso que a permissão legada "Gerenciar configurações de e-mail", esse usuário precisa ter tanto a permissão granular "Ver configurações de e-mail" quanto "Editar configurações de e-mail".

| | Permissões legadas | Permissões granulares |
|---------------|---------------|---------------|
| **Nível** | **Nome** | **Nome** |
| Administrador | Administrador | Administrador |
| Espaço de trabalho | Administrador do espaço de trabalho | Administrador do espaço de trabalho |
| Empresa | Criar e excluir espaços de trabalho | Criar e excluir espaços de trabalho |
| Empresa | Gerenciar configurações da empresa | Gerenciar configurações da empresa |
| Espaço de trabalho | Acessar Campanhas, Canvas, Cartões, Blocos de Conteúdo, Feature Flags, Segmentos, Biblioteca de Mídia, Locais, Códigos de Promoção e Centrais de Preferências | Ver Campanhas<br>Editar Campanhas<br>Arquivar Campanhas<br>Ver Canvas<br>Editar Canvas<br>Arquivar Canvas<br>Ver regras de limite de frequência<br>Editar regras de limite de frequência<br>Ver priorização de mensagens<br>Editar priorização de mensagens<br>Ver blocos de conteúdo<br>Ver Feature Flags<br>Editar Feature Flags<br>Arquivar Feature Flags<br>Ver Segmentos<br>Editar Segmentos<br>Editar grupo de controle global<br>Ver modelos de IAM<br>Editar modelos de IAM<br>Arquivar modelos de IAM<br>Ver modelos de e-mail<br>Editar modelos de e-mail<br>Arquivar modelos de e-mail<br>Ver modelos de webhook<br>Editar modelos de webhook<br>Arquivar modelos de webhook<br>Ver modelos de links de e-mail<br>Editar modelos de links de e-mail<br>Ver ativos da biblioteca de mídia<br>Ver locais<br>Editar locais<br>Arquivar locais<br>Ver códigos de promoção<br>Editar códigos de promoção<br>Exportar códigos de promoção<br>Ver Centrais de Preferências<br>Editar Centrais de Preferências<br>Editar relatórios<br>Ver modelos de banner<br>Ver configurações de localização<br>Usar Operator<br>Ver agentes do Decisioning Studio<br>Ver evento de conversão do Decisioning Studio |
| Espaço de trabalho | Acessar console de desenvolvedores | Ver chaves de API<br>Editar chaves de API<br>Ver grupos internos<br>Editar grupos internos<br>Excluir grupos internos<br>Ver registro de atividades de mensagens<br>Ver registro de usuários de eventos<br>Ver identificadores de API<br>Ver dashboard de uso da API<br>Ver limites da API<br>Ver alertas de uso da API<br>Editar alertas de uso da API<br>Ver depurador do SDK<br>Editar depurador do SDK |
| Espaço de trabalho | Aprovar e rejeitar Campanhas | Aprovar Campanhas |
| Espaço de trabalho | Aprovar e rejeitar Canvas | Aprovar Canvas |
| Espaço de trabalho | Exportar dados de usuários | Exportar dados de usuários |
| Espaço de trabalho | Importar e atualizar dados de usuários | Ver importação de usuários<br>Importar usuários<br>Editar dados de usuários |
| Espaço de trabalho | Editar Segmentos | Arquivar Segmentos |
| Espaço de trabalho | Lançar e gerenciar blocos de conteúdo | Editar blocos de conteúdo<br>Arquivar blocos de conteúdo<br>Lançar blocos de conteúdo |
| Espaço de trabalho | Gerenciar biblioteca de mídia | Editar ativos da biblioteca de mídia<br>Excluir ativos da biblioteca de mídia |
| Espaço de trabalho | Lançar Centrais de Preferências | Lançar Centrais de Preferências |
| Espaço de trabalho | Gerenciar apps | Ver configurações do app<br>Editar configurações do app<br>Ver configurações de push<br>Editar configurações de push<br>Editar modelos de banner<br>Arquivar modelos de banner |
| Espaço de trabalho | Permissão para gerenciar Catálogos do dashboard | Ver Catálogos<br>Editar Catálogos<br>Exportar Catálogos<br>Excluir Catálogos |
| Espaço de trabalho | Gerenciar usuários do dashboard | Editar usuários do dashboard |
| Espaço de trabalho | Gerenciar configurações de e-mail | Ver configurações de e-mail<br>Editar configurações de e-mail |
| Espaço de trabalho | Gerenciar eventos, atributos, compras | Ver atributos personalizados<br>Editar atributos personalizados<br>Bloquear atributos personalizados<br>Excluir atributos personalizados<br>Exportar atributos personalizados<br>Ver eventos personalizados<br>Editar eventos personalizados<br>Bloquear eventos personalizados<br>Excluir eventos personalizados<br>Exportar eventos personalizados<br>Editar segmentação de propriedades de eventos personalizados<br>Ver produtos<br>Editar produtos<br>Bloquear produtos<br>Editar segmentação de propriedades de compra |
| Espaço de trabalho | Gerenciar integrações externas | Editar parceiros de tecnologia<br>Editar ingestão de dados na nuvem |
| Espaço de trabalho | Gerenciar configurações multilíngues | Editar configurações de localização<br>Excluir configurações de localização |
| Espaço de trabalho | Gerenciar grupos de inscrições | Editar inscrições |
| Espaço de trabalho | Gerenciar tags | Ver tags<br>Editar tags<br>Excluir tags |
| Espaço de trabalho | Gerenciar equipes | Ver equipes<br>Editar equipes<br>Arquivar equipes |
| Espaço de trabalho | Ver transformações de dados | Ver transformação de dados |
| Espaço de trabalho | Editar transformações de dados | Editar transformação de dados |
| Espaço de trabalho | Gerenciar criptografia de dados de usuários | Editar criptografia em nível de campo do identificador |
| Espaço de trabalho | Enviar Campanhas, Canvas | Lançar Campanhas<br>Lançar Canvas |
| Espaço de trabalho | Ver informações de faturamento | Ver informações de faturamento |
| Espaço de trabalho | Ver integrações do Currents | Ver integrações do Currents |
| Espaço de trabalho | Editar integrações do Currents | Editar integrações do Currents |
| Espaço de trabalho | Ver atributos personalizados marcados como IPI | Ver atributos personalizados marcados como IPI |
| Espaço de trabalho | Ver IPI | Ver IPI |
| Espaço de trabalho | Ver perfis de usuário em conformidade com IPI | Ver perfis de usuário (IPI ocultada) |
| Espaço de trabalho | Ver dados de uso | Ver dados de uso |
| Espaço de trabalho | Mesclar usuários duplicados | Mesclar usuários duplicados |
| Espaço de trabalho | Criar e editar modelos de Canvas | Editar modelos de Canvas |
| Espaço de trabalho | Ver modelos de Canvas | Ver modelos de Canvas |
| Espaço de trabalho | Arquivar modelos de Canvas | Arquivar modelos de Canvas |
| Espaço de trabalho | Publicar landing pages | Publicar landing pages |
| Espaço de trabalho | Criar rascunhos de landing page | Editar rascunhos de landing page |
| Espaço de trabalho | Acessar landing pages | Ver landing pages |
| Espaço de trabalho | Criar e editar modelos de landing page | Editar modelos de landing page |
| Espaço de trabalho | Ver modelos de landing page | Ver modelos de landing page |
| Espaço de trabalho | Arquivar modelos de landing page | Arquivar modelos de landing page |
| Espaço de trabalho | Ver agentes de IA personalizados | Ver agentes de IA personalizados |
| Espaço de trabalho | Editar agentes de IA personalizados | Editar agentes de IA personalizados<br> Arquivar agentes de IA personalizados |
| Espaço de trabalho | Ver posicionamentos | Ver posicionamentos |
| Espaço de trabalho | Editar posicionamentos | Editar posicionamentos |
| Espaço de trabalho | Arquivar posicionamentos | Arquivar posicionamentos |
| Espaço de trabalho | Novo | Ver mesclagem de usuários |
| Espaço de trabalho | Novo | Ver registros de exclusão de usuários |
| Espaço de trabalho | Novo | Ver modelos de banner |
| Espaço de trabalho | Novo | Editar modelos de banner |
| Espaço de trabalho | Novo | Arquivar modelos de banner |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Perguntas frequentes

### Posso optar por não participar ou reverter a migração?

A Braze não oferece suporte para reverter a migração. Vamos apoiar você durante a migração e monitorá-la de perto para resolver rapidamente quaisquer problemas.

### Os usuários existentes perderão o acesso à Braze durante a migração?

Não, não haverá tempo de inatividade na Braze durante a migração. No entanto, as atualizações de permissões ficarão bloqueadas durante a migração. Prevemos que a migração levará até 15 minutos para ser concluída.