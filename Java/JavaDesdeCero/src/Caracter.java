public class Caracter {
    public static void main(String[] args) {
        char  caracter = '\u0040';
        System.out.println("caracter = " + caracter);
        char decimal = 64;
        System.out.println("decimal = " + decimal);
        System.out.println("¿Decimal = Caracter?: " +(decimal==caracter));

        System.out.println("Char en bytes: " + Character.BYTES);
        System.out.println("Char en bites: "+ Character.SIZE);
        System.out.println("Char.MIN_VALUE " + Character.MIN_VALUE);
        System.out.println("Char.MAX_VALUE " + Character.MAX_VALUE);
    }
}
