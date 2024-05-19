#include <stdio.h>
#include <assert.h>
#include <stdbool.h>
#include "calculador_puntuacion_bolos.c"

static void test_prueba_uno(){
	assert(1);
}

static void test_prueba_dos(){
	assert(!0);
}

static void test_calcular_partida_uno(){
	char* partida = "00000000000000000000";
	assert(calcular_resultado(partida) == 0);
}

static void test_calcular_partida_dos(){
	char* partida = "00000000000000000001";
	assert(calcular_resultado(partida) == 1);
}

static void test_calcular_partida_tres(){
	char* partida = "11111111111111111111";
	assert(calcular_resultado(partida) == 20);
}

static void test_partida_con_un_spare(){
	char* partida = "3/000000000000000000";
	assert(calcular_resultado(partida) == 10);

}

static void test_partida_con_un_spare_mas_bonus(){
	char* partida = "4/500000000000000000";
	assert(calcular_resultado(partida) == 10+5+5);
}

static void test_partida_con_dos_spares_mas_bonus(){
	char* partida = "4/505/70000000000000";
	assert(calcular_resultado(partida) == 10+5+5+10+7+7);
}

static void test_partida_con_dos_spares_consecutivos(){
	char* partida = "4/5/5000000000000000";
	assert(calcular_resultado(partida) == 10+5+10+5+5);
}

static void test_partida_con_un_strike(){
	char* partida = "X000000000000000000";
	assert(calcular_resultado(partida) == 10);
}
static void test_partida_con_dos_strikes(){
	char* partida = "X00X00000000000000";
	assert(calcular_resultado(partida) == 20);
}

static void test_partida_con_un_strike_con_bonus(){
	char* partida = "X450000000000000000";
	assert(calcular_resultado(partida) == 10+4+4+5+5);
}

static void test_partida_con_dos_strikes_consecutivos(){
	char* partida = "XX6300000000000000";
	assert(calcular_resultado(partida) == 54);
}

static void test_partida_con_spare_en_la_ultima_tirada(){
	char* partida = "0000000000000000000/4";
	int result = calcular_resultado(partida);
	//printf("%d\n", result);
	assert(result == 14);
}

static void test_partida_con_un_strike_en_la_ultima_tirada(){
	char* partida = "000000000000000000X81";
	assert(calcular_resultado(partida) == 19);
}

static void test_partida_con_un_strike_en_la_ultima_tirada_con_bonus_strikes(){
	char* partida = "000000000000000000XXX";
	//printf("Resultado: %d\n", calcular_resultado(partida));
	assert(calcular_resultado(partida) == 30);
}

static void test_partida_con_un_strike_en_la_ultima_tirada_con_bonus_spare(){
	char* partida = "000000000000000000X9/";
	//printf("%d\n", calcular_resultado(partida));
	assert(calcular_resultado(partida) == 20);
}

static void test_partida_con_un_spare_en_la_ultima_tirada_con_bonus_strikes(){
	char* partida = "0000000000000000009/X";
	printf("%d\n", calcular_resultado(partida));
	assert(calcular_resultado(partida) == 20);
}

void main(){
	test_prueba_uno();
	test_prueba_dos();
	test_calcular_partida_uno();
	test_calcular_partida_dos();
	test_calcular_partida_tres();
	test_partida_con_un_spare();
	test_partida_con_un_spare_mas_bonus();
	test_partida_con_dos_spares_mas_bonus();
	test_partida_con_dos_spares_consecutivos();
	test_partida_con_un_strike();
	test_partida_con_dos_strikes();
	test_partida_con_un_strike_con_bonus();
	test_partida_con_dos_strikes_consecutivos();
	test_partida_con_spare_en_la_ultima_tirada();
	test_partida_con_un_strike_en_la_ultima_tirada();
	test_partida_con_un_strike_en_la_ultima_tirada_con_bonus_strikes();
	test_partida_con_un_strike_en_la_ultima_tirada_con_bonus_spare();
	test_partida_con_un_spare_en_la_ultima_tirada_con_bonus_strikes();
}
