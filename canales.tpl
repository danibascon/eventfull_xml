%include('header.tpl')
<br>
	<h1>BUSCADOR DE CANALES</h1>
	<form action="/canal" method="post">
		<label>Nombre del canal:</label>
		<input type="text" name="buscar" required/>
		<label>Numero de videos:</label>
		<input type="number" name="cantidad" min='1' value='1' max='10' required/>
		<input type="submit" value="Enviar">
	</form>
<br>
<p><a href="/">Volver atras</a></p>
%include('footer.tpl')

