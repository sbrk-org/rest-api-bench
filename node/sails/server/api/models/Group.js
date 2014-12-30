/**
* Group.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

var bcrypt = require('bcrypt');

module.exports = {

  attributes: {
    name: 'string',
    password: 'string',

    toJSON: function() {
      var obj = this.toObject();
      delete obj.password;
      return obj;
    }
  },


  beforeCreate: function(group, cb) {

    // Encrypt password
    bcrypt.hash(group.password, 10, function(err, hash) {
      if(err) return cb(err);
      group.password = hash;
      //calling cb() with an argument returns an error. Useful for canceling the entire operation if some criteria fails.
      cb();
    });

  }

};
