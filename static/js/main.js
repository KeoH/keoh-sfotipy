Sfotipy = {}
Sfotipy.Models = {}
Sfotipy.Collections = {}
Sfotipy.Views = {}

Sfotipy.Models.Song = Backbone.Model.extend({});
Sfotipy.Models.Artists = Backbone.Model.extend({});
Sfotipy.Models.Albums = Backbone.Model.extend({});

Sfotipy.Collections.Songs = Backbone.Collection.extend({
	model: Sfotipy.Models.Song
});

Sfotipy.Collections.Artists = Backbone.Collection.extend({
	model: Sfotipy.Models.Artists
});

Sfotipy.Views.Artist = Backbone.View.extend({

	tagName: 'div',
	className: 'row',
	template: Handlebars.compile($('#artist-template').html()),

	initialize: function () {
		//this.listenTo(this.model, "change", this.render, this);
	},

	render: function () {
		var artist = this.model.toJSON();
		var html = this.template(artist);
		this.$el.html(html);
		return this;
	}

});

Sfotipy.Views.Artists = Backbone.View.extend({

	el: $("#lista-artistas"),

	initialize: function () {
		this.listenTo(this.collection, "add", this.addOne, this);
		this.listenTo(this.collection, "reset", this.render, this);
	},

	render: function () {
		this.$el.empty();
		this.addAll();
	},

	addOne: function (artist) {
		var artistview = new Sfotipy.Views.Artist({ model: artist });
		this.$el.append(artistview.render().el);
	},

	addAll: function () {
		this.collection.forEach(this.addOne, this);
	}
});

Sfotipy.Views.Song = Backbone.View.extend({

	tagName: 'div',
	className: 'row',
	template: Handlebars.compile($('#song-template').html()),

	initialize: function () {
		//this.listenTo(this.model, "change", this.render, this);
	},

	render: function () {

	}
});


function busca_artista (artist_id) {
	url = 'http://api.jamendo.com/v3.0/artists/?client_id=decdc402&format=json&id='+artist_id
	return url
}

function artistas (cantidad) {
	url = 'http://api.jamendo.com/v3.0/artists/?client_id=decdc402&format=json&limit='+cantidad
	return url
}
//'http://api.jamendo.com/v3.0/artists/?client_id=decdc402&format=json&id='+artist_id



Sfotipy.Router = Backbone.Router.extend({

	routes: {
		"": "index",
	},

	initialize: function () {
		console.log("init ...");

		this.current = {};
		this.jsonData = {};

		this.artists = new Sfotipy.Collections.Artists();
		this.artistslist = new Sfotipy.Views.Artists({ collection: this.artists });


		Backbone.history.start();
	},

	index: function () {
		this.fetchData();
	},

	fetchData: function () {
		var self = this;
		return $.getJSON(artistas(10)).then(function (data) {
			data = data.results;
			self.jsonData = data;
			for(artista in data){
				self.addArtist(data[artista]);
			}
		});
	},

	addArtist: function (artista) {
		this.artists.add( new Sfotipy.Models.Artists({
			name: artista.name,
			id: artista.id,
			website: artista.website,
			joindate: artista.joindate,
			image: artista.image 
		}));
	}

});

window.Sfotipy = Sfotipy

$(function() {
	Sfotipy.app = new Sfotipy.Router();
	
	$('#datosaenviar').val(Sfotipy.app.artists.toJSON());
});