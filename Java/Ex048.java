/*
Ex048 Faça um programa que calcule a soma entre todos os números impares que 
são múltiplos de três e que se encontram no intervalo de 1 até 500.
 */
package ex048;

public class Ex048 {


    public static void main(String[] args) {
        int s = 0;
        for (int c = 0; c <= 500; c+=3)
            if(c % 2 == 1){
                s = s+c;
            }
        System.out.printf("A soma de todos os números impares múltiplos de três no intervalo de 1 a 500 é %d\n",s);
        

    }
    
}
