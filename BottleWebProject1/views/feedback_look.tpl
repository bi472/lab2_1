% rebase('layout.tpl', title=title, year=year)

%import myform

<h1>Reviews</h1>

<div>
	%reviews = myform.get_all_reviews()
	%for review in reviews:
		<div class="review review--preview">
			<h1><div class="review__title">{{review['author']}}</div></h1>
			<div class="review__author">{{review['feedback']}}</div>
			<div class="review__date">{{review['date']}}</div>
		</div>
	%end
</div>
