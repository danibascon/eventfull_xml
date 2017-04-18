%include('header.tpl')
<br>
	<h1>Los eventos que hay en <strong>{{ciudad}}</strong> del tipo <strong>{{tipo}}</strong> son:</h1>
	% for x,y in zip(titulo,empezar):
		<li>Evento: {{x.text}} --> Fecha: {{y.text}}</li>
	%end
</br>
%include('footer.tpl')
