typedef struct {
    char nome[200];
    int idade;
    float salario;
} Funcionario;

Funcionario func[10];

for (int i = 0; i < 10; i++) {
    strcpy(func[i].nome, "NULL");
    func[i].idade = 0;
    func[i].salario = 0.0;
}

for (int i = 0; i < 10; i++) {
    printf("Digite o nome do funcionário %d: ", i + 1);
    scanf("%s", func[i].nome);
    printf("Digite a idade do funcionário %d: ", i + 1);
    scanf("%d", &func[i].idade);
    printf("Digite o salário do funcionário %d: ", i + 1);
    scanf("%f", &func[i].salario);
}
