// PREPARCIAL LAURA MONTAÑA Y CAROL MORALES

public class Poo {
    public static void main(String[] args) {
        /*
         * 1 Metodo length: devuelve la longitud de cadena
         * String a="Hola soy Pepito";
         * int length=a.length();
         * System.out.println("Longitud de cadena: "+length);
         */

        /*
         * 2 Metodo charAt: devuelve el caracter que corresponde a su posicion segun el
         * index
         * String a="Hola soy Pepito";
         * System.out.println("Caracter en la posicion 0: "+a.charAt(0));
         */

        /*
         * 3 Metodo isEmpty: devuelve un booleano que determina si el string esta vacio
         * o no
         * String a="Hola soy Pepito";
         * System.out.println(a.isEmpty());
         */

        /*
         * 4 Metodo substring: devuelve la cadena a partir del index indicado
         * String a="Hola soy Pepito";
         * System.out.println(a.substring(9));
         */

        /*
         * 5 Metodo concat: concatena dos o mas cadenas
         * String a="Pepito";
         * System.out.println(a.concat("@gmail.com"));
         */

        /*
         * 6 Metodo startsWith: devuelve un booleano que determina si la variable
         * empieza con una cadena
         * String a="Hola soy Pepito";
         * System.out.println(a.startsWith("Hola"));
         */

        /*
         * 7 Metodo toUpperCase: devuelve la cadena en mayusculas
         * String a="Hola soy Pepito";
         * System.out.println(a.toUpperCase());
         */

        /*
         * 8 Metodo toLowerCase: devuelve la cadena en minusculas
         * String a="Hola soy Pepito";
         * System.out.println(a.toLowerCase());
         */

        /*
         * 9 Metodo trim: elimina espacios iniciales y finales
         * String a=" Hola soy Pepito ";
         * System.out.println(a.trim());
         */

        /*
         * 10 Metodo split: imprime cada cadena que hace parte de una matriz
         * String strMain = "Pepito,Carol,Laura";
         * String[] arrSplit = strMain.split(",");
         * for (int i = 0; i<arrSplit.length; i++) {
         * System.out.println(arrSplit[i]);
         * }
         */

        /*
         * 11 Metodo replace: reemplaza un valor en la cadena
         * String a="Hola soy Pepito";
         * System.out.println(a.replace("Pepito","Carol"));
         */

        /*
         * 12 Metodo replaceAll: reemplaza caracteres que cumplan con la expresion
         * regular
         * String str = "Hola soy Pepito";
         * String str2 = str.replaceAll("\\s", "");//remueve espacios en blanco
         * System.out.println(str2);
         */

        /*
         * 13 Metodo replaceFirst: remplaza un carcater de la cadena
         * String str = "Hola soy Pepito";
         * String str2 = str.replaceFirst("s", "z");
         * System.out.println(str2);
         */

        /*
         * 14 Metodo endsWith: devuelve un booleano que determina si la variable termina
         * con una cadena
         * String a="Hola soy Pepito";
         * System.out.println(a.endsWith("Pepito"));
         */

        /*
         * 15 Metodo contentEquals compara caracteres true: son iguales false si no
         * String a="Hola soy Pepito";
         * System.out.println(a.contentEquals("hola soy pepito"));
         */
        /*
         * 16 Metodo valueOf une el array
         * char miarray[]={'H', 'o', 'l' , 'a'};
         * System.out.println(String.valueOf(miarray));
         */

        /*
         * 17 Metodo toCharArray enumera los caracteres en el array
         * String a="Hola soy Pepito";
         * char[] a2 = a.toCharArray();
         * for (int x=0;x<a2.length;x++)
         * System.out.println("[" + x + "] " + a2[x]);
         */
        /*
         * //18 Metodo Matches se usa comprobar si un string cumple una expresion
         * regular
         * String a="Hola soy Pepito";
         * System.out.println("Hola, como te llamas? "+a.matches("Hola"));
         */
        /*
         * 19. Metodo intern se usa para obtener la cadena de la memoria si ya exite, es
         * decir el metodo asegura que que todos mismas cuerdas compartan la misma
         * memoria
         * String str1="Hola";
         * String str2 = new String("Hola").intern();
         * System.out.println("str1==str2: "+(str1==str2));
         */
        /*
         * 20.El método indexOf devuelve el índice del primer carácter de la subcadena
         * pasado como un parámetro a él
         * String a="Hola soy Pepito";
         * System.out.println("Indice de caracteres: 'o':"+a.indexOf('o'));
         */
        /*
         * 21. Metodo format retorna nuevo string
         * String str1 = "Soy";
         * String str2 = "Pepito";
         * String str3 = String.format("%s %s", str1, str2);
         * System.out.println(str3);
         */
        /*
         * 22. Metodo concat sirve para una concatenación entre dos cadenas
         * String str = "Pepito es muy... ";
         * str = str.concat(args[0]);
         * System.out.println(str);
         */
        /*
         * 23. Meodo regionMatches comprueba si dos cadenas son iguales
         * String str1 = new String("Hola, soy Pepito");
         * String str2 = new String("Hola");
         * System.out.println(str1.regionMatches(2, str2, 0, 3));
         */
        /*
         * //24. Metodo subSequence nos ayuda a imprimir caracteres de la manera que
         * elijamos el inicio y el final
         * String cdn = "Bienvenidos a tinchicus.com";
         * System.out.println(cdn.subSequence(0,11));
         */
        /*
         * 25. Método chars nos devuelve la cadena de texto como un InputStream.
         * String a = "Hola somos Carol, Laura y Pepito";
         * a.chars()
         * .forEach(c -> System.out.print(Character.toString((char) c)));
         */
    }
}
