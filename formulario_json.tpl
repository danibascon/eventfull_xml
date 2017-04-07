%include('header.tpl')
<br>
	<h1>Los eventos que hay en <strong>{{ciudad}}</strong> del tipo <strong>{{tipo}}</strong> son:</h1>
	% for x in js["events"]["event"]:
		<li>Evento: {{x["title"]}} --> Fecha: {{x["start_time"]}}</li>
	%end
</br>
%include('footer.tpl')
