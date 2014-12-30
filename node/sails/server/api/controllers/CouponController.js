/**
 * CouponController
 *
 * @description :: Server-side logic for managing coupons
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

// TODO: admin action to redeem coupon to group

module.exports = {

  redeem: function(req, res) {

    var couponValue = req.param('coupon');

    if (!couponValue) return res.json(500, {error: 'coupon required'});

    // TODO: Use a service instead, if coupon can be validated only once,
    //       Maybe we don't even need a table and store info in Coupon model.
    Coupon.findOneByValue(couponValue).exec(function(err, coupon) {
      if (!coupon)
        return res.json(500, {error: 'No such coupon'});

      CouponValidation.create({group: req.group.id, coupon: coupon.id})
      .exec(function(err, values) {
        if (err)
          return res.json(500, {error: 'Server error'});

        res.json({success: 'Coupon '+coupon.value+' redeemed'});
      });
    });

  }

};
