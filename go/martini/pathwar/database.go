package pathwar

import (
	"github.com/go-martini/martini"
	"gopkg.in/mgo.v2"
)

type DatabaseSession struct {
	*mgo.Session
	databaseName string
}

func NewSession(name string) *DatabaseSession {
	session, err := mgo.Dial("mongodb://localhost")
	if err != nil {
		panic(err)
	}
	addIndexToCoupons(session.DB(name))
	return &DatabaseSession{session, name}
}

func addIndexToCoupons(db *mgo.Database) {
	index := mgo.Index{
		Key:      []string{"uuid"},
		Unique:   true,
		DropDups: true,
	}
	indexErr := db.C("coupons").EnsureIndex(index)
	if indexErr != nil {
		panic(indexErr)
	}
}

func (session *DatabaseSession) Database() martini.Handler {
	return func(context martini.Context) {
		s := session.Clone()
		context.Map(s.DB(session.databaseName))
		defer s.Close()
		context.Next()
	}
}
