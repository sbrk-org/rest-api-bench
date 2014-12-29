package main

import "github.com/sbrk-org/rest-api-bench/go/martini/pathwar"

func main() {
	m := pathwar.NewServer()

	// Run
	m.Run()
}
