using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using MySql.Data.MySqlClient;
using System.Runtime.Remoting;

namespace Lenguajes_programacion
{
    public partial class Form1 : Form
    {

        private MySqlConnection conexion = new MySqlConnection ("Server=localhost; Database=formulario;User=Felix;Password=Felix.2023");

        public Form1()
        {
            InitializeComponent();
        }

        public DataTable ConsultarFormulario()
        {
            DataTable dt = new DataTable();

            try
            {
                conexion.Open();

                // Consulta SQL para seleccionar todos los registros de la tabla "formulario"
                string consulta = "SELECT * FROM formulario";

                using (MySqlCommand cmd = new MySqlCommand(consulta, conexion))
                {
                    using (MySqlDataAdapter da = new MySqlDataAdapter(cmd))
                    {
                        da.Fill(dt);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
            finally
            {
                conexion.Close();
            }

            return dt;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void txtID_TextChanged(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = ConsultarFormulario();
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs clic)
        {
            string nombre = txtNombre.Text;
            string edad = txtEdad.Text;
            string estado = txtEstado.Text;

            conexion.Close();

            using (conexion)
            {
                try
                {
                    // Abrir la conexión
                    conexion.Open();

                    // Crear una consulta SQL parametrizada para insertar el usuario en la tabla
                    string query = "INSERT INTO formulario (Nombre, Edad, Estado) VALUES (@Nombre, @Edad, @Estado)";

                    // Crear un comando SQL
                    using (MySqlCommand command = new MySqlCommand(query, conexion))
                    {
                        // Agregar parámetros para la consulta
                        command.Parameters.AddWithValue("@Nombre", nombre);
                        command.Parameters.AddWithValue("@Edad", edad);
                        command.Parameters.AddWithValue("@Estado", estado);

                        // Ejecutar la consulta para insertar el usuario
                        int rowsAffected = command.ExecuteNonQuery();

                        if (rowsAffected > 0)
                        {
                            Console.WriteLine("Usuario registrado correctamente.");
                        }
                        else
                        {
                            Console.WriteLine("No se pudo registrar al usuario.");
                        }
                        limpiar();
                    }

                    // Cerrar la conexión
                    conexion.Close();
                }
                catch (Exception ex)
                {
                    Console.WriteLine("Error: " + ex.Message);
                }
            }
        }

        void limpiar()
        {
            txtID.Text = "";
            txtNombre.Text = "";
            txtEdad.Text = "";
            txtEstado.Text = "";
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            string id_1 = txtID.Text;
            string nombre_1 = txtNombre.Text;
            string edad_1 = txtEdad.Text;
            string estado_1 = txtEstado.Text;

            try
            {
                conexion.Open();

                // Consulta SQL para actualizar un registro en la tabla "formulario" por ID
                string consulta = "UPDATE formulario SET Nombre = @Nombre, Edad = @Edad, Estado = @Estado WHERE ID = @ID";

                using (MySqlCommand command = new MySqlCommand(consulta, conexion))
                {
                    command.Parameters.AddWithValue("@Nombre", nombre_1);
                    command.Parameters.AddWithValue("@Edad", edad_1);
                    command.Parameters.AddWithValue("@Estado", estado_1);
                    command.Parameters.AddWithValue("@ID", id_1);

                    command.ExecuteNonQuery();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            finally
            {
                conexion.Close();
            }
            
        }

        private void borrarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string id_1 = txtID.Text;

            try
            {
                conexion.Open();

                // Consulta SQL para actualizar un registro en la tabla "formulario" por ID
                string consulta = "DELETE FROM formulario WHERE ID = @ID";

                using (MySqlCommand command = new MySqlCommand(consulta, conexion))
                {
            
                    command.Parameters.AddWithValue("@ID", id_1);

                    command.ExecuteNonQuery();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
            finally
            {
                conexion.Close();
            }
        }

        private void txtNombre_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtEdad_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtEstado_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtBuscar_TextChanged(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            int fila = dataGridView1.CurrentCell.RowIndex;

            txtID.Text = dataGridView1[0, fila].Value.ToString();
            txtNombre.Text = dataGridView1[1, fila].Value.ToString();
            txtEdad.Text = dataGridView1[2, fila].Value.ToString();
            txtEstado.Text = dataGridView1[3, fila].Value.ToString();
        }
    }
}
