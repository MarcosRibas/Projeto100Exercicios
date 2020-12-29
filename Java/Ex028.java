/*
Ex028 Escreva um programa que faça o computador ‘’pensar’’ um número inteiro 
entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo 
computador.
 */
package ex028;

import java.util.Scanner;

public class Ex028 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        int s = (int)(Math.random()*6);
        System.out.println("Pensando...");
        System.out.println("Tente adivinhar o número que estou pensan. Dica: é um número de 1 a 5.");
        int n = t.nextInt();
        if (s==n){
            System.out.println("Uau! Você acertou!");
        }
        else
        {
            System.out.printf("ERROU!(voz do faustão). O número que eu pensei foi %d. Tente novamente\n", s);
            
        }
        
    
    }
    
}
