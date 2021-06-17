% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<form action="/home" method="post">
        <label class="form__label">
		Name:  <input class="form__input" type="text" name="AUTHOR"/>
		</label>
		<label class="form__label">
			Email: <input class="form__input" type="email" name="EMAIL"/>
		</label>
		<label class="form__label">
			Phone: <input class="form__input" type="text" name="PHONE"/>
		</label>
		<label class="form__label">
			Feedback: <textarea class="form__textarea" name="FEEDBACK"></textarea>
		</label>
		<p><input type="submit" class="btn btn-default" value="Create review"></p>
</form>
