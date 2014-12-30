package pathwar

import "gopkg.in/mgo.v2"

// Coupons
type Coupon struct {
	Uuid string `json:"uuid"`
	code string `json:"code"`
}

func (coupon *Coupon) valid() bool {
	// FIXME: improve validation
	return true
}

func fetchAllCoupons(db *mgo.Database) []Coupon {
	coupons := []Coupon{}
	err := db.C("coupons").Find(nil).All(&coupons)
	if err != nil {
		panic(err)
	}
	return coupons
}

// Organizations
type Organization struct {
	Uuid string `json:"uuid"`
	name string `json:"name"`
}

func (organization *Organization) valid() bool {
	// FIXME: check if organization.name is reserved
	return len(organization.name) < 64
}

// OrganizationCoupons
func (organizationCoupon *OrganizationCoupon) valid() bool {
	// FIXME:
	// - check if organization exists
	// - check if coupon exists
	// - check if coupon is still available
	return true
}

type OrganizationCoupon struct {
	Organization string `json:"organization_uuid"`
	Coupon       string `json:"coupon_uuid"`
}
