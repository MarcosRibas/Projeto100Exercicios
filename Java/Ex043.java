/*
Ex043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre o status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso Ideal
- Entre 25 até 30: Sobrepeso
- Acima de 40: Obesidade mórbida
(É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).)

 */
package ex043;

import java.util.Scanner;

public class Ex043 {

    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        System.out.println("Qual seu peso? (kg)");
        float peso = t.nextFloat();
        System.out.println("Qual a sua altura? (m)");
        float altura = t.nextFloat();
        float imc = peso / (altura * altura);
        System.out.printf("Seu IMC é de %.1f\n", imc);
        if(imc < 18.5){
            System.out.println("Você está abaixo do peso ideal");
        }
        else if (imc>= 18.5 && imc < 25){
            System.out.println("Você está com peso ideal");
        }
        else if(imc >= 25 && imc < 30){
            System.out.println("Você está com sobrepeso");
        }
        else if(imc >= 30 && imc < 40){
            System.out.println("Você está obeso");
        }
        else{
            System.out.println("Você tem obesidade mórbida");
        }

    }
    
}
