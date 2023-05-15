
package main

import "fmt"

func main() {
    var lado int
    var superficie int

    fmt.Print("Ingrese el valor del lado del cuadrado:")
    fmt.Scan(&lado)
    superficie = lado * lado
    fmt.Print("La superficie del cuadrado es:",superficie)
}
