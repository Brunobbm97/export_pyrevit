from pyrevit import revit, DB, forms
doc = revit.doc
options = DB.SaveAsOptions()
dwg_path = forms.save_file("Exportar para DWG", "DWG Files (*.dwg)|*.dwg")
if dwg_path:
    try:
        doc.SaveAs(dwg_path, options)
        forms.alert("Exportacao DWG concluida com sucesso!", title="Exportar DWG")
    except Exception as e:
        forms.alert("Erro na exportacao DWG: "+str(e), title="Erro na Exportacao DWG")
else:
    forms.alert("Caminho do arquivo DWG nao especificado. Exportacao cancelada.", title="Exportar DWG")