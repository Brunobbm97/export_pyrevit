Os Scripts seguem a mesma lógica.

# Importação das bibliotecas
from pyrevit import revit, DB, forms

# Captura o arquivo atual aberto
doc = revit.doc

# Configurar as opções de exportação IFC
options = DB.SaveAsOptions()

# Obter o caminho para salvar o arquivo IFC usando uma caixa de diálogo
ifc_path = forms.save_file("Exportar para IFC", "IFC Files (*.ifc)|*.ifc")

# Verifica se o caminho é válido
if ifc_path:
    try:
	# Salva o documento passando como parâmetro o caminho e as configurações
        doc.SaveAs(ifc_path, options)
        forms.alert("Exportacao IFC concluida com sucesso!", title="Exportar IFC")
    except Exception as e:
	# Retorna uma mensagem de erro 
        forms.alert("Erro na exportacao IFC: "+str(e), title="Erro na Exportacao IFC")
else:
    forms.alert("Caminho do arquivo IFC nao especificado. Exportacao cancelada.", title="Exportar IFC")