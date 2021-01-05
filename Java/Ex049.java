/*
Ex049 Refaça o desafio 009, mostrando a tabuada de um número que o usuário 
escolher, só que agora utilizando um laço for.
*/
package ex049;

import java.util.Scanner;

public class Ex049 {

    public static void main(String[] args) {
        
        Scanner t = new Scanner(System.in);
        System.out.println("Digite o número no qual você deseja saber a tabuada: ");
        int i = t.nextInt();

	for (int j = 0; j<=10; j++){
	System.out.println (i+" x "+ j + " = " + i*j);
		}
	}
}

    
    

