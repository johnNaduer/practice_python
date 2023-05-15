package main

import (
    "fmt"
    "net/http"
)

func main() {
    // Define a function to handle HTTP requests
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, World!")
    })

    // Start the web server on port 8080
    http.ListenAndServe(":8080", nil)
}

