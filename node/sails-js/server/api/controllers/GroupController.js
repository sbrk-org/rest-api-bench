/**
 * GroupController
 *
 * @description :: Server-side logic for managing groups
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

var bcrypt = require('bcrypt');

module.exports = {

  login: function(req, res) {

    console.log(req.body);

    Group.findOneByName(req.body.name).exec(function(err, group) {

      if (err) return res.json({error: 'DB error'}, 500);
      if (!group) return res.json({error: 'invalid username or password'}, 403);

      bcrypt.compare(req.body.password, group.password, function(err, match) {
        if (err) return res.json({error: 'Server error'}, 500);

        if (!match) {
          return res.json({error: 'invalid username or password'}, 403);
        }
        else {
          res.json({group: group, token: TokenService.issueToken({sid: group.id})});
        }
      });

    });
  },

  logout: function(req, res) {
    res.send("Successfully logged out");
  }

};
