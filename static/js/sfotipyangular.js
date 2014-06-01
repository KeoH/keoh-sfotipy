(function() {
	var app = angular.module('sfotipy', []);
	/*.config([
    '$httpProvider', 
    '$interpolateProvider', 
    function($httpProvider, $interpolateProvider) {
        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    }]).
    run([
    '$http', 
    '$cookies', 
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    }]);*/

	app.controller('TophitsController', ['$http',function($http){
			var lista = this;
			$http.get('/api/tracks/?format=json').success(function(data){
				//console.log("datos");
				window.products =data;
				lista.products = data;
			}).error(function(e){
				console.log("Error");
			});
		}]);

	app.controller('SectionController', ['$http', function($http){
		this.tab = 1;
		this.user = user
		var lista = this;

		this.IsSection = function(seccion){
			return seccion==this.tab;
		};

		this.setSection = function(seccion){
			this.tab = seccion;
		};

		this.trackdetail = function(id){
			this.tab = 5;
			$http.get('/api/tracks/'+id+'/?format=json').success(function(data){
				lista.product = data;
				var albumid = lista.product.album.id;
				$http.get('/api/albums/'+albumid+'/?format=json').success(function(data){
					lista.album = data;
					console.log(lista.album);
				});

			}).error(function(e){
				console.log("Error");
			});
			
		};
	}]);
})();

