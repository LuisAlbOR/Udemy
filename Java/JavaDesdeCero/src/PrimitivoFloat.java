public class PrimitivoFloat {
    public static void main(String[] args) {
        float realFloat = 1.0F;
        System.out.println("numeroFloat = " + realFloat);
    
        float realFloatExponente = 2.13e5F;
        System.out.println("realFloatExponente = " + realFloatExponente);
    
        float realFloatExponenteNegativo = 0.00000000015F;//1.5e-10F;
        System.out.println("realFloatExponenteNegativo = " + realFloatExponenteNegativo);
        System.out.println("Float corresponde en byte: " + Float.BYTES);
        System.out.println("Float corresponde en bites: " + Float.SIZE);
        System.out.println("El valor minimo de float: " + Float.MIN_VALUE);
        System.out.println("El valor maximo de float: " + Float.MAX_VALUE);

        double realDouble = 3.4028235E38;
        System.out.println("realDouble = " + realDouble);
        System.out.println("Double corresponde en byte: " + Double.BYTES);
        System.out.println("Double corresponde en bites: " + Double.SIZE);
        System.out.println("El valor minimo de double: " + Double.MIN_VALUE);
        System.out.println("El valor maximo de double: " + Double.MAX_VALUE);


    }
}
