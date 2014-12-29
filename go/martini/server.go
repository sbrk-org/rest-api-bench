package main

import "github.com/go-martini/martini"

func main() {
	m := martini.New()
	m.Use(martini.Recovery())
	m.Use(martini.Logger())
	//m.Use(martini.Router())
	//m.use(martini.Static())
	//m.Use(auth.Basic(AuthToken, ""))
	//m.Use(MapEncoder)

	r := martini.NewRouter()
	r.Get("/", func() string {
		return "Hello World"
	})
	m.Action(r.Handle)
	m.Run()
}
