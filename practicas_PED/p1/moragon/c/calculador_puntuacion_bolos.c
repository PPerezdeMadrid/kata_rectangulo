#include <string.h>

int cast_to_int(char character){
	if(character == 'X' | character == '/'){
		return 10;
	}else return character - '0';
}

int calcular_resultado(char* partida){
	int resultado = 0, extra = 0, plus = 0, valor = 0;

	resultado += arreglar_plus_final(partida);
	
	// printf("\n\n%d", resultado);
		
	for(int i = 0; partida[i] != '\0'; i++){
		if(partida[i] == 'X'){ //CASO DE STRIKE
			valor = 10;
			plus = 2;
			// printf("\nENTRA EN X\n");
		}else if(partida[i] == '/'){ // CASO DE SPARE
			resultado -= cast_to_int(partida[i-1]); // ELIMINAMOS EL VALOR ANTERIOR
			valor = 10;
			plus = 1;
			// printf("\nENTRA EN /\n");
		}else{ // PUNTUACIÓN ESTANDAR
			valor = cast_to_int(partida[i]);
			// printf("\nENTRA EN num\n");
		}

		if(extra>0){ // SE DEBE SUMAR EL PLUS DE / o X.
			if(extra>2){ // ESTO SIGNIFICA QUE HAY MÁS DE UN / o X
				resultado += valor; // AQUI ESTÁ EL ERROR
				extra -= 1;
			}
			resultado += valor;
			extra -= 1;
		}

		resultado += valor;
		// printf("%d -> %d\n", cast_to_int(partida[i]), resultado);

		if(valor == 10){
			extra += plus;
		}

	}

	return resultado;
}

int arreglar_plus_final(char* partida){
	int total = strlen(partida), mod = 0, n = strlen(partida);
	for(int i = 0; partida[i] != '\0'; i++){
		if(partida[i] == 'X'){
			total += 1;
		}
	}

	mod = total % 20;
	
	if(mod == 1){ // Spare al final
		return - cast_to_int(partida[strlen(partida)-1]);
	}else if(mod > 1){ // Strike al final
		return -(cast_to_int(partida[strlen(partida)-1]) + 
				cast_to_int(partida[strlen(partida)-2]) + 
				(10 * (partida[n-1] == 'X' & partida[n-2] == 'X')) // Para el caso expecifico ...nXXX
				);
	}else if(mod == 0){ // Sin bonus final
		return 0;
	}else{ // Error
		return -11;
	}

	
}
/*
int cast_to_int(char character){
	if(character == 'X' | character == '/'){
		return 10;
	}else return character - '0';
}
*/
