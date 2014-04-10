
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'Servidor de Archivos estáticos' });
};