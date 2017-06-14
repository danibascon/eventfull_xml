%include('header.tpl')
<br>
	<h1>BUSCADOR DE VIDEOS</h1>
	<h1>Resultado de la busqueda <strong>{{buscar}}</strong> son:</h1>
	% for a,b in zip(lista_ti,lista_id):
		<p>Enlace: <a href="https://www.youtube.com/watch?v={{b}}"><strong>{{a}}</strong></a></p>
		<form action="/twitter" method="post">
			<input type="hidden" name="url" value="https://www.youtube.com/watch?v={{b}}"/>
    		<p><input type="submit" class="button" value="Twittear" /></p>
		</form>
		<br>
		<form action="/letra" method="post">
			<input type="hidden" name="artista" value="{{a}}"/>
    		<p><input type="submit" class="button" value="Letra" /></p>
		</form>
		<iframe width="854" height="480" src="https://www.youtube.com/embed/{{b}}"  allowfullscreen></iframe>
	%end
<br>
<p><a href="/videos">Volver atras</a></p>
%include('footer.tpl')
