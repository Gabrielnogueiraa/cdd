package aula02;

public class ex02 {

	public static void main(String[] args) {
		int[] arrayUm = {12,3,5,68,9,6,73,44,456,65,321};
		int[] arrayDois = {43,42,4,8,55,21,2,45};
		
		if (arrayDois.length > 8) {
			System.out.println("tamanho do arrayDois - Maior que 8!");
		} else if (arrayDois.length == 8) {
			System.out.println("tamano do arrayDois - Igual a 8!");
		} else {
			System.out.println("tamanho do arrayDois - Menor que 8!");
		}
			System.out.println("\nTamanho do arrayUm = "+arrayUm.length);
	}

}
