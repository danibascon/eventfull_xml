%include('header.tpl')
<br>
	<h1>BUSCADOR DE VIDEOS</h1>
	<form action="/formulario" method="post">
		<label>Nombre que buscar:</label>
		<input type="text" name="buscar" required/>
		<label>Numero de videos:</label>
		<input type="number" name="cantidad" min='1' value='1' max='10' required/>
		<input type="submit" value="Enviar">
	</form>
<br>
<p><a href="/">Volver atras</a></p>
%include('footer.tpl')




