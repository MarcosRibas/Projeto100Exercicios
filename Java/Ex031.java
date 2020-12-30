/*
Ex031 Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas.

 */
package ex031;

import java.util.Scanner;


public class Ex031 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual a distância da viagem?(km)");
        int km = t.nextInt();
        float val;
        if(km < 200){
           val = ((float) km * 0.50f);
        }
        else
        {
           val = ((float) km * 0.45f);
            
        }
        
        System.out.printf("O valor da passagem é R$%.2f\n", val);
    
    }
    
}
