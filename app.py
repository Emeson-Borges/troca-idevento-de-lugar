import re

def process_update_scripts(file_path):
    # Abrir e ler o arquivo
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    updated_lines = []

    # Processar cada linha do arquivo
    for line in lines:
        if line.strip().lower().startswith("update"):
            # Encontrar o primeiro e o segundo idevento
            matches = re.findall(r"idevento\s*=\s*'([^']+)'", line)
            if len(matches) >= 2:
                first_idevento = matches[0]
                # Substituir o segundo idevento pelo primeiro
                updated_line = re.sub(r"(where.*?idevento\s*=\s*')([^']+)(')", rf"\1{first_idevento}\3", line, flags=re.IGNORECASE)
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Salvar o resultado em um novo arquivo
    with open("updated_scripts.txt", 'w') as file:
        file.writelines(updated_lines)
    print("Arquivo processado e salvo como 'updated_scripts.txt'.")

# Caminho para o arquivo txt com os scripts originais
file_path = "C:/Users/itarg/Downloads/updates_errados.txt"
process_update_scripts(file_path)
