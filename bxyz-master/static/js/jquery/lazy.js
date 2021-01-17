function lazyload (){
	const placeholder = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
	const targets = document.querySelectorAll("img");
	targets.forEach(target => {
		target.src = placeholder
	});
	const options = {
		root: null,
		rootMargin: '0px' ,
		threshold: 0.03
	};
	const loadImage = function(entries, observer)
	{
		entries.forEach(entry => {
		if (entry.isIntersecting && entry.target.parentNode.classList.contains('loading')){
		entry.target.src = entry.target.getAttribute('data-src');
			entry.target.onload = () => {
			entry.target.parentNode.classList.remove('loading');
			entry.target.removeAttribute('data-src');
				};
			}
		});
	};
	const observer = new IntersectionObserver(loadImage, options);
	targets.forEach(target => {
	observer.observe(target);
		});
	}