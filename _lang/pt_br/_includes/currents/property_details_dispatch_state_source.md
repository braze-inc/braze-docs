<ul>
<li><code>dispatch_id</code> é um ID para um envio de mensagem específico, como um envio de campanha. Todos os eventos de push que se originam do mesmo envio incluem o mesmo <code>dispatch_id</code>. Uso <code>dispatch_id</code> para agrupar eventos que pertencem ao mesmo envio, permitindo que você agrupe e correlacione o ciclo de vida da mensagem de push para esse envio (como Enviar, Bounce e Abrir).</li>
<li><code>state_change_source</code> retorna uma string do nome completo da fonte. Por exemplo, a importação de CSV da fonte retornará a string <code>CSV import</code>. As fontes disponíveis estão listadas abaixo:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Origem</th><th>Descrição</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Endpoints de SDK</td></tr>
<tr><td>Dashboard</td><td>Quando o estado da inscrição de um usuário é atualizado na página Perfil do usuário no dashboard</td></tr>
<tr><td>Página de inscrição</td><td>Quando um usuário cancela a inscrição por meio de um link de cancelamento de inscrição por e-mail que não seja a Central de Preferências</td></tr>
<tr><td>API REST</td><td>Pontos de extremidade da API REST</td></tr>
<tr><td>Importação de CSV</td><td>Importação de usuário CSV</td></tr>
<tr><td>Central de Preferências</td><td>Quando um usuário é atualizado a partir da Central de Preferências</td></tr>
<tr><td>Mensagem recebida</td><td>Quando um usuário é atualizado por mensagens recebidas de usuários finais por meio de canais como SMS</td></tr>
<tr><td>Migração</td><td>Quando um usuário é atualizado por migrações internas ou scripts de manutenção</td></tr>
<tr><td>Mesclagem de usuários</td><td>Quando um usuário é atualizado pelo processo de mesclagem de usuários</td></tr>
<tr><td>Etapa de atualização do usuário do canva</td><td>Quando um usuário é atualizado pela etapa de atualização do usuário do Canva</td></tr>
</tbody>
</table>
