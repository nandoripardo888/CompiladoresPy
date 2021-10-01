<h1>DOCUMENTA&Ccedil;&Atilde;O DO PROJETO</h1>

<h2>Arquivos de c&oacute;digos-fonte presentes</h2>

<ol>
	<li style="text-align:justify"><strong>main.py</strong> - executa todo o c&oacute;digo fonte.</li>
	<li style="text-align:justify"><strong>analisadorSintatico.py</strong> - cont&eacute;m o arquivo do analisador sint&aacute;tico.</li>
	<li style="text-align:justify"><strong>analisadorLexico.py</strong> - cont&eacute;m o c&oacute;digo analisador L&eacute;xico.</li>
	<li style="text-align:justify"><strong>exemplo1.txt</strong> - cont&eacute;m um arquivo de programa a ser analisado.</li>
	<li style="text-align:justify"><strong>exemplo2.txt</strong> - cont&eacute;m um arquivo de programa inv&aacute;lido a ser analisado.</li>
</ol>

<h2>fases de desenvolvimento</h2>

<ul>
	<li>Parte 1 - Analisador L&eacute;xico.</li>
	<li>parte 2&nbsp;- Analisador Sint&aacute;tico.</li>
	<li>parte 3 - Analisador Sem&acirc;ntico.</li>
</ul>

<h2>DESENVOLVIMENTO</h2>

<p>Foi implementado um analisador l&eacute;xico para a seguinte tabela de s&iacute;mbolos</p>

<table>
	<thead>
		<tr>
			<th>Palavra Token</th>
			<th>Express&atilde;o regular correspondente</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>KeyWords</td>
			<td>if then else write read integer real program begin end</td>
		</tr>
		<tr>
			<td>Identificadores</td>
			<td>(Letra)*</td>
		</tr>
		<tr>
			<td>Numero</td>
			<td>(Digito)*</td>
		</tr>
		<tr>
			<td>Letra</td>
			<td>a..z</td>
		</tr>
		<tr>
			<td>D&iacute;gito</td>
			<td><code>0..9</code></td>
		</tr>
		<tr>
			<td>Operadores</td>
			<td>= &lt; &lt;= &lt;&gt; &gt; &gt;= :=&nbsp;</td>
		</tr>
		<tr>
			<td>S&iacute;mbolos</td>
			<td><code>; , : $ ( ) { } [ ]</code></td>
		</tr>
	</tbody>
</table>

<h2>regras L&eacute;xicas</h2>

<p>seguinte o aut&ocirc;mato abaixo:</p>

<h3 style="text-align:center"><strong>Aut&ocirc;mato Analisador L&eacute;xico</strong></h3>

<p style="text-align:center"><img alt="" height="201" src="https://i.stack.imgur.com/Wgyh1.png" width="715" /></p>
![alt text](https://github.com/nandoripardo888/CompiladoresPy/blob/main/compiladores.png?raw=true)


<h2>&nbsp;</h2>

<h2>Gram&aacute;tica Livre de Contexto da Linguagem - Forma BNF</h2>

<ul>
	<li>
	<p><code>&lt;programa&gt; -&gt; program ident &lt;corpo&gt; .</code></p>
	</li>
	<li>
	<p><code>&lt;corpo&gt; -&gt; &lt;dc&gt; begin &lt;comandos&gt; end</code></p>
	</li>
	<li>
	<p><code>&lt;dc&gt; -&gt; &lt;dc_v&gt; &lt;mais_dc&gt; | &lambda; </code></p>
	</li>
	<li>
	<p><code>&lt;mais_dc&gt; -&gt; ; &lt;dc&gt; | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;dc_v&gt; -&gt; &lt;tipo_var&gt; : &lt;variaveis&gt; </code></p>
	</li>
	<li>
	<p><code>&lt;tipo_var&gt; -&gt; real | integer <span style="color:#FF0000">{Memoria.tipo=real or Memoria.tipo=integer}</span></code></p>
	</li>
	<li>
	<p><code>&lt;variaveis&gt; -&gt; ident &lt;mais_var&gt; <span style="color:#FF0000">{inserir(Memoria.tipo)}{emtabela(ident.termo)}</span></code></p>
	</li>
	<li>
	<p><code>&lt;mais_var&gt; -&gt; , &lt;variaveis&gt; | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;comandos&gt; -&gt; &lt;comando&gt; &lt;mais_comandos&gt;</code></p>
	</li>
	<li>
	<p><code>&lt;mais_comandos&gt; -&gt; ; &lt;comandos&gt; | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;comando&gt; -&gt; read &lt;parident&gt; |write &lt;parident&gt; |ident|if</code></p>
	</li>
	<li>
	<p><code>&lt;parident&gt; -&gt; (ident)</code></p>
	</li>
	<li>
	<p><code>&lt;atribuir_val&gt; -&gt; := &lt;expressao&gt; <span style="color:#FF0000">{setvarutilizada(ident.termo)} {emtabela(ident.termo)}</span></code></p>
	</li>
	<li>
	<p><code>&lt;condicional&gt; -&gt; &lt;condicao&gt; then &lt;comandos&gt; &lt;pfalsa&gt; $</code></p>
	</li>
	<li>
	<p><code>&lt;condicao&gt; -&gt; &lt;expressao&gt; &lt;relacao&gt; &lt;expressao&gt;</code></p>
	</li>
	<li>
	<p><code>&lt;relacao&gt; -&gt; = | &lt;&gt; | &gt;= | &lt;= | &gt; | &lt;</code></p>
	</li>
	<li>
	<p><code>&lt;expressao&gt; -&gt; &lt;termo&gt; &lt;outros_termos&gt;</code></p>
	</li>
	<li>
	<p><code>&lt;termo&gt; -&gt; &lt;op_un&gt; &lt;fator&gt; &lt;mais_fatores&gt;</code></p>
	</li>
	<li>
	<p><code>&lt;op_un&gt; -&gt; - | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;fator&gt; -&gt; ident <span style="color:#FF0000">{setvarutilizada(ident.termo)}{emtabela(ident.termo)}</span> | numero_int | numero_real | (&lt;expressao&gt;)</code></p>
	</li>
	<li>
	<p><code>&lt;outros_termos&gt; -&gt; &lt;op_ad&gt; &lt;termo&gt; &lt;outros_termos&gt; | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;op_ad&gt; -&gt; + | -</code></p>
	</li>
	<li>
	<p><code>&lt;mais_fatores&gt; -&gt; &lt;op_mul&gt; &lt;fator&gt; &lt;mais_fatores&gt; | &lambda;</code></p>
	</li>
	<li>
	<p><code>&lt;op_mul&gt; -&gt; * | /</code></p>
	</li>
	<li>
	<p><code>&lt;pfalsa&gt; -&gt; else &lt;comandos&gt; | λ</code></p>
	</li>
</ul>

<h2>Analise sint&aacute;tica:</h2>

<p>para an&aacute;lise Sem&acirc;ntica foram adicionadas as seguintes regras</p>

<ul>
	<li>atribuir tipo ao identificador na tabela de simbolos -&gt;&nbsp;{Memoria.tipo=real or Memoria.tipo=integer} e&nbsp;{inserir(Memoria.tipo)}</li>
	<li>verificar se um&nbsp;identificador foi declarada para ser usada. -&gt;&nbsp;{emtabela{ident.termo}</li>
	<li>garantir unicidade de identificador -&gt;&nbsp;{setvarutilizada(ident.termo)} {emtabela(ident.termo)}</li>
	<li>verificar variaveis utilizadas -&gt;&nbsp;{setvarutilizada(ident.termo)</li>
</ul>

<p>&nbsp;</p>

<h2>Informa&ccedil;&otilde;es Gerais:</h2>

<ul>
	<li>O analisador sint&aacute;tico constru&iacute;do foi do tipo Descendente Preditivo Recursivo. Para cada s&iacute;mbolo n&atilde;o-terminal da gram&aacute;tica, uma nova fun&ccedil;&atilde;o foi constru&iacute;da. As produ&ccedil;&otilde;es da gram&aacute;tica foram representadas por chamadas sucessivas dessas fun&ccedil;&otilde;es.</li>
	<li>Quando um erro l&eacute;xico ou Sint&aacute;tico ou Sem&acirc;ntico &eacute; encontrado o programa &eacute; parado imediatamente uma vez que o analisador sint&aacute;tico pode encontrar erros em cascata devido ao erro inicial. e para os erros Sint&aacute;ticos e sem&acirc;nticos &eacute; colocado no arquivo o erro e a linha onde este se encontra.</li>
	<li>o programa main.py ao iniciar ira procurar todos os arquivos com extens&atilde;o&nbsp; .txt e ir&aacute; tentar compilar cada um deles, gerando uma saida individual para cada uma das entradas encontradas onde constar&aacute; as fun&ccedil;&otilde;es ou seja&nbsp; cada s&iacute;mbolo n&atilde;o-terminal da gram&aacute;tica ou os possiveis erros. (entrada.txt) -&gt; (entrada_saida.txt).</li>
	<li>No emulador terminal ser&atilde;o printados cada uma das fun&ccedil;&otilde;es ou seja&nbsp; cada s&iacute;mbolo n&atilde;o-terminal da gram&aacute;tica.</li>
	<li>por fim se o arquivo estiver de acordo com a linguagem &eacute; printado uma mensagem de sucesso tanto no arquivo quanto no emulador.</li>
</ul>

<p>&nbsp;</p>
