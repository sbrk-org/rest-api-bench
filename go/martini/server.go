package main

import "github.com/go-martini/martini"

func main() {
	// Martini setup
	r := martini.NewRouter()
	m := martini.New()

	m.Use(martini.Logger())
	m.Use(martini.Recovery())
	m.MapTo(r, (*martini.Routes)(nil))
	m.Action(r.Handle)
	//m.use(martini.Static("public"))
	//m.Use(auth.Basic(AuthToken, ""))
	//m.Use(MapEncoder)

	// Methods
	r.Get("/", func() string {
		return "Hello World"
	})

	// Run
	m.Run()
}
