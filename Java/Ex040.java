/*
Ex040 Crie um programa que calcule duas notas de um aluno e calcule sua média, mostrando a mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
REPROVADO
- Média entre 5.0 e 6.9:
RECUPERAÇÃO
- Média 7.0 ou superior:
APROVADO

 */
package ex040;

import java.util.Scanner;


public class Ex040 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Nota um: ");
        float n1 = t.nextFloat();
        System.out.println("Nota dois: ");
        float n2 = t.nextFloat();
        float media = (n1 + n2) / 2;
        System.out.printf("Sua média é de %.1f \n",media);
        if(media < 5){
            System.out.println("Está REPROVADO");
        }else if (media >= 5 && media < 7){
            System.out.println("Ficou em RECUPERAÇÃO");
        }
        else{
            System.out.println("Parabéns! Está APROVADO");
        }

    }
    
}
