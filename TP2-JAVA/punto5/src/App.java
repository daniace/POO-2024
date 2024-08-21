import java.time.LocalDate;

public class App {
    public static void main(String[] args) throws Exception {
        Persona persona = new Persona("Juan", "Perez", LocalDate.of(1990, 1, 1));
        System.out.println(persona.toString());
    }
}
