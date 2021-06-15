% rebase('layout.tpl', title=title, year=year)

%import API

<h1>Reviews</h1>

<div>
	%orders = API.get_all_reviews()
	%for review in reviews:
		<div class="review review--preview">
			<h1 class="review__title">{{review['feedback']}}</h1>
			<time class="review__time">{{review['date']}}</time>
			<p class="review__phone review__phone--preview">{{review['phone']}}</p>
			<div class="review__author">{{review['author']}}</div>
			<a href="mailto:{{review['email']}}" class="review__email">{{review['email']}}</a>
		</div>
	%end
</div>
