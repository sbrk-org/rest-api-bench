package pathwar

import (
	"github.com/go-martini/martini"
	"github.com/martini-contrib/binding"
	"github.com/martini-contrib/render"
	"gopkg.in/mgo.v2"
)

func emptyreply() string {
	return ""
}

type Server *martini.ClassicMartini

func NewServer(session *DatabaseSession) Server {
	// Martini setup
	m := Server(martini.Classic())
	m.Use(render.Renderer(render.Options{
		IndentJSON: true,
	}))
	m.Use(session.Database())

	// Methods
	m.Get("/", func(r render.Render) {
		r.JSON(200, "Hello World !")
	})

	m.Get("/coupons", func(r render.Render, db *mgo.Database) {
		r.JSON(200, fetchAllCoupons(db))
	})

	m.Post("/coupons", binding.Json(Coupon{}),
		func(coupon Coupon, r render.Render, db *mgo.Database) {
			if coupon.valid() {
				err := db.C("coupons").Insert(coupon)
				if err != nil {
					r.JSON(400, map[string]string{
						"error": err.Error(),
					})
				} else {
					r.JSON(201, coupon)
				}
			} else {
				r.JSON(400, map[string]string{
					"error": "Not a valid coupon",
				})
			}
		})

	// Favicon, etc
	//for _, path := range []string{
	//	"/apple-touch-icon-precomposed.png",
	//	"apple-touch-icon.png", "favicon.ico"} {
	//	r.Get(path, emptyreply)
	//}

	return m
}
