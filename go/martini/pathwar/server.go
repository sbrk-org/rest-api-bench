package pathwar

import (
	"github.com/go-martini/martini"
	"github.com/martini-contrib/method"
)

func emptyreply() string {
	return ""
}

type Server *martini.Martini

func NewServer() Server {
	// Martini setup
	m := Server(martini.New())
	r := martini.NewRouter()

	m.Use(martini.Logger())
	m.Use(martini.Recovery())
	m.Use(method.Override())
	m.MapTo(r, (*martini.Routes)(nil))
	m.Action(r.Handle)
	//m.use(martini.Static("public"))
	//m.Use(auth.Basic(AuthToken, ""))
	//m.Use(MapEncoder)

	// Methods
	r.Get("/", func() string {
		return "Hello World"
	})

	// Favicon, etc
	for _, path := range []string{
		"/apple-touch-icon-precomposed.png",
		"apple-touch-icon.png", "favicon.ico"} {
		r.Get(path, emptyreply)
	}

	return m
}
