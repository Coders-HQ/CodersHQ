$(document).ready(function(){

(function(){

	if(!('requestAnimationFrame' in window)) return;
	if(/Mobile|Android/.test(navigator.userAgent)) return;

	var backgrounds = [];

	$('.parallax').each(function(){
		var el = $(this);
		var bg = el.children('.parallax-background');
		bg.css({
			position: 'absolute',
			'min-width':'100%',
            'width':'auto',
            'min-height': '100vh',
			top:0, left:0,
			zIndex: -100,
            display: 'block'
		});
		backgrounds.push(bg);

		el.css({
			position:'relative',
			background:'transparent',
			overflow: 'hidden',
		});
	});

	if(!backgrounds.length) return;

	var visible = [];
	var scheduled;

	$(window).on('scroll resize', scroll);

	scroll();

	function scroll(){

		visible.length = 0;

		for(var i = 0; i < backgrounds.length; i++){
			var rect = backgrounds[i][0].parentNode.getBoundingClientRect();

			if(rect.bottom > 0 && rect.top < window.innerHeight){
				visible.push({
					rect: rect,
					node: backgrounds[i]
				});
			}

		}

		cancelAnimationFrame(scheduled);

		if(visible.length){
			scheduled = requestAnimationFrame(update);
		}

	}

	function update(){

		for(var i = 0; i < visible.length; i++){
			var rect = visible[i].rect;
			var node = visible[i].node[0];

			var quot = Math.max(rect.bottom, 0) / (window.innerHeight + rect.height);
            var shift = '';
            if (node.hasAttribute('parallax-center')) {
                var nodeHeight = visible[i].node.outerHeight();
                shift = -((nodeHeight - rect.height)/2 + rect.top) + 'px';
            } else {
                shift = -rect.top+'px';
            }
            console.log(shift);
			node.style.transform = 'translate3d(0, '+(shift)+', 0)';
		}

	}

})();
});