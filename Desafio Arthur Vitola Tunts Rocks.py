import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuração das credenciais
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Abre a planilha
sheet = client.open("Desafio Arthur Vitola").sheet1

# Define as colunas
name_col = sheet.col_values(1)[1:]  # Ignora o cabeçalho
p1_col = sheet.col_values(2)[1:]
p2_col = sheet.col_values(3)[1:]
p3_col = sheet.col_values(4)[1:]
absences_col = sheet.col_values(5)[1:]

# Função para calcular a situação e a nota para aprovação final
def calculate_status(p1, p2, p3, absences):
    average = (float(p1) + float(p2) + float(p3)) / 3
    if int(absences) > 0.25 * total_classes:
        return "Reprovado por Falta", 0
    elif average < 5:
        return "Reprovado por Nota", 0
    elif 5 <= average < 7:
        naf = max(10 - average, 0) * 2
        return "Exame Final", round(naf)
    else:
        return "Aprovado", 0

# Define o número total de aulas
total_classes = len(name_col)

# Atualiza a planilha com os resultados
for i in range(len(name_col)):
    status, naf = calculate_status(p1_col[i], p2_col[i], p3_col[i], absences_col[i])
    sheet.update_cell(i + 2, 6, status)
    sheet.update_cell(i + 2, 7, naf)

print("Processo concluído. Verifique a planilha para os resultados.")