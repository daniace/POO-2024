import psycopg2

class Employee:
    def __init__(self, id=None, name=None, position=None, salary=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee(id={self.id}, name='{self.name}', position='{self.position}', salary={self.salary})"


class EmployeeDAO:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = psycopg2.connect(dsn)  # Conectar a PostgreSQL
        # Si usas MySQL usa: mysql.connector.connect(**config)

    def create_employee(self, employee):
        """Crea un nuevo empleado en la base de datos."""
        query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s) RETURNING id"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (employee.name, employee.position, employee.salary))
            employee.id = cursor.fetchone()[0]
        self.conn.commit()
        return employee

    def get_employee(self, employee_id):
        """Obtiene un empleado por su ID."""
        query = "SELECT id, name, position, salary FROM employees WHERE id = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (employee_id,))
            row = cursor.fetchone()
            if row:
                return Employee(id=row[0], name=row[1], position=row[2], salary=row[3])
        return None

    def update_employee(self, employee):
        """Actualiza los datos de un empleado existente."""
        query = "UPDATE employees SET name = %s, position = %s, salary = %s WHERE id = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (employee.name, employee.position, employee.salary, employee.id))
        self.conn.commit()

    def delete_employee(self, employee_id):
        """Elimina un empleado por su ID."""
        query = "DELETE FROM employees WHERE id = %s"
        with self.conn.cursor() as cursor:
            cursor.execute(query, (employee_id,))
        self.conn.commit()

    def get_all_employees(self):
        """Obtiene todos los empleados."""
        query = "SELECT id, name, position, salary FROM employees"
        employees = []
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                employees.append(Employee(id=row[0], name=row[1], position=row[2], salary=row[3]))
        return employees

    def close(self):
        """Cierra la conexión a la base de datos."""
        self.conn.close()

class EmployeeService:
    def __init__(self, dao):
        self.dao = dao

    def add_employee(self, name, position, salary):
        employee = Employee(name=name, position=position, salary=salary)
        return self.dao.create_employee(employee)

    def get_employee(self, employee_id):
        return self.dao.get_employee(employee_id)

    def update_employee(self, employee_id, name, position, salary):
        employee = self.dao.get_employee(employee_id)
        if employee:
            employee.name = name
            employee.position = position
            employee.salary = salary
            self.dao.update_employee(employee)
            return employee
        return None

    def delete_employee(self, employee_id):
        return self.dao.delete_employee(employee_id)

    def list_all_employees(self):
        return self.dao.get_all_employees()

if __name__ == "__main__":
    # Configura la conexión (PostgreSQL DSN)
    dsn = "dbname=test user=postgres password=secret host=localhost port=5432"
    
    # Inicializa el DAO
    employee_dao = EmployeeDAO(dsn)
    
    # Inicializa el servicio de empleados
    employee_service = EmployeeService(employee_dao)
    
    # Crea un nuevo empleado
    new_employee = employee_service.add_employee("John Doe", "Developer", 75000)
    print(f"Empleado creado: {new_employee}")
    
    # Obtiene un empleado por su ID
    employee = employee_service.get_employee(new_employee.id)
    print(f"Empleado obtenido: {employee}")
    
    # Actualiza los datos del empleado
    updated_employee = employee_service.update_employee(new_employee.id, "John Smith", "Senior Developer", 85000)
    print(f"Empleado actualizado: {updated_employee}")
    
    # Lista todos los empleados
    all_employees = employee_service.list_all_employees()
    print(f"Todos los empleados: {all_employees}")
    
    # Elimina el empleado
    employee_service.delete_employee(new_employee.id)
    print(f"Empleado con ID {new_employee.id} eliminado.")
    
    # Cierra la conexión a la base de datos
    employee_dao.close()
