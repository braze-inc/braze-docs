<ul>
<li><code>dispatch_id</code> 特定のメッセージ配信（キャンペーン送信など）の識別子である。同じディスパッチから発生するすべてのプッシュイベントは、同じものを含む。 <code>dispatch_id</code>.使う <code>dispatch_id</code> 同じ配信に属するイベントをグループ化することで、その配信におけるプッシュメッセージのライフサイクル（送信、バウンス、開封など）をまとめて関連付けられる。</li>
<li><code>state_change_source</code> 完全なソース名の文字列を返す。例えば、ソースCSVのインポートは文字列を返す。 <code>CSV import</code>.利用可能なソースを以下に示します。</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>ソース</th><th>説明</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>SDKエンドポイントs</td></tr>
<tr><td>ダッシュボード</td><td>ダッシュボードのユーザープロファイルのページからユーザーのサブスクリプションの状態が更新された場合</td></tr>
<tr><td>サブスクリプションページ</td><td>ユーザー設定センター以外のメールを介してユーザー 配信停止が発生した場合</td></tr>
<tr><td>REST API</td><td>REST APIエンドポイント</td></tr>
<tr><td>CSV インポート</td><td>CSVユーザーインポート</td></tr>
<tr><td>環境設定センター</td><td>ユーザー設定センターからユーザーを更新した場合</td></tr>
<tr><td>受信メッセージ</td><td>ユーザーが更新の場合、エンドユーザーsからSMSなどのチャネルsを経由した着信メッセージ</td></tr>
<tr><td>移行</td><td>ユーザーが内部移行または保守スクリプトによって更新されている場合</td></tr>
<tr><td>ユーザーマージ</td><td>ユーザー結合処理で更新した場合</td></tr>
<tr><td>Canvas ユーザー更新ステップ</td><td>キャンバスユーザー更新ステップによってユーザーが更新された場合</td></tr>
</tbody>
</table>
