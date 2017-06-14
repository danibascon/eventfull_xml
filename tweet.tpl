%include('header.tpl')  
    <h1>.::Usando la API de twitter::.</h1>
    <p>Buen momento para un tweet:</p>
    <br />
    <form action="/twittear" method="post">
      <p><textarea name="tweet" id="textbox" rows="3" cols="50" maxlength="140">
        Me ha gustado: https://www.youtube.com/channel/UCc1QpDE0iT0n6ZLckjflNHw


      </textarea></p>
      <p><input type="submit" class="button" value="Enviar" /></p>
      <p><a href="/">Buscar de nuevo</a></p>
    </form>
%include('footer.tpl')
