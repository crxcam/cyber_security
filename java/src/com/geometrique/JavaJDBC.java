package src.com.geometrique;
//package cours_exercices;

//java -classpath ".;mysql-connector-j-8.3.0.jar" JavaJDBC.java

//javac JavaJDBC.java

import java.sql.*;
import java.util.Date;

public class JavaJDBC {
	static String cxn_url = "jdbc:mysql://localhost:3306/formation";
	static String user = "root";
	static String pswd = "root";
	static String sql_query_create_table = "create table if not exists forms(id int primary key, longeur int ,largeur int,distance int, name varchar(30) );";
	static String sql_query_insert_table = "insert into java_table values (2,'test');";
	// static String sql_query_get_all_table = "select * from java_table;";
	static Connection cxn;

	public static void main(String[] args) {
		Connection my_cxn = get_connexion();
		execute_sql(my_cxn, sql_query_create_table);
		save_Form(my_cxn);

	}

	// Point

	public static void save_Form(Connection my_cxn) {
		Point p = new Point(8, 4);
		Rectangle r = new Rectangle(p, 42, 12);
		String query = "insert into forms values (" + new Date().getTime() + "," + r.longeur + "," + r.largeur + ","
				+ r.point.distance + ",rectangle";
		execute_sql(my_cxn, query);
	}

	public static Connection get_connexion() {
		try {
			cxn = DriverManager.getConnection(cxn_url, user, pswd);
			return cxn;
		} catch (SQLException e) {
			System.out.println("### => JavaJDBC connexion exception :" + e);
			return cxn;
		}
	}

	public static void execute_sql(Connection cxn, String sql) {
		try {
			Statement st = cxn.createStatement();
			st.executeUpdate(sql);
			// cxn.close();
			System.out.println("### => JavaJDBC execute_sql " + sql);
		} catch (SQLException e) {
			System.out.println("### => JavaJDBC execute_sql EXCEPTION " + sql);
			System.out.println("### => JavaJDBC connexion exception :" + e);
		}
	}

}
