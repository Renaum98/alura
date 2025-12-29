//notas
//entre 9 e 10: excelente
//entre 7 e 8: bom
//entre 4 e 6: médio
//entre 0 e 3: ruim

const notaDoAluno = 2;

switch (notaDoAluno) {
    case 10:
    case 9:
        console.log("Nota Excelente");
        break;
    case 8:
    case 7:
        console.log("Nota Boa");
        break;
    case 6:
    case 5:
    case 4:
        console.log("Nota Média");
        break;
    case 3:
    case 2:
    case 1:
        console.log("Nota Ruim");
        break;
    default:
        console.log('Valor invalido');
        break;
}
