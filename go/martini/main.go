package main

import "github.com/sbrk-org/rest-api-bench/go/martini/pathwar"

func main() {
	session := pathwar.NewSession("pathwar")
	server := pathwar.NewServer(session)
	server.Run()
}
