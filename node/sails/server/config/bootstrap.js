/**
 * Bootstrap
 * (sails.config.bootstrap)
 *
 * An asynchronous bootstrap function that runs before your Sails app gets lifted.
 * This gives you an opportunity to set up your data model, run jobs, or perform some special logic.
 *
 * For more information on bootstrapping your app, check out:
 * http://sailsjs.org/#/documentation/reference/sails.config/sails.config.bootstrap.html
 */

function logCreated(message) {
    return function(err, values) {
      if (err) return console.log(err);
      console.log(message);
    }
}

module.exports.bootstrap = function(cb) {

  var testGroups = [{name: 'ken-mousse_a_raser', password: 'gomme'}, {name: 'anal', password: 'mobylette'}];
  var testLevels = [{name: 'gilbert-le-bg'}, {name: 'nabilla'}];
  var testCoupons = [{value: 'testcoupon', reward: 42}, {value: 'cyberenclume', reward: 1337}];

  Coupon.create(testCoupons).exec(logCreated('Test coupons created'));
  Group.create(testGroups).exec(logCreated('Test groups created'));

  // It's very important to trigger this callback method when you are finished
  // with the bootstrap!  (otherwise your server will never lift, since it's waiting on the bootstrap)
  cb();
};
