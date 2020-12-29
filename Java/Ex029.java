/*
Ex029 Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.

 */
package ex029;

import java.util.Scanner;


public class Ex029 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("------RADAR ELETRONICO------");
        System.out.println("Velocidade do carro: ");
        int vel = t.nextInt();
        if (vel > 80){
            float multa = (vel - 80) * 7;
            System.out.printf("Velocidade a cima do permitido. Multa de R$%.2f\n", multa);
        }
        else
        {
            System.out.println("Velocidade dentro do permitido");
        }
    
    }
    
}
