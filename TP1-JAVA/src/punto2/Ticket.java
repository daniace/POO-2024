public class Ticket {
    private int nventa;
    private LocalDate fecha;
    private double total;
    private ArrayList<Medicamento> Medicamento;

    public Ticket(int nventa, LocalDate fecha, double total) {
        this.nventa = nventa;
        this.fecha = fecha;
        this.total = total;
        Medicamento = new ArrayList<Medicamento>();
    }

    public int getNventa() {
        return nventa;
    }

    public void setNventa(int nventa) {
        this.nventa = nventa;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public void setFecha(LocalDate fecha) {
        this.fecha = fecha;
    }

    public double getTotal() {
        return total;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public ArrayList<Medicamento> getMedicamento() {
        return Medicamento;
    }

    public void setMedicamento(ArrayList<Medicamento> Medicamento) {
        this.Medicamento = Medicamento;
    }

    public void imprimeMedicamento() {
        for (Medicamento m : Medicamento) {
            System.out.println(m);
        }
    }
}

public class Medicamento {
    private String nombre;
    private int dosis;
    private float precio;

    public Medicamento(String nombre, int dosis, float precio) {
        this.nombre = nombre;
        this.dosis = dosis;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getDosis() {
        return dosis;
    }

    public void setDosis(int dosis) {
        this.dosis = dosis;
    }

    public float getPrecio() {
        return precio;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }
}
