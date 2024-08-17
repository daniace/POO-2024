public class App {
    public static void main(String[] args) throws Exception {
        Cancion cancion = new Cancion();
        cancion.setNombre("Un velero llamado libertad");
        cancion.setAutor("Jose Luis Perales");
        cancion.setDuracion(222.0);

        System.out.println(cancion.getNombre());
        System.out.println(cancion.getAutor());
        System.out.println(cancion.getDuracion());
    }
}