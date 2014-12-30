module.exports = function Authentificated (req, res, next) {
  var token;

  if (req.headers && req.headers.authorization) {
    var parts = req.headers.authorization.split(' ');
    if (parts.length == 2) {
      var scheme = parts[0],
      credentials = parts[1];

      if (/^Bearer$/i.test(scheme)) {
        token = credentials;
      }
    }
    else {
      return res.json(401, {error: 'Format is Authorization: Bearer [token]'});
    }
  }
  else if (req.param('token')) {
    token = req.param('token');
    delete req.query.token;
  }
  else {
    return res.json(401, {error: 'No Authorization header was found'});
  }

  TokenService.verifyToken(token, function(err, token) {
    if (err) return res.json(401, {error: 'The token is not valid'});

    Group.findOne({ id: token.sid })
    .exec(function (err, group) {
      if (err) return next(err);
      if (!group) return res.json(401, {error: 'The token is not valid'});

      req.group = group;
      next();
    });

  });
};
