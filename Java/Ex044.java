/*
Ex044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no catão: preço normal
- Em 3x ou mais no cartão: 20% de juros

 */
package ex044;

import java.util.Scanner;

public class Ex044 {


    public static void main(String[] args) {
        Scanner t = new Scanner(System.in);
        float valor;
        System.out.print("Qual o valor do produto? R$ ");
        float preco = t.nextFloat();
        System.out.println("Formas de pagamento: \n"
                + "[ 1 ] Á vista no dinheiro/cheque (10% de desconto)\n"
                + "[ 2 ] À vista no cartão (5% de desconto)\n"
                + "[ 3 ] Em até duas vezes no cartão (preço normal)\n"
                + "[ 4 ] Em 3 vezes ou mais no cartão (20% de juros)");
        System.out.println("Qual a forma de pagamento escolhida? ");
        int forma = t.nextInt();
        String x = "%";
        if (forma == 1){
            valor = preco - (preco * 10 / 100);
            System.out.printf("O valor final à vista com 10%s de desconto fica R$%.2f\n", x, valor);
        }
        else if (forma == 2){
            valor = preco - (preco * 5 / 100);
            System.out.printf("O valor final à vista com 5%s de desconto fica R$%.2f\n", x, valor);
        }
        else if (forma == 3){
            System.out.printf("Parcelando em duas vezes o produto mantém o preço de R$%.2f\n", preco);
        }
        else if (forma == 4){
            valor = preco + (preco * 20 /100);
            System.out.printf("O valor em 3 ou mais vezes com 20%s de juros fica em R$%.2f\n",x , valor);
        }
        else{
            System.out.println("Valor informado inválido, tente novamente");
        }
        
        
    
    }
    
}
