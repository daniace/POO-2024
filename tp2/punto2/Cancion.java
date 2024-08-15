public class Cancion {
    private String nombre;
    private String autor;
    private int duracion;

    public Cancion(String nombre, String autor, int duracion) {
        this.nombre = nombre;
        this.autor = autor;
        this.duracion = duracion;
    }

    public Cancion(){
        this.nombre = "";
        this.autor = "";
        this.duracion = 0.0;
    }

    public String getNombre() {
        return nombre;
    }

    public String getAutor() {
        return autor;
    }

    public int getDuracion() {
        return duracion;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setDuracion(int duracion) {
        this.duracion = duracion;
    }

    public String toString() {
        return "Nombre: " + nombre + "\nAutor: " + autor + "\nDuracion: " + duracion;
    }
}