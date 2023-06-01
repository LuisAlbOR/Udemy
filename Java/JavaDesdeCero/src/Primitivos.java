public class Primitivos {
    public static void main(String[] argos){
        byte numeroByte = 8;
        System.out.println("numeroByte = " + numeroByte);
        System.out.println("Tipo Byte corresponde a: " + Byte.BYTES);
        System.out.println("Tipo Byte corresponde a: " + Byte.SIZE);
        System.out.println("El valor minimo de un byte: " + Byte.MIN_VALUE);
        System.out.println("El valor maximo de un byte: " + Byte.MAX_VALUE);

        short numeroShort = 10000;
        System.out.println("numeroShort: " + numeroShort);
        System.out.println("Tipo short corresponde en byte: " + Short.BYTES);
        System.out.println("Tipo short corresponde en bite: " + Short.SIZE);
        System.out.println("El valor minimo de un short: "  + Short.MIN_VALUE);
        System.out.println("El valor maximo de un short: " + Short.MAX_VALUE);

        int numeroInt = 32768;
        System.out.println("numeroInt = " + numeroInt);
        System.out.println("Tipo int corresponde en byte: " + Integer.BYTES);
        System.out.println("Tipo int corresponde en bite: " + Integer.SIZE);
        System.out.println("El valor minimo de un int: "  + Integer.MIN_VALUE);
        System.out.println("El valor maximo de un int: " + Integer.MAX_VALUE);

        long numeroLong = 2147483648L;
        System.out.println("numeroLong = " + numeroLong);
        System.out.println("Tipo long corresponde en byte: " + Long.BYTES);
        System.out.println("Tipo long corresponde en bite: " + Long.SIZE);
        System.out.println("El valor minimo de un long: "  + Long.MIN_VALUE);
        System.out.println("El valor maximo de un long: " + Long.MAX_VALUE);

        //El valor por defecto de cualquier dato primitivo numérico es 0
    }
}
