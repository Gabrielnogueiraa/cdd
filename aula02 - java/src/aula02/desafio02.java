package aula02;
import java.util.Scanner;

public class desafio02 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		double[] notas;
		notas = new double[5];
		double soma = 0;
		double media = 0;
		for(int x=0; x <= notas.length -1;x++) {
			System.out.printf("digite a %d primeira nota: ", x + 1);
			notas[x] = scanner.nextDouble();
		}
		System.out.print("as notas são: ");
		for(int i=0; i <= notas.length -1; i++) {
			System.out.print(notas[i] + " ");
		}
		for(int j = 0; j <= notas.length - 1; j++) {
			soma += notas[j];
		}
		media = soma / notas.length;
		System.out.printf("\na media final da turma é igual a: %2f ", media);
	}
}
