/*
Ex015 Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 
por km rodado.
 */
package ex015;

import java.util.Scanner;


public class Ex015 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Quantos km você percorreu? ");
        float km = t.nextFloat();
        System.out.println("Quantos dias você ficou com o carro?");
        int dia = t.nextInt();
        float valor = (dia * 60f) + (0.15f * km);
        System.out.printf("O valor a pagar é: R$%.2f %n", valor);

    }
    
}
